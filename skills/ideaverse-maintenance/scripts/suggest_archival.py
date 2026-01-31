#!/usr/bin/env python3
"""
Suggest notes for archival based on staleness indicators.

Usage:
    ./suggest_archival.py [vault_path] [--days N] [--json]
    python3 suggest_archival.py [vault_path] [--days N] [--json]

Staleness indicators:
- No modifications in N days (default: 180)
- Few/no outgoing links (isolated content)
- Located in Efforts/ and potentially complete
- Minimal content (< 100 words)

This script audits only vault content, excluding:
- node_modules/ directories (package dependencies)
- Build artifacts and documentation files  
- Other non-vault content matching .gitignore
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta
from vault_utils import load_gitignore_patterns, is_vault_content

def get_args():
    args = {
        'vault_path': Path.cwd(),
        'stale_days': 180,
        'json_output': False
    }
    
    positional = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--days' and i + 1 < len(sys.argv):
            args['stale_days'] = int(sys.argv[i + 1])
            i += 2
        elif arg == '--json':
            args['json_output'] = True
            i += 1
        elif not arg.startswith('--'):
            positional.append(arg)
            i += 1
        else:
            i += 1
    
    if positional:
        args['vault_path'] = Path(positional[0])
    
    return args

def get_modification_date(file_path):
    """Get file modification date."""
    return datetime.fromtimestamp(file_path.stat().st_mtime)

def count_words(content):
    """Count words in content body (excluding frontmatter)."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    # Remove wikilinks formatting but keep text
    content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', content)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    
    # Remove other markdown
    content = re.sub(r'[#*`~\[\]()]', '', content)
    
    words = content.split()
    return len(words)

def count_outgoing_links(content):
    """Count outgoing wikilinks."""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = set()
    for match in re.finditer(pattern, content):
        links.add(match.group(1).strip())
    return len(links)

def is_in_efforts(file_path, vault_path):
    """Check if file is in Efforts/ directory."""
    rel_path = file_path.relative_to(vault_path)
    return str(rel_path).startswith('Efforts')

def is_already_archived(file_path, vault_path):
    """Check if file is already in an archive folder."""
    rel_path = str(file_path.relative_to(vault_path)).lower()
    return 'archive' in rel_path

def calculate_staleness_score(note_info, stale_days):
    """Calculate staleness score (higher = more likely to archive)."""
    score = 0
    reasons = []
    
    # Age factor (0-40 points)
    days_old = note_info['days_since_modified']
    if days_old > stale_days:
        age_score = min(40, int((days_old - stale_days) / 30) * 10)
        score += age_score
        reasons.append(f"stale ({days_old} days)")
    
    # Isolation factor (0-30 points)
    if note_info['outgoing_links'] == 0:
        score += 30
        reasons.append("no outgoing links")
    elif note_info['outgoing_links'] < 3:
        score += 15
        reasons.append("few links")
    
    # Content factor (0-20 points)
    if note_info['word_count'] < 50:
        score += 20
        reasons.append("minimal content")
    elif note_info['word_count'] < 100:
        score += 10
        reasons.append("short content")
    
    # Location factor (0-10 points)
    if note_info['in_efforts']:
        score += 10
        reasons.append("in Efforts/")
    
    return score, reasons

def suggest_archival(vault_path, stale_days):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    now = datetime.now()
    candidates = []
    
    # Skip certain folders entirely
    skip_patterns = {'Templates', 'templates', 'Archive', 'archive', 'Archived'}
    
    for md_file in vault.rglob('*.md'):
        # Skip ignored and non-vault content
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        # Skip already archived
        if is_already_archived(md_file, vault_path):
            continue
        
        # Skip templates and special folders
        if any(pattern in str(md_file) for pattern in skip_patterns):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            mod_date = get_modification_date(md_file)
            days_old = (now - mod_date).days
            
            note_info = {
                'path': str(md_file.relative_to(vault_path)),
                'name': md_file.stem,
                'days_since_modified': days_old,
                'last_modified': mod_date.strftime('%Y-%m-%d'),
                'word_count': count_words(content),
                'outgoing_links': count_outgoing_links(content),
                'in_efforts': is_in_efforts(md_file, vault_path)
            }
            
            score, reasons = calculate_staleness_score(note_info, stale_days)
            
            if score >= 30:  # Threshold for suggestion
                note_info['staleness_score'] = score
                note_info['reasons'] = reasons
                candidates.append(note_info)
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
    
    # Sort by staleness score descending
    candidates.sort(key=lambda x: x['staleness_score'], reverse=True)
    return candidates

def main():
    args = get_args()
    
    if not args['vault_path'].exists():
        print(f"Error: Path does not exist: {args['vault_path']}", file=sys.stderr)
        sys.exit(1)
    
    candidates = suggest_archival(args['vault_path'], args['stale_days'])
    
    if args['json_output']:
        print(json.dumps(candidates, indent=2))
        sys.exit(0)
    
    if not candidates:
        print(f"No archival candidates found (stale threshold: {args['stale_days']} days).")
        sys.exit(0)
    
    print(f"Found {len(candidates)} potential archival candidate(s):\n")
    
    # Group by score ranges
    high = [c for c in candidates if c['staleness_score'] >= 60]
    medium = [c for c in candidates if 40 <= c['staleness_score'] < 60]
    low = [c for c in candidates if c['staleness_score'] < 40]
    
    if high:
        print("🔴 High priority (score >= 60):\n")
        for c in high[:10]:
            reasons = ', '.join(c['reasons'])
            print(f"  {c['path']}")
            print(f"      Score: {c['staleness_score']} | {reasons}")
        if len(high) > 10:
            print(f"      ... and {len(high) - 10} more")
        print()
    
    if medium:
        print("🟡 Medium priority (score 40-59):\n")
        for c in medium[:10]:
            reasons = ', '.join(c['reasons'])
            print(f"  {c['path']}")
            print(f"      Score: {c['staleness_score']} | {reasons}")
        if len(medium) > 10:
            print(f"      ... and {len(medium) - 10} more")
        print()
    
    if low:
        print(f"🟢 Low priority (score 30-39): {len(low)} notes\n")
    
    print("Recommendation: Review high-priority candidates for archival.")
    print("Before archiving, extract any reusable knowledge to Atlas/.")

if __name__ == '__main__':
    main()

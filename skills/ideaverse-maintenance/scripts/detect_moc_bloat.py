#!/usr/bin/env python3
"""
Detect MOC bloat - find Maps of Content with too many direct links.

Usage:
    ./detect_moc_bloat.py [vault_path] [--threshold N] [--json]
    python3 detect_moc_bloat.py [vault_path] [--threshold N] [--json]

MOCs with 50+ links are considered bloated and should be split.
Default threshold: 50 (warning at 40)

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
from vault_utils import load_gitignore_patterns, is_vault_content

def get_args():
    args = {
        'vault_path': Path.cwd(),
        'threshold': 50,
        'warning_threshold': 40,
        'json_output': False
    }
    
    positional = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--threshold' and i + 1 < len(sys.argv):
            args['threshold'] = int(sys.argv[i + 1])
            args['warning_threshold'] = int(args['threshold'] * 0.8)
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

def is_moc(file_path, content):
    """Determine if a note is a Map of Content."""
    name = file_path.stem
    
    # Check name patterns
    if 'MOC' in name or name.endswith(' Map'):
        return True
    
    # Check if it's in a Maps folder
    if 'Maps' in str(file_path):
        return True
    
    # Check frontmatter for 'in: [[Maps]]' pattern
    if re.search(r'in:\s*\n\s*-\s*["\']?\[\[Maps\]\]["\']?', content):
        return True
    
    return False

def count_wikilinks(content):
    """Count unique wikilinks in content (excluding frontmatter links)."""
    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    # Find all wikilinks
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = set()
    for match in re.finditer(pattern, content):
        links.add(match.group(1).strip())
    
    return links

def detect_moc_bloat(vault_path, threshold, warning_threshold):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    results = []
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            
            if not is_moc(md_file, content):
                continue
            
            links = count_wikilinks(content)
            link_count = len(links)
            
            if link_count >= warning_threshold:
                rel_path = md_file.relative_to(vault_path)
                status = 'bloated' if link_count >= threshold else 'warning'
                results.append({
                    'path': str(rel_path),
                    'name': md_file.stem,
                    'link_count': link_count,
                    'status': status
                })
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
    
    # Sort by link count descending
    results.sort(key=lambda x: x['link_count'], reverse=True)
    return results

def main():
    args = get_args()
    
    if not args['vault_path'].exists():
        print(f"Error: Path does not exist: {args['vault_path']}", file=sys.stderr)
        sys.exit(1)
    
    results = detect_moc_bloat(
        args['vault_path'], 
        args['threshold'], 
        args['warning_threshold']
    )
    
    if args['json_output']:
        print(json.dumps(results, indent=2))
        sys.exit(1 if any(r['status'] == 'bloated' for r in results) else 0)
    
    if not results:
        print(f"No MOC bloat detected (threshold: {args['threshold']} links).")
        sys.exit(0)
    
    bloated = [r for r in results if r['status'] == 'bloated']
    warnings = [r for r in results if r['status'] == 'warning']
    
    if bloated:
        print(f"🔴 BLOATED MOCs (>= {args['threshold']} links):\n")
        for r in bloated:
            print(f"  {r['path']}: {r['link_count']} links")
        print()
    
    if warnings:
        print(f"🟡 Warning (>= {args['warning_threshold']} links):\n")
        for r in warnings:
            print(f"  {r['path']}: {r['link_count']} links")
        print()
    
    print("Recommendation: Split bloated MOCs into focused child MOCs.")
    
    sys.exit(1 if bloated else 0)

if __name__ == '__main__':
    main()

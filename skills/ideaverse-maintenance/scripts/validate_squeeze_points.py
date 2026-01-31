#!/usr/bin/env python3
"""
Validate squeeze points - find unstructured note clusters that need MOCs.
Usage: python3 validate_squeeze_points.py [vault_path] [--threshold N] [--json]

A squeeze point occurs when 10+ notes reference the same concept without
a dedicated MOC to organize them. This script identifies these opportunities.
"""

import os
import re
import sys
import json
from pathlib import Path
from collections import defaultdict

def get_args():
    args = {
        'vault_path': Path.cwd(),
        'threshold': 10,
        'json_output': False
    }
    
    positional = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--threshold' and i + 1 < len(sys.argv):
            args['threshold'] = int(sys.argv[i + 1])
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

def extract_wikilinks(content):
    """Extract all wikilinks from content."""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = []
    for match in re.finditer(pattern, content):
        link = match.group(1).strip()
        # Normalize: handle paths, remove heading anchors
        if '/' in link:
            link = Path(link).stem
        if '#' in link:
            link = link.split('#')[0]
        if link:
            links.append(link)
    return links

def is_moc(note_name, file_path, existing_mocs):
    """Check if a note is an MOC."""
    if note_name in existing_mocs:
        return True
    if 'MOC' in note_name or note_name.endswith(' Map'):
        return True
    if 'Maps' in str(file_path):
        return True
    return False

def find_existing_mocs(vault_path):
    """Build set of existing MOC names."""
    vault = Path(vault_path)
    mocs = set()
    
    skip_dirs = {'.obsidian', '.git', '.github'}
    
    for md_file in vault.rglob('*.md'):
        if any(part.startswith('.') or part in skip_dirs for part in md_file.parts):
            continue
        
        name = md_file.stem
        if 'MOC' in name or name.endswith(' Map') or 'Maps' in str(md_file):
            mocs.add(name)
        
        # Also check frontmatter for 'in: [[Maps]]'
        try:
            content = md_file.read_text(encoding='utf-8')
            if re.search(r'in:\s*\n\s*-\s*["\']?\[\[Maps\]\]["\']?', content):
                mocs.add(name)
        except:
            pass
    
    return mocs

def find_existing_notes(vault_path):
    """Build set of all existing note names."""
    vault = Path(vault_path)
    notes = set()
    
    skip_dirs = {'.obsidian', '.git', '.github'}
    
    for md_file in vault.rglob('*.md'):
        if any(part.startswith('.') or part in skip_dirs for part in md_file.parts):
            continue
        notes.add(md_file.stem)
    
    return notes

def validate_squeeze_points(vault_path, threshold):
    vault = Path(vault_path)
    
    # Count references to each link target
    link_references = defaultdict(list)  # target -> list of source files
    
    skip_dirs = {'.obsidian', '.git', '.github', 'x', '+'}
    existing_mocs = find_existing_mocs(vault_path)
    existing_notes = find_existing_notes(vault_path)
    
    for md_file in vault.rglob('*.md'):
        if any(part.startswith('.') or part in skip_dirs for part in md_file.parts):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_wikilinks(content)
            source_name = md_file.stem
            
            for link in links:
                # Don't count self-links
                if link != source_name:
                    link_references[link].append(str(md_file.relative_to(vault_path)))
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
    
    # Find squeeze points: heavily referenced terms without MOCs
    squeeze_points = []
    
    for target, sources in link_references.items():
        ref_count = len(sources)
        
        if ref_count < threshold:
            continue
        
        # Skip if this IS an MOC
        if target in existing_mocs:
            continue
        
        # Skip if target note doesn't exist (broken link)
        if target not in existing_notes:
            continue
        
        # Skip if there's an MOC for this concept (e.g., "X MOC" exists)
        if f"{target} MOC" in existing_mocs or f"{target} Map" in existing_mocs:
            continue
        
        squeeze_points.append({
            'term': target,
            'reference_count': ref_count,
            'sources': sorted(sources)[:10],  # Limit for readability
            'total_sources': ref_count
        })
    
    # Sort by reference count descending
    squeeze_points.sort(key=lambda x: x['reference_count'], reverse=True)
    return squeeze_points

def main():
    args = get_args()
    
    if not args['vault_path'].exists():
        print(f"Error: Path does not exist: {args['vault_path']}", file=sys.stderr)
        sys.exit(1)
    
    squeeze_points = validate_squeeze_points(args['vault_path'], args['threshold'])
    
    if args['json_output']:
        print(json.dumps(squeeze_points, indent=2))
        sys.exit(1 if squeeze_points else 0)
    
    if not squeeze_points:
        print(f"No squeeze points found (threshold: {args['threshold']} references).")
        print("Your vault structure is healthy!")
        sys.exit(0)
    
    print(f"Found {len(squeeze_points)} squeeze point(s) - concepts needing MOCs:\n")
    
    for sp in squeeze_points:
        print(f"  📍 [[{sp['term']}]] - {sp['reference_count']} references")
        print(f"      Sample sources:")
        for source in sp['sources'][:5]:
            print(f"        - {source}")
        if sp['total_sources'] > 5:
            print(f"        ... and {sp['total_sources'] - 5} more")
        print()
    
    print("Recommendation: Create MOCs for these terms to improve navigation.")
    print("Follow the MOC creation workflow in the ideaverse skill.")
    
    sys.exit(1 if squeeze_points else 0)

if __name__ == '__main__':
    main()

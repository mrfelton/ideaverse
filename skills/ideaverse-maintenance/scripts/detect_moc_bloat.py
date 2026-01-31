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
from vault_utils import load_gitignore_patterns, is_vault_content, extract_wikilinks_set
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='Detect MOC bloat - find Maps of Content with too many direct links.'
    )
    parser.add_argument(
        'vault_path',
        nargs='?',
        type=Path,
        default=Path.cwd(),
        help='Path to vault (default: current directory)'
    )
    parser.add_argument(
        '--threshold',
        type=int,
        default=50,
        help='Link count to consider bloated (default: 50)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        dest='json_output',
        help='Output results as JSON'
    )
    return parser.parse_args()

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

def detect_moc_bloat(vault_path, threshold):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    warning_threshold = int(threshold * 0.8)
    results = []
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            
            if not is_moc(md_file, content):
                continue
            
            links = extract_wikilinks_set(content)
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
        
        except (IOError, OSError, UnicodeDecodeError) as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
    
    # Sort by link count descending
    results.sort(key=lambda x: x['link_count'], reverse=True)
    return results

def main():
    args = get_args()
    
    if not args.vault_path.exists():
        print(f"Error: Path does not exist: {args.vault_path}", file=sys.stderr)
        sys.exit(1)
    
    results = detect_moc_bloat(args.vault_path, args.threshold)
    
    if args.json_output:
        print(json.dumps(results, indent=2))
        sys.exit(1 if any(r['status'] == 'bloated' for r in results) else 0)
    
    if not results:
        print(f"No MOC bloat detected (threshold: {args.threshold} links).")
        sys.exit(0)
    
    bloated = [r for r in results if r['status'] == 'bloated']
    warnings = [r for r in results if r['status'] == 'warning']
    
    if bloated:
        print(f"🔴 BLOATED MOCs (>= {args.threshold} links):\n")
        for r in bloated:
            print(f"  {r['path']}: {r['link_count']} links")
        print()
    
    if warnings:
        warning_threshold = int(args.threshold * 0.8)
        print(f"🟡 Warning (>= {warning_threshold} links):\n")
        for r in warnings:
            print(f"  {r['path']}: {r['link_count']} links")
        print()
    
    print("Recommendation: Split bloated MOCs into focused child MOCs.")
    
    sys.exit(1 if bloated else 0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Validate squeeze points - find unstructured note clusters that need MOCs.

Usage:
    ./validate_squeeze_points.py [vault_path] [--threshold N] [--json]
    python3 validate_squeeze_points.py [vault_path] [--threshold N] [--json]

A squeeze point occurs when 10+ notes reference the same concept without
a dedicated MOC to organize them. This script identifies these opportunities.

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
from collections import defaultdict
from vault_utils import load_gitignore_patterns, is_vault_content, extract_wikilinks
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='Validate squeeze points - find unstructured note clusters that need MOCs.'
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
        default=10,
        help='Reference count threshold to consider a squeeze point (default: 10)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        dest='json_output',
        help='Output results as JSON'
    )
    return parser.parse_args()

def extract_wikilinks_normalized(content: str) -> list:
    """Extract wikilinks and normalize them (handle paths, remove anchors)."""
    links = extract_wikilinks(content)
    normalized = []
    for link in links:
        # Handle path-style links (Folder/Note)
        if '/' in link:
            link = Path(link).stem
        # Remove heading anchors
        if '#' in link:
            link = link.split('#')[0]
        if link:
            normalized.append(link)
    return normalized

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
    ignore_patterns = load_gitignore_patterns(vault)
    mocs = set()
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
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
    ignore_patterns = load_gitignore_patterns(vault)
    notes = set()
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        notes.add(md_file.stem)
    
    return notes

def validate_squeeze_points(vault_path, threshold):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    
    # Count references to each link target
    link_references = defaultdict(list)  # target -> list of source files
    
    existing_mocs = find_existing_mocs(vault_path)
    existing_notes = find_existing_notes(vault_path)
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_wikilinks_normalized(content)
            source_name = md_file.stem
            
            for link in links:
                # Don't count self-links
                if link != source_name:
                    link_references[link].append(str(md_file.relative_to(vault_path)))
        
        except (IOError, OSError, UnicodeDecodeError) as e:
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
    
    if not args.vault_path.exists():
        print(f"Error: Path does not exist: {args.vault_path}", file=sys.stderr)
        sys.exit(1)
    
    squeeze_points = validate_squeeze_points(args.vault_path, args.threshold)
    
    if args.json_output:
        print(json.dumps(squeeze_points, indent=2))
        sys.exit(1 if squeeze_points else 0)
    
    if not squeeze_points:
        print(f"No squeeze points found (threshold: {args.threshold} references).")
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

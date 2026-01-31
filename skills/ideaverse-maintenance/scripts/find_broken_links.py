#!/usr/bin/env python3
"""
Find broken links - wikilinks that point to non-existent notes.
Usage: python3 find_broken_links.py [vault_path]
"""

import os
import re
import sys
from pathlib import Path

def get_vault_path():
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path.cwd()

def extract_wikilinks(content):
    """Extract all wikilinks from content."""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = []
    for match in re.finditer(pattern, content):
        links.append(match.group(1).strip())
    return links

def find_broken_links(vault_path):
    vault = Path(vault_path)
    
    # Build set of all existing note names
    existing_notes = set()
    skip_dirs = {'.obsidian', '.git', '.github'}
    
    for md_file in vault.rglob('*.md'):
        if any(part.startswith('.') for part in md_file.parts):
            continue
        existing_notes.add(md_file.stem)
    
    # Find broken links
    broken = []  # (source_file, broken_link)
    
    for md_file in vault.rglob('*.md'):
        if any(part.startswith('.') or part in skip_dirs for part in md_file.parts):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_wikilinks(content)
            
            for link in links:
                # Handle path-style links (Folder/Note)
                link_name = Path(link).stem if '/' in link else link
                
                # Skip headings/blocks (links with #)
                if '#' in link_name:
                    link_name = link_name.split('#')[0]
                
                if link_name and link_name not in existing_notes:
                    broken.append((md_file, link))
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
    
    return broken

def main():
    vault_path = get_vault_path()
    
    if not vault_path.exists():
        print(f"Error: Path does not exist: {vault_path}", file=sys.stderr)
        sys.exit(1)
    
    broken = find_broken_links(vault_path)
    
    if not broken:
        print("No broken links found.")
        sys.exit(0)
    
    # Group by source file
    by_source = {}
    for source, link in broken:
        rel_path = str(source.relative_to(vault_path))
        if rel_path not in by_source:
            by_source[rel_path] = []
        by_source[rel_path].append(link)
    
    print(f"Found {len(broken)} broken link(s) in {len(by_source)} file(s):\n")
    for source, links in sorted(by_source.items()):
        print(f"  {source}:")
        for link in sorted(set(links)):
            print(f"    -> [[{link}]]")
    
    sys.exit(1 if broken else 0)

if __name__ == '__main__':
    main()

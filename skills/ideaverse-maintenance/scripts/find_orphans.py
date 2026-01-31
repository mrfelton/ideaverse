#!/usr/bin/env python3
"""
Find orphan notes - notes with no incoming links from other notes.
Usage: python3 find_orphans.py [vault_path]

This script audits only vault content, excluding:
- node_modules/ directories (package dependencies)
- Build artifacts (dist/, build/, .next/, etc.)
- Version control (.git/, .github/)
- Other non-vault content matching .gitignore
"""

import os
import re
import sys
from pathlib import Path
from vault_utils import load_gitignore_patterns, is_vault_content

def get_vault_path():
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path.cwd()

def extract_wikilinks(content):
    """Extract all wikilinks from note content and frontmatter."""
    # Match [[Link]] and [[Link|Alias]] patterns
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    # Also match YAML frontmatter links like - "[[Link]]"
    yaml_pattern = r'"?\[\[([^\]|]+)(?:\|[^\]]+)?\]\]"?'
    
    links = set()
    for match in re.finditer(pattern, content):
        links.add(match.group(1).strip())
    for match in re.finditer(yaml_pattern, content):
        links.add(match.group(1).strip())
    return links

def find_orphans(vault_path):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    
    # Collect all notes and their incoming links (vault content only)
    notes = {}  # filename (no ext) -> file path
    incoming_links = {}  # filename -> set of files that link to it
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        note_name = md_file.stem
        notes[note_name] = md_file
        incoming_links[note_name] = set()
    
    # Build incoming link graph (vault content only)
    for note_name, file_path in notes.items():
        try:
            content = file_path.read_text(encoding='utf-8')
            links = extract_wikilinks(content)
            for link in links:
                # Normalize link (handle paths like Folder/Note)
                link_name = Path(link).stem if '/' in link else link
                if link_name in incoming_links:
                    incoming_links[link_name].add(note_name)
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
    
    # Find orphans (notes with no incoming links)
    orphans = []
    # Exclude Home and root-level MOCs from orphan detection
    root_notes = {'Home', 'Home Basic', 'Ideaverse Map'}
    
    for note_name, linkers in incoming_links.items():
        if not linkers and note_name not in root_notes:
            orphans.append((note_name, notes[note_name]))
    
    return sorted(orphans, key=lambda x: x[0])

def main():
    vault_path = get_vault_path()
    
    if not vault_path.exists():
        print(f"Error: Path does not exist: {vault_path}", file=sys.stderr)
        sys.exit(1)
    
    orphans = find_orphans(vault_path)
    
    if not orphans:
        print("No orphan notes found.")
        sys.exit(0)
    
    print(f"Found {len(orphans)} orphan note(s):\n")
    for name, path in orphans:
        rel_path = path.relative_to(vault_path)
        print(f"  - {rel_path}")
    
    sys.exit(1 if orphans else 0)

if __name__ == '__main__':
    main()

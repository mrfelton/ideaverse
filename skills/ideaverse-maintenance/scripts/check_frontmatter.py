#!/usr/bin/env python3
"""
Check for missing frontmatter properties in notes.
Usage: python3 check_frontmatter.py [vault_path] [--strict] [--json]

Checks for:
- Missing 'up:' property (except for Home and root notes)
- Missing 'created:' date
- MOCs missing 'in:' property (strict mode)

This script audits only vault content, excluding:
- node_modules/ directories (package dependencies)
- Build artifacts and documentation files
- Other non-vault content matching .gitignore
"""

import re
import sys
import json
from pathlib import Path
from vault_utils import load_gitignore_patterns, is_vault_content, should_check_frontmatter

def get_args():
    args = {
        'vault_path': Path.cwd(),
        'strict': False,
        'json_output': False
    }
    
    positional = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--strict':
            args['strict'] = True
            i += 1
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

def parse_frontmatter(content):
    """Extract YAML frontmatter as dict."""
    if not content.startswith('---'):
        return None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    yaml_text = parts[1].strip()
    if not yaml_text:
        return {}
    
    # Simple YAML parsing (no dependencies)
    props = {}
    current_key = None
    current_list = None
    
    for line in yaml_text.split('\n'):
        line = line.rstrip()
        if not line:
            continue
        
        # Check for list item
        if line.startswith('  - '):
            if current_key and current_list is not None:
                current_list.append(line[4:].strip().strip('"'))
            continue
        
        # Check for key: value or key:
        match = re.match(r'^(\w+):\s*(.*)', line)
        if match:
            current_key = match.group(1)
            value = match.group(2).strip()
            
            if value == '' or value == '[]':
                props[current_key] = []
                current_list = props[current_key]
            elif value.startswith('[') and value.endswith(']'):
                # Inline array
                props[current_key] = [v.strip().strip('"') for v in value[1:-1].split(',') if v.strip()]
                current_list = None
            else:
                props[current_key] = value.strip('"')
                current_list = None
    
    return props

def check_frontmatter(vault_path, strict=False):
    vault = Path(vault_path)
    ignore_patterns = load_gitignore_patterns(vault)
    issues = []
    
    root_notes = {'Home', 'Home Basic', 'Ideaverse Map'}
    
    for md_file in vault.rglob('*.md'):
        if not is_vault_content(md_file, vault, ignore_patterns):
            continue
        
        # Skip library files that don't need frontmatter
        if not should_check_frontmatter(md_file, vault):
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
            props = parse_frontmatter(content)
            rel_path = str(md_file.relative_to(vault_path))
            note_name = md_file.stem
            
            # Check: No frontmatter at all
            if props is None:
                issues.append({
                    'path': rel_path,
                    'issue': 'missing frontmatter',
                    'severity': 'error'
                })
                continue
            
            # Check: Missing 'created' date
            if 'created' not in props:
                issues.append({
                    'path': rel_path,
                    'issue': "missing 'created' date",
                    'severity': 'warning'
                })
            
            # Check: Missing 'up' property (except root notes and daily logs)
            is_root = note_name in root_notes
            is_daily = 'Calendar' in rel_path and re.match(r'\d{4}-\d{2}-\d{2}', note_name)
            
            if not is_root and not is_daily:
                up_val = props.get('up', [])
                if not up_val or (isinstance(up_val, list) and len(up_val) == 0):
                    issues.append({
                        'path': rel_path,
                        'issue': "missing 'up' property",
                        'severity': 'warning'
                    })
            
            # Check: MOCs should have 'in' property (strict mode)
            if strict:
                is_moc = 'MOC' in note_name or 'Map' in note_name or 'Maps' in rel_path
                if is_moc:
                    in_val = props.get('in', [])
                    if not in_val or (isinstance(in_val, list) and len(in_val) == 0):
                        issues.append({
                            'path': rel_path,
                            'issue': "MOC missing 'in' property",
                            'severity': 'info'
                        })
        
        except Exception as e:
            issues.append({
                'path': str(md_file.relative_to(vault_path)),
                'issue': f'read error: {e}',
                'severity': 'error'
            })
    
    return issues

def main():
    args = get_args()
    
    if not args['vault_path'].exists():
        print(f"Error: Path does not exist: {args['vault_path']}", file=sys.stderr)
        sys.exit(1)
    
    issues = check_frontmatter(args['vault_path'], args['strict'])
    
    if args['json_output']:
        print(json.dumps(issues, indent=2))
        sys.exit(1 if issues else 0)
    
    if not issues:
        print("All notes have required frontmatter properties.")
        sys.exit(0)
    
    # Group by issue type
    by_issue = {}
    for item in issues:
        issue = item['issue']
        if issue not in by_issue:
            by_issue[issue] = []
        by_issue[issue].append(item['path'])
    
    print(f"Found {len(issues)} frontmatter issue(s):\n")
    for issue, paths in sorted(by_issue.items()):
        print(f"  {issue} ({len(paths)} files):")
        for path in sorted(paths)[:10]:  # Limit output
            print(f"    - {path}")
        if len(paths) > 10:
            print(f"    ... and {len(paths) - 10} more")
        print()
    
    sys.exit(1 if issues else 0)

if __name__ == '__main__':
    main()

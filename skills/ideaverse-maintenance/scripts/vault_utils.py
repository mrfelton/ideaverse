#!/usr/bin/env python3
"""
Shared utilities for vault auditing scripts.
Provides consistent path filtering using .gitignore patterns and git submodules.
Uses only Python 3 standard library (no external dependencies).

Exclusions:
- Patterns from .gitignore (respects project's own ignore rules)
- Git submodule paths from .gitmodules (external repositories)
- Built-in patterns for common non-vault content (node_modules, dist, etc.)

Usage:
    from vault_utils import load_gitignore_patterns, is_vault_content, extract_wikilinks
    
    ignore_patterns = load_gitignore_patterns(vault_root)
    for md_file in vault_root.rglob('*.md'):
        if not is_vault_content(md_file, vault_root, ignore_patterns):
            continue
        links = extract_wikilinks(md_file.read_text())
        # Process vault content
"""

from pathlib import Path
from typing import List, Set
import fnmatch
import re

# Shared constants
ROOT_NOTES = {'Home', 'Home Basic', 'Ideaverse Map'}
WIKILINK_PATTERN = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'


def extract_wikilinks(content: str) -> List[str]:
    """
    Extract all wikilinks from content.
    
    Handles both [[Link]] and [[Link|Alias]] patterns.
    Returns list of link targets (not aliases).
    
    Args:
        content: File content as string
    
    Returns:
        List of wikilink targets (deduplicated if same_dedup=True not passed)
    """
    links = []
    for match in re.finditer(WIKILINK_PATTERN, content):
        links.append(match.group(1).strip())
    return links


def extract_wikilinks_set(content: str) -> Set[str]:
    """Extract unique wikilinks from content as a set."""
    return set(extract_wikilinks(content))


def load_gitignore_patterns(vault_root: Path) -> List[str]:
    """
    Load patterns from .gitignore file and git submodules in vault root.
    Returns list of glob patterns to exclude from audits.
    
    Always includes built-in patterns for common non-vault content.
    Falls back to built-in patterns if no .gitignore exists.
    
    This function is robust and handles:
    - Missing .gitignore or .gitmodules files (uses built-in patterns only)
    - Empty config files (skips blank lines and comments)
    - Malformed config files (silently ignores errors)
    - Permission errors (falls back gracefully)
    
    Args:
        vault_root: Path to vault root directory
    
    Returns:
        List of gitignore-style glob patterns (always returns at least built-in patterns)
    """
    # Start with built-in patterns - these are always applied
    patterns = _get_builtin_patterns()
    
    # Add submodule paths to exclusions (handles missing .gitmodules gracefully)
    try:
        patterns.extend(_load_submodule_paths(vault_root))
    except Exception:
        pass  # Continue with built-in patterns if submodule parsing fails
    
    # Add patterns from .gitignore (optional)
    gitignore_path = vault_root / '.gitignore'
    if not gitignore_path.exists():
        return patterns
    
    # Parse .gitignore file
    try:
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith('#'):
                    continue
                # Remove trailing slash (gitignore convention)
                line = line.rstrip('/')
                if line:  # Only add non-empty patterns
                    patterns.append(line)
    except (IOError, OSError, UnicodeDecodeError):
        # Silently continue if .gitignore can't be read
        # Built-in patterns will still protect against common false positives
        pass
    
    return patterns


def _get_builtin_patterns() -> List[str]:
    """
    Built-in exclusion patterns for common non-vault content.
    These are always applied, even if .gitignore doesn't exist.
    
    Covers:
    - Hidden directories (anything starting with . except .obsidian which is handled separately)
    - Package managers (node_modules, pip, etc.)
    - Build outputs (dist, build, .next, .vite, etc.)
    - Version control (.git, .github)
    - IDE/OS files (.vscode, .DS_Store, etc.)
    """
    return [
        # Hidden directories - configuration/tooling, not vault content
        # Matches any folder starting with . at any level
        '.*/**',
        '.*',
        
        # Package managers - primary causes of false positives
        '**/node_modules',
        '**/node_modules/**',
        '*.egg-info',
        '__pycache__',
        '.venv',
        'venv',
        '.pnpm-store',
        '.yarn',
        
        # Build outputs
        'dist/**',
        'build/**',
        'out/**',
        
        # OS files
        '.DS_Store',
        'Thumbs.db',
        '*.swp',
        '*.swo',
        '*~',
    ]


def _load_submodule_paths(vault_root: Path) -> List[str]:
    """
    Load paths from .gitmodules file to exclude git submodules.
    
    Git submodules are external repositories and should not be audited
    as vault content. This parses the .gitmodules INI-like config file
    and extracts all submodule paths.
    
    This function is robust and handles:
    - Missing .gitmodules file (returns empty list)
    - Malformed .gitmodules content (skips invalid lines)
    - Permission errors (returns empty list)
    - Empty .gitmodules (returns empty list)
    
    Args:
        vault_root: Path to vault root directory
    
    Returns:
        List of glob patterns for submodule paths to exclude (may be empty)
    """
    submodule_patterns = []
    gitmodules_path = vault_root / '.gitmodules'
    
    if not gitmodules_path.exists():
        return submodule_patterns
    
    try:
        with open(gitmodules_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Parse lines like: path = path/to/submodule
                # Skip comments, empty lines, and section headers
                if not line or line.startswith('#') or line.startswith('['):
                    continue
                    
                if line.startswith('path = ') or line.startswith('path='):
                    # Extract path value, handling both "path = " and "path="
                    submodule_path = line.split('=', 1)[1].strip()
                    if submodule_path:  # Only add non-empty paths
                        # Add pattern to exclude submodule and all its contents
                        submodule_patterns.append(f'{submodule_path}/**')
                        submodule_patterns.append(submodule_path)
    except (IOError, OSError, UnicodeDecodeError):
        # Silently return empty list if .gitmodules can't be read
        pass
    
    return submodule_patterns


def _path_matches_patterns(rel_path: str, patterns: List[str]) -> bool:
    """
    Check if a relative path matches any of the gitignore patterns.
    Uses fnmatch for glob matching (standard Python library).
    
    Special handling:
    - Hidden directories (starting with .) are excluded at any level
    - Directory-level matching for patterns like '**/node_modules/**'
    - File-level matching for specific patterns
    
    Handles both file-level and directory-level matches:
    - 'node_modules/package/README.md' matches '**/node_modules/**'
    - 'dist/index.html' matches 'dist/**'
    - '.git/config' matches '.git/**'
    - '.agents/skills/file.md' matches '.*/**' (hidden dir at any level)
    
    Args:
        rel_path: Relative path from vault root (forward slashes)
        patterns: List of glob patterns from gitignore
    
    Returns:
        True if path matches any pattern, False otherwise
    """
    # Normalize to forward slashes for consistent matching
    rel_path = rel_path.replace('\\', '/')
    
    # Quick check: Exclude any path with hidden directories (starting with .)
    # This catches .agents, .github, .codex, .ralph-tui, etc.
    path_parts = rel_path.split('/')
    for part in path_parts:
        if part.startswith('.') and part != '.' and part != '..':
            # Hidden directory found - exclude this path
            # (skip special directories . and ..)
            return True
    
    for pattern in patterns:
        # Direct file/path match
        if fnmatch.fnmatch(rel_path, pattern):
            return True
        
        # Check each path component for directory matches
        # This helps match patterns like '*/node_modules/**' or '**/dist/**'
        for i, part in enumerate(path_parts):
            # Match against bare pattern (e.g., 'dist' from 'dist/**')
            bare_pattern = pattern.strip('*').strip('/')
            if fnmatch.fnmatch(part, bare_pattern):
                # Also check if everything after this part should be excluded
                # e.g., if 'node_modules' matched, exclude everything under it
                if i < len(path_parts) - 1 or '/**' in pattern:
                    return True
    
    return False


def is_vault_content(
    file_path: Path, 
    vault_root: Path, 
    ignore_patterns: List[str] = None
) -> bool:
    """
    Determine if a file should be audited as vault content.
    
    Returns False for:
    - Files matching .gitignore patterns
    - Files matching built-in exclusion patterns
    - Files in excluded directories (node_modules, dist, .git, etc.)
    - Files in git submodules
    - Files outside the vault root
    
    Returns True only for files that are actual vault content.
    
    This function is robust and handles:
    - Files outside vault root (returns False)
    - None ignore_patterns (loads them automatically)
    - Invalid file paths (returns False)
    
    Args:
        file_path: Absolute path to file being checked
        vault_root: Absolute path to vault root directory
        ignore_patterns: List of gitignore patterns (loads from .gitignore if None)
    
    Returns:
        True if file should be audited, False if it should be skipped
    """
    # Load patterns if not provided (handles missing config files gracefully)
    if ignore_patterns is None:
        ignore_patterns = load_gitignore_patterns(vault_root)
    
    # Get relative path, handling files outside vault root
    try:
        rel_path = str(file_path.relative_to(vault_root))
    except ValueError:
        # File is not under vault root - not vault content
        return False
    except Exception:
        # Any other error - skip this file to be safe
        return False
    
    # Skip if matches any ignore pattern
    if _path_matches_patterns(rel_path, ignore_patterns):
        return False
    
    return True


def should_check_frontmatter(file_path: Path, vault_root: Path) -> bool:
    """
    Determine if a file should be checked for frontmatter.
    
    Vault content should have frontmatter, but generated/library
    files don't need it:
    - Documentation files (README.md, CHANGELOG.md, etc.)
    - Generated HTML/CSS in dist folders
    - Library files from dependencies
    
    This function is robust and handles:
    - Files outside vault root (returns False)
    - Invalid file paths (returns False)
    
    Args:
        file_path: Absolute path to file
        vault_root: Absolute path to vault root
    
    Returns:
        True if file should have frontmatter, False if it's exempt
    """
    try:
        rel_path = str(file_path.relative_to(vault_root)).lower()
        filename = file_path.name.lower()
    except (ValueError, AttributeError):
        # File outside vault or invalid path - exempt from frontmatter check
        return False
    
    # Patterns for files that don't need frontmatter
    library_patterns = [
        '**/readme*',
        '**/changelog*',
        '**/license*',
        '**/code_of_conduct*',
        '**/contributing*',
        '**/history*',
        '**/releases*',
        '**/api.md',
        '**/contributing/**',
        '*.html',
        '*.css',
    ]
    
    for pattern in library_patterns:
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(filename, pattern):
            return False
    
    return True

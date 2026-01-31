````markdown
# Troubleshooting Reference

Decision trees and resolution guides for common Ideaverse vault problems.

## Table of Contents

1. [Quick Diagnosis](#quick-diagnosis)
2. [Broken Links](#broken-links)
3. [Orphan Notes](#orphan-notes)
4. [Frontmatter Issues](#frontmatter-issues)
5. [MOC Problems](#moc-problems)
6. [Navigation Confusion](#navigation-confusion)
7. [Performance Issues](#performance-issues)

---

## Quick Diagnosis

### Symptom → Problem Map

| Symptom | Likely Problem | First Check |
|---------|----------------|-------------|
| Purple/red links in Obsidian | Broken links | `find_broken_links.py` |
| Note feels "lost" | Missing up: property or orphan | Check frontmatter |
| Can't find related notes | Poor linking or missing MOC | Check for squeeze point |
| MOC is overwhelming | MOC bloat | `detect_moc_bloat.py` |
| Same info in multiple places | Duplication | Search for concept |
| Graph view looks disconnected | Orphan proliferation | `find_orphans.py` |
| Frontmatter warnings | Missing/invalid properties | `check_frontmatter.py` |

---

## Broken Links

### Decision Tree

```
Broken link found: [[Missing Note]]
    │
    ├── Was note renamed?
    │   └── Yes → Update link to new name
    │   
    ├── Was note deleted intentionally?
    │   └── Yes → Remove or rephrase the reference
    │   
    ├── Is this a typo?
    │   └── Yes → Correct the link
    │   
    ├── Should this note exist?
    │   ├── Yes, important → Create the note
    │   └── Yes, later → Add to creation queue
    │   
    └── Is this an external reference?
        └── Yes → Consider using external link format instead
```

### Resolution Steps

**Case: Note was renamed**
```
1. Search for the renamed note
2. Copy the correct name
3. Find and replace [[old name]] with [[new name]]
4. Verify with find_broken_links.py
```

**Case: Creating the missing note**
```
1. Create note with proper frontmatter
2. Add up: property pointing to relevant MOC
3. Add basic content
4. Link from appropriate places
```

**Prevention**: Use Obsidian's built-in rename refactor to automatically update links.

---

## Orphan Notes

### Decision Tree

```
Orphan note found: Note.md
    │
    ├── Is this note valuable?
    │   │
    │   ├── High value, actively useful
    │   │   └── Find integration point (MOC + links)
    │   │
    │   ├── Historical/archival value
    │   │   └── Move to archive with context
    │   │
    │   ├── Duplicate content
    │   │   └── Merge with primary note, delete this
    │   │
    │   └── No value / outdated
    │       └── Delete
    │
    ├── Is it a special note type?
    │   │
    │   ├── Template → Expected to be orphan, ignore
    │   ├── Configuration → Expected to be orphan, ignore
    │   └── Daily log → Should have date-based links
    │
    └── Unsure about value?
        └── Add to triage queue for review
```

### Integration Options

**Option A: Add to MOC**
```
1. Identify relevant MOC
2. Add link to note in appropriate section
3. Update note's up: property to point to MOC
```

**Option B: Link from related notes**
```
1. Search for notes on similar topics
2. Add contextual links to this note
3. Add reciprocal links if relevant
```

**Option C: Create bridging MOC**
```
If orphan + several related notes exist without structure:
1. Create MOC for the concept
2. Link all related notes to new MOC
3. Add new MOC to parent structure
```

---

## Frontmatter Issues

### Issue: Missing frontmatter entirely

```
Resolution:
1. Add YAML frontmatter block at top of file
2. Include at minimum:
   ---
   up:
     - "[[Relevant MOC]]"
   created: YYYY-MM-DD
   ---
3. Add related: if there are lateral connections
```

### Issue: Missing 'created' date

```
Resolution:
1. Check file creation date in filesystem
2. Add created: YYYY-MM-DD to frontmatter
```

### Issue: Missing 'up' property

```
Decision:
├── Is this a root note (Home)?
│   └── Root notes don't need up:
│
├── Is this a daily log?
│   └── Daily logs can omit up: (time-based navigation)
│
└── Regular note?
    └── Find appropriate parent MOC and add up:
```

### Issue: Invalid frontmatter syntax

Common problems and fixes:

| Problem | Example | Fix |
|---------|---------|-----|
| Missing quotes on wikilinks | `up: [[Note]]` | `up: - "[[Note]]"` |
| Not using array format | `up: "[[Note]]"` | `up: - "[[Note]]"` |
| Inline text pattern | `Up: [[Note]]` in body | Move to YAML frontmatter |
| Mixed indentation | Tabs + spaces | Use consistent 2-space indent |

---

## MOC Problems

### Problem: MOC has 50+ links (bloated)

```
Diagnosis:
1. Run detect_moc_bloat.py
2. Review flagged MOCs

Resolution:
1. Read through the MOC
2. Identify 3-5 natural groupings
3. For largest group (15+ notes):
   a. Create child MOC
   b. Move relevant links to child
   c. Add child MOC link to parent
   d. Update affected notes' up: properties
4. Repeat until parent has < 40 direct links
```

### Problem: MOC is disorganized

```
Signs:
- No section headers
- Random ordering
- No descriptions
- Hard to scan

Resolution:
1. Group links by sub-theme
2. Add ## headers for each group
3. Add brief descriptions where helpful
4. Order sections by importance/frequency
5. Consider adding a brief intro paragraph
```

### Problem: Overlapping MOCs

```
Signs:
- Same note appears in multiple MOCs at same level
- Unclear which MOC is "primary"
- Redundant structures

Resolution:
1. Decide primary home for each shared note
2. Update up: to point to primary MOC
3. Use related: to reference secondary MOC
4. Review MOC scopes - clarify boundaries
```

---

## Navigation Confusion

### Problem: Can't find where a note belongs

```
Diagnosis questions:
1. What topic/domain is this note about?
2. Is there an existing MOC for that domain?
3. Would it fit under a broader MOC?

Resolution path:
├── MOC exists → Add note to it
├── No MOC, but 10+ related notes → Create MOC
└── No MOC, few related notes → Use broader MOC or Atlas root
```

### Problem: Graph view shows disconnected clusters

```
Diagnosis:
1. Identify disconnected clusters
2. Check if they should be connected

Resolution:
├── Missing cross-domain links
│   └── Add relevant related: properties
├── Missing MOC hierarchy
│   └── Ensure up: chains connect to Home
└── Genuinely separate domains
    └── This may be acceptable
```

### Problem: Too many paths to the same note

```
Signs:
- Note has many up: parents
- Appears in many MOCs
- Confusing navigation

Resolution:
1. Identify primary conceptual home
2. Set up: to primary parent only
3. Use related: for secondary connections
4. Remove from redundant MOC listings
```

---

## Performance Issues

### Problem: Vault feels slow

```
Diagnosis:
1. How many notes total?
2. How many plugins enabled?
3. Large embedded files?

Resolution by cause:
├── Too many notes (5000+)
│   └── Ensure indexes, consider vault splitting
├── Plugin overload
│   └── Disable unused plugins
├── Large attachments
│   └── Move to external storage, link
└── Graph view rendering all
    └── Use local graph, filter global
```

### Problem: Search returns too many irrelevant results

```
Resolution:
1. Use more specific search terms
2. Use path: operator to limit scope
   Example: path:Atlas/ concept
3. Use tag: operator if using tags
4. Start from MOC and follow links instead
```

---

## Emergency Recovery

### Vault backup is missing or corrupted

```
Recovery options:
1. Check cloud sync history (iCloud, Dropbox, etc.)
2. Check .obsidian/workspace.json for recent state
3. Use git history if vault is version controlled
4. Rebuild from filesystem + run all diagnostic scripts

Prevention:
- Enable automatic backups
- Use version control (git)
- Sync to cloud service
```

### Accidentally deleted important note

```
Recovery:
1. Check trash folder (if using plugin)
2. Check filesystem trash
3. Check cloud sync versions
4. Check git history: git log --all --full-history -- "**/NoteName*"
5. Search for content in other notes (may be excerpted)
```

````

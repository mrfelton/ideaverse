````markdown
# Duplicate Detection Reference

Finding, evaluating, and handling duplicate concepts in Ideaverse vaults.

## Table of Contents

1. [Why Duplicates Matter](#why-duplicates-matter)
2. [Search Strategy](#search-strategy)
3. [Evaluation Framework](#evaluation-framework)
4. [Resolution Options](#resolution-options)
5. [Merge Process](#merge-process)
6. [Prevention](#prevention)

---

## Why Duplicates Matter

### The Problem

Duplicates fragment knowledge:
- Same concept in multiple places
- Updates miss some instances
- Links go to wrong versions
- Structure becomes unclear

### Types of Duplicates

| Type | Example | Risk Level |
|------|---------|------------|
| Exact duplicate | Two notes titled "Atomic Notes" | High |
| Synonym duplicate | "Personal Knowledge Management" vs "PKM" | Medium |
| Overlap duplicate | Two notes covering 70% same content | Medium |
| Perspective duplicate | Same concept from different angles | Low |

### When Duplicates Are Okay

Not all duplicates are bad:
- **Deliberate**: Different perspectives on same topic
- **Scoped**: Same term in different domains
- **Temporal**: Old and new versions (kept intentionally)

---

## Search Strategy

### Before Creating Any Note

Always search first using this sequence:

### Step 1: Exact Name Search

```
Search: [[Concept Name]]
```

Find any notes with exact or similar titles.

### Step 2: Synonym Expansion

List synonyms and search each:

| Concept | Synonyms to Search |
|---------|-------------------|
| PKM | Personal Knowledge Management, Second Brain, Note-taking System |
| MOC | Map of Content, Index, Hub Note |
| Atomic Notes | Evergreen Notes, Zettelkasten Notes |

```
Search: [[Synonym 1]]
Search: [[Synonym 2]]
```

### Step 3: MOC Review

Browse relevant MOC(s) manually:

1. Find the MOC for this concept's domain
2. Scan all listed notes
3. Look for similar concepts

### Step 4: Content Search

Search for key phrases that would appear in similar notes:

```
Search: "definition of [concept]"
Search: "[core distinguishing phrase]"
```

### Step 5: Graph Exploration

In Obsidian:
1. Open local graph for related notes
2. Look for clusters that might indicate similar concepts
3. Check notes linked from same MOC

---

## Evaluation Framework

When potential duplicates are found, evaluate them.

### Similarity Assessment Matrix

| Factor | Weight | Questions |
|--------|--------|-----------|
| Title similarity | High | Same or synonymous names? |
| Definition overlap | High | Same core meaning? |
| Content overlap | Medium | Same key points? |
| Link overlap | Medium | Same connections? |
| Scope overlap | Medium | Same domain/context? |
| Perspective | Low | Same angle or viewpoint? |

### Decision Tree

```
Are titles identical or synonymous?
├── Yes → Likely duplicate, evaluate further
└── No → Probably distinct

Do definitions mean the same thing?
├── Yes → Definitely duplicate territory
└── No → May be distinct concepts

Is content > 50% overlapping?
├── Yes → Should merge
└── No → Consider linking instead

Are they in the same domain/scope?
├── Yes → Higher merge priority
└── No → May be valid separate notes
```

### Scoring Guide

| Score | Overlap Level | Action |
|-------|---------------|--------|
| 0-2 | Distinct | Create separate note, add related: link |
| 3-4 | Related | Consider merging OR keep with clear differentiation |
| 5-6 | Duplicate | Must resolve: merge or delete one |

---

## Resolution Options

### Option 1: Keep Both (Differentiate)

**When to use**:
- Same term, different domains
- Same concept, different perspectives
- Intentional coverage from multiple angles

**Action**:
1. Clarify titles to distinguish: "PKM (Definition)" vs "PKM (My Approach)"
2. Add explicit cross-references
3. Note the relationship in both notes

### Option 2: Merge

**When to use**:
- True duplicates with overlapping content
- One note is clearly better
- Both have valuable unique content

**Action**:
1. Select primary note
2. Migrate unique content from secondary
3. Update all links pointing to secondary
4. Delete or archive secondary

### Option 3: Redirect

**When to use**:
- Secondary note has minimal content
- Primary note is definitive
- Quick resolution needed

**Action**:
1. Replace secondary content with redirect:
   ```markdown
   See [[Primary Note]] for this concept.
   ```
2. Update frontmatter to point to primary
3. Optionally delete after confirming no incoming links

### Option 4: Create Parent

**When to use**:
- Both notes are valuable
- They represent sub-types of a broader concept
- Pattern suggests missing abstraction

**Action**:
1. Create parent concept note
2. Make both existing notes children (up: to parent)
3. Clarify what distinguishes each
4. Add parent to MOC

---

## Merge Process

### Step 1: Select Primary

Choose based on:
- Which has better structure?
- Which has more content?
- Which has more incoming links?
- Which has better placement in MOC?

### Step 2: Content Migration

From secondary to primary:

```
1. Open both notes side by side
2. Identify unique content in secondary
3. Copy to appropriate section in primary
4. Note source if relevant: "(from [original note])"
5. Preserve valuable links from secondary
```

### Step 3: Link Update

```
1. Search for all links to secondary: [[Secondary Note]]
2. For each occurrence:
   a. Open the source note
   b. Update link to [[Primary Note]]
   c. Verify context still makes sense
3. Update any MOCs referencing secondary
```

### Step 4: Frontmatter Reconciliation

```
1. Merge related: arrays (dedupe)
2. Keep earlier created: date
3. Ensure up: points to correct MOC
```

### Step 5: Archive or Delete Secondary

**Archive** if:
- Uncertain about merge quality
- Historical value in keeping
- Contains unique metadata

**Delete** if:
- All content migrated
- No unique value remains
- Ready to clean up

### Step 6: Verification

```
1. Search for [[Secondary Note]] - should return no results
2. Check primary note links work
3. Verify MOC is updated
4. Run find_broken_links.py
```

---

## Prevention

### Habits to Prevent Duplicates

1. **Always search first**: Before creating, search for existing
2. **Use consistent naming**: Follow naming conventions
3. **Check MOC before adding**: Browse before creating
4. **Link liberally**: More links = easier duplicate detection
5. **Review regularly**: Monthly duplicate scan

### Naming Conventions

Reduce duplicates through consistent naming:

| Type | Convention | Example |
|------|------------|---------|
| Concept | Noun phrase | "Mental Model" |
| Process | Action noun | "Note Taking Process" |
| MOC | "[Topic] MOC" | "Psychology MOC" |
| Person | Full name | "Nick Milo" |
| Principle | Short phrase | "One Note One Idea" |

### Periodic Audits

Schedule regular duplicate checks:

**Weekly**: Review notes created that week for potential overlaps
**Monthly**: Run duplicate scan on heavily-used MOCs
**Quarterly**: Full vault duplicate audit

### Duplicate Scan Script

For systematic detection:

```bash
# Find notes with similar titles (manual review needed)
# Look for:
# - Plural/singular variations
# - Acronym/full name pairs
# - "My X" / "X" patterns
```

Consider building a custom script if duplicates are a recurring issue.

````

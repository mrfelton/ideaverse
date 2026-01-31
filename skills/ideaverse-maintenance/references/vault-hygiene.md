````markdown
# Vault Hygiene Reference

Comprehensive guide to maintaining a healthy Ideaverse vault through systematic hygiene practices.

## Table of Contents

1. [Hygiene Philosophy](#hygiene-philosophy)
2. [Maintenance Cadences](#maintenance-cadences)
3. [Archival Strategy](#archival-strategy)
4. [Link Health Management](#link-health-management)
5. [MOC Lifecycle](#moc-lifecycle)
6. [Hygiene Metrics](#hygiene-metrics)

---

## Hygiene Philosophy

### The Garden Metaphor

An Ideaverse vault is a knowledge garden, not a warehouse:

| Garden Approach | Warehouse Approach |
|-----------------|-------------------|
| Regular pruning | Let it accumulate |
| Intentional structure | Flat organization |
| Living relationships | Static storage |
| Periodic review | Set and forget |

**Core principle**: Small, consistent maintenance prevents large cleanups.

### Decay Patterns

Knowledge vaults decay in predictable ways:

1. **Link rot** - References to renamed/deleted notes
2. **Orphan proliferation** - Notes disconnected from structure
3. **MOC bloat** - Navigation structures grow unwieldy
4. **Frontmatter drift** - Inconsistent metadata over time
5. **Stale content** - Outdated information not archived
6. **Structure collapse** - Squeeze points ignored, navigation fails

### Prevention vs. Cure

| Decay Type | Prevention | Cure |
|------------|------------|------|
| Link rot | Update links on rename | Run `find_broken_links.py` |
| Orphans | Always add `up:` property | Triage with `find_orphans.py` |
| MOC bloat | Split at 40 links | Restructure at 50+ |
| Frontmatter | Use templates | Run `check_frontmatter.py` |
| Stale content | Archive completed work | Run `suggest_archival.py` |
| Structure | Honor squeeze points | Run `validate_squeeze_points.py` |

---

## Maintenance Cadences

### Daily Maintenance (5 minutes)

**Trigger**: End of each working day

**Checklist**:
- [ ] Review daily log for unprocessed items
- [ ] Quick check: any new notes missing `up:` property?
- [ ] Process any fleeting notes to proper locations

**Time investment**: ~5 minutes

### Weekly Maintenance (15-30 minutes)

**Trigger**: Weekly review session (e.g., Friday afternoon)

**Checklist**:
- [ ] Run `find_broken_links.py` - fix any issues
- [ ] Run `find_orphans.py` - quick triage (link, archive, or flag)
- [ ] Review notes created this week - spot-check frontmatter
- [ ] Check active Efforts - any ready for completion?

**Time investment**: 15-30 minutes

### Monthly Maintenance (1-2 hours)

**Trigger**: First week of each month

**Checklist**:
- [ ] Full diagnostic suite (all 6 scripts)
- [ ] Process all orphans identified
- [ ] Review MOC health - split any over 50 links
- [ ] Process squeeze points - create warranted MOCs
- [ ] Review archival suggestions - take action
- [ ] Generate vault health report
- [ ] Update any stale MOC descriptions

**Time investment**: 1-2 hours

### Quarterly Maintenance (Half day)

**Trigger**: End of quarter

**Checklist**:
- [ ] Comprehensive vault audit
- [ ] Review Archive folder - delete truly obsolete content
- [ ] Assess top-level MOC hierarchy - simplify if needed
- [ ] Review and update vault-level documentation
- [ ] Identify any structural improvements needed
- [ ] Plan any major reorganizations for upcoming quarter

**Time investment**: 3-4 hours

---

## Archival Strategy

### What to Archive

Archive content when:
- Project/effort is complete
- Information is outdated but historically valuable
- Content hasn't been accessed in 6+ months
- Temporary notes have served their purpose

### What NOT to Archive

Don't archive:
- Active reference material
- Evergreen concepts (move to Atlas/ instead)
- Templates and configuration notes
- Notes frequently linked from other places

### Archival Process

```
1. Identify archival candidate
    ↓
2. Extract reusable knowledge
    ├── Any concepts worth keeping? → Extract to Atlas/
    ├── Any processes documented? → Create process note in Atlas/
    └── Any useful templates? → Save to templates area
    ↓
3. Update references
    ├── Notes linking TO this note → Update or remove links
    └── MOCs containing this note → Remove from active sections
    ↓
4. Move to archive
    ├── Efforts/ items → Efforts/Archived/
    └── Other items → Designated archive location
    ↓
5. Update completion record
    └── Note in daily log or project summary
```

### Archive Organization

```
Efforts/Archived/
├── 2024/
│   ├── Q1/
│   │   └── [archived projects]
│   ├── Q2/
│   └── ...
└── 2025/
    └── ...
```

**Principle**: Archived content remains searchable but is excluded from active navigation structures.

---

## Link Health Management

### Link Types

| Link Type | Health Check |
|-----------|--------------|
| Forward links (outgoing) | Check targets exist |
| Back links (incoming) | Check for orphans |
| Frontmatter links | Check up:/related: targets |
| Transclusions | Check embedded notes exist |

### Healthy Link Patterns

**Good**:
```markdown
This concept relates to [[Existing Note]] and builds on [[Another Note]].
```

**Problematic**:
```markdown
See [[Probably Doesn't Exist]] for more details.
```

### Link Maintenance Workflow

```
When renaming a note:
    ↓
1. Use Obsidian's rename refactor (updates links automatically)
2. If manual rename: search for [[old name]] and update
3. Run find_broken_links.py to verify

When deleting a note:
    ↓
1. Search for [[note name]] in vault
2. Update or remove all references
3. Remove from MOCs
4. Then delete the note
```

---

## MOC Lifecycle

### MOC Creation (Squeeze Point)

MOCs should be created when:
- 10+ notes reference the same concept
- Navigation becomes difficult without structure
- Natural groupings emerge

MOCs should NOT be created:
- Preemptively for empty categories
- For < 5 related notes
- To mirror external taxonomies

### MOC Growth Phases

```
Phase 1: Nascent (5-15 links)
├── Simple flat list is fine
├── Brief section headers optional
└── Focus on capturing related notes

Phase 2: Established (15-40 links)
├── Organize into sections
├── Add context/descriptions
└── Ensure all relevant notes included

Phase 3: Mature (40-50 links)
├── Watch for bloat
├── Consider splitting
└── Identify natural sub-domains

Phase 4: Bloated (50+ links)
├── MUST restructure
├── Extract child MOCs
└── Parent becomes navigation hub
```

### MOC Splitting Process

```
1. Identify natural sub-groupings
    ↓
2. Create child MOC for largest group
    ├── Set up: to point to parent MOC
    ├── Move relevant links to child
    └── Add description
    ↓
3. Update parent MOC
    ├── Remove moved links
    ├── Add link to child MOC
    └── Describe the split
    ↓
4. Update affected notes
    └── Change up: from parent to child where appropriate
    ↓
5. Repeat for other groups if needed
```

---

## Hygiene Metrics

### Key Health Indicators

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Broken links | 0 | 1-5 | > 5 |
| Orphan ratio | < 5% | 5-15% | > 15% |
| Frontmatter compliance | > 95% | 80-95% | < 80% |
| Largest MOC size | < 40 | 40-60 | > 60 |
| Squeeze points | 0-2 | 3-5 | > 5 |

### Tracking Over Time

Recommend logging metrics in monthly health reports:

```yaml
---
type: log
created: YYYY-MM-DD
---

# Vault Health Report - YYYY-MM

## Metrics
- Total notes: X
- Broken links: X
- Orphan notes: X (Y%)
- Frontmatter issues: X
- MOC bloat warnings: X
- Squeeze points: X

## Actions Taken
- [describe fixes/improvements]

## Deferred
- [items for next review]
```

### Trend Analysis

Track month-over-month to identify:
- Decay acceleration (needs more frequent maintenance)
- Structural problems (recurring squeeze points)
- Process gaps (consistent frontmatter issues)

````

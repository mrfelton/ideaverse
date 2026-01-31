````markdown
# Enrichment Workflow Reference

Complete guide to the ARC (Add → Relate → Communicate) enrichment workflow for systematic knowledge assimilation.

## Table of Contents

1. [Workflow Overview](#workflow-overview)
2. [Phase 1: ADD](#phase-1-add)
3. [Phase 2: RELATE](#phase-2-relate)
4. [Phase 3: COMMUNICATE](#phase-3-communicate)
5. [Batch Processing](#batch-processing)
6. [Quality Gates](#quality-gates)

---

## Workflow Overview

The ARC workflow transforms raw information into connected knowledge.

```
Raw Input → ADD (capture) → RELATE (integrate) → COMMUNICATE (use) → Connected Knowledge
```

### Key Principles

1. **Speed in capture, care in connection**: Don't let organization slow capture; invest time in relation.
2. **Search before create**: Always check if the concept exists before adding.
3. **Atomic extraction**: One concept per note.
4. **Structure follows content**: Let MOCs emerge from content, not vice versa.

### Input Types

| Input Type | ADD Location | Processing Priority |
|------------|--------------|---------------------|
| Fleeting thought | Daily log | Process within 24h |
| Meeting notes | Daily log | Process same day |
| Article/book | Direct capture or source note | Process within week |
| Research batch | Synthesis note | Process in dedicated session |
| Experience insight | Daily log | Process when ready |

---

## Phase 1: ADD

**Goal**: Get information into the system without friction.

### Capture Locations

**Daily Log** (for temporal capture):
```markdown
## Captures

- Interesting idea about [[concept]] from conversation with [[Person]]
- Article to process: [Title](url) - key insight about X
- Thought: What if we applied [[Framework]] to [[Problem]]?
```

**Fleeting Note** (for ideas needing development):
```markdown
---
created: 2026-01-31
status: fleeting
---

# [Working Title]

Raw thoughts here. This needs processing.

- Point 1
- Point 2
- Question: ???

Source: [where this came from]
```

**Direct to Permanent** (for clear, complete ideas):
```markdown
---
up:
  - "[[Relevant MOC]]"
created: 2026-01-31
---

# [Concept Name]

[Complete note content]
```

### Capture Best Practices

1. **Include source**: Always note where information came from
2. **Add context**: Why does this matter? What triggered capture?
3. **Use provisional links**: `[[Maybe Related]]` signals "check this later"
4. **Flag for processing**: Use status: fleeting or add to inbox

### What NOT to Do in ADD Phase

- Don't spend time organizing
- Don't worry about perfect wording
- Don't search extensively
- Don't create complex structures
- Don't block on uncertainty

---

## Phase 2: RELATE

**Goal**: Transform captures into connected, permanent knowledge.

### Step 2.1: Pre-Creation Search

Before creating any note:

```
1. Search vault for exact concept name
   └── Found? → Update existing note

2. Search for synonyms/related terms
   └── Found similar? → Consider merging or linking

3. Browse relevant MOC(s)
   └── Similar concept listed? → Verify distinction

4. Check daily logs for prior mentions
   └── Already captured elsewhere? → Consolidate
```

**Decision tree**:
```
Concept already exists?
├── Yes, exact → Update that note
├── Yes, similar → Decide: merge or differentiate
└── No → Proceed with creation
```

### Step 2.2: Knowledge Classification

Determine the type of knowledge:

| Type | Characteristics | Signal Words |
|------|-----------------|--------------|
| **Concept** | Abstract idea, framework, model | "is a", "means", "framework for" |
| **Process** | Steps, workflow, procedure | "how to", "steps", "workflow" |
| **Entity** | Person, org, tool, place | Proper names, specific instances |
| **Principle** | Rule, heuristic, guideline | "always", "never", "when X, do Y" |

Select appropriate extraction pattern based on type.

### Step 2.3: Atomic Extraction

Extract ONE concept per note:

```markdown
---
up:
  - "[[Parent MOC]]"
related:
  - "[[Connected Concept]]"
created: YYYY-MM-DD
---

# [Concept Name]

[Focused content about this ONE concept]
```

**Atomic note test**:
- Can this note have a clear, specific title?
- Does it discuss ONE main idea?
- Could someone understand this without other notes? (through its links)

If a note covers multiple concepts, split it.

### Step 2.4: Connection Building

**Set up: property**:
```yaml
up:
  - "[[Most Relevant MOC]]"
```

Rules for `up:`:
- Choose the most natural conceptual parent
- Prefer specific MOCs over general ones
- Daily logs typically don't need `up:`
- Most notes have ONE parent

**Set related: property**:
```yaml
related:
  - "[[Lateral Connection 1]]"
  - "[[Lateral Connection 2]]"
```

Rules for `related:`:
- Links to concepts on same level (not parent/child)
- Only include genuine conceptual relationships
- Empty is okay: `related: []`

**Update parent MOC**:
- Add new note to appropriate section
- Consider if section headers need adjustment
- Keep MOC organized

**Add back-links** (optional but valuable):
- Update related notes to link back
- Strengthens graph connectivity

### Step 2.5: Consistency Validation

Checklist before marking complete:
- [ ] Frontmatter has `up:` pointing to valid MOC
- [ ] Frontmatter has `created:` date
- [ ] Note added to parent MOC
- [ ] Any `related:` links are valid notes
- [ ] Title is clear and specific
- [ ] Content is focused (atomic)
- [ ] No duplicate concept created

---

## Phase 3: COMMUNICATE

**Goal**: Use connected knowledge; complete the cycle.

### Usage Patterns

**Reference in daily logs**:
```markdown
Today I applied [[Concept Name]] to the project. See [[Related Work]].
```

**Build on existing knowledge**:
```markdown
Building on [[Foundation Concept]], I realized [[New Insight]].
```

**Create output from notes**:
```markdown
This document draws from:
- [[Concept A]]
- [[Concept B]]
- [[Process C]]
```

### Completion Tracking

Log enrichment in daily log:
```markdown
## Knowledge Work

- Processed article: [Title] → extracted [[Concept 1]], [[Concept 2]]
- Updated [[MOC Name]] with new structure
- Merged duplicate notes on [topic]
```

---

## Batch Processing

For processing multiple items efficiently.

### Batch Workflow

```
1. Gather: Collect all items to process
    ↓
2. Triage: Sort by type and priority
    │   ├── Quick wins (5 min each)
    │   ├── Standard processing (15 min each)
    │   └── Deep work (30+ min each)
    ↓
3. Process: Work through in priority order
    │   ├── Quick wins first (momentum)
    │   ├── Then standard items
    │   └── Deep work if time remains
    ↓
4. Validate: Run checks on all new notes
    ↓
5. Record: Log batch processing in daily note
```

### Time Boxing

| Item Complexity | Time Box | Notes |
|-----------------|----------|-------|
| Simple concept | 5-10 min | Single note, clear placement |
| Standard item | 15-20 min | Note + MOC update + links |
| Complex item | 30-45 min | Multiple notes, research needed |
| Research synthesis | 1-2 hours | Multiple sources, structure work |

### Batch Size Guidelines

- Daily: 3-5 quick items
- Weekly session: 10-15 items
- Deep processing: 3-5 complex items

Don't over-batch. Quality degrades with fatigue.

---

## Quality Gates

Checkpoints to ensure enrichment quality.

### Gate 1: Pre-Creation

Before creating ANY note:
- [ ] Searched for existing coverage
- [ ] Identified knowledge type
- [ ] Chose appropriate parent MOC

### Gate 2: Post-Creation

After creating note:
- [ ] Frontmatter complete (up, created)
- [ ] Title is specific and clear
- [ ] Content is atomic (one concept)
- [ ] Links are valid

### Gate 3: Integration

After connecting:
- [ ] Note added to parent MOC
- [ ] Related links established where warranted
- [ ] No broken links introduced

### Gate 4: Validation (Weekly)

Run periodically:
```bash
python3 find_broken_links.py /path/to/vault
python3 find_orphans.py /path/to/vault
python3 check_frontmatter.py /path/to/vault
```

---

## Common Enrichment Scenarios

### Scenario: Article Processing

```
1. Read article, highlight key points
2. Create source note (optional)
3. Extract 2-5 atomic concepts
4. For each concept:
   - Classify (concept/process/principle)
   - Search for existing coverage
   - Create or update note
   - Add to MOC
5. Link concepts to each other
6. Log in daily note
```

### Scenario: Meeting Insights

```
1. Capture in daily log during/after meeting
2. Same day: review capture
3. Identify any generalizable insights
4. Extract insights to permanent notes
5. Link back to daily log for context
```

### Scenario: Learning a New Domain

```
1. Create overview MOC for domain
2. Process sources incrementally
3. Extract concepts as you learn
4. Let structure emerge from content
5. Reorganize MOC as understanding deepens
```

````

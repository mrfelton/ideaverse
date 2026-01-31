# Ideaverse Workflows

The core workflow methodology for Ideaverse-based vaults: ARC (Add → Relate → Communicate).

## Table of Contents

1. [The ARC Workflow](#the-arc-workflow)
2. [Creating and Evolving MOCs](#creating-and-evolving-mocs)
3. [Daily Log Maintenance](#daily-log-maintenance)
4. [Work Completion & Knowledge Extraction](#work-completion--knowledge-extraction)
5. [Cross-Reference Discovery](#cross-reference-discovery)

---

## The ARC Workflow

The complete ADD → RELATE → COMMUNICATE cycle for knowledge management.

### Phase 1: ADD (Capture)

**Goal**: Get information into the system without friction.

```
Input arrives (article, idea, meeting notes, inspiration, etc.)
    ↓
Capture to:
    - Today's Daily Log (temporal record)
    - Direct note if immediate capture
    - Fleeting notepad (if available)
    ↓
Mark with tentative status (draft if using status field)
    ↓
Do NOT organize yet - avoid decision fatigue
```

**Key Principle**: Speed and capture matter. Organization happens later.

### Phase 2: RELATE (Connect)

**Goal**: Transform raw capture into connected knowledge.

**Step 2.1: Search Before Creating**

```
Search vault for existing notes on the concept
    ↓
If found → Update existing note, add new information
If not found → Continue to Step 2.2
```

**Step 2.2: Read Relevant MOCs**

```
Identify the domain or subject area
    ↓
Read relevant MOC(s) in your vault
    - Understand existing structure
    - Note related concepts already captured
    - Identify where new concept fits
```

**Step 2.3: Extract Atomic Notes**

```
For each distinct concept in the capture:
    ↓
Create ONE note with:
    - Single focused idea
    - Proper frontmatter (up, related, created)
    - Clear, descriptive title
    ↓
Place in appropriate location (Atlas, Calendar, or work area)
```

**Step 2.4: Set Relationship Properties**

```
For each new note, add frontmatter:
    ↓
up: property pointing to parent MOC:
    up:
      - "[[Parent MOC]]"
    ↓
related: property for lateral connections:
    related:
      - "[[Related Concept A]]"
      - "[[Related Concept B]]"
    ↓
Update the MOC to include the new note
    ↓
Check related notes - add forward links if relevant
```

**Step 2.5: Squeeze Point Check**

```
Count how many notes link to an unstructured term
    ↓
If > 10 links without an MOC → Create a new MOC for that term
If < 10 → Continue, structure will emerge naturally
```

### Phase 3: COMMUNICATE (Express)

**Goal**: Use connected knowledge to produce output.

```
Create output note or project artifact
    ↓
Link (don't copy) from existing notes:
    - Use transclusion: ![[Note Name]] to embed content
    - Or standard links: [[Note Name]] to reference
    ↓
Assemble output from connected thoughts
    ↓
When work completes → Extract reusable knowledge back to permanent store
```

---

## Creating and Evolving MOCs

Maps of Content are the navigation layer. Create them at the right time - not too early, not too late.

### When to Create an MOC

**The Mental Squeeze Point**: Create an MOC when:

- You have 10+ notes on a topic with no structure
- You feel overwhelmed navigating a concept area
- You're linking to the same term repeatedly

**Do NOT create an MOC**:

- Preemptively for empty categories
- For topics with < 5 related notes
- Just to mirror an external taxonomy

**Principle**: Structure should be earned, not pre-built.

### MOC Creation Procedure

```
1. Identify the concept needing structure
    ↓
2. Search vault for all related notes
    - Wikilink search: [[concept
    - Text search for mentions
    - Browse related areas
    ↓
3. Create MOC file
    - Title: "[Concept] MOC" (e.g., "Programming MOC")
    - Frontmatter with up: and in: properties
    ↓
4. Group related notes by sub-theme
    - Use ## headers for categories
    - Add brief descriptions
    ↓
5. Add links to all relevant notes
    - Include short context where helpful
    ↓
6. Update linked notes' frontmatter
    - Add MOC to their up: property
```

### MOC Structure Template

```yaml
---
up:
  - "[[Home]]"  # or appropriate parent
related:
  - "[[Related MOC]]"
created: YYYY-MM-DD
in:
  - "[[Maps]]"
---
```

```markdown
# [Concept] MOC

Brief description of what this MOC covers and why it matters.

## [Sub-theme 1]
- [[Note A]] - brief context
- [[Note B]]

## [Sub-theme 2]
- [[Note C]]
- [[Note D]] - brief context
```

### Evolving Existing MOCs

```
When adding a note to an existing MOC:
    ↓
1. Read the MOC structure first
2. Identify the correct section
3. Add the link with context if needed
4. If no section fits → Consider adding a new section
5. If MOC is growing (50+ links) → Consider splitting into sub-MOCs
```

---

## Daily Log Maintenance

The daily log is the temporal anchor - everything that happens "today" goes here.

### Creating Today's Log

```
1. Create file: Calendar/Days/YYYY-MM-DD.md
2. Add basic frontmatter with created: date
3. Fill with daily content
```

### What Goes in Daily Logs

| Include | Don't Include |
|---------|---------------|
| Achievements and progress | Permanent knowledge (extract to Atlas) |
| Decisions made | Detailed how-to guides (extract to Atlas) |
| Meeting summaries | Long-form content (extract to Atlas) |
| Ideas and sparks (to process later) | |
| Links to notes created/updated | |
| Blockers and next steps | |

### End of Day Review

```
Before closing the day:
    ↓
1. Review captured items
    - Any fleeting notes to process? → Mark for RELATE workflow
    - Any decisions to document? → Link to relevant notes
    ↓
2. Add links throughout the log
    - Link to people mentioned: [[Person Name]]
    - Link to projects/topics worked on: [[Topic]]
    - Link to concepts discussed: [[Concept]]
    ↓
3. Set priorities for tomorrow
    - Add to "Next Steps" section
    - Update any project/work lists as needed
```

---

## Work Completion & Knowledge Extraction

When a project or initiative completes, extract reusable knowledge before archiving.

### Knowledge Extraction Checklist

```
Before closing/archiving work:
    ↓
1. IDENTIFY reusable knowledge
    - Processes that worked well
    - Concepts and frameworks learned
    - Decisions made and their rationale
    - Useful templates or artifacts
    ↓
2. EXTRACT to permanent store
    For each reusable item:
        - Create atomic note
        - Add proper frontmatter (up, related, created)
        - Link back to original work
        - Add to relevant MOC
    ↓
3. CREATE completion summary
    - What was accomplished
    - Key learnings (linked to extraction notes)
    - What worked and what didn't
    ↓
4. UPDATE references
    - Remove from active work lists
    - Archive the work container
    - Ensure MOCs still link to extracted knowledge
```

### Post-Completion Access

Archived work remains searchable and linkable. The reusable knowledge lives on in the permanent store; the work folder is just the historical container.

---

## Cross-Reference Discovery

After adding or updating content, proactively find and create connections.

### Discovery Procedure

```
After creating/updating a note:
    ↓
1. IDENTIFY key terms in the note
    - Concepts, entities, themes
    ↓
2. SEARCH for related notes
    - Wikilink search: [[term
    - Text search: "term"
    - Check MOCs in related areas
    ↓
3. For each meaningful match:
    - Add link FROM new note TO existing note
    - Add back-link FROM existing note TO new note
    ↓
4. UPDATE MOCs
    - If new note fits an existing MOC → Add it
    - If MOC should reference this note → Update it
```

### When to Add Back-References

Add a back-reference when:

- The existing note would benefit from knowing about the new note
- Future readers of the existing note should discover the new concept
- There's a genuine conceptual relationship

Do NOT add back-references for:

- Superficial keyword matches
- Every note that mentions the same word
- References that add no navigational value

### Maintenance Sweeps

Periodically (weekly, monthly, or quarterly):

```
1. Review orphan notes (no incoming links)
    - Should they be linked? → Add connections
    - Are they still relevant? → Archive or consolidate
    ↓
2. Review MOCs for completeness
    - Any new notes missing? → Add them
    - Any dead links? → Fix or remove
    ↓
3. Check for emergent patterns
    - Topics with many unstructured notes → Create MOC
    - Duplicate concepts → Merge notes
    - Over-crowded MOCs → Split into sub-MOCs
```

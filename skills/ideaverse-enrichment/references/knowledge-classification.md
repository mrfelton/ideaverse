````markdown
# Knowledge Classification Reference

Deep dive into the four knowledge types and their extraction patterns.

## Table of Contents

1. [Classification Framework](#classification-framework)
2. [Type 1: Concepts](#type-1-concepts)
3. [Type 2: Processes](#type-2-processes)
4. [Type 3: Entities](#type-3-entities)
5. [Type 4: Principles](#type-4-principles)
6. [Edge Cases](#edge-cases)

---

## Classification Framework

### Why Classify?

Different knowledge types benefit from different structures:
- Concepts need relationship mapping
- Processes need step sequencing
- Entities need attribute tracking
- Principles need boundary conditions

Correct classification → better note structure → more useful knowledge.

### Quick Classification Guide

| If the knowledge... | It's probably a... |
|---------------------|-------------------|
| Describes what something IS | Concept |
| Describes HOW to do something | Process |
| Is about a specific instance | Entity |
| Tells you what you SHOULD do | Principle |

### Classification Decision Tree

```
Is this about a specific instance (person, org, tool)?
├── Yes → Entity
└── No ↓

Does this describe a sequence of actions?
├── Yes → Process
└── No ↓

Is this prescriptive (a rule or guideline)?
├── Yes → Principle
└── No → Concept
```

---

## Type 1: Concepts

### Definition

Concepts are abstract ideas, frameworks, mental models, or theories that help you understand something.

### Identifying Concepts

**Signal language**:
- "X is a..."
- "The idea of..."
- "This framework..."
- "The theory that..."
- "A way of thinking about..."

**Examples**:
- "Compound Interest" (financial concept)
- "Second Brain" (productivity concept)
- "Emergence" (systems concept)
- "Squeeze Point" (Ideaverse concept)

### Concept Note Structure

```markdown
---
up:
  - "[[Domain MOC]]"
related:
  - "[[Related Concept]]"
  - "[[Contrasting Concept]]"
created: YYYY-MM-DD
---

# [Concept Name]

One-line definition that captures the essence.

## Core Idea

What is this concept fundamentally about? Expand the definition.
Explain it as if to someone unfamiliar with the domain.

## Key Principles

What are the essential elements or rules of this concept?

- Principle 1: ...
- Principle 2: ...
- Principle 3: ...

## Connections

How does this concept relate to other ideas?

- It builds on [[Foundation Concept]] by...
- It contrasts with [[Different Approach]] in that...
- It's a specific case of [[Broader Concept]]

## Applications

Where and when does this concept apply?

- In [context 1], it helps with...
- When [situation], apply this by...

## Examples

Concrete instances that illustrate the concept:

1. Example 1: [description]
2. Example 2: [description]
```

### Concept Quality Checklist

- [ ] Definition is concise and clear
- [ ] Core idea explains the "why"
- [ ] Key principles are specific, not vague
- [ ] Connections show relationships (not just mentions)
- [ ] Examples are concrete

---

## Type 2: Processes

### Definition

Processes are sequences of actions that produce an outcome. They describe HOW to do something.

### Identifying Processes

**Signal language**:
- "How to..."
- "Steps for..."
- "The process of..."
- "Workflow for..."
- "First... then... finally..."

**Examples**:
- "ARC Workflow" (knowledge process)
- "Morning Routine" (personal process)
- "Code Review Process" (engineering process)
- "Decision-Making Framework" (thinking process)

### Process Note Structure

```markdown
---
up:
  - "[[Processes MOC]]"
related:
  - "[[Related Process]]"
created: YYYY-MM-DD
---

# [Process Name]

Brief description of what this process accomplishes and when to use it.

## When to Use

Triggers or conditions that indicate this process is appropriate:

- When [situation 1]
- When [situation 2]
- NOT when [exception]

## Prerequisites

What's needed before starting?

- [ ] Prerequisite 1
- [ ] Prerequisite 2
- [ ] Access to [resource]

## Steps

### Step 1: [Action Name]

Description of what to do.

- Sub-step if needed
- Key point to remember

### Step 2: [Action Name]

Description of what to do.

### Step 3: [Action Name]

Description of what to do.

## Decision Points

Critical junctures where the path may vary:

**If [condition A]:**
→ Do [action A]

**If [condition B]:**
→ Do [action B]

## Common Variations

Alternative approaches for different contexts:

- **Variation 1**: When [context], modify step X by...
- **Variation 2**: For [situation], skip steps Y-Z

## Failure Modes

What can go wrong and how to recover:

| Problem | Symptom | Solution |
|---------|---------|----------|
| Issue 1 | [what you see] | [how to fix] |
| Issue 2 | [what you see] | [how to fix] |
```

### Process Quality Checklist

- [ ] Clear trigger for when to use
- [ ] Prerequisites are explicit
- [ ] Steps are actionable (verbs)
- [ ] Decision points surface choices
- [ ] Failure modes help troubleshoot

---

## Type 3: Entities

### Definition

Entities are specific instances: people, organizations, tools, products, places. They have unique identities.

### Identifying Entities

**Signal language**:
- Proper names
- "This person/company/tool..."
- Specific instance, not a category

**Examples**:
- "Nick Milo" (person)
- "Obsidian" (tool)
- "LYT" (framework/product)
- "Y Combinator" (organization)

### Entity Note Structure

```markdown
---
up:
  - "[[People MOC]]"  # or Tools, Organizations, etc.
related:
  - "[[Related Entity]]"
created: YYYY-MM-DD
---

# [Entity Name]

Brief one-line description of what/who this is.

## Identity

Core identifying information:

- **Type**: [Person/Tool/Org/Place]
- **Key attribute 1**: value
- **Key attribute 2**: value

## Relationships

How this entity connects to your world:

- Works with [[Person]]
- Created by [[Organization]]
- Used for [[Domain]]
- Part of [[Larger System]]

## Context

Why does this entity matter to you?
What role does it play in your knowledge/work?

## History

Key events or timeline (if relevant):

- YYYY: [Event]
- YYYY: [Event]

## Notes

Additional observations, quotes, or details:

- Note 1
- Note 2
```

### Entity-Specific Templates

**For People**:
```markdown
## Identity
- **Role**: [job/relationship]
- **Organization**: [[Where they work]]
- **Expertise**: [domains]

## Interactions
- Met on [date/context]
- Key conversations: ...
```

**For Tools**:
```markdown
## Identity
- **Type**: [app/service/hardware]
- **Category**: [productivity/development/etc]
- **URL**: [link]

## Usage
- What I use it for: ...
- Key features: ...
- Limitations: ...
```

### Entity Quality Checklist

- [ ] Identity is clear (what/who)
- [ ] Relationships show connections
- [ ] Context explains relevance to you
- [ ] Not confused with a concept

---

## Type 4: Principles

### Definition

Principles are rules, heuristics, or guidelines that prescribe behavior. They tell you what you SHOULD do.

### Identifying Principles

**Signal language**:
- "Always..."
- "Never..."
- "When X, do Y"
- "The rule is..."
- "Best practice is..."

**Examples**:
- "One Note, One Idea" (atomicity principle)
- "Search Before Create" (deduplication principle)
- "Ship Early, Ship Often" (development principle)
- "Don't Repeat Yourself (DRY)" (coding principle)

### Principle Note Structure

```markdown
---
up:
  - "[[Principles MOC]]"
related:
  - "[[Related Principle]]"
created: YYYY-MM-DD
---

# [Principle Name]

The principle stated clearly in one sentence.

> "Quote version if applicable"

## Definition

What does this principle mean in practical terms?
Expand on the one-liner with concrete explanation.

## When It Applies

Conditions or contexts where this principle is relevant:

- In [context 1], because...
- When [situation], because...
- Applies to [domain]

## How to Apply

Practical guidance for implementing this principle:

1. Action 1
2. Action 2
3. Action 3

## Counter-Examples

When does this principle NOT apply?

- Exception 1: When [condition], instead do [alternative]
- Exception 2: [Context] where this principle would cause harm

This principle can conflict with [[Other Principle]] in cases of...

## Why It Matters

The reasoning behind this principle:

- Without it, [negative outcome]
- With it, [positive outcome]
- It exists because [root cause]

## Related Principles

- [[Complementary Principle]] - works well together
- [[Contrasting Principle]] - represents a trade-off
```

### Principle Quality Checklist

- [ ] Core statement is crisp and memorable
- [ ] Application context is clear
- [ ] Counter-examples show boundaries
- [ ] Rationale explains the WHY
- [ ] Related principles show trade-offs

---

## Edge Cases

### Hybrid Knowledge

Some knowledge spans multiple types:

**"Agile" could be**:
- Concept (the philosophy)
- Process (the methodology)
- Principle (the values)

**Solution**: Create multiple notes or choose primary type with sections for others.

### Abstract vs. Concrete

- "Leadership" (abstract concept)
- "How to Run a 1:1" (concrete process)
- "My Leadership Philosophy" (personal principle)

**Tip**: The more actionable it is, the more it tends toward Process or Principle.

### When Unsure

If classification is unclear:
1. Start with your best guess
2. Use the corresponding template
3. If it feels wrong, reclassify
4. Some knowledge just doesn't fit neatly - that's okay

The goal is useful structure, not perfect taxonomy.

````

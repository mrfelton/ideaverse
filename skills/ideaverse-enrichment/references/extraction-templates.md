````markdown
# Extraction Templates & Guidelines

Detailed templates and workflows for extracting each knowledge type into Ideaverse notes.

## Table of Contents

1. [Type 1: Concepts](#type-1-concepts)
2. [Type 2: Processes](#type-2-processes)
3. [Type 3: Entities](#type-3-entities)
4. [Type 4: Principles](#type-4-principles)

---

## Type 1: Concepts

### Signal Words

Use when you encounter: "is a", "means", "framework for", "the idea of", "model of", "theory of"

### Pre-Extraction Checklist

- [ ] Searched for existing notes on this concept
- [ ] Searched for synonyms/related terms
- [ ] Checked relevant MOC(s) for similar ideas
- [ ] Confirmed this is genuinely NEW knowledge

### Template

```markdown
---
up:
  - "[[{Relevant MOC}]]"
related:
  - "[[{Connected Concept}]]"
created: {YYYY-MM-DD}
---

# {Concept Name}

{One-line definition capturing the essence.}

## Core Idea

{What is this concept fundamentally about? Explain as if to someone unfamiliar.}

## Key Principles

- {Principle 1}
- {Principle 2}
- {Principle 3}

## Connections

{How does this relate to other existing concepts in the vault?}

- Builds on [[{Foundation}]] by...
- Contrasts with [[{Alternative}]] in that...
- Represents a specific case of [[{Broader Concept}]]

## Applications

{Where/when does this concept apply?}

- In {context 1}, it helps with...
- When {situation}, apply this by...

## Examples

{Concrete instances illustrating this concept:}

1. {Example 1}
2. {Example 2}
```

### Extraction Guidelines

**Definition Quality**
- Keep to 1-2 sentences
- Avoid jargon unless defining jargon
- Should be understandable without other notes

**Connection Mapping** — Focus on three relationship types:
1. **Foundation**: What concepts does this build on?
2. **Contrast**: What is this NOT? What alternative exists?
3. **Abstraction**: Is this a specific case of something broader?

**Example Selection** — Good examples are:
- Concrete, not abstract
- Familiar to your context
- Illustrative of the core idea

### Post-Extraction Checklist

- [ ] Frontmatter has `up:` pointing to valid MOC
- [ ] Frontmatter has `created:` date
- [ ] Note added to parent MOC
- [ ] At least one `related:` link established
- [ ] No duplicate concept created
- [ ] Logged enrichment in daily note

### Quality Signals

**Strong**:
- Definition is quotable
- Someone could explain it after reading
- Connections reveal non-obvious relationships
- Examples make it concrete

**Weak** (revise):
- Definition is circular or vague
- No connections established
- Examples are too abstract
- Overlaps significantly with existing note

---

## Type 2: Processes

### Signal Words

Use when you encounter: "how to", "steps for", "process of", "workflow", "first... then... finally"

### Pre-Extraction Checklist

- [ ] Searched for existing process notes on this topic
- [ ] Checked if this is a variation of an existing process
- [ ] Identified the appropriate MOC (often Processes or domain-specific)
- [ ] Confirmed this process is worth documenting

### Template

```markdown
---
up:
  - "[[{Relevant MOC}]]"
related:
  - "[[{Related Process}]]"
created: {YYYY-MM-DD}
---

# {Process Name}

{Brief description of what this process accomplishes.}

## When to Use

{Triggers or conditions indicating this process is appropriate:}

- When {situation 1}
- When {situation 2}
- NOT when {exception}

## Prerequisites

{What's needed before starting?}

- [ ] {Prerequisite 1}
- [ ] {Prerequisite 2}
- [ ] Access to {resource}

## Steps

### Step 1: {Action Name}

{Description of what to do.}

- {Sub-step if needed}
- {Key point to remember}

### Step 2: {Action Name}

{Description of what to do.}

### Step 3: {Action Name}

{Description of what to do.}

## Decision Points

{Critical junctures where the path varies:}

**If {condition A}:**
→ Do {action A}

**If {condition B}:**
→ Do {action B}

## Common Variations

{Alternative approaches for different contexts:}

- **{Variation 1}**: When {context}, modify step X by...
- **{Variation 2}**: For {situation}, skip steps Y-Z

## Failure Modes

{What can go wrong and how to recover:}

| Problem | Symptom | Solution |
|---------|---------|----------|
| {Issue 1} | {what you see} | {how to fix} |
| {Issue 2} | {what you see} | {how to fix} |
```

### Extraction Guidelines

**Step Granularity**
- Each step should be a single, clear action
- Use verbs: "Create", "Review", "Update", not "The creation of"
- If a step has >3 sub-steps, consider splitting

**Decision Point Clarity**
- Make conditions explicit and testable
- Include both paths (if A, then X; else Y)
- Don't hide decisions inside steps

**Failure Mode Coverage**
- Include at least 2-3 common failure modes
- Focus on recoverable errors
- Add prevention hints where possible

**Prerequisites vs. Steps**
- Prerequisites: things you need BEFORE starting
- Steps: actions you take DURING the process
- Don't mix them

### Post-Extraction Checklist

- [ ] Frontmatter has `up:` pointing to valid MOC
- [ ] Frontmatter has `created:` date
- [ ] Note added to parent MOC
- [ ] Related processes linked (similar, prerequisite, or follow-up)
- [ ] Steps are numbered and actionable
- [ ] Decision points are explicit
- [ ] Logged enrichment in daily note

### Quality Signals

**Strong**:
- Someone could follow it cold
- Decision points are clear
- Failure modes help troubleshoot
- Variations cover common cases

**Weak** (revise):
- Steps are vague ("do the thing")
- Missing decision logic
- No failure mode coverage
- Assumes too much context

---

## Type 3: Entities

### Signal Words

Use when you encounter: Proper names, specific instances, "this person/company/tool", "the [specific thing]"

### Pre-Extraction Checklist

- [ ] Searched for existing note on this entity
- [ ] Confirmed this is a specific instance, not a concept
- [ ] Identified the appropriate MOC (People, Tools, Organizations, etc.)
- [ ] Have enough information to make the note useful

### Person Template

```markdown
---
up:
  - "[[People MOC]]"
related:
  - "[[{Related Person}]]"
  - "[[{Organization}]]"
created: {YYYY-MM-DD}
---

# {Person Name}

{One-line description of who this is and why they matter to you.}

## Identity

- **Role**: {job title/relationship to you}
- **Organization**: [[{Where they work}]]
- **Expertise**: {domains they're known for}
- **Contact**: {if relevant, how to reach them}

## Relationships

- Works with [[{Colleague}]]
- Connection through [[{How you know them}]]
- Mentioned by [[{Source}]]

## Context

{Why does this person matter to you? What role do they play in your knowledge/work?}

## Interactions

{Key interactions or touchpoints:}

- {Date}: {Context of meeting/interaction}
- Key insight from them: "{quote or paraphrase}"

## Notes

{Additional observations, impressions, or details:}

- {Note 1}
- {Note 2}
```

### Tool Template

```markdown
---
up:
  - "[[Tools MOC]]"
related:
  - "[[{Alternative Tool}]]"
created: {YYYY-MM-DD}
---

# {Tool Name}

{One-line description of what this tool does.}

## Identity

- **Type**: {app/service/hardware/library}
- **Category**: {productivity/development/communication/etc.}
- **URL**: [{domain}]({full URL})
- **Pricing**: {free/paid/freemium}

## Usage

{What do you use this tool for?}

- Primary use: {main workflow}
- Secondary use: {other uses}

## Key Features

{Features that matter to you:}

- {Feature 1}: {why it matters}
- {Feature 2}: {why it matters}

## Limitations

{What doesn't work or causes friction:}

- {Limitation 1}
- {Limitation 2}

## Alternatives

- [[{Alternative 1}]] - {comparison note}
- [[{Alternative 2}]] - {comparison note}

## Notes

{Additional observations:}

- {Note 1}
```

### Organization Template

```markdown
---
up:
  - "[[Organizations MOC]]"
related:
  - "[[{Related Org}]]"
created: {YYYY-MM-DD}
---

# {Organization Name}

{One-line description of what this organization is/does.}

## Identity

- **Type**: {company/non-profit/community/team}
- **Industry**: {sector}
- **Size**: {if known}
- **URL**: [{domain}]({full URL})

## Key People

- [[{Person 1}]] - {role}
- [[{Person 2}]] - {role}

## Relationship

{How do you interact with this organization?}

- {Customer/partner/employee/observer}
- Connection through: {how you know them}

## Products/Services

{What do they offer that's relevant to you?}

- [[{Product 1}]]
- [[{Service 1}]]

## Context

{Why does this organization matter to your knowledge/work?}

## Notes

{Additional observations:}
```

### Extraction Guidelines

**Identity vs. Context**
- **Identity**: Objective facts (role, URL, type)
- **Context**: Subjective relevance (why this matters to YOU)
- Both are important - don't skip context

**Relationship Mapping**
- Link to OTHER entities in your vault
- Show how this entity connects to your world
- Update related entity notes to link back

**Time Sensitivity**
- Entity information changes over time
- Include dates where relevant
- Review periodically for accuracy

**Level of Detail**
- More detail for high-relevance entities
- Minimal stubs OK for passing references
- Can always expand later

### Post-Extraction Checklist

- [ ] Frontmatter has `up:` pointing to type-appropriate MOC
- [ ] Frontmatter has `created:` date
- [ ] Note added to parent MOC
- [ ] Related entities linked (people, orgs, tools)
- [ ] Context explains relevance to you
- [ ] Any referenced entities have notes (or stubs)
- [ ] Logged enrichment in daily note

### Quality Signals

**Strong**:
- Clear identity information
- Relationships show network connections
- Context explains why you care
- Useful for future reference

**Weak** (revise):
- Just a name with no context
- No relationship mapping
- Unclear why this entity matters
- Could be confused with a concept note

---

## Type 4: Principles

### Signal Words

Use when you encounter: "always", "never", "when X do Y", "the rule is", "best practice", "should/shouldn't"

### Pre-Extraction Checklist

- [ ] Searched for existing notes on this principle
- [ ] Checked for synonymous principles (same rule, different name)
- [ ] Identified if this is truly prescriptive (not just descriptive)
- [ ] Found the appropriate MOC (often Principles or domain-specific)

### Template

```markdown
---
up:
  - "[[{Relevant MOC}]]"
related:
  - "[[{Complementary Principle}]]"
  - "[[{Contrasting Principle}]]"
created: {YYYY-MM-DD}
---

# {Principle Name}

{The principle stated clearly in one memorable sentence.}

> "{Optional: quotable version or source attribution}"

## Definition

{What does this principle mean in practical terms? Expand on the one-liner.}

## When It Applies

{Conditions or contexts where this principle is relevant:}

- In {context 1}, because...
- When {situation}, because...
- Applies to {domain}

## How to Apply

{Practical guidance for implementing this principle:}

1. {Action 1}
2. {Action 2}
3. {Action 3}

## Counter-Examples

{When does this principle NOT apply?}

- **Exception 1**: When {condition}, instead do {alternative}
- **Exception 2**: In {context}, this causes {harm}

{This principle can conflict with [[{Other Principle}]] when...}

## Why It Matters

{The reasoning behind this principle:}

- Without it: {negative outcome}
- With it: {positive outcome}
- Root cause: {why this rule exists}

## Related Principles

- [[{Complementary Principle}]] - works well together
- [[{Contrasting Principle}]] - represents a trade-off
- [[{More Specific Principle}]] - applies this in {context}
```

### Extraction Guidelines

**Statement Quality** — The principle statement should be:
- **Memorable**: Easy to recall and repeat
- **Actionable**: Clear what to do differently
- **Testable**: Can tell if you're following it or not

**Good**: "Search before you create"
**Weak**: "Try to avoid creating duplicate notes when possible"

**Exception Mapping** — Finding counter-examples is critical:
- When does this rule break down?
- What's the boundary condition?
- When does the opposite rule apply?

(No exceptions = suspicious. Most principles have limits.)

**Trade-off Identification** — Principles often trade off against each other:
- "Move fast" vs. "Be careful"
- "Be thorough" vs. "Be brief"
- "Optimize for now" vs. "Optimize for later"

Identify what this principle trades against.

**Source Attribution** — If the principle comes from someone specific:
- Quote them directly if possible
- Link to the source material
- Note the original context

### Pattern Examples

**Directive Pattern**
```markdown
# Always Do X

Do X in all situations.

## Counter-Examples
- Unless Y, then don't do X
```

**Conditional Pattern**
```markdown
# When A, Do B

In situation A, the right action is B.

## Counter-Examples
- But if C, then do D instead
```

**Prohibition Pattern**
```markdown
# Never Do X

Avoid X because of negative outcome Y.

## Counter-Examples
- Exception: When Z, X is acceptable
```

**Heuristic Pattern**
```markdown
# Prefer X Over Y

When choosing between X and Y, lean toward X.

## Counter-Examples
- But when Z, prefer Y
```

### Post-Extraction Checklist

- [ ] Frontmatter has `up:` pointing to valid MOC
- [ ] Frontmatter has `created:` date
- [ ] Note added to parent MOC
- [ ] Related principles linked (complementary and contrasting)
- [ ] At least one counter-example documented
- [ ] "How to Apply" section is actionable
- [ ] "Why It Matters" explains the rationale
- [ ] Logged enrichment in daily note

### Quality Signals

**Strong**:
- Statement is crisp and memorable
- Clear when to apply
- Counter-examples show you've thought about limits
- Trade-offs with other principles identified

**Weak** (revise):
- Statement is vague or wordy
- No application guidance
- Zero counter-examples (suspicious)
- No connection to related principles
- Reads like a concept, not a directive

````

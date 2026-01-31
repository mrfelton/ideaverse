# Frontmatter Reference: Core Ideaverse

This defines the standard frontmatter properties for Ideaverse-based vaults following LYT (Linking Your Thinking) conventions.

## Core Relationship Properties

These properties express how notes connect within your vault:

### `up:` - Parent Links

Points to the parent note(s) in the hierarchy. Use for the note this one "belongs under."

```yaml
up:
  - "[[Home]]"
```

Or multiple parents (rare, but valid):

```yaml
up:
  - "[[Library]]"
  - "[[Psychology MOC]]"
```

**Rule**: Every note except root notes (Home) should have an `up:` property.

### `related:` - Lateral Links

Notes that are conceptually related but NOT in a parent/child relationship.

```yaml
related:
  - "[[Similar Concept]]"
  - "[[Contrasting Idea]]"
```

Can be empty:

```yaml
related: []
```

### `in:` - Collection Membership (Optional)

Declares membership in a collection. Commonly used to identify MOCs:

```yaml
in:
  - "[[Maps]]"
```

### `down:` - Child Links (Optional)

Points to child notes. Less commonly used since `up:` creates implicit reciprocal relationships.

```yaml
down:
  - "[[Sub-concept A]]"
  - "[[Sub-concept B]]"
```

## Required Metadata

### `created:` - Creation Date

Simple date in YYYY-MM-DD format.

```yaml
created: 2026-01-22
```

## Examples by Note Type

### MOC (Map of Content)

```yaml
---
up:
  - "[[Home]]"
related:
  - "[[Adjacent MOC]]"
created: 2026-01-15
in:
  - "[[Maps]]"
---
```

### Concept/Atomic Note

```yaml
---
up:
  - "[[Parent MOC]]"
related:
  - "[[Related Concept]]"
created: 2026-01-20
---
```

### Daily Note (Calendar)

```yaml
---
created: 2026-01-22
---
```

### Project Note (Efforts)

```yaml
---
up:
  - "[[Efforts MOC]]"
related: []
created: 2026-01-10
---
```

## Key Rules

1. **Quoted wikilinks in frontmatter**: `"[[Note Name]]"` - Keep quotes
2. **Relationship properties are arrays**: Even single values should be `[item]`
3. **Empty arrays are valid**: `related: []` explicitly shows "no lateral connections"
4. **Do NOT use inline text patterns** like `Up: [[Note]]` in note body - use frontmatter only
5. **No inline markdown in frontmatter values** - Keep values simple

## Vault-Specific Extensions

Individual Ideaverse implementations may extend this core spec with additional properties. Common extensions include:

- `type:` - Note categorization
- `status:` - Lifecycle stage
- `tags:` - Additional categorical markers
- `area:` - Domain or subject area
- Domain-specific metadata fields

**These are optional** and should be documented in your specific vault implementation guide. The core Ideaverse requires only the relationship properties and `created:` date.

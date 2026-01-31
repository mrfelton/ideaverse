# ideaverse

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

ideaverse is a set of Agent Skills for working with Ideaverse-based [Obsidian](https://obsidian.md) vaults. See [Ideaverse for Obsidian](https://start.linkingyourthinking.com/ideaverse-for-obsidian) for the source system. It codifies the ACE framework (Atlas/Calendar/Efforts), [LYT (Linking Your Thinking)](https://linkingyourthinking.com) conventions, and the ARC workflow (Add → Relate → Communicate) for capture, connection, and communication.

## About

This repository packages repeatable workflows, reference docs, and validation scripts that help keep Ideaverse-style vaults consistent, connected, and maintainable.

## Core concepts

- **ACE (Atlas/Calendar/Efforts)**: Organize by intention - knowledge, time, and active work
- **ARC (Add/Relate/Communicate)**: Capture quickly, connect meaningfully, and express output
- **MOCs**: Use Maps of Content as curated navigation layers

## Who this is for

- People using [Obsidian](https://obsidian.md) vaults that follow Ideaverse conventions
- Teams or agents that need repeatable workflows for capture, enrichment, and maintenance
- Anyone who wants consistent frontmatter, MOCs, and linking patterns

## Features

- Core methodology skill: [skills/ideaverse/SKILL.md](skills/ideaverse/SKILL.md)
- Enrichment workflows: [skills/ideaverse-enrichment/SKILL.md](skills/ideaverse-enrichment/SKILL.md)
- Maintenance workflows and diagnostics: [skills/ideaverse-maintenance/SKILL.md](skills/ideaverse-maintenance/SKILL.md)
- Reference docs and templates under each skill directory
- Optional Python scripts for vault validation and health checks

## Repository layout

- [skills/ideaverse/SKILL.md](skills/ideaverse/SKILL.md) - Core Ideaverse methodology and conventions
- [skills/ideaverse/references/](skills/ideaverse/references/) - Frontmatter and workflow references
- [skills/ideaverse/assets/](skills/ideaverse/assets/) - Templates, including the daily log template
- [skills/ideaverse-maintenance/scripts/](skills/ideaverse-maintenance/scripts/) - Maintenance scripts and diagnostics
- [skills/ideaverse-enrichment/](skills/ideaverse-enrichment/) - Knowledge assimilation workflows and templates
- [skills/ideaverse-maintenance/](skills/ideaverse-maintenance/) - Vault maintenance workflows and diagnostics

## Quick start

1. Read the core methodology in [skills/ideaverse/SKILL.md](skills/ideaverse/SKILL.md).
2. Use the ARC workflow reference at [skills/ideaverse/references/workflows.md](skills/ideaverse/references/workflows.md).
3. If you are enriching a vault, follow [skills/ideaverse-enrichment/SKILL.md](skills/ideaverse-enrichment/SKILL.md).
4. For vault health checks, use [skills/ideaverse-maintenance/SKILL.md](skills/ideaverse-maintenance/SKILL.md).

## Installation

Clone or download the repository and use the skill folders in [skills/](skills/). If your agent expects skills under .github/skills, copy the relevant skill folders there.

## Example requests

- “Create a new MOC and link these notes under it.”
- “Process these article notes into atomic concepts and add them to the right MOCs.”
- “Run a vault health check and summarize issues.”

## Skill boundaries

- [skills/ideaverse/SKILL.md](skills/ideaverse/SKILL.md): Core methodology, conventions, and daily usage
- [skills/ideaverse-enrichment/SKILL.md](skills/ideaverse-enrichment/SKILL.md): Assimilating new knowledge and deduping concepts
- [skills/ideaverse-maintenance/SKILL.md](skills/ideaverse-maintenance/SKILL.md): Audits, diagnostics, and maintenance scripts

## Scripts (optional)

These scripts are zero-dependency and run with Python 3. They read your vault and report issues without modifying files.

**Requirements**: Python 3.8+ (no external dependencies required)

Scripts are executable and can be run directly:

```bash
# Frontmatter validation
./skills/ideaverse-maintenance/scripts/check_frontmatter.py /path/to/vault

# Broken link detection  
./skills/ideaverse-maintenance/scripts/find_broken_links.py /path/to/vault

# Orphan detection
./skills/ideaverse-maintenance/scripts/find_orphans.py /path/to/vault
```

Or invoke via `python3` (or `python` if it points to Python 3.x):

```bash
python3 skills/ideaverse-maintenance/scripts/check_frontmatter.py /path/to/vault
```

For the full maintenance suite, see [skills/ideaverse-maintenance/SKILL.md](skills/ideaverse-maintenance/SKILL.md).

## Templates

- Daily log template: [skills/ideaverse/assets/daily-log-template.md](skills/ideaverse/assets/daily-log-template.md)

## Reference highlights

- Core frontmatter specification: [skills/ideaverse/references/frontmatter.md](skills/ideaverse/references/frontmatter.md)
- ARC workflow details: [skills/ideaverse/references/workflows.md](skills/ideaverse/references/workflows.md)
- Enrichment workflows: [skills/ideaverse-enrichment/references/enrichment-workflow.md](skills/ideaverse-enrichment/references/enrichment-workflow.md)
- Knowledge classification: [skills/ideaverse-enrichment/references/knowledge-classification.md](skills/ideaverse-enrichment/references/knowledge-classification.md)
- Duplicate detection: [skills/ideaverse-enrichment/references/duplicate-detection.md](skills/ideaverse-enrichment/references/duplicate-detection.md)
- Extraction templates: [skills/ideaverse-enrichment/references/extraction-templates.md](skills/ideaverse-enrichment/references/extraction-templates.md)
- Vault hygiene guidance: [skills/ideaverse-maintenance/references/vault-hygiene.md](skills/ideaverse-maintenance/references/vault-hygiene.md)
- Troubleshooting: [skills/ideaverse-maintenance/references/troubleshooting.md](skills/ideaverse-maintenance/references/troubleshooting.md)

## External resources

- Ideaverse for Obsidian: https://start.linkingyourthinking.com/ideaverse-for-obsidian
- Linking Your Thinking (LYT): https://linkingyourthinking.com
- Obsidian app: https://obsidian.md
- Obsidian help docs: https://help.obsidian.md

## Contributing

Issues and pull requests are welcome. Focus on clarity, correctness, and keeping skills concise.

## License

MIT. See [LICENSE](LICENSE).

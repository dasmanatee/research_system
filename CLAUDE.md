# Research System - Agent Operating Instructions

## Overview

This is an autonomous research system. Agents operating within this repository conduct research, process information, and produce publishable outputs. This file establishes baseline operating principles that apply **before** and **in addition to** any folder-specific instructions.

## Instruction Hierarchy

```
CLAUDE.md (this file)     ← Global rules, always apply
    │
    ├── 1_raw_information/CLAUDE.md      ← Raw data handling rules
    ├── 2_ingested_information/CLAUDE.md ← Processing rules
    ├── 3_user_documents/CLAUDE.md       ← User content rules
    └── 4_output_documents/CLAUDE.md     ← Publishing rules
```

**Precedence**: Sub-folder instructions extend (not override) these global rules. If conflict exists, sub-folder rules take precedence for operations within that folder only.

## Folder Structure

| Folder | Purpose | Agent Role |
|--------|---------|------------|
| `1_raw_information/` | Unprocessed downloads, raw data | Store only, never modify source |
| `2_ingested_information/` | Processed, structured content | Transform raw → usable format |
| `3_user_documents/` | User-provided reference materials | Read and cross-reference |
| `4_output_documents/` | Final deliverables for publishing | Create polished outputs |

## Core Operating Principles

### 1. Always Log Actions
Every significant action must be logged in `1_raw_information/log.md`:
- Web searches and fetches
- File processing operations
- Errors and recovery attempts
- Decisions and rationale

**Log Format**:
```markdown
## [YYYY-MM-DD HH:MM:SS]

**Action**: [Description]
**Tool Used**: [Tool name]
**Query/Target**: [What was searched/processed]
**Outcome**: SUCCESS | PARTIAL | FAILED
**What Worked**: [Successes]
**What Didn't Work**: [Failures]
**Notes**: [Observations, lessons learned]

---
```

### 2. Read Before Acting
Before operating in any folder:
1. Check for a `CLAUDE.md` in that folder
2. Read and follow folder-specific instructions
3. If no CLAUDE.md exists, apply only global rules

### 3. Preserve Data Integrity
- **Never delete** files from `1_raw_information/`
- **Never modify** files in `3_user_documents/`
- **Always cite** sources in outputs
- **Track provenance** - know where every piece of data came from

### 4. Fail Gracefully
When errors occur:
1. Log the error with full details
2. Attempt one alternative approach
3. Log the alternative attempt
4. If still failing, document and notify user

### 5. Verify Before Proceeding
Before completing any task:
- Cross-check facts against multiple sources when possible
- Verify file operations completed successfully
- Confirm outputs meet quality standards in folder CLAUDE.md

## Agent Workflow

### On Invocation
```
1. Read this file (CLAUDE.md in root)
2. Identify target folder for current task
3. Read target folder's CLAUDE.md (if exists)
4. Plan task using TodoWrite
5. Execute with logging
6. Verify completion
7. Update log with lessons learned
```

### Task Planning
Use `TodoWrite` for any task with 3+ steps:
- Break complex tasks into discrete items
- Update status as work progresses
- Mark items complete only when fully done

### Information Flow
```
External Sources → 1_raw_information/
                          ↓
                   2_ingested_information/
                          ↓
    3_user_documents/ →  Cross-reference
                          ↓
                   4_output_documents/ → Publication
```

## Available Tools

| Tool | Use For |
|------|---------|
| `WebSearch` | Finding current information online |
| `WebFetch` | Extracting content from specific URLs |
| `Read` | Reading files, PDFs, images |
| `Write` | Creating new files |
| `Edit` | Modifying existing files |
| `Glob` | Finding files by pattern |
| `Grep` | Searching file contents |
| `Task` | Launching specialized sub-agents |
| `TodoWrite` | Tracking task progress |

## Quality Standards

### Research Quality
- Verify claims from 2+ sources when possible
- Note when information is single-sourced
- Include access dates for web sources
- Flag outdated information (>1 year old)

### Output Quality
- Follow folder-specific formatting (see sub-folder CLAUDE.md)
- Include methodology sections
- Cite all sources
- Note limitations and uncertainties

## Prohibited Actions

1. **Never fabricate** sources, quotes, or data
2. **Never delete** raw information or user documents
3. **Never skip** logging significant actions
4. **Never proceed** without reading folder instructions
5. **Never ignore** errors - always log and address

## Sub-Folder Quick Reference

### `1_raw_information/`
Store raw downloads. Never modify. Contains main `log.md`.

### `2_ingested_information/`
Process raw files into structured formats. See folder CLAUDE.md for conversion rules and naming conventions.

### `3_user_documents/`
User-provided materials. Read-only reference. Cross-reference with research findings.

### `4_output_documents/`
Final outputs for publication. Follow NYT D3.js standards for data visualization. See folder CLAUDE.md for formatting guidelines.

## Getting Started

1. **New to this repo?** Read all CLAUDE.md files to understand the system
2. **Starting a task?** Create a plan with TodoWrite
3. **Confused about where to put something?** Check the folder structure table above
4. **Something went wrong?** Log it, try an alternative, log again

## Version

Last Updated: 2026-01-11
System Version: 1.0

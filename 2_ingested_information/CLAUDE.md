# Ingestion Agent Instructions

## Purpose
This agent processes raw research materials into structured, machine-readable formats.

## Core Rules

1. **NEVER delete files from `1_raw_information/`** - Raw data is sacred and must be preserved
2. **Always check coverage** - Every time this agent is invoked, verify all raw files have corresponding ingested versions
3. **Use appropriate formats** - Convert to markdown (.md) for text, JSON for structured data, CSV for tabular data

## Workflow

### Step 1: Audit Raw Information
On every invocation, scan `1_raw_information/` and compare against `2_ingested_information/`:

```
1. List all files in 1_raw_information/
2. List all files in 2_ingested_information/
3. Identify any raw files without corresponding ingested versions
4. Process missing files
```

### Step 2: Process Each Unprocessed File

For each raw file without an ingested counterpart:

| Raw File Type | Output Format | Processing Action |
|---------------|---------------|-------------------|
| PDF | .md | Extract text, structure with headings, preserve tables |
| Images | .md | Describe content, extract any visible text |
| HTML | .md | Convert to clean markdown, preserve links |
| JSON | .json | Clean, validate, add metadata |
| CSV/Excel | .csv or .json | Normalize, add column descriptions |
| Plain text | .md | Structure with appropriate headings |
| Audio/Video | .md | Create transcript or description file |

### Step 3: Naming Convention

Ingested files should follow this pattern:
```
[original_filename]_ingested.[appropriate_extension]
```

Example: `research_paper.pdf` → `research_paper_ingested.md`

### Step 4: Ingested File Structure

Each ingested markdown file must include:

```markdown
# [Document Title]

## Metadata
- **Source File**: [path to raw file]
- **Ingestion Date**: [YYYY-MM-DD HH:MM:SS]
- **File Type**: [original format]
- **Status**: Complete | Partial | Needs Review

## Summary
[Brief overview of content]

## Content
[Processed content here]

## Notes
[Any issues, uncertainties, or observations during processing]
```

## Quality Standards

1. **Preserve meaning** - Never lose information during conversion
2. **Add structure** - Use headings, lists, and tables to improve readability
3. **Flag issues** - Note any content that couldn't be processed or is unclear
4. **Maintain traceability** - Always link back to source file

## Error Handling

If a file cannot be processed:
1. Create a stub file named `[filename]_ingested_FAILED.md`
2. Document the error and reason for failure
3. Log the failure in the main `log.md`

## Verification Checklist

Run this check on every invocation:

- [ ] All files in `1_raw_information/` have been scanned
- [ ] Each raw file has a corresponding ingested file
- [ ] No ingested files exist without a raw source
- [ ] All ingested files contain required metadata
- [ ] Processing logged in main `log.md`

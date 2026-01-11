# Claude Research System Instructions

## Overview
This file directs how Claude should conduct research within this system. All research actions must be logged in `log.md` with timestamps and outcomes.

## Folder Structure
- `1_raw_information/` - Store raw data, downloads, and unprocessed content
- `2_ingested_information/` - Store processed, summarized, and analyzed content
- `3_user_documents/` - User-provided documents and reference materials
- `4_output_documents/` - Final research outputs, reports, and deliverables

## Available Tools & When to Use Them

### Web Research
- **WebSearch** - Find article URLs and sources (use for discovery, NOT content retrieval)
- **Python script (`download_articles.py`)** - Download raw article content without LLM summarization

### File Operations
- **Read** - Read files, PDFs, images, and Jupyter notebooks
- **Write** - Create new files
- **Edit** - Modify existing files
- **Glob** - Find files by pattern (e.g., `**/*.pdf`)
- **Grep** - Search file contents for specific text or patterns

### Code & Analysis
- **mcp__ide__executeCode** - Execute Python code in Jupyter kernel for data analysis
- **mcp__ide__getDiagnostics** - Get language diagnostics from VS Code

### Task Management
- **Task** - Launch specialized agents for complex multi-step research
- **TodoWrite** - Track research tasks and progress

## Research Workflow

### 1. Planning Phase
- Use `TodoWrite` to create a research plan
- Break complex research into discrete, trackable tasks
- Identify which tools are needed for each task

### 2. Information Gathering (Two-Step Process)

**IMPORTANT**: Do NOT use WebFetch for article content - it summarizes through an LLM. Use this workflow instead:

#### Step 1: Find URLs with WebSearch
```
Use WebSearch to find relevant article URLs
Include year in queries for current results (e.g., "data centers 2025 2026")
Note all promising URLs from search results
```

#### Step 2: Download Raw Content with Python
```python
# Add URLs to the URLS list in download_articles.py
URLS = [
    "https://example.com/article1",
    "https://example.com/article2",
]

# Run the script
python download_articles.py
```

**What the script produces:**
- `.html` files - Raw HTML for archival/full fidelity
- `.md` files - Extracted text with structure preserved (headers, paragraphs, lists)
- `download_results.json` - Programmatic log of successes/failures

### 3. Processing & Analysis
- Read downloaded `.md` files from `1_raw_information/`
- Use `Grep` to search across multiple articles for specific topics
- Use `mcp__ide__executeCode` for data analysis when needed
- Save processed/synthesized content to `2_ingested_information/`
- Cross-reference with user documents in `3_user_documents/`

### 4. Output Generation
- Create final deliverables in `4_output_documents/`
- Include citations and sources (APA 7th Edition format)
- Log completion of research tasks

## Why This Workflow?

| Approach | Pros | Cons |
|----------|------|------|
| WebFetch | Quick, single tool | **Summarizes content** - loses detail |
| Python script | **Raw content preserved**, both HTML and text | Requires running script |

**Always prefer raw content** - summaries lose important details, quotes, and context.

## Logging Requirements

**CRITICAL**: Every research action MUST be logged in `log.md` using this format:

```markdown
## [YYYY-MM-DD HH:MM:SS]

**Action**: [Brief description of what was attempted]
**Tool Used**: [Tool name]
**Query/Target**: [Search query, URL, or file path]
**Outcome**: SUCCESS | PARTIAL | FAILED
**What Worked**: [Description of successful aspects]
**What Didn't Work**: [Description of failures or issues]
**Notes**: [Any additional observations or learnings]

---
```

### Logging Best Practices
- Log BEFORE and AFTER each significant research action
- Be specific about what succeeded and what failed
- Note rate limits, access issues, or content quality problems
- Record which search terms produced useful vs. poor results
- Track which sources were reliable vs. unreliable
- Note any redirects, paywalls, or access restrictions encountered

## Research Quality Standards

1. **Verify information** from multiple sources when possible
2. **Date-check** information for currency and relevance
3. **Cite sources** with URLs and access dates (APA 7th Edition)
4. **Note limitations** of the research conducted
5. **Flag uncertainties** clearly in outputs

## Error Handling

When a research action fails:
1. Log the failure with specific error details
2. Attempt an alternative approach
3. Log the alternative attempt
4. If all approaches fail, document in log and notify user

## Example: Complete Research Workflow

```markdown
## [2026-01-11 12:30:00]

**Action**: Search for data center project articles
**Tool Used**: WebSearch
**Query/Target**: "data center projects 2025 2026 new construction"
**Outcome**: SUCCESS
**What Worked**: Found 10 relevant URLs from industry sources
**What Didn't Work**: N/A
**Notes**: Adding year range ensured current results

---

## [2026-01-11 12:35:00]

**Action**: Download raw article content
**Tool Used**: Python script (download_articles.py)
**Query/Target**: 7 URLs added to script
**Outcome**: PARTIAL (6/7 success)
**What Worked**: Downloaded 6 articles with full HTML + extracted markdown
**What Didn't Work**: 1 site timed out (blackridgeresearch.com)
**Notes**: Raw content preserved without LLM summarization

---
```

## Script Reference

The `download_articles.py` script:
- Uses `requests` + `BeautifulSoup` for raw content extraction
- Saves both `.html` (raw) and `.md` (extracted text)
- Handles timeouts and logs failures
- Creates sanitized filenames from URLs

To add new articles: Edit the `URLS` list and re-run the script.

# Output Documents - Publishing Guidelines

## Purpose
This folder contains final research outputs formatted for publication. All documents should follow New York Times visual journalism standards for data presentation.

## NYT D3.js Standards & Libraries

### Recommended Libraries
- **D3.js v7** - Core visualization library
- **@nytimes/svg-crowbar** - SVG export utility
- **ai2html** - Illustrator to HTML conversion (NYT standard)
- **Scrollama** - Scroll-driven storytelling
- **d3-annotation** - Annotations for charts

### Color Palettes (NYT Style)
```javascript
// Primary palette
const nytColors = {
  primary: '#121212',      // Text black
  secondary: '#666666',    // Secondary text
  accent: '#326891',       // NYT blue (links/highlights)
  background: '#FFFFFF',   // Clean white
  lightGray: '#F7F7F7',    // Background accent
  border: '#EBEBEB'        // Dividers
};

// Data visualization palette
const chartColors = [
  '#e41a1c',  // Red
  '#377eb8',  // Blue
  '#4daf4a',  // Green
  '#984ea3',  // Purple
  '#ff7f00',  // Orange
  '#ffff33',  // Yellow
  '#a65628',  // Brown
  '#f781bf'   // Pink
];

// Sequential palette (single hue)
const sequential = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#084594'];
```

### Typography Standards
```css
/* Headlines */
font-family: 'nyt-cheltenham', 'Georgia', serif;
font-weight: 700;

/* Body text */
font-family: 'nyt-imperial', 'Georgia', serif;
font-size: 1.125rem;
line-height: 1.75;

/* Chart labels */
font-family: 'nyt-franklin', 'Arial', sans-serif;
font-size: 0.8125rem;

/* Data annotations */
font-family: 'nyt-franklin', 'Arial', sans-serif;
font-size: 0.75rem;
font-weight: 500;
```

### Fallback Web-Safe Fonts
```css
/* If NYT fonts unavailable */
--headline-font: Georgia, 'Times New Roman', serif;
--body-font: Georgia, 'Times New Roman', serif;
--chart-font: Arial, Helvetica, sans-serif;
```

## Chart Standards

### Dimensions
- **Mobile**: 300px width, flexible height
- **Desktop**: 600-720px width
- **Margins**: `{ top: 20, right: 20, bottom: 40, left: 50 }`

### Axis Formatting
```javascript
// Y-axis: minimal ticks, left-aligned labels
const yAxis = d3.axisLeft(yScale)
  .ticks(5)
  .tickSize(-width)  // Grid lines
  .tickFormat(d3.format(',.0f'));

// X-axis: bottom only, sparse labels
const xAxis = d3.axisBottom(xScale)
  .ticks(d3.timeYear.every(2))
  .tickSizeOuter(0);
```

### Grid Lines
- Light gray (#EBEBEB) horizontal lines only
- No vertical grid lines
- Remove axis domain line

### Annotations
- Use d3-annotation for callouts
- Point to specific data, not empty space
- Keep annotation text under 15 words

## Document Structure

### Required Sections
1. **Headline** - Clear, specific, under 10 words
2. **Deck/Subhead** - One sentence summary
3. **Byline** - Author and date
4. **Lead** - Key finding in first paragraph
5. **Body** - Analysis with embedded visualizations
6. **Methodology** - Data sources and limitations
7. **Sources** - Full citations with URLs

### File Naming Convention
```
YYYY-MM-DD_topic-slug_version.ext

Examples:
2026-01-11_ai-regulation-analysis_v1.html
2026-01-11_market-trends_final.md
```

## Responsive Design

### Breakpoints
```css
/* Mobile first */
@media (min-width: 600px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
```

### Chart Responsiveness
- Use `viewBox` for SVG scaling
- Recalculate dimensions on resize
- Simplify mobile views (fewer labels, larger touch targets)

## Accessibility Requirements

1. **Alt text** for all visualizations
2. **ARIA labels** for interactive elements
3. **Color contrast** minimum 4.5:1 ratio
4. **Keyboard navigation** for interactive charts
5. **Data tables** as fallback for screen readers

## Export Formats

| Format | Use Case |
|--------|----------|
| `.html` | Interactive web publication |
| `.md` | Documentation and reports |
| `.svg` | Print-quality graphics |
| `.png` | Social media / thumbnails |
| `.json` | Data files |

## Quality Checklist

Before publishing, verify:
- [ ] Headline is clear and specific
- [ ] Data sources are cited
- [ ] Charts have titles and axis labels
- [ ] Color palette is consistent
- [ ] Mobile view tested
- [ ] Accessibility reviewed
- [ ] Methodology section included
- [ ] Date and author noted

## Example D3 Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chart Title</title>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <style>
    body {
      font-family: Georgia, serif;
      max-width: 720px;
      margin: 0 auto;
      padding: 20px;
    }
    .chart-title {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }
    .chart-subtitle {
      font-size: 0.875rem;
      color: #666;
      margin-bottom: 1rem;
    }
    .axis text {
      font-family: Arial, sans-serif;
      font-size: 0.75rem;
    }
    .axis path,
    .axis line {
      stroke: #ebebeb;
    }
    .source {
      font-size: 0.75rem;
      color: #999;
      margin-top: 1rem;
    }
  </style>
</head>
<body>
  <h1 class="chart-title">Chart Title Here</h1>
  <p class="chart-subtitle">Brief description of what the data shows</p>
  <div id="chart"></div>
  <p class="source">Source: Data source name</p>
  <script>
    // D3 visualization code here
  </script>
</body>
</html>
```

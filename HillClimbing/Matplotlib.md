## Matplotlib:

Matplotlib is the foundational, low-level data visualization library in Python. Built in 2003 by John D. Hunter to emulate MATLAB's plotting interface, it provides complete control over every element of a figure—from axes and tick marks to legends, colors, and layouts. Higher-level libraries like Seaborn and Pandas' plotting API are built directly on top of Matplotlib.

## Core Architecture & Mental Model:

Matplotlib structures a visualization in a hierarchical tree:

Figure (The overall canvas / window)
 └── Axes (The actual plot area containing data, ticks, labels, and title)
      ├── XAxis & YAxis (Ticks, tick labels, axis limits, axis scales)
      ├── Spines (The boundary lines framing the plot)
      └── Primitives (Lines, markers, text, bars, patches, collections)
Figure: The top-level container holding one or more subplots (Axes).

Axes: The region where data is plotted. A figure can have multiple axes (e.g., a 2x2 grid of subplots). Note: Do not confuse Axes (the plot object) with Axis (the 1D x/y scale line).

Axis: Handles numerical limits, ticks, tick formatting, and grid lines.

Artist: Everything visible on the canvas—lines, text, legends, shapes—is an "Artist" object under the hood.

## The Two Interfaces: Pyplot vs. Object-Oriented (OO):
Matplotlib offers two distinct workflows:

A. State-Machine Interface (plt)
Emulates MATLAB by maintaining a hidden global "current figure" and "current axes."

```Python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Quick Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

Best for: Fast interactive checks, exploratory data analysis, and one-liners.

Drawback: Hard to debug and unwieldy when dealing with multiple subplots or complex layouts.

## Object-Oriented (OO) Interface (Recommended):
Explicitly creates Figure and Axes objects and calls methods directly on them.

```Python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3], [4, 5, 6], label="Series A", color="tab:blue", linewidth=2)
ax.set_title("Structured Plot")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()
plt.show()
```

Best for: Production code, reusable plotting functions, multi-panel layouts, and fine-grained customizations.

## Key Plotting Functions

Most core plotting routines reside on the `Axes` object (or in `pyplot` under the same name):

| Function | Plot Type | Primary Use Case | Key Parameters |
| :--- | :--- | :--- | :--- |
| `ax.plot()` | Line Plot | Trends, time-series, continuous mathematical functions | `color`, `linestyle`, `linewidth`, `marker` |
| `ax.scatter()` | Scatter Plot | Relationships, correlations, multi-dimensional distributions | `s` (size), `c` (color mapping), `alpha`, `cmap` |
| `ax.bar()` / `ax.barh()` | Vertical / Horizontal Bar Chart | Comparing discrete categories | `width`, `align`, `edgecolor`, `bottom` (for stacking) |
| `ax.hist()` | Histogram | Frequency distributions of continuous data | `bins`, `density`, `cumulative`, `histtype` |
| `ax.boxplot()` | Box & Whisker Plot | Five-number summary (median, IQR, outliers) | `vert`, `patch_artist`, `notch`, `showmeans` |
| `ax.pie()` | Pie Chart | Part-to-whole proportions (best for few categories) | `autopct`, `explode`, `startangle`, `shadow` |
| `ax.imshow()` | Image / Matrix Display | Heatmaps, 2D arrays, pixel data | `cmap`, `interpolation`, `aspect`, `origin` |
| `ax.contour()` / `ax.contourf()` | Contour Plot (Line / Filled) | 3D surfaces projected onto a 2D plane | `levels`, `cmap`, `alpha` |
| `ax.fill_between()` | Area / Ribbon Plot | Confidence intervals, shaded error bands | `y1`, `y2`, `where`, `alpha`, `color` |
| `ax.errorbar()` | Error Bar Plot | Visualizing measurement uncertainty/deviations | `xerr`, `yerr`, `fmt`, `ecolor`, `capsize` |

---

## 4. Customization & Styling Functions

### Annotations & Text
* `ax.set_title("...")` / `ax.set_xlabel("...")` / `ax.set_ylabel("...")`: Titles and labels.
* `ax.text(x, y, "label")`: Places arbitrary text at explicit data coordinates.
* `ax.annotate("text", xy=(x, y), xytext=(x2, y2), arrowprops=...)`: Adds text with a pointing arrow to call out specific data points.

### Scales & Limits
* `ax.set_xlim(min, max)` / `ax.set_ylim(min, max)`: Explicitly crops or expands axis boundaries.
* `ax.set_xscale('log')` / `ax.set_yscale('log')`: Switches linear scales to logarithmic, symlog, or logit.

### Ticks & Grids
* `ax.set_xticks(positions)` / `ax.set_xticklabels(labels)`: Customizes tick marks and their display text.
* `ax.tick_params(axis='both', which='major', labelsize=10, rotation=45)`: Adjusts tick font sizes, rotation, direction, and colors.
* `ax.grid(True, linestyle='--', alpha=0.6)`: Toggles coordinate gridlines.

### Legends & Colorbars
* `ax.legend(loc='best', frameon=True)`: Displays the dataset legend based on `label=` arguments.
* `fig.colorbar(mappable, ax=ax)`: Adds a color gradient scale bar (used with `imshow`, `contourf`, or `scatter`).

---

## 5. Subplots & Layout Control

### Standard Grid: `plt.subplots()`
Creates a grid of plots sharing unified spacing or axes:

```python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), sharex=True)
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data)
plt.tight_layout()  # Automatically prevents overlapping labels

```

## Complex / Asymmetric Grids: GridSpec
For layouts where plots span multiple rows or columns:

```Python
fig = plt.figure(figsize=(10, 6))
gs = fig.add_gridspec(nrows=2, ncols=2, height_ratios=[2, 1])

ax_main = fig.add_subplot(gs[0, :])     # Spans all columns of row 0
ax_sub1 = fig.add_subplot(gs[1, 0])     # Bottom left
ax_sub2 = fig.add_subplot(gs[1, 1])     # Bottom right
```
## Exporting Figures
Save figures using fig.savefig():

```Python
fig.savefig(
    "figure.png",
    dpi=300,                  # Print-quality resolution
    bbox_inches="tight",       # Crops unnecessary white padding
    transparent=False
)
```
Supported formats include raster types (.png, .jpg) and vector types (.pdf, .svg, .eps).


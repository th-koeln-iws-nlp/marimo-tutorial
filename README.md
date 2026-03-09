# marimo Tutorial

A hands-on, data-science focused introduction to [marimo](https://marimo.io).

[Marimo in 100 seconds](https://www.youtube.com/watch?v=3dUagnSKaA8) by the one and only Vincent Warmerdam.

## Notebooks

| # | File | Topics |
|---|------|--------|
| 1 | `01_intro_reactivity.py` | What is marimo, reactivity, sidebar (packages + AI), running as scripts |
| 2 | `02_inputs.py` | Sliders, dropdowns, checkboxes, text, date, run button, forms |
| 3 | `03_dataframes.py` | Penguins dataset, `mo.ui.dataframe`, `mo.ui.data_explorer` |
| 4 | `04_visualizations.py` | Matplotlib, Plotly, interactive selections |
| 5 | `05_pytorch.py` | `nn.Module` rich display, interactive architecture, training loop |

## Setup

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Edit a notebook (dependencies install automatically via PEP 723)
uv run marimo edit --watch
```

## Running notebooks

```bash
uv run marimo edit  <notebook.py>   # interactive editor
uv run marimo run   <notebook.py>   # read-only app
uv run python       <notebook.py>   # plain script
uvx marimo check    <notebook.py>   # lint
```

## Gallery

Explore more examples at **https://marimo.io/gallery** — 57 notebooks covering
ML, geospatial, SQL, signal processing, custom widgets, and more.

## Claude Code Skills

marimo provides official [Claude Code skills](https://docs.marimo.io/guides/generate_with_ai/skills/) to help coding agents write high-quality notebooks — converting Jupyter notebooks, creating interactive widgets, and authoring standalone notebooks. See also the [Claude Code + marimo guide](https://docs.marimo.io/guides/generate_with_ai/using_claude_code/).

## Tips

- Open the **left sidebar** in the editor for package management and the AI assistant
- `Cmd/Ctrl + Shift + P` opens the command palette
- marimo notebooks are plain `.py` files — diff them, import them, run them in CI

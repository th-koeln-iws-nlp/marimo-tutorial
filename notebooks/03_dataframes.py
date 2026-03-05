# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo", "pandas", "kagglehub"]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import kagglehub
    import pandas as pd
    from pathlib import Path

    _path = kagglehub.dataset_download(
        "parulpandey/palmer-archipelago-antarctica-penguin-data"
    )
    penguins = pd.read_csv(Path(_path) / "penguins_size.csv").dropna()
    return (penguins,)


@app.cell
def _(penguins):
    penguins
    return


@app.cell
def _(mo):
    mo.md("""
    # DataFrames & Filtering
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Raw data — sortable, searchable table
    """)
    return


@app.cell
def _(mo, penguins):
    mo.ui.table(penguins)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `mo.ui.dataframe` — filter, group, aggregate

    Use the controls below to interactively filter the dataset.
    The filtered result flows into downstream cells.
    """)
    return


@app.cell
def _(mo, penguins):
    df_ui = mo.ui.dataframe(penguins)
    df_ui
    return (df_ui,)


@app.cell
def _(df_ui, mo):
    filtered = df_ui.value
    mo.md(f"**{len(filtered)}** rows selected")
    return (filtered,)


@app.cell
def _(filtered):
    filtered.describe()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `mo.ui.data_explorer` — drag-and-drop EDA

    Build charts without writing code.
    """)
    return


@app.cell
def _(mo, penguins):
    mo.ui.data_explorer(penguins)
    return


if __name__ == "__main__":
    app.run()

# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo", "matplotlib", "plotly", "pandas", "kagglehub"]
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
    import matplotlib.pyplot as plt
    import pandas as pd
    import plotly.express as px
    from pathlib import Path

    _path = kagglehub.dataset_download(
        "parulpandey/palmer-archipelago-antarctica-penguin-data"
    )
    penguins = (
        pd.read_csv(Path(_path) / "penguins_size.csv")
        .dropna()
        .rename(
            columns={
                "culmen_length_mm": "bill_length_mm",
                "culmen_depth_mm": "bill_depth_mm",
            }
        )
    )
    return penguins, plt, px


@app.cell
def _(mo):
    mo.md("""
    # Visualizations
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Matplotlib
    """)
    return


@app.cell
def _(penguins, plt):
    fig_mpl, ax = plt.subplots(figsize=(6, 4))
    for _species, _group in penguins.groupby("species"):
        ax.scatter(
            _group["flipper_length_mm"],
            _group["body_mass_g"],
            label=_species,
            alpha=0.7,
        )
    ax.set_xlabel("Flipper length (mm)")
    ax.set_ylabel("Body mass (g)")
    ax.legend()
    ax.set_title("Penguins")
    fig_mpl
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Matplotlib — interactive selection (`mo.ui.matplotlib`)

    Draw a **box or lasso** selection on the scatter plot.
    Selected points flow into the cell below.
    """)
    return


@app.cell
def _(mo, penguins, plt):
    fig_sel, ax_sel = plt.subplots(figsize=(6, 4))
    x_flip = penguins["flipper_length_mm"].to_numpy()
    y_mass = penguins["body_mass_g"].to_numpy()
    ax_sel.scatter(
        x_flip,
        y_mass,
        c=penguins["species"].astype("category").cat.codes,
        cmap="tab10",
        alpha=0.7,
    )
    ax_sel.set_xlabel("Flipper length (mm)")
    ax_sel.set_ylabel("Body mass (g)")
    ax_sel.set_title("Select points with box/lasso")

    mpl_chart = mo.ui.matplotlib(ax_sel)
    mpl_chart
    return mpl_chart, x_flip, y_mass


@app.cell
def _(mo, mpl_chart, penguins, x_flip, y_mass):
    if mpl_chart.value:
        _mask = mpl_chart.value.get_mask(x_flip, y_mass)
        selected_df = penguins[_mask]
        _msg = mo.md(
            f"**{_mask.sum()}** points selected — mean body mass: **{selected_df['body_mass_g'].mean():.0f} g**"
        )
    else:
        _msg = mo.md("_Draw a selection on the plot above._")
    _msg
    return


@app.cell
def _(mo):
    mo.md("""
    ## Plotly
    """)
    return


@app.cell
def _(penguins, px):
    fig_plotly = px.scatter(
        penguins,
        x="flipper_length_mm",
        y="body_mass_g",
        color="species",
        hover_data=["bill_length_mm", "island"],
        title="Penguins — hover for details",
    )
    fig_plotly
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Plotly — interactive selection (`mo.ui.plotly`)

    **Box-select or lasso-select** points in the chart.
    Selected rows are available as a dataframe below.
    """)
    return


@app.cell
def _(mo, penguins, px):
    plotly_chart = mo.ui.plotly(
        px.scatter(
            penguins,
            x="flipper_length_mm",
            y="body_mass_g",
            color="species",
            title="Select points",
        )
    )
    plotly_chart
    return (plotly_chart,)


@app.cell
def _(mo, plotly_chart):
    sel = plotly_chart.value
    if sel is not None and len(sel) > 0:
        _msg = mo.md(f"**{len(sel)}** points selected")
    else:
        _msg = mo.md("_Draw a selection on the plot above._")
    _msg
    return


if __name__ == "__main__":
    app.run()

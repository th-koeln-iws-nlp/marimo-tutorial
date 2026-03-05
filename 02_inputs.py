# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo"]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Input Types
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(0, 100, value=42, label="Slider")
    number = mo.ui.number(0, 100, value=42, label="Number")
    mo.hstack([slider, number], gap=2)
    return number, slider


@app.cell
def _(mo, number, slider):
    mo.md(f"""
    slider = **{slider.value}**, number = **{number.value}**
    """)
    return


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(
        ["Penguins", "Iris", "Titanic"], value="Penguins", label="Dataset"
    )
    radio = mo.ui.radio(["mean", "median", "std"], value="mean", label="Statistic")
    checkbox = mo.ui.checkbox(label="Normalize")
    mo.vstack([dropdown, radio, checkbox])
    return checkbox, dropdown, radio


@app.cell
def _(checkbox, dropdown, mo, radio):
    mo.md(f"""
    dataset=`{dropdown.value}`, stat=`{radio.value}`, normalize=`{checkbox.value}`
    """)
    return


@app.cell
def _(mo):
    text = mo.ui.text(placeholder="Enter name…", label="Name")
    date = mo.ui.date(label="Date")
    mo.hstack([text, date], gap=2)
    return date, text


@app.cell
def _(date, mo, text):
    mo.md(f"""
    name=`{text.value or "—"}`, date=`{date.value}`
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Run Button

    Use `mo.ui.run_button` to gate expensive computations — the cell below
    only runs when you click.
    """)
    return


@app.cell
def _(mo):
    run_btn = mo.ui.run_button(label="Run expensive computation")
    run_btn
    return (run_btn,)


@app.cell
def _(mo, run_btn):
    mo.stop(not run_btn.value, mo.md("_Click the button above to run._"))
    result = sum(range(10_000_000))
    mo.md(f"Result: **{result:,}**")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Form

    Batch multiple inputs — downstream cells only update on **Submit**.
    """)
    return


@app.cell
def _(mo):
    form = (
        mo.md(
            r"""
            **Training config**

            Epochs: {epochs}

            Optimizer: {optimizer}

            Learning rate: {lr}
            """
        )
        .batch(
            epochs=mo.ui.slider(1, 100, value=10, label="Epochs"),
            optimizer=mo.ui.dropdown(["adam", "sgd", "rmsprop"], value="adam"),
            lr=mo.ui.number(
                start=1e-5, stop=1e-1, value=1e-3, step=1e-4, label="LR"
            ),
        )
        .form(submit_button_label="Submit config")
    )
    form
    return (form,)


@app.cell
def _(form, mo):
    mo.stop(form.value is None, mo.md("_Submit the form above._"))
    mo.md(f"Config: `{form.value}`")
    return


if __name__ == "__main__":
    app.run()

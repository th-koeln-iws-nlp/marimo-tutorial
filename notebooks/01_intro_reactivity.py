# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo", "matplotlib"]
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
    mo.md(r"""
    # marimo — Reactive Python Notebooks

    **marimo** reinvents the Python notebook:

    - Cells re-run **automatically** when their dependencies change
    - Stored as plain `.py` files — version-controllable & importable
    - Run as interactive apps **or** plain Python scripts
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Reactivity — move the slider and watch the cells below update
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.slider(1, 30, value=10, label="n")
    n
    return (n,)


@app.cell
def _(mo, n):
    import argparse

    _is_script = mo.app_meta().mode == "script"

    if _is_script:
        _parser = argparse.ArgumentParser()
        _parser.add_argument("--n", type=int, default=n.value)
        _args = _parser.parse_args()
        n_effective = _args.n
    else:
        n_effective = n.value
    return (n_effective,)


@app.cell
def _(n_effective):
    numbers = list(range(1, n_effective + 1))
    total = sum(numbers)
    return numbers, total


@app.cell
def _(mo, n_effective, total):
    mo.md(f"""
    Sum of 1 … {n_effective} = **{total}**
    """)
    return


@app.cell
def _(numbers):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(numbers, [x**2 for x in numbers], color="steelblue")
    ax.set_xlabel("n")
    ax.set_ylabel("n²")
    ax.set_title("Squares — updates with slider")
    fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sidebar

    Open the **left sidebar** in the marimo editor:

    - **Packages** tab — install packages on the fly
    - **AI assistant** tab — generate & edit cells with an LLM

    `Cmd/Ctrl + Shift + P` opens the command palette.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Running as a script

    marimo notebooks are plain Python files:

    ```bash
    uv run marimo edit   01_intro_reactivity.py          # interactive editor
    uv run marimo run    01_intro_reactivity.py          # read-only app
    uv run python        01_intro_reactivity.py          # plain script (n=slider default)
    uv run python        01_intro_reactivity.py --n 20   # pass n as argument → prints sum
    uv run marimo check  01_intro_reactivity.py          # lint
    ```

    In script mode the slider is ignored — `--n` sets the value and the sum is printed.
    """)
    return


@app.cell
def _(mo, n_effective, total):
    _is_script = mo.app_meta().mode == "script"
    if _is_script:
        print(f"n={n_effective}, sum={total}")
    mo.md(f"**Current mode:** `{mo.app_meta().mode}`")
    return


if __name__ == "__main__":
    app.run()

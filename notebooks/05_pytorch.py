# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo", "torch", "matplotlib", "pandas", "kagglehub"]
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
    import torch
    import torch.nn as nn
    from pathlib import Path

    return Path, kagglehub, nn, pd, plt, torch


@app.cell
def _(Path, kagglehub, pd, torch):
    _path = kagglehub.dataset_download(
        "parulpandey/palmer-archipelago-antarctica-penguin-data"
    )
    _df = (
        pd.read_csv(Path(_path) / "penguins_size.csv")
        .dropna()
        .rename(
            columns={
                "culmen_length_mm": "bill_length_mm",
                "culmen_depth_mm": "bill_depth_mm",
            }
        )
    )

    _feature_cols = [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]
    _species = sorted(_df["species"].unique())
    species_names = {i: s for i, s in enumerate(_species)}

    _X = _df[_feature_cols].values
    _X = (_X - _X.mean(axis=0)) / _X.std(axis=0)  # standardize
    _y = _df["species"].map({s: i for i, s in species_names.items()}).values

    X_data = torch.tensor(_X, dtype=torch.float32)
    y_data = torch.tensor(_y, dtype=torch.long)
    return X_data, y_data


@app.cell
def _(mo):
    mo.md("""
    # PyTorch in marimo
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Rich model display (marimo ≥ 0.20)

    Just output an `nn.Module` — marimo renders it as a **collapsible tree**
    with color-coded layer types, frozen layers dimmed, and trainable
    parameter counts inline. Hover a layer to see its docstring.
    """)
    return


@app.cell
def _(nn):
    class MLP(nn.Module):
        def __init__(self, in_features: int, hidden: int, out_features: int):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(in_features, hidden),
                nn.ReLU(),
                nn.Linear(hidden, hidden),
                nn.ReLU(),
                nn.Linear(hidden, out_features),
            )

        def forward(self, x):
            return self.net(x)

    return (MLP,)


@app.cell
def _(MLP):
    # Just output the model — marimo renders it as a rich HTML tree
    model = MLP(in_features=4, hidden=64, out_features=3)
    model
    return


@app.cell
def _(mo):
    mo.md("""
    ## Build a model interactively
    """)
    return


@app.cell
def _(mo):
    hidden_slider = mo.ui.slider(16, 256, value=64, step=16, label="Hidden size")
    n_layers_slider = mo.ui.slider(1, 5, value=2, label="Hidden layers")
    mo.hstack([hidden_slider, n_layers_slider], gap=2)
    return hidden_slider, n_layers_slider


@app.cell
def _(hidden_slider, n_layers_slider, nn):
    def _build_model(hidden: int, n_layers: int) -> nn.Module:
        layers = []
        in_dim = 4
        for _ in range(n_layers):
            layers += [nn.Linear(in_dim, hidden), nn.ReLU()]
            in_dim = hidden
        layers.append(nn.Linear(in_dim, 3))
        return nn.Sequential(*layers)


    custom_model = _build_model(hidden_slider.value, n_layers_slider.value)
    params = sum(p.numel() for p in custom_model.parameters())
    custom_model
    return custom_model, params


@app.cell
def _(mo, params):
    mo.md(f"""
    Trainable parameters: **{params:,}**
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Training loop
    """)
    return


@app.cell
def _(mo):
    epochs_slider = mo.ui.slider(10, 200, value=50, step=10, label="Epochs")
    lr_slider = mo.ui.slider(
        1e-4, 1e-1, value=1e-2, step=1e-4, label="Learning rate"
    )
    train_btn = mo.ui.run_button(label="Train")
    mo.vstack([epochs_slider, lr_slider, train_btn])
    return epochs_slider, lr_slider, train_btn


@app.cell
def _(
    X_data,
    custom_model,
    epochs_slider,
    lr_slider,
    mo,
    nn,
    torch,
    train_btn,
    y_data,
):
    import copy

    mo.stop(not train_btn.value, mo.md("_Click **Train** to start._"))

    # deepcopy so each Train click starts from the same initial weights,
    # not continuing from the last run (custom_model's cell doesn't re-run on button click)
    _model = copy.deepcopy(custom_model)
    _optimizer = torch.optim.Adam(_model.parameters(), lr=lr_slider.value)
    _loss_fn = nn.CrossEntropyLoss()

    losses = []
    for _epoch in range(epochs_slider.value):
        _optimizer.zero_grad()
        _loss = _loss_fn(_model(X_data), y_data)
        _loss.backward()
        _optimizer.step()
        losses.append(_loss.item())

    trained_model = _model
    return losses, trained_model


@app.cell
def _(losses, plt):
    fig_loss, ax_loss = plt.subplots(figsize=(6, 3))
    ax_loss.plot(losses)
    ax_loss.set_xlabel("Epoch")
    ax_loss.set_ylabel("Loss")
    ax_loss.set_title("Training loss — penguins")
    fig_loss
    return


@app.cell
def _(X_data, mo, torch, trained_model, y_data):
    with torch.no_grad():
        _preds = trained_model(X_data).argmax(dim=1)
    _acc = (_preds == y_data).float().mean().item()
    mo.md(f"Accuracy: **{_acc:.1%}**")
    return


@app.cell
def _(trained_model):
    # Inspect the trained model — rich HTML tree again
    trained_model
    return


if __name__ == "__main__":
    app.run()

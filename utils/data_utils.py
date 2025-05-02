import pandas as pd
import matplotlib.pyplot as plt


def load_dataset() -> pd.DataFrame:
    """
    Load dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded dataset.
    """
    file_path = "data/sales_data.csv"
    return pd.read_csv(file_path)


def plot_dataset_generic(
    data: pd.DataFrame,
    plot_kind: str,
    title: str,
    xlabel: str,
    ylabel: str,
    output_path: str,
    plot_kwargs: dict = None,
) -> None:
    """
    Plot the dataset using a generic plot type.

    Args:
        data (pd.DataFrame): Data to plot.
        plot_kind (str): Type of plot to create. For pie charts, use "pie".
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis (ignored for pie charts).
        ylabel (str): Label for the y-axis (ignored for pie charts).
        output_path (str): File path to save the plot.
        plot_kwargs (dict, optional): Additional keyword arguments for the plotting function.
    """
    if plot_kwargs is None:
        plot_kwargs = {}

    plt.figure(figsize=(12, 6))

    if plot_kind.lower() == "pie":
        # For pie chart, data is expected to be a Series or similar
        plt.pie(data, **plot_kwargs)
        plt.title(title)
    else:
        data.plot(kind=plot_kind, marker="o", **plot_kwargs)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_path)

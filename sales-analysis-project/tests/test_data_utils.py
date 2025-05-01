import os
import pandas as pd
import pytest
from utils.data_utils import plot_dataset_generic


@pytest.fixture(autouse=True)
def close_plots():
    # Cleanup: Close plots after each test to avoid matplotlib state issues.
    yield
    import matplotlib.pyplot as plt

    plt.close("all")


def test_plot_line_chart(tmp_path):
    # Create a sample DataFrame for a line chart
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 15, 25]})
    output_file = tmp_path / "line_chart.png"
    # Call the function with plot_kind 'line'
    plot_dataset_generic(
        data=df,
        plot_kind="line",
        title="Line Chart Test",
        xlabel="X Axis",
        ylabel="Y Axis",
        output_path=str(output_file),
    )
    # Assert that output file exists and is not empty
    assert output_file.exists(), "Output file was not created."
    assert os.path.getsize(output_file) > 0, "Output file is empty."


def test_plot_pie_chart(tmp_path):
    # Create a sample Series for a pie chart
    data = pd.Series([30, 45, 25], index=["A", "B", "C"])
    output_file = tmp_path / "pie_chart.png"
    # Call the function with plot_kind 'pie'
    plot_dataset_generic(
        data=data,
        plot_kind="pie",
        title="Pie Chart Test",
        xlabel="",  # Ignored for pie charts
        ylabel="",  # Ignored for pie charts
        output_path=str(output_file),
        plot_kwargs={"autopct": "%1.1f%%"},
    )
    # Assert output file exists and is not empty
    assert output_file.exists(), "Output file was not created."
    assert os.path.getsize(output_file) > 0, "Output file is empty."


def test_plot_with_plot_kwargs(tmp_path):
    # Create a sample DataFrame for line chart with a custom color through plot_kwargs
    df = pd.DataFrame({"x": [0, 1, 2, 3], "y": [5, 15, 10, 20]})
    output_file = tmp_path / "custom_line_chart.png"
    # Define custom plotting kwargs
    custom_kwargs = {"color": "red"}
    plot_dataset_generic(
        data=df,
        plot_kind="line",
        title="Custom Line Chart Test",
        xlabel="Time",
        ylabel="Value",
        output_path=str(output_file),
        plot_kwargs=custom_kwargs,
    )
    # Assert output file exists and is not empty
    assert output_file.exists(), "Output file was not created."
    assert os.path.getsize(output_file) > 0, "Output file is empty."

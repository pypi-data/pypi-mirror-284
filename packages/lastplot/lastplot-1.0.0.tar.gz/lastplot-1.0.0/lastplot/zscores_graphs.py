import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import starbars

from lastplot.computing_statistics import get_test
from lastplot.graph_constructor import mpl_calc_series
from lastplot.saving import save_sheet

__all__: [
    "zscore_graph_lipid_class",
    "zscore_graph_lipid",
]


# Graphs by Z scores
def zscore_graph_lipid(
    df_final, control_name, experimental_name, output_path, palette, xlabel=None, ylabel=None, title=None, show=True
):
    """
    The `zscore_graph_lipid` function generates boxplots and statistical annotations for visualizing Z scores of lipids
    across regions. It performs the following tasks:

    - Iterates through each region and lipid combination in the final DataFrame (`df_final`).
    - Calculates Shapiro-Wilk and Levene's test results for normality and equality of variances.
    - Plots boxplots to visualize the distribution of Z scores, distinguishing between control and experimental groups.
    - Retrieves statistical test results (`pvalue` and `test`) using a custom function (`get_test`).
    - Annotates the plot with statistical significance indicators using `starbars.draw_annotation`.
    - Saves each plot as a PNG file in the specified `output_path`.
    - Optionally displays the plot (`show=True`) and closes it after display.

    The function also saves comments regarding the statistical tests performed for each lipid and region in an Excel
    sheet named "Comments" within the `output_path`.

    :param df_final: DataFrame containing Z scores and statistical test results.
    :param control_name: Name of the control group.
    :param experimental_name:Name of the experimental group.
    :param output_path: Path of the output folder.
    :param palette: Color palette for plotting.
    :param xlabel: Label for the x-axis. If None, defaults to "Genotype".
    :param ylabel: Label for the y-axis. If None, defaults to "Z Scores".
    :param title: Title for the plot. If None, defaults to "Z Scores for {lipid} in {region}".
    :param show: Whether to display plots interactively (default True).

    """

    group_width = 0.4
    bar_width = 0.04
    bar_gap = 0.02
    palette = sns.color_palette(palette)

    if not os.path.exists(output_path + "/output/zscore_graphs/lipid"):
        os.makedirs(output_path + "/output/zscore_graphs/lipid")

    for (region, lipid), data in df_final.groupby(["Regions", "Lipids"]):
        shapiro = data.iloc[0]["Shapiro Normality"]
        levene = data.iloc[0]["Levene Equality"]
        test = get_test(shapiro, levene)

    test_comment = [f"{test} will be performed for all of the lipids"]
    save_sheet(test_comment, "Comments", output_path)

    for (region, lipid), data in df_final.groupby(["Regions", "Lipids"]):
        print(f"Creating graph for {lipid} in {region}")
        control_group = data[data["Genotype"] == control_name]
        experimental_group = data[data["Genotype"] != control_name]
        control_values = control_group["Z Scores"]
        experimental_values = experimental_group["Z Scores"]

        fig, ax = plt.subplots()
        bar_width, positions = mpl_calc_series(
            len(lipid), 2, group_width=group_width, bar_width=bar_width, bar_gap=bar_gap
        )

        # Create boxplots
        bp1 = ax.boxplot(
            control_values,
            positions=[positions[0]],
            widths=bar_width,
            patch_artist=True,
            boxprops=dict(facecolor=palette[0], color="k"),
            medianprops=dict(color="k"),
        )
        bp2 = ax.boxplot(
            experimental_values,
            positions=[positions[1]],
            widths=bar_width,
            patch_artist=True,
            boxprops=dict(facecolor=palette[1], color="k"),
            medianprops=dict(color="k"),
        )

        # Add scatterplot
        ax.scatter(np.ones(len(control_values)) * positions[0], control_values, color="k", s=6, zorder=3)
        ax.scatter(
            np.ones(len(experimental_values)) * positions[1],
            experimental_values,
            color="k",
            s=6,
            zorder=3,
        )

        # Add statistical annotation
        pvalue, test = get_test(shapiro, levene)
        pairs = [(control_name, experimental_name, pvalue)]
        starbars.draw_annotation(pairs)
        comment = [f"For z scores of {lipid} in {region}, P-value is {pvalue}."]
        save_sheet(comment, "Comments", output_path)

        if xlabel:
            plt.xlabel(xlabel)
        else:
            plt.xlabel("Genotype")
        if ylabel:
            plt.ylabel(ylabel)
        else:
            plt.ylabel("Z Scores")
        if title:
            ax.set_title(title)
        else:
            ax.title(f"Z Scores for {lipid} in {region}")

        plt.savefig(output_path + f"/output/zscore_graphs/lipid/Z Scores for {lipid} in {region}.png", dpi=1200)

        if show:
            plt.show()
        plt.close()


def zscore_graph_lipid_class(
    df_final, control_name, experimental_name, output_path, palette, xlabel=None, ylabel=None, title=None, show=True
):
    """
    The `zscore_graph_lipid_class` function generates boxplots to visualize the distribution of Z scores across different lipid classes within each region. It performs the following tasks:

    - Iterates through each region in the DataFrame (`df_final`).
    - Plots boxplots to show the distribution of Z scores for each lipid class, distinguishing between control and experimental groups (`control_name` and `experimental_name`).
    - Customizable plots with appropriate labels and title for better visualization.
    - Saves each plot as a PNG file in the specified `output_path`.
    - Optionally displays the plot (`show=True`).

    :param df_final: Final DataFrame containing Z scores and statistical test results.
    :param control_name: Name of the control group genotype.
    :param experimental_name: Name of the experimental group genotype.
    :param output_path: Path to save output graphs.
    :param palette: Color palette for plotting.
    :param xlabel: Label for the x-axis. If None, defaults to "Lipid Class".
    :param ylabel: Label for the y-axis. If None, defaults to "Z Scores".
    :param title: Title for the plot. If None, defaults to "Z Scores in {region}".
    :param show: Whether to display plots interactively (default True).

    """

    group_width = 0.4
    bar_width = 0.04
    bar_gap = 0.02
    palette = sns.color_palette(palette)

    if not os.path.exists(output_path + "/output/zscore_graphs/lipid_class"):
        os.makedirs(output_path + "/output/zscore_graphs/lipid_class")

    for region, region_data in df_final.groupby("Regions"):
        print(f"Creating graphs for {region}")

        lipid_classes = region_data["Lipid Class"].unique()

        for i, lipid_class in enumerate(lipid_classes):
            fig, ax = plt.subplots()
            data = region_data[region_data["Lipid Class"] == lipid_class]
            lipids = data["Lipids"].unique()

            bar_width, positions = mpl_calc_series(
                len(lipids), 2, group_width=group_width, bar_width=bar_width, bar_gap=bar_gap
            )

            for j, lipid in enumerate(lipids):
                control_values = data[(data["Lipids"] == lipid) & (data["Genotype"] == control_name)]["Z Scores"]
                experimental_values = data[(data["Lipids"] == lipid) & (data["Genotype"] == experimental_name)][
                    "Z Scores"
                ]

                # Create boxplots
                ax.boxplot(
                    control_values,
                    positions=[positions[j][0]],
                    widths=bar_width,
                    patch_artist=True,
                    boxprops=dict(facecolor=palette[0], color="k"),
                    medianprops=dict(color="k"),
                )
                ax.boxplot(
                    experimental_values,
                    positions=[positions[j][1]],
                    widths=bar_width,
                    patch_artist=True,
                    boxprops=dict(facecolor=palette[1], color="k"),
                    medianprops=dict(color="k"),
                )

                # Add scatter points
                ax.scatter(
                    np.ones(len(control_values)) * positions[j][0],
                    control_values,
                    color="k",
                    s=6,
                    zorder=3,
                )
                ax.scatter(
                    np.ones(len(experimental_values)) * positions[j][1],
                    experimental_values,
                    color="k",
                    s=6,
                    zorder=3,
                )

            ax.set_xticks([*range(len(lipids))])
            ax.set_xticklabels(lipids, rotation=90)

            if xlabel:
                ax.set_xlabel(xlabel)
            else:
                ax.set_xlabel(lipid_class)
            if ylabel:
                ax.set_ylabel(ylabel)
            else:
                ax.set_ylabel("Z Scores")
            if title:
                ax.set_title(title)
            else:
                ax.set_title(f"Z Scores in {region}")

            plt.tight_layout()
            plt.savefig(
                f"{output_path}/output/zscore_graphs/lipid_class/Z-Scores {region} {lipid_class}.png",
                dpi=1200,
            )
            if show:
                plt.show()

            plt.close()

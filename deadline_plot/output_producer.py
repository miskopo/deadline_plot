import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from deadline_plot.file_processor import FileProcessor


class OutputProducer:
    def __init__(self, path: str, file_processor: FileProcessor):
        self.path = path
        self.fp = file_processor

    def __call__(self, *args, **kwargs):
        self.generate_timeline()

    def generate_timeline(self):
        df = self.fp.df
        dates = df['dates']
        names = df['names']
        # Choose some nice levels
        levels = np.tile([-5, 5, -3, 3, -1, 1],
                         int(np.ceil(len(dates) / 6)))[:len(dates)]

        # Create figure and plot a stem plot with the date
        fig, ax = plt.subplots(figsize=(29.7, 21), constrained_layout=False)
        ax.set(title="Deadlines")

        markerline, stemline, baseline = ax.stem(dates, levels,
                                                 linefmt="C3-", basefmt="k-",
                                                 use_line_collection=True)

        plt.setp(markerline, mec="k", mfc="w", zorder=3)

        # Shift the markers to the baseline by replacing the y-data by zeros.
        markerline.set_ydata(np.zeros(len(dates)))

        # annotate lines
        vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
        for d, l, r, va in zip(dates, levels, names, vert):
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3 + np.log(len(r))),
                        textcoords="offset points", va=va, ha="right", fontsize=18)
        plt.tick_params(labelsize=16)

        # format xaxis with daily intervals
        ax.get_xaxis().set_major_locator(mdates.DayLocator(interval=1))
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%d %b"))
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        plt.grid(True)

        # remove y axis and spines
        ax.get_yaxis().set_visible(False)
        for spine in ["left", "top", "right"]:
            ax.spines[spine].set_visible(False)

        ax.margins(y=0.1)
        plt.show()

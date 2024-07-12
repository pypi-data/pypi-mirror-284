"""
Contains a plotter class: LineChart.

NOTE: this module is private. All functions and objects are available in the main
`dataplot` namespace - use that instead.

"""

from typing import TYPE_CHECKING, Optional

from attrs import define

from ..plotter import PlotSettable
from .base import Plotter

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from ..container import AxesWrapper
    from ..dataset import PlotDataSet

__all__ = ["LineChart"]


@define
class LineChart(Plotter):
    """
    A plotter class that creates a line chart.

    """

    ticks: Optional["NDArray | PlotDataSet"]
    scatter: bool

    def paint(self, ax: "AxesWrapper", reflex: None = None) -> None:
        ax.set_default(title="Line Chart")
        ax.loading(self.settings)
        self.__plot(ax)
        return reflex

    def __plot(self, ax: "AxesWrapper") -> None:
        if isinstance(self.ticks, PlotSettable):
            ticks = self.ticks.data
        else:
            ticks = self.ticks
        if ticks is None:
            ax.ax.plot(self.data, label=self.label)
        elif (len_t := len(ticks)) == (len_d := len(self.data)):
            ax.ax.plot(ticks, self.data, label=self.label)
        else:
            raise ValueError(
                "ticks and data must have the same length, but have "
                f"lengths {len_t} and {len_d}"
            )
        if self.scatter:
            ax.ax.scatter(self.data)

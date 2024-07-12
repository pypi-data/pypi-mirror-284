"""
Contains dataclasses: PlotSettings, Plotter.

NOTE: this module is private. All functions and objects are available in the main
`dataplot` namespace - use that instead.

"""

from typing import TYPE_CHECKING, Any, Optional, Self, TypeVar, Unpack

from attrs import Factory, asdict, define, field

if TYPE_CHECKING:
    from ._typing import (
        DefaultVar,
        FontDict,
        PlotSettableVar,
        SettingDict,
        SettingKey,
        StyleStr,
        SubplotDict,
    )


__all__ = ["PlotSettings", "PlotSettable"]

T = TypeVar("T")


@define
class PlotSettings:
    """Stores and manages settings for plotting."""

    title: Optional[str] = None
    xlabel: Optional[str] = None
    ylabel: Optional[str] = None
    alpha: Optional[float] = None
    dpi: Optional[float] = None
    grid: Optional[bool] = None
    grid_alpha: Optional[float] = None
    style: Optional["StyleStr"] = None
    figsize: Optional[tuple[int, int]] = None
    fontdict: Optional["FontDict"] = None
    legend_loc: Optional[str] = None
    subplots_adjust: Optional["SubplotDict"] = None

    def __getitem__(self, __key: "SettingKey") -> Any:
        return getattr(self, __key)

    def __setitem__(self, __key: "SettingKey", __value: Any) -> None:
        setattr(self, __key, __value)

    def __repr__(self) -> str:
        return self.__class__.__name__ + "(" + self.repr_not_none() + ")"

    def repr_not_none(self) -> str:
        """
        Returns a string representation of attributes with not-None values.

        Returns
        -------
        str
            String representation.

        """
        diff = [f"{k}={repr(v)}" for k, v in asdict(self).items() if v is not None]
        return ", ".join(diff)

    def keys(self) -> list["SettingKey"]:
        """
        Keys of settings.

        Returns
        -------
        list[SettingKey]
            Keys of the settings.

        """
        return getattr(self, "__match_args__")

    def reset(self) -> None:
        """
        Reset all the settings to None.

        """
        for k in self.keys():
            self[k] = None


@define(init=False)
class PlotSettable:
    """Contains an attribute of plot settings, and provides methods for
    handling these settings.

    """

    settings: PlotSettings = field(default=Factory(PlotSettings), init=False)

    def _set(
        self, *, inplace: bool = False, **kwargs: Unpack["SettingDict"]
    ) -> Self | None:
        obj = self if inplace else self.copy()
        keys = obj.settings.keys()
        for k, v in kwargs.items():
            if k in keys and v is not None:
                obj.setting_check(k, v)
                if isinstance(v, dict) and isinstance(obj.settings[k], dict):
                    obj.settings[k] = {**obj.settings[k], **v}
                else:
                    obj.settings[k] = v
        if not inplace:
            return obj

    def setting_check(self, key: "SettingKey", value: Any) -> None:
        """
        Checks if a new setting is legal.

        Parameters
        ----------
        key : SettingKey
            Key of the setting.
        value : Any
            Value of the setting.

        """

    def set_default(self, **kwargs: Unpack["SettingDict"]) -> None:
        """
        Sets the default settings.

        Parameters
        ----------
        **kwargs : Unpack[SettingDict]
            Specifies the settings.

        """
        keys = self.settings.keys()
        for k, v in kwargs.items():
            if k in keys and self.settings[k] is None:
                self.settings[k] = v

    def loading(self, settings: PlotSettings) -> None:
        """
        Load in the settings.

        Parameters
        ----------
        settings : PlotSettings
            An instance of `PlotSettings`.

        """
        self._set(inplace=True, **asdict(settings))

    def get_setting(
        self, key: "SettingKey", default: Optional["DefaultVar"] = None
    ) -> "DefaultVar | Any":
        """
        Returns the value of a setting if it is not None, otherwise returns the
        default value.

        Parameters
        ----------
        key : SettingKey
            Key of the setting.
        default : DefaultVar, optional
            Specifies the default value to be returned if the requested value
            is None, by default None.

        Returns
        -------
        DefaultVar | Any
            Value of the setting.

        """
        return default if (value := self.settings[key]) is None else value

    def customize(
        self, cls: type["PlotSettableVar"], *args, **kwargs
    ) -> "PlotSettableVar":
        """
        Initialize another instance with the same settings as `self`.

        Parameters
        ----------
        cls : type[PlotSetableVar]
            Type of the new instance.
        *args :
            Positional arguments.
        **kwargs :
            Keyword arguments.

        Returns
        -------
        PlotSetableVar
            The new instance.

        Raises
        ------
        ValueError
            Raised when `cls` cannot be customized.

        """
        if not issubclass(cls, PlotSettable):
            raise ValueError(f"type {cls} cannot be customized")
        matched: dict[str, Any] = {}
        unmatched: dict[str, Any] = {}
        for k, v in kwargs.items():
            if k in cls.__init__.__code__.co_varnames[1:]:
                matched[k] = v
            else:
                unmatched[k] = v
        obj = cls(*args, **matched)
        obj.settings = PlotSettings(**asdict(self.settings))
        for k, v in unmatched.items():
            setattr(obj, k, v)
        return obj

    def copy(self) -> Self:
        """
        Copy the instance of self (but not deepcopy).

        Returns
        -------
        Self
            A new instance of self.

        """
        raise TypeError(f"cannot copy instance of {self.__class__}")

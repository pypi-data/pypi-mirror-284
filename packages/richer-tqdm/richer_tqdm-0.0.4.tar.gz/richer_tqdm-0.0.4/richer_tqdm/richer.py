#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ──────────────────────────────────────────────────────────────────────────────
"""
Improved `rich.progress` decorator for iterators.

Usage:
>>> from richer_tqdm import trange, tqdm
>>> for i in trange(10):
...     ...
"""
# ──────────────────────────────────────────────────────────────────────────────
from math import fabs
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from rich.progress import BarColumn
from rich.progress import Progress
from rich.progress import ProgressColumn
from rich.progress import Text
from rich.progress import TimeElapsedColumn
from rich.progress import TimeRemainingColumn
from safe_assert import safe_assert as sassert
from tqdm.std import tqdm as std_tqdm

# ──────────────────────────────────────────────────────────────────────────────

__author__ = {"github.com/": ["casperdcl", "glensc", "emaballarin"]}
__all__ = ["tqdm_rich", "trrange", "tqdm", "trange"]

MSUFFIXES: List[str] = ["", "K", "M", "G", "T", "P", "E", "Z", "Y", "X", "W", "V", "U"]

# ──────────────────────────────────────────────────────────────────────────────


def pick_unit_and_suffix(
    quantity: Union[int, float],
    base: Union[int, float],
    suffixes: List[str],
    do_apply: bool = True,
) -> Tuple[Union[int, float], str]:
    if not do_apply:
        return 1, ""
    sassert(quantity >= 0, "`quantity` must be >= 0")
    sassert(base >= 1, "`base` must be >= 1")
    sassert(len(suffixes) >= 1, "`suffixes` must have at least one element")
    unit: Union[int, float] = 1
    suffix: str = ""
    for i, suffix in enumerate(suffixes):
        unit: Union[int, float] = base**i
        if quantity < unit * base:
            break
    return unit, suffix


def make_improper(
    quantity: Union[int, float], nunit: str, dunit: str
) -> Tuple[Union[int, float], str, str]:
    if fabs(quantity) < 1:
        return 1 / quantity, dunit, nunit
    return quantity, nunit, dunit


# ──────────────────────────────────────────────────────────────────────────────


class FractionColumn(ProgressColumn):
    """Renders human-readable completed/total fraction, e.g. '0.5/2.3 G'."""

    def __init__(self, unit_scale: bool = False, unit_divisor: int = 1000) -> None:
        self.unit_scale: bool = unit_scale
        self.unit_divisor: Union[int, float] = unit_divisor
        super().__init__()

    def render(self, task) -> Text:
        """Show completed/total fraction."""
        completed: int = int(task.completed)
        total: int = int(task.total)
        unit, suffix = pick_unit_and_suffix(
            total, self.unit_divisor, MSUFFIXES, self.unit_scale
        )
        precision: int = 0 if unit == 1 else 1
        return Text(
            f"{completed/unit:,.{precision}f}/{total/unit:,.{precision}f} {suffix}",
            style="progress.download",
        )


class RateColumn(ProgressColumn):
    """Renders human-readable completion rate, e.g. '2.45 it/s'."""

    def __init__(
        self,
        unit: str = "",
        unit_scale: bool = False,
        unit_divisor: Union[int, float] = 1000,
        precision: int = 2,
    ) -> None:
        self.unit: str = unit
        self.unit_scale: bool = unit_scale
        self.unit_divisor: Union[int, float] = unit_divisor
        self.precision: int = precision
        super().__init__()

    def render(self, task) -> Text:
        """Show completion rate."""
        speed: Optional[float] = task.speed
        if speed is None:
            return Text(f"? {self.unit}/s", style="progress.data.speed")
        unit, suffix = pick_unit_and_suffix(
            speed, self.unit_divisor, MSUFFIXES, self.unit_scale
        )
        ispeed, up, down = make_improper((speed / unit), f"{suffix}{self.unit}", "s")
        return Text(
            f"{ispeed:,.{self.precision}f} {up}/{down}",
            style="progress.data.speed",
        )


class PostfixColumn(ProgressColumn):
    """Renders tqdm postfix."""

    def __init__(self, tqdm_class: std_tqdm) -> None:
        self.tqdm_class: std_tqdm = tqdm_class
        super().__init__()

    def render(self, task) -> Text:
        """Show tqdm postfix."""
        return Text(
            (
                f"[ {self.tqdm_class.postfix} ]"
                if self.tqdm_class.postfix is not None
                else ""
            ),
            style="progress.postfix",
        )


# ──────────────────────────────────────────────────────────────────────────────


class TqdmRich(std_tqdm):
    """rich.progress version of tqdm"""

    def __init__(self, *args, **kwargs) -> None:
        """
        Accepts the following parameters, *in addition* to
        the usual parameters accepted by `tqdm`.

        Parameters
        ----------
        progress  : tuple, optional
            arguments for `rich.progress.Progress()`.
        options  : dict, optional
            keyword arguments for `rich.progress.Progress()`.
        """
        kwargs = kwargs.copy()
        kwargs["gui"] = True
        kwargs["disable"] = bool(kwargs.get("disable", False))
        progress = kwargs.pop("progress", None)
        options = kwargs.pop("options", {}).copy()
        render_postfix: bool = kwargs.pop("render_postfix", False)
        super().__init__(*args, **kwargs)

        if self.disable:
            return

        d = self.format_dict
        drop_postfix: List[PostfixColumn] = (
            [PostfixColumn(self)] if render_postfix else []
        )
        if progress is None:
            progress = (
                "[progress.description]{task.description}"
                "[progress.percentage]{task.percentage:>4.0f}%",
                BarColumn(bar_width=None),
                FractionColumn(
                    unit_scale=d["unit_scale"], unit_divisor=d["unit_divisor"]
                ),
                "[",
                TimeElapsedColumn(),
                "<",
                TimeRemainingColumn(),
                ",",
                RateColumn(
                    unit=d["unit"],
                    unit_scale=d["unit_scale"],
                    unit_divisor=d["unit_divisor"],
                ),
                "]",
                *drop_postfix,
            )
        options.setdefault("transient", not self.leave)
        self._prog = Progress(*progress, **options)
        self._prog.__enter__()
        self._task_id = self._prog.add_task(self.desc or "", **d)

    def close(self) -> None:
        if self.disable:
            return
        self.display()
        super().close()
        self._prog.__exit__(None, None, None)

    def clear(self, *_, **__) -> None:
        # Must do nothing
        pass

    def display(self, *_, **__) -> None:
        if not hasattr(self, "_prog"):
            return
        self._prog.update(self._task_id, completed=self.n, description=self.desc)

    def reset(self, total=None) -> None:
        """
        Resets to 0 iterations for repeated use.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """
        if hasattr(self, "_prog"):
            self._prog.reset(self._task_id, total=total)
        super().reset(total=total)


# ──────────────────────────────────────────────────────────────────────────────


def trrange(*args, **kwargs) -> TqdmRich:
    """Shortcut for `tqdm.rich.tqdm(range(*args), **kwargs)`."""
    return TqdmRich(range(*args), **kwargs)


# ──────────────────────────────────────────────────────────────────────────────

# Aliases
tqdm_rich = TqdmRich
tqdm = TqdmRich
trange = trrange

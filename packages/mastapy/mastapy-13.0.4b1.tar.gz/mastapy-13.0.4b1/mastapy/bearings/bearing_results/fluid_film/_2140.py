"""LoadedGreaseFilledJournalBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.fluid_film import _2142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm",
    "LoadedGreaseFilledJournalBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2139
    from mastapy.bearings.bearing_results import _1974, _1977, _1969
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedGreaseFilledJournalBearingResults",)


Self = TypeVar("Self", bound="LoadedGreaseFilledJournalBearingResults")


class LoadedGreaseFilledJournalBearingResults(_2142.LoadedPlainJournalBearingResults):
    """LoadedGreaseFilledJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedGreaseFilledJournalBearingResults"
    )

    class _Cast_LoadedGreaseFilledJournalBearingResults:
        """Special nested class for casting LoadedGreaseFilledJournalBearingResults to subclasses."""

        def __init__(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
            parent: "LoadedGreaseFilledJournalBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_2142.LoadedPlainJournalBearingResults":
            return self._parent._cast(_2142.LoadedPlainJournalBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_2139.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
        ) -> "LoadedGreaseFilledJournalBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "LoadedGreaseFilledJournalBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults":
        return self._Cast_LoadedGreaseFilledJournalBearingResults(self)

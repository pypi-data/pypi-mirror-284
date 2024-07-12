"""LoadedThreePointContactBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2022
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedThreePointContactBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2053
    from mastapy.bearings.bearing_results import _1974, _1977, _1969
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedThreePointContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedThreePointContactBallBearingResults")


class LoadedThreePointContactBallBearingResults(_2022.LoadedBallBearingResults):
    """LoadedThreePointContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedThreePointContactBallBearingResults"
    )

    class _Cast_LoadedThreePointContactBallBearingResults:
        """Special nested class for casting LoadedThreePointContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
            parent: "LoadedThreePointContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "LoadedThreePointContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedThreePointContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults":
        return self._Cast_LoadedThreePointContactBallBearingResults(self)

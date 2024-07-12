"""LoadedAngularContactBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2022
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2006, _2053
    from mastapy.bearings.bearing_results import _1974, _1977, _1969
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedAngularContactBallBearingResults")


class LoadedAngularContactBallBearingResults(_2022.LoadedBallBearingResults):
    """LoadedAngularContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactBallBearingResults"
    )

    class _Cast_LoadedAngularContactBallBearingResults:
        """Special nested class for casting LoadedAngularContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
            parent: "LoadedAngularContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "_2006.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(
                _2006.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "LoadedAngularContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedAngularContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults":
        return self._Cast_LoadedAngularContactBallBearingResults(self)

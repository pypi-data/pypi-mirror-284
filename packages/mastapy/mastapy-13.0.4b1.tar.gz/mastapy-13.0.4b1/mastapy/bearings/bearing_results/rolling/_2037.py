"""LoadedFourPointContactBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2022
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedFourPointContactBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1992, _2053
    from mastapy.bearings.bearing_results import _1974, _1977, _1969
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFourPointContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedFourPointContactBallBearingResults")


class LoadedFourPointContactBallBearingResults(_2022.LoadedBallBearingResults):
    """LoadedFourPointContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedFourPointContactBallBearingResults"
    )

    class _Cast_LoadedFourPointContactBallBearingResults:
        """Special nested class for casting LoadedFourPointContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
            parent: "LoadedFourPointContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
        ) -> "LoadedFourPointContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedFourPointContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def raceway_control(self: Self) -> "_1992.FrictionModelForGyroscopicMoment":
        """mastapy.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RacewayControl

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.FrictionModelForGyroscopicMoment",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._1992",
            "FrictionModelForGyroscopicMoment",
        )(value)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFourPointContactBallBearingResults._Cast_LoadedFourPointContactBallBearingResults":
        return self._Cast_LoadedFourPointContactBallBearingResults(self)

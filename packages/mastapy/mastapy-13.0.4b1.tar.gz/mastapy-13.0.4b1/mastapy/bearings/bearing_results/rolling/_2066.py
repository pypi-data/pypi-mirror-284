"""LoadedTaperRollerBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2043
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedTaperRollerBearingDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1979, _1976, _1968


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTaperRollerBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedTaperRollerBearingDutyCycle")


class LoadedTaperRollerBearingDutyCycle(_2043.LoadedNonBarrelRollerBearingDutyCycle):
    """LoadedTaperRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTaperRollerBearingDutyCycle")

    class _Cast_LoadedTaperRollerBearingDutyCycle:
        """Special nested class for casting LoadedTaperRollerBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
            parent: "LoadedTaperRollerBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "_2043.LoadedNonBarrelRollerBearingDutyCycle":
            return self._parent._cast(_2043.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "_1979.LoadedRollingBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1979

            return self._parent._cast(_1979.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "_1976.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1976

            return self._parent._cast(_1976.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "_1968.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1968

            return self._parent._cast(_1968.LoadedBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "LoadedTaperRollerBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
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
        self: Self, instance_to_wrap: "LoadedTaperRollerBearingDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle":
        return self._Cast_LoadedTaperRollerBearingDutyCycle(self)

"""LoadedNonBarrelRollerElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2048
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNonBarrelRollerElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2013,
        _2016,
        _2028,
        _2040,
        _2067,
        _2034,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerElement",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerElement")


class LoadedNonBarrelRollerElement(_2048.LoadedRollerBearingElement):
    """LoadedNonBarrelRollerElement

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonBarrelRollerElement")

    class _Cast_LoadedNonBarrelRollerElement:
        """Special nested class for casting LoadedNonBarrelRollerElement to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
            parent: "LoadedNonBarrelRollerElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2048.LoadedRollerBearingElement":
            return self._parent._cast(_2048.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2034.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedElement)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2013.LoadedAxialThrustCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2013

            return self._parent._cast(
                _2013.LoadedAxialThrustCylindricalRollerBearingElement
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2016.LoadedAxialThrustNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2016

            return self._parent._cast(_2016.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2028.LoadedCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_needle_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2040.LoadedNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedNeedleRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "_2067.LoadedTaperRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2067

            return self._parent._cast(_2067.LoadedTaperRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
        ) -> "LoadedNonBarrelRollerElement":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonBarrelRollerElement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_smt_rib_stress_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSMTRibStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement":
        return self._Cast_LoadedNonBarrelRollerElement(self)

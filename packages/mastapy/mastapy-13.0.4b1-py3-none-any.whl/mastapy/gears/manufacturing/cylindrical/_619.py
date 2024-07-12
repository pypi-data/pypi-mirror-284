"""CylindricalManufacturedGearDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1238
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1236, _1233


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearDutyCycle",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearDutyCycle")


class CylindricalManufacturedGearDutyCycle(_1238.GearImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalManufacturedGearDutyCycle")

    class _Cast_CylindricalManufacturedGearDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
            parent: "CylindricalManufacturedGearDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
        ) -> "_1238.GearImplementationAnalysisDutyCycle":
            return self._parent._cast(_1238.GearImplementationAnalysisDutyCycle)

        @property
        def gear_design_analysis(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
        ) -> "_1236.GearDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
        ) -> "_1233.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1233

            return self._parent._cast(_1233.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
        ) -> "CylindricalManufacturedGearDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle":
        return self._Cast_CylindricalManufacturedGearDutyCycle(self)

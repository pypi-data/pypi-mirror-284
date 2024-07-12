"""GearSetImplementationAnalysisDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1247
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysisDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _623
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120
    from mastapy.gears.analysis import _1244, _1235


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysisDutyCycle",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysisDutyCycle")


class GearSetImplementationAnalysisDutyCycle(
    _1247.GearSetImplementationAnalysisAbstract
):
    """GearSetImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetImplementationAnalysisDutyCycle"
    )

    class _Cast_GearSetImplementationAnalysisDutyCycle:
        """Special nested class for casting GearSetImplementationAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
            parent: "GearSetImplementationAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "_1247.GearSetImplementationAnalysisAbstract":
            return self._parent._cast(_1247.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "_1244.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1244

            return self._parent._cast(_1244.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "_1235.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "_623.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "_1120.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120

            return self._parent._cast(_1120.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
        ) -> "GearSetImplementationAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "GearSetImplementationAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle":
        return self._Cast_GearSetImplementationAnalysisDutyCycle(self)

"""CylindricalGearSetMicroGeometryDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1248
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _466
    from mastapy.gears.gear_two_d_fe_analysis import _900
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111
    from mastapy.gears.analysis import _1247, _1244, _1235


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetMicroGeometryDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearSetMicroGeometryDutyCycle")


class CylindricalGearSetMicroGeometryDutyCycle(
    _1248.GearSetImplementationAnalysisDutyCycle
):
    """CylindricalGearSetMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetMicroGeometryDutyCycle"
    )

    class _Cast_CylindricalGearSetMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearSetMicroGeometryDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
            parent: "CylindricalGearSetMicroGeometryDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
        ) -> "_1248.GearSetImplementationAnalysisDutyCycle":
            return self._parent._cast(_1248.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
        ) -> "_1247.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1247

            return self._parent._cast(_1247.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
        ) -> "_1244.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1244

            return self._parent._cast(_1244.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
        ) -> "_1235.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
        ) -> "CylindricalGearSetMicroGeometryDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearSetMicroGeometryDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_466.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tiff_analysis(self: Self) -> "_900.CylindricalGearSetTIFFAnalysisDutyCycle":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearSetTIFFAnalysisDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshes(self: Self) -> "List[_1111.CylindricalGearMeshMicroGeometryDutyCycle]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometryDutyCycle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle":
        return self._Cast_CylindricalGearSetMicroGeometryDutyCycle(self)

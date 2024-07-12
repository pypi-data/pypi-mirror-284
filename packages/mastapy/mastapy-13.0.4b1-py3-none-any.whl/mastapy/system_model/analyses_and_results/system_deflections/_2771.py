"""CylindricalPlanetGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalPlanetGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.power_flows import _4104
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2766,
        _2782,
        _2803,
        _2736,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalPlanetGearSystemDeflection")


class CylindricalPlanetGearSystemDeflection(
    _2768.CylindricalGearSystemDeflectionWithLTCAResults
):
    """CylindricalPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearSystemDeflection"
    )

    class _Cast_CylindricalPlanetGearSystemDeflection:
        """Special nested class for casting CylindricalPlanetGearSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
            parent: "CylindricalPlanetGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2768.CylindricalGearSystemDeflectionWithLTCAResults":
            return self._parent._cast(
                _2768.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2766.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2782.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "CylindricalPlanetGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4104.CylindricalPlanetGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection":
        return self._Cast_CylindricalPlanetGearSystemDeflection(self)

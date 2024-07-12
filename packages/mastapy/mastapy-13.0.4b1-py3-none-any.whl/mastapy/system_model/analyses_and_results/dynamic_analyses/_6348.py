"""CylindricalPlanetGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CylindricalPlanetGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6358,
        _6377,
        _6323,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearDynamicAnalysis")


class CylindricalPlanetGearDynamicAnalysis(_6345.CylindricalGearDynamicAnalysis):
    """CylindricalPlanetGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearDynamicAnalysis")

    class _Cast_CylindricalPlanetGearDynamicAnalysis:
        """Special nested class for casting CylindricalPlanetGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
            parent: "CylindricalPlanetGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6345.CylindricalGearDynamicAnalysis":
            return self._parent._cast(_6345.CylindricalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6358.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "CylindricalPlanetGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearDynamicAnalysis.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis":
        return self._Cast_CylindricalPlanetGearDynamicAnalysis(self)

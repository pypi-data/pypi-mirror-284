"""CylindricalPlanetGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CylindricalPlanetGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.system_deflections import _2771
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4657,
        _4679,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysis")


class CylindricalPlanetGearModalAnalysis(_4642.CylindricalGearModalAnalysis):
    """CylindricalPlanetGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearModalAnalysis")

    class _Cast_CylindricalPlanetGearModalAnalysis:
        """Special nested class for casting CylindricalPlanetGearModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
            parent: "CylindricalPlanetGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4642.CylindricalGearModalAnalysis":
            return self._parent._cast(_4642.CylindricalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4657.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "CylindricalPlanetGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2771.CylindricalPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis":
        return self._Cast_CylindricalPlanetGearModalAnalysis(self)

"""PlanetaryGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PlanetaryGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3845,
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetStabilityAnalysis")


class PlanetaryGearSetStabilityAnalysis(_3833.CylindricalGearSetStabilityAnalysis):
    """PlanetaryGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetStabilityAnalysis")

    class _Cast_PlanetaryGearSetStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
            parent: "PlanetaryGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3833.CylindricalGearSetStabilityAnalysis":
            return self._parent._cast(_3833.CylindricalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "PlanetaryGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2562.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis":
        return self._Cast_PlanetaryGearSetStabilityAnalysis(self)

"""VirtualComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "VirtualComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.system_deflections import _2856
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5805,
        _5806,
        _5817,
        _5818,
        _5857,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysis")


class VirtualComponentHarmonicAnalysis(_5807.MountableComponentHarmonicAnalysis):
    """VirtualComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysis")

    class _Cast_VirtualComponentHarmonicAnalysis:
        """Special nested class for casting VirtualComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            parent: "VirtualComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5805.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5806.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.MeasurementComponentHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5817.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5818.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.PowerLoadHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5857.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5857,
            )

            return self._parent._cast(_5857.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "VirtualComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "_2856.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

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
    ) -> "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis":
        return self._Cast_VirtualComponentHarmonicAnalysis(self)

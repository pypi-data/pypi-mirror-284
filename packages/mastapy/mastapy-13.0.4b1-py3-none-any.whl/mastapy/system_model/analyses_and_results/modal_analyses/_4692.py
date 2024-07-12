"""PulleyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "PulleyModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4636,
        _4679,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PulleyModalAnalysis",)


Self = TypeVar("Self", bound="PulleyModalAnalysis")


class PulleyModalAnalysis(_4632.CouplingHalfModalAnalysis):
    """PulleyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyModalAnalysis")

    class _Cast_PulleyModalAnalysis:
        """Special nested class for casting PulleyModalAnalysis to subclasses."""

        def __init__(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
            parent: "PulleyModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_4632.CouplingHalfModalAnalysis":
            return self._parent._cast(_4632.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "_4636.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.CVTPulleyModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis",
        ) -> "PulleyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyModalAnalysis._Cast_PulleyModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2611.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6962.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2814.PulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PulleyModalAnalysis._Cast_PulleyModalAnalysis":
        return self._Cast_PulleyModalAnalysis(self)

"""CVTPulleyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CVTPulleyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4632,
        _4679,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyModalAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyModalAnalysis")


class CVTPulleyModalAnalysis(_4692.PulleyModalAnalysis):
    """CVTPulleyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyModalAnalysis")

    class _Cast_CVTPulleyModalAnalysis:
        """Special nested class for casting CVTPulleyModalAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
            parent: "CVTPulleyModalAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4692.PulleyModalAnalysis":
            return self._parent._cast(_4692.PulleyModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4632.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis",
        ) -> "CVTPulleyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2754.CVTPulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPulleyModalAnalysis._Cast_CVTPulleyModalAnalysis":
        return self._Cast_CVTPulleyModalAnalysis(self)

"""VirtualComponentModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "VirtualComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.system_deflections import _2856
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4673,
        _4674,
        _4690,
        _4691,
        _4726,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysis")


class VirtualComponentModalAnalysis(_4679.MountableComponentModalAnalysis):
    """VirtualComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentModalAnalysis")

    class _Cast_VirtualComponentModalAnalysis:
        """Special nested class for casting VirtualComponentModalAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            parent: "VirtualComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4673.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4674.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.MeasurementComponentModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4690.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4691.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PowerLoadModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4726.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "VirtualComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentModalAnalysis.TYPE"):
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
    ) -> "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis":
        return self._Cast_VirtualComponentModalAnalysis(self)

"""SynchroniserSleeveMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserSleeveMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.static_loads import _6992
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5438,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveMultibodyDynamicsAnalysis")


class SynchroniserSleeveMultibodyDynamicsAnalysis(
    _5527.SynchroniserPartMultibodyDynamicsAnalysis
):
    """SynchroniserSleeveMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserSleeveMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserSleeveMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
            parent: "SynchroniserSleeveMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_5527.SynchroniserPartMultibodyDynamicsAnalysis":
            return self._parent._cast(_5527.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_5438.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
        ) -> "SynchroniserSleeveMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6992.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserSleeveMultibodyDynamicsAnalysis(self)

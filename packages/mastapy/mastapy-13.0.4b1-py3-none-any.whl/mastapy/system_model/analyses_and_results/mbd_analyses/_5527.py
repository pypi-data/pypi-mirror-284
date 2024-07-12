"""SynchroniserPartMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserPartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5525,
        _5528,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartMultibodyDynamicsAnalysis")


class SynchroniserPartMultibodyDynamicsAnalysis(
    _5438.CouplingHalfMultibodyDynamicsAnalysis
):
    """SynchroniserPartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserPartMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserPartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
            parent: "SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5438.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5438.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5525.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5525

            return self._parent._cast(_5525.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5528.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(_5528.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "SynchroniserPartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserPartMultibodyDynamicsAnalysis(self)

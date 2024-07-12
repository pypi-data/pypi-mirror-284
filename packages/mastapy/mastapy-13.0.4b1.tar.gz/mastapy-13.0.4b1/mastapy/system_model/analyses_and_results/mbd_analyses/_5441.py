"""CVTMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5510,
        _5397,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTMultibodyDynamicsAnalysis")


class CVTMultibodyDynamicsAnalysis(_5409.BeltDriveMultibodyDynamicsAnalysis):
    """CVTMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTMultibodyDynamicsAnalysis")

    class _Cast_CVTMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            parent: "CVTMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5409.BeltDriveMultibodyDynamicsAnalysis":
            return self._parent._cast(_5409.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5510.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5397.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "CVTMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.CVT":
        """mastapy.system_model.part_model.couplings.CVT

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
    ) -> "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis":
        return self._Cast_CVTMultibodyDynamicsAnalysis(self)

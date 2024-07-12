"""BevelDifferentialSunGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelDifferentialSunGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5416,
        _5402,
        _5433,
        _5460,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearMultibodyDynamicsAnalysis")


class BevelDifferentialSunGearMultibodyDynamicsAnalysis(
    _5411.BevelDifferentialGearMultibodyDynamicsAnalysis
):
    """BevelDifferentialSunGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialSunGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5411.BevelDifferentialGearMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5411.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5416.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5402.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(
                _5402.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5433.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5460.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialSunGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialSunGearMultibodyDynamicsAnalysis(self)

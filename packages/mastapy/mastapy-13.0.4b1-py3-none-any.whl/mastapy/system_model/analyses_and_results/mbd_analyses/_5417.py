"""BevelGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5412,
        _5513,
        _5519,
        _5522,
        _5543,
        _5434,
        _5461,
        _5510,
        _5397,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetMultibodyDynamicsAnalysis")


class BevelGearSetMultibodyDynamicsAnalysis(
    _5403.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
):
    """BevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
            parent: "BevelGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5403.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5403.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5434.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5461.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5510.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5397.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5412.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(
                _5412.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5513.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(_5513.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5519.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(
                _5519.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5522.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(
                _5522.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5543.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5543

            return self._parent._cast(_5543.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
        ) -> "BevelGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

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
    ) -> "BevelGearSetMultibodyDynamicsAnalysis._Cast_BevelGearSetMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearSetMultibodyDynamicsAnalysis(self)

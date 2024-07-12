"""PlanetaryGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5449
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PlanetaryGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5461,
        _5510,
        _5397,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetMultibodyDynamicsAnalysis")


class PlanetaryGearSetMultibodyDynamicsAnalysis(
    _5449.CylindricalGearSetMultibodyDynamicsAnalysis
):
    """PlanetaryGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
            parent: "PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_5449.CylindricalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5449.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_5461.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_5510.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_5397.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "PlanetaryGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetMultibodyDynamicsAnalysis.TYPE"
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
    ) -> "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis(self)

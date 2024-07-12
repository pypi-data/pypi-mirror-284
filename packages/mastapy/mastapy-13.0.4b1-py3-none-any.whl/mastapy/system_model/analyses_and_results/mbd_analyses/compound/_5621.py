"""KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5476
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5619,
        _5620,
        _5584,
        _5610,
        _5648,
        _5550,
        _5629,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis(
    _5618.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5618.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5618.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5550.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5476.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5619.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundMultibodyDynamicsAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundMultibodyDynamicsAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5476.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis(
            self
        )

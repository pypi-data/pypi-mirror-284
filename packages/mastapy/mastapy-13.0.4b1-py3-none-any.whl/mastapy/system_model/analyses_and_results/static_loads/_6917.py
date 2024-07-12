"""GearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, overridable_enum_runtime
from mastapy._internal.implicit import overridable
from mastapy.system_model.analyses_and_results.static_loads import _6945, _6974
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5459
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7034,
    )
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6912,
        _6914,
        _6837,
        _6846,
        _6851,
        _6865,
        _6870,
        _6887,
        _6908,
        _6929,
        _6936,
        _6939,
        _6942,
        _6955,
        _6977,
        _6983,
        _6986,
        _7006,
        _7009,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadCase",)


Self = TypeVar("Self", bound="GearSetLoadCase")


class GearSetLoadCase(_6974.SpecialisedAssemblyLoadCase):
    """GearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadCase")

    class _Cast_GearSetLoadCase:
        """Special nested class for casting GearSetLoadCase to subclasses."""

        def __init__(
            self: "GearSetLoadCase._Cast_GearSetLoadCase", parent: "GearSetLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6837.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6846.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6851.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6865.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6870.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConicalGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6887.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6908.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.FaceGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6929.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6936.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(
                _6936.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(
                _6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(
                _6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def planetary_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6955.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PlanetaryGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6977.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6983.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6986.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelGearSetLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_7006.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7006

            return self._parent._cast(_7006.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_7009.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.ZerolBevelGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "GearSetLoadCase":
            return self._parent

        def __getattr__(self: "GearSetLoadCase._Cast_GearSetLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def gear_mesh_stiffness_model(self: Self) -> "_5459.GearMeshStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel"""
        temp = self.wrapped.GearMeshStiffnessModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5459",
            "GearMeshStiffnessModel",
        )(value)

    @gear_mesh_stiffness_model.setter
    @enforce_parameter_types
    def gear_mesh_stiffness_model(self: Self, value: "_5459.GearMeshStiffnessModel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )
        self.wrapped.GearMeshStiffnessModel = value

    @property
    def mesh_stiffness_source(
        self: Self,
    ) -> "overridable.Overridable_MeshStiffnessSource":
        """Overridable[mastapy.system_model.analyses_and_results.static_loads.MeshStiffnessSource]"""
        temp = self.wrapped.MeshStiffnessSource

        if temp is None:
            return None

        value = overridable.Overridable_MeshStiffnessSource.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @mesh_stiffness_source.setter
    @enforce_parameter_types
    def mesh_stiffness_source(
        self: Self,
        value: "Union[_6945.MeshStiffnessSource, Tuple[_6945.MeshStiffnessSource, bool]]",
    ):
        wrapper_type = overridable.Overridable_MeshStiffnessSource.wrapper_type()
        enclosed_type = overridable.Overridable_MeshStiffnessSource.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.MeshStiffnessSource = value

    @property
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return False

        return temp

    @use_advanced_model_in_advanced_time_stepping_analysis_for_modulation.setter
    @enforce_parameter_types
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self, value: "bool"
    ):
        self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation = (
            bool(value) if value is not None else False
        )

    @property
    def advanced_time_stepping_analysis_for_modulation_options(
        self: Self,
    ) -> "_7034.AdvancedTimeSteppingAnalysisForModulationOptions":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulationOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2552.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6912.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_without_clones(self: Self) -> "List[_6912.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsWithoutClones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_without_planetary_duplicates(
        self: Self,
    ) -> "List[_6914.GearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesWithoutPlanetaryDuplicates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearSetLoadCase._Cast_GearSetLoadCase":
        return self._Cast_GearSetLoadCase(self)

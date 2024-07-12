"""GearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6916,
        _6836,
        _6845,
        _6850,
        _6864,
        _6868,
        _6885,
        _6907,
        _6928,
        _6935,
        _6938,
        _6941,
        _6976,
        _6982,
        _6985,
        _7005,
        _7008,
        _6871,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadCase",)


Self = TypeVar("Self", bound="GearMeshLoadCase")


class GearMeshLoadCase(_6933.InterMountableComponentConnectionLoadCase):
    """GearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadCase")

    class _Cast_GearMeshLoadCase:
        """Special nested class for casting GearMeshLoadCase to subclasses."""

        def __init__(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase", parent: "GearMeshLoadCase"
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6836.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6845.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6850.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelGearMeshLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6864.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6868.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConicalGearMeshLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6885.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6907.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.FaceGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6928.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(
                _6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(
                _6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6976.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6982.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6985.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.StraightBevelGearMeshLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_7005.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7005

            return self._parent._cast(_7005.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_7008.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.ZerolBevelGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "GearMeshLoadCase":
            return self._parent

        def __getattr__(self: "GearMeshLoadCase._Cast_GearMeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def number_of_steps_for_one_tooth_pass(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStepsForOneToothPass

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_passed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth_passed.setter
    @enforce_parameter_types
    def number_of_teeth_passed(self: Self, value: "float"):
        self.wrapped.NumberOfTeethPassed = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def connection_design(self: Self) -> "_2333.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6916.GearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.GearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "GearMeshLoadCase._Cast_GearMeshLoadCase":
        return self._Cast_GearMeshLoadCase(self)

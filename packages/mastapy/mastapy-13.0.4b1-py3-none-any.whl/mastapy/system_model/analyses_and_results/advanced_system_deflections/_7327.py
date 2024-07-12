"""ConicalGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConicalGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1168, _1178
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7299,
        _7306,
        _7311,
        _7359,
        _7363,
        _7366,
        _7369,
        _7397,
        _7403,
        _7406,
        _7425,
        _7361,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshAdvancedSystemDeflection")


class ConicalGearMeshAdvancedSystemDeflection(_7355.GearMeshAdvancedSystemDeflection):
    """ConicalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearMeshAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
            parent: "ConicalGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7355.GearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7355.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7361.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(
                _7361.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(
                _7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7306.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(
                _7306.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7311.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(_7311.BevelGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7359.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7363.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(
                _7363.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> (
            "_7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7397.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7403.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(
                _7403.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7406.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(
                _7406.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7425.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
        ) -> "ConicalGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_1168.ActiveConicalFlank":
        """mastapy.gears.gear_designs.conical.ActiveConicalFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.ActiveConicalFlank"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1168", "ActiveConicalFlank"
        )(value)

    @property
    def inactive_flank(self: Self) -> "_1168.ActiveConicalFlank":
        """mastapy.gears.gear_designs.conical.ActiveConicalFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InactiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.ActiveConicalFlank"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1168", "ActiveConicalFlank"
        )(value)

    @property
    def connection_design(self: Self) -> "_2327.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_pinion(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_total(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_wheel(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_pinion(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_total(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_wheel(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_pinion(
        self: Self,
    ) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_total(
        self: Self,
    ) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_wheel(
        self: Self,
    ) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshAdvancedSystemDeflection._Cast_ConicalGearMeshAdvancedSystemDeflection":
        return self._Cast_ConicalGearMeshAdvancedSystemDeflection(self)

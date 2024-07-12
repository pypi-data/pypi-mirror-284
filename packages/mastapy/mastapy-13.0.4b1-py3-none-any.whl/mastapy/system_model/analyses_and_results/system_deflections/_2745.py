"""ConicalGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConicalGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1168, _1173, _1178
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2747,
        _2710,
        _2722,
        _2727,
        _2784,
        _2789,
        _2792,
        _2795,
        _2828,
        _2834,
        _2837,
        _2860,
        _2788,
        _2748,
    )
    from mastapy.gears.ltca.conical import _873
    from mastapy.gears.rating.conical import _542
    from mastapy.system_model.analyses_and_results.power_flows import _4085
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshSystemDeflection")


class ConicalGearMeshSystemDeflection(_2780.GearMeshSystemDeflection):
    """ConicalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshSystemDeflection")

    class _Cast_ConicalGearMeshSystemDeflection:
        """Special nested class for casting ConicalGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
            parent: "ConicalGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2780.GearMeshSystemDeflection":
            return self._parent._cast(_2780.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(
                _2788.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2710.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2722.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2727.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelGearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2784.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2789.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(
                _2789.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2795.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2828.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2834.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2837.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2860.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.ZerolBevelGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "ConicalGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_e(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaE

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_sigma(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaSigma

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xp(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaXP

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xw(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaXW

        if temp is None:
            return 0.0

        return temp

    @property
    def include_mesh_node_misalignments_in_default_report(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @property
    def linear_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def load_in_line_of_action_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadInLineOfActionFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_flank(self: Self) -> "_1168.ActiveConicalFlank":
        """mastapy.gears.gear_designs.conical.ActiveConicalFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedFlank

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
    def pinion_angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_torque_for_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorqueForLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_force_in_line_of_action_at_mesh_node(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearADueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_moment_at_mesh_node(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearADueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_force_in_line_of_action_at_mesh_node(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearBDueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_moment_at_mesh_node(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearBDueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

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
    def gear_a(self: Self) -> "_2747.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_2747.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ltca_results(self: Self) -> "_873.ConicalMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.conical.ConicalMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_design(self: Self) -> "_1173.ConicalGearMeshDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshDesign

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
    def rating(self: Self) -> "_542.ConicalGearMeshRating":
        """mastapy.gears.rating.conical.ConicalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

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
    def power_flow_results(self: Self) -> "_4085.ConicalGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection":
        return self._Cast_ConicalGearMeshSystemDeflection(self)

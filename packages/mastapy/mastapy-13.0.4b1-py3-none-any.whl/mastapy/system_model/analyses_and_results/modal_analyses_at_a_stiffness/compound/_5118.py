"""StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5026,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4988,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5014,
        _5042,
        _5068,
        _5074,
        _5044,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundModalAnalysisAtAStiffness")


class StraightBevelGearMeshCompoundModalAnalysisAtAStiffness(
    _5026.BevelGearMeshCompoundModalAnalysisAtAStiffness
):
    """StraightBevelGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5026.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5014.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5042.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5068.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(_5068.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2347.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2347.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4988.StraightBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4988.StraightBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness(self)

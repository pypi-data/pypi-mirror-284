"""BevelGearMeshCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4754
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4609
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4761,
        _4849,
        _4855,
        _4858,
        _4876,
        _4782,
        _4808,
        _4814,
        _4784,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundModalAnalysis")


class BevelGearMeshCompoundModalAnalysis(
    _4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis
):
    """BevelGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCompoundModalAnalysis")

    class _Cast_BevelGearMeshCompoundModalAnalysis:
        """Special nested class for casting BevelGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
            parent: "BevelGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            return self._parent._cast(
                _4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4782.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4808.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4814.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(
                _4814.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4761.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(
                _4761.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4849.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4855.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(
                _4855.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4858.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "_4876.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4876,
            )

            return self._parent._cast(_4876.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
        ) -> "BevelGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4609.BevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4609.BevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundModalAnalysis._Cast_BevelGearMeshCompoundModalAnalysis":
        return self._Cast_BevelGearMeshCompoundModalAnalysis(self)

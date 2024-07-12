"""BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7179,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7044,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7167,
        _7195,
        _7221,
        _7227,
        _7197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> (
        "List[_7044.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> (
        "List[_7044.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )

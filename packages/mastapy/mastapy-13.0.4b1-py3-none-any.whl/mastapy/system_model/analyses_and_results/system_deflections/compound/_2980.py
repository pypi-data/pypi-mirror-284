"""StraightBevelDiffGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2345
    from mastapy.system_model.analyses_and_results.system_deflections import _2834
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2877,
        _2905,
        _2932,
        _2938,
        _2907,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshCompoundSystemDeflection")


class StraightBevelDiffGearMeshCompoundSystemDeflection(
    _2889.BevelGearMeshCompoundSystemDeflection
):
    """StraightBevelDiffGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshCompoundSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearMeshCompoundSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
            parent: "StraightBevelDiffGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2889.BevelGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2889.BevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(
                _2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2905.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2932.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2938.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(
                _2938.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
        ) -> "StraightBevelDiffGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

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
    ) -> "List[_2834.StraightBevelDiffGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection]

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
    ) -> "List[_2834.StraightBevelDiffGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection]

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
    ) -> "StraightBevelDiffGearMeshCompoundSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection":
        return self._Cast_StraightBevelDiffGearMeshCompoundSystemDeflection(self)

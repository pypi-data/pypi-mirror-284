"""BevelDifferentialGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.system_deflections import _2722
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
__all__ = ("BevelDifferentialGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundSystemDeflection")


class BevelDifferentialGearMeshCompoundSystemDeflection(
    _2889.BevelGearMeshCompoundSystemDeflection
):
    """BevelDifferentialGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshCompoundSystemDeflection"
    )

    class _Cast_BevelDifferentialGearMeshCompoundSystemDeflection:
        """Special nested class for casting BevelDifferentialGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
            parent: "BevelDifferentialGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2889.BevelGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2889.BevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(
                _2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2905.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2932.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2938.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(
                _2938.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
        ) -> "BevelDifferentialGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundSystemDeflection.TYPE",
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
    ) -> "List[_2722.BevelDifferentialGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection]

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
    ) -> "List[_2722.BevelDifferentialGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection]

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
    ) -> "BevelDifferentialGearMeshCompoundSystemDeflection._Cast_BevelDifferentialGearMeshCompoundSystemDeflection":
        return self._Cast_BevelDifferentialGearMeshCompoundSystemDeflection(self)

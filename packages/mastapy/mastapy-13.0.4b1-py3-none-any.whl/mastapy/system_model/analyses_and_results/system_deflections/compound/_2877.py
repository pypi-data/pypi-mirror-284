"""AGMAGleasonConicalGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2905
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2710
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2884,
        _2889,
        _2936,
        _2974,
        _2980,
        _2983,
        _3001,
        _2932,
        _2938,
        _2907,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundSystemDeflection")


class AGMAGleasonConicalGearMeshCompoundSystemDeflection(
    _2905.ConicalGearMeshCompoundSystemDeflection
):
    """AGMAGleasonConicalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2905.ConicalGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2905.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2932.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2938.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(
                _2938.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2884.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(
                _2884.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2889.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.BevelGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2936.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.HypoidGearMeshCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2974.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2980.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(
                _2980.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2983.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(
                _2983.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_3001.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3001,
            )

            return self._parent._cast(_3001.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2710.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

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
    ) -> "List[_2710.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection(self)

"""ShaftToMountableComponentConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6453,
        _6473,
        _6512,
        _6464,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundDynamicAnalysis"
)


class ShaftToMountableComponentConnectionCompoundDynamicAnalysis(
    _6432.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
):
    """ShaftToMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6432.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6432.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6453.CoaxialConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6512.PlanetaryConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6397.ShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis]

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
    ) -> "List[_6397.ShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundDynamicAnalysis(
            self
        )

"""CouplingHalfCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6773,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6603
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6719,
        _6724,
        _6738,
        _6778,
        _6784,
        _6788,
        _6800,
        _6810,
        _6811,
        _6812,
        _6815,
        _6816,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundCriticalSpeedAnalysis")


class CouplingHalfCompoundCriticalSpeedAnalysis(
    _6773.MountableComponentCompoundCriticalSpeedAnalysis
):
    """CouplingHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CouplingHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
            parent: "CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6719.ClutchHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6724.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6738.CVTPulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(_6738.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6778.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def pulley_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6784.PulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(_6784.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6788.RollingRingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(_6788.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6800.SpringDamperHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(
                _6800.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6810.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6810,
            )

            return self._parent._cast(
                _6810.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6811.SynchroniserPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6811,
            )

            return self._parent._cast(
                _6811.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6812.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6812,
            )

            return self._parent._cast(
                _6812.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6815.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6815,
            )

            return self._parent._cast(
                _6815.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6816.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6816,
            )

            return self._parent._cast(
                _6816.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6603.CouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingHalfCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6603.CouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingHalfCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis":
        return self._Cast_CouplingHalfCompoundCriticalSpeedAnalysis(self)

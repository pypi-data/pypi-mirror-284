"""CylindricalPlanetGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CylindricalPlanetGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4644
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4807,
        _4826,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundModalAnalysis")


class CylindricalPlanetGearCompoundModalAnalysis(
    _4796.CylindricalGearCompoundModalAnalysis
):
    """CylindricalPlanetGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundModalAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundModalAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
            parent: "CylindricalPlanetGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4796.CylindricalGearCompoundModalAnalysis":
            return self._parent._cast(_4796.CylindricalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4807.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "CylindricalPlanetGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4644.CylindricalPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4644.CylindricalPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundModalAnalysis(self)

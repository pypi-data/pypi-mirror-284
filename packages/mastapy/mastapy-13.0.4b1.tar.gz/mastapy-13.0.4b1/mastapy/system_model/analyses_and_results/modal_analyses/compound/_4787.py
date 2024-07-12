"""CouplingConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4631
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4771,
        _4776,
        _4830,
        _4852,
        _4867,
        _4784,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundModalAnalysis")


class CouplingConnectionCompoundModalAnalysis(
    _4814.InterMountableComponentConnectionCompoundModalAnalysis
):
    """CouplingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundModalAnalysis"
    )

    class _Cast_CouplingConnectionCompoundModalAnalysis:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
            parent: "CouplingConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4814.InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4814.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4771.ClutchConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4776.ConceptCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(
                _4776.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4830.PartToPartShearCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(
                _4830.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4852.SpringDamperConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4867.TorqueConverterConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4867,
            )

            return self._parent._cast(
                _4867.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "CouplingConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4631.CouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis]

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
    ) -> "List[_4631.CouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis]

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
    ) -> "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis":
        return self._Cast_CouplingConnectionCompoundModalAnalysis(self)

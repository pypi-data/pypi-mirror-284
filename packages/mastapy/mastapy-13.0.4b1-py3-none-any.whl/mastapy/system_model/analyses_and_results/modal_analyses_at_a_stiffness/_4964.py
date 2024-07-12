"""PlanetaryGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4927,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PlanetaryGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4939,
        _4978,
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysisAtAStiffness")


class PlanetaryGearSetModalAnalysisAtAStiffness(
    _4927.CylindricalGearSetModalAnalysisAtAStiffness
):
    """PlanetaryGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetaryGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetaryGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
            parent: "PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_4927.CylindricalGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4927.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_4939.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(_4939.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "PlanetaryGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2562.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness":
        return self._Cast_PlanetaryGearSetModalAnalysisAtAStiffness(self)

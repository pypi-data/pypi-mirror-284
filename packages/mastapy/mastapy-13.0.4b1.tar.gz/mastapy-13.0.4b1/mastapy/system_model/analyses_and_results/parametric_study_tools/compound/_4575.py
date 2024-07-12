"""StraightBevelPlanetGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4569,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6987
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4446
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4480,
        _4468,
        _4496,
        _4522,
        _4541,
        _4489,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundParametricStudyTool")


class StraightBevelPlanetGearCompoundParametricStudyTool(
    _4569.StraightBevelDiffGearCompoundParametricStudyTool
):
    """StraightBevelPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundParametricStudyTool"
    )

    class _Cast_StraightBevelPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
            parent: "StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4569.StraightBevelDiffGearCompoundParametricStudyTool":
            return self._parent._cast(
                _4569.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4480.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4468.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(
                _4468.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4496.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4522.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4541.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "StraightBevelPlanetGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6987.StraightBevelPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4446.StraightBevelPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool]

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
    ) -> "List[_4446.StraightBevelPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool]

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
    ) -> "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool":
        return self._Cast_StraightBevelPlanetGearCompoundParametricStudyTool(self)

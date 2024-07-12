"""BeltDriveCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6665
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BeltDriveCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6608,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BeltDriveCriticalSpeedAnalysis")


class BeltDriveCriticalSpeedAnalysis(_6665.SpecialisedAssemblyCriticalSpeedAnalysis):
    """BeltDriveCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveCriticalSpeedAnalysis")

    class _Cast_BeltDriveCriticalSpeedAnalysis:
        """Special nested class for casting BeltDriveCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
            parent: "BeltDriveCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "_6608.CVTCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.CVTCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "BeltDriveCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis":
        return self._Cast_BeltDriveCriticalSpeedAnalysis(self)

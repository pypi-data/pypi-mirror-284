"""FaceGearSetLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca.cylindrical import _863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "FaceGearSetLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _849
    from mastapy.gears.analysis import _1246, _1247, _1244, _1235


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetLoadDistributionAnalysis")


class FaceGearSetLoadDistributionAnalysis(
    _863.CylindricalGearSetLoadDistributionAnalysis
):
    """FaceGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetLoadDistributionAnalysis")

    class _Cast_FaceGearSetLoadDistributionAnalysis:
        """Special nested class for casting FaceGearSetLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
            parent: "FaceGearSetLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
            return self._parent._cast(_863.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_849.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _849

            return self._parent._cast(_849.GearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_1246.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1246

            return self._parent._cast(_1246.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_1247.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1247

            return self._parent._cast(_1247.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_1244.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1244

            return self._parent._cast(_1244.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "_1235.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.AbstractGearSetAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
        ) -> "FaceGearSetLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearSetLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis"
    ):
        return self._Cast_FaceGearSetLoadDistributionAnalysis(self)

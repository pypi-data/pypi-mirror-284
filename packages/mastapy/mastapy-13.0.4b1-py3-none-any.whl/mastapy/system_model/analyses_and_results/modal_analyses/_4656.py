"""GearMeshModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "GearMeshModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.system_deflections import _2780
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4597,
        _4604,
        _4609,
        _4622,
        _4625,
        _4641,
        _4650,
        _4660,
        _4664,
        _4667,
        _4670,
        _4704,
        _4710,
        _4713,
        _4731,
        _4734,
        _4628,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshModalAnalysis",)


Self = TypeVar("Self", bound="GearMeshModalAnalysis")


class GearMeshModalAnalysis(_4663.InterMountableComponentConnectionModalAnalysis):
    """GearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshModalAnalysis")

    class _Cast_GearMeshModalAnalysis:
        """Special nested class for casting GearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
            parent: "GearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4663.InterMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4663.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4628.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4597.AGMAGleasonConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4604.BevelDifferentialGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4609.BevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelGearMeshModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4622.ConceptGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4625.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConicalGearMeshModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4641.CylindricalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4650.FaceGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(_4650.FaceGearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4660.HypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.HypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4664.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(
                _4664.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4667.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4670.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(
                _4670.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4704.SpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4710.StraightBevelDiffGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4713.StraightBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelGearMeshModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4731.WormGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4731

            return self._parent._cast(_4731.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "_4734.ZerolBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4734

            return self._parent._cast(_4734.ZerolBevelGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis",
        ) -> "GearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2780.GearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshModalAnalysis._Cast_GearMeshModalAnalysis":
        return self._Cast_GearMeshModalAnalysis(self)

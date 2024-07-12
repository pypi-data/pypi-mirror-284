"""InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6064,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6034,
        _6038,
        _6041,
        _6046,
        _6050,
        _6055,
        _6059,
        _6062,
        _6066,
        _6069,
        _6077,
        _6083,
        _6088,
        _6093,
        _6097,
        _6100,
        _6103,
        _6111,
        _6121,
        _6123,
        _6131,
        _6133,
        _6137,
        _6140,
        _6148,
        _6155,
        _6158,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
)


class InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6064.ConnectionHarmonicAnalysisOfSingleExcitation
):
    """InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6064.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.BeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(
                _6041.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.ClutchConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6062.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6077.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6083.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(
                _6093.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6100.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6103.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6111.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6121.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6123.RollingRingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6137.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6140.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6140,
            )

            return self._parent._cast(
                _6140.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6148.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6148,
            )

            return self._parent._cast(
                _6148.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6155.WormGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6155,
            )

            return self._parent._cast(
                _6155.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6158.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6158,
            )

            return self._parent._cast(
                _6158.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )

"""PartHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PartHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5787
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6091,
        _6029,
        _6030,
        _6031,
        _6033,
        _6035,
        _6036,
        _6037,
        _6039,
        _6040,
        _6042,
        _6043,
        _6044,
        _6045,
        _6047,
        _6048,
        _6049,
        _6051,
        _6052,
        _6054,
        _6056,
        _6057,
        _6058,
        _6060,
        _6061,
        _6063,
        _6065,
        _6067,
        _6068,
        _6070,
        _6071,
        _6072,
        _6074,
        _6076,
        _6078,
        _6079,
        _6080,
        _6081,
        _6082,
        _6084,
        _6085,
        _6086,
        _6087,
        _6089,
        _6090,
        _6092,
        _6094,
        _6096,
        _6098,
        _6099,
        _6101,
        _6102,
        _6104,
        _6105,
        _6106,
        _6108,
        _6109,
        _6112,
        _6113,
        _6115,
        _6116,
        _6117,
        _6118,
        _6119,
        _6120,
        _6122,
        _6124,
        _6125,
        _6126,
        _6127,
        _6129,
        _6130,
        _6132,
        _6134,
        _6135,
        _6136,
        _6138,
        _6139,
        _6141,
        _6142,
        _6143,
        _6144,
        _6145,
        _6146,
        _6147,
        _6149,
        _6150,
        _6151,
        _6152,
        _6153,
        _6154,
        _6156,
        _6157,
        _6159,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4683
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PartHarmonicAnalysisOfSingleExcitation")


class PartHarmonicAnalysisOfSingleExcitation(_7569.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
            parent: "PartHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6030.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(
                _6030.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6036.AssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(_6036.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(_6037.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.BeltDriveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(_6039.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(
                _6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(_6045.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6047.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6048.BoltedJointHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.BoltHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6052.ClutchHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(_6052.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6057.ConceptCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6060.ConceptGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6063.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.CouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.CVTHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6072.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6078.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.DatumHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(_6080.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6081.ExternalCADModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(_6082.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6084.FaceGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.FEPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6086.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(
                _6086.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(_6087.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6090.GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6094.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(
                _6094.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(
                _6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6101.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6104.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(_6105.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6109.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(_6109.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(_6117.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6118.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(_6118.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(_6119.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(_6120.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.RootAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(_6126.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6127.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6135.SpringDamperHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6141,
            )

            return self._parent._cast(
                _6141.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6145.SynchroniserHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6145,
            )

            return self._parent._cast(
                _6145.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6149.TorqueConverterHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6149,
            )

            return self._parent._cast(
                _6149.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6150,
            )

            return self._parent._cast(
                _6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6151,
            )

            return self._parent._cast(
                _6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6153.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6153,
            )

            return self._parent._cast(
                _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6154,
            )

            return self._parent._cast(_6154.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6156.WormGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6156,
            )

            return self._parent._cast(
                _6156.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6157,
            )

            return self._parent._cast(
                _6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6159.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6159,
            )

            return self._parent._cast(
                _6159.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "PartHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "PartHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2488.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5787.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "_6091.HarmonicAnalysisOfSingleExcitation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def uncoupled_modal_analysis(self: Self) -> "_4683.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartHarmonicAnalysisOfSingleExcitation(self)

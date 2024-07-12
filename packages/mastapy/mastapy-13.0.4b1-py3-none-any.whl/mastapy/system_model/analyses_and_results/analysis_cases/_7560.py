"""ConnectionCompoundAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionCompoundAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2875,
        _2877,
        _2881,
        _2884,
        _2889,
        _2894,
        _2896,
        _2899,
        _2902,
        _2905,
        _2907,
        _2910,
        _2912,
        _2916,
        _2918,
        _2920,
        _2927,
        _2932,
        _2936,
        _2938,
        _2940,
        _2943,
        _2946,
        _2954,
        _2956,
        _2963,
        _2966,
        _2971,
        _2974,
        _2977,
        _2980,
        _2983,
        _2992,
        _2998,
        _3001,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3140,
        _3142,
        _3146,
        _3149,
        _3154,
        _3159,
        _3161,
        _3164,
        _3167,
        _3170,
        _3172,
        _3175,
        _3177,
        _3181,
        _3183,
        _3185,
        _3191,
        _3196,
        _3200,
        _3202,
        _3204,
        _3207,
        _3210,
        _3218,
        _3220,
        _3227,
        _3230,
        _3234,
        _3237,
        _3240,
        _3243,
        _3246,
        _3255,
        _3261,
        _3264,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3399,
        _3401,
        _3405,
        _3408,
        _3413,
        _3418,
        _3420,
        _3423,
        _3426,
        _3429,
        _3431,
        _3434,
        _3436,
        _3440,
        _3442,
        _3444,
        _3450,
        _3455,
        _3459,
        _3461,
        _3463,
        _3466,
        _3469,
        _3477,
        _3479,
        _3486,
        _3489,
        _3493,
        _3496,
        _3499,
        _3502,
        _3505,
        _3514,
        _3520,
        _3523,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3658,
        _3660,
        _3664,
        _3667,
        _3672,
        _3677,
        _3679,
        _3682,
        _3685,
        _3688,
        _3690,
        _3693,
        _3695,
        _3699,
        _3701,
        _3703,
        _3709,
        _3714,
        _3718,
        _3720,
        _3722,
        _3725,
        _3728,
        _3736,
        _3738,
        _3745,
        _3748,
        _3752,
        _3755,
        _3758,
        _3761,
        _3764,
        _3773,
        _3779,
        _3782,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3921,
        _3923,
        _3927,
        _3930,
        _3935,
        _3940,
        _3942,
        _3945,
        _3948,
        _3951,
        _3953,
        _3956,
        _3958,
        _3962,
        _3964,
        _3966,
        _3972,
        _3977,
        _3981,
        _3983,
        _3985,
        _3988,
        _3991,
        _3999,
        _4001,
        _4008,
        _4011,
        _4015,
        _4018,
        _4021,
        _4024,
        _4027,
        _4036,
        _4042,
        _4045,
    )
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4191,
        _4193,
        _4197,
        _4200,
        _4205,
        _4210,
        _4212,
        _4215,
        _4218,
        _4221,
        _4223,
        _4226,
        _4228,
        _4232,
        _4234,
        _4236,
        _4242,
        _4247,
        _4251,
        _4253,
        _4255,
        _4258,
        _4261,
        _4269,
        _4271,
        _4278,
        _4281,
        _4285,
        _4288,
        _4291,
        _4294,
        _4297,
        _4306,
        _4312,
        _4315,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4467,
        _4469,
        _4473,
        _4476,
        _4481,
        _4486,
        _4488,
        _4491,
        _4494,
        _4497,
        _4499,
        _4502,
        _4504,
        _4508,
        _4510,
        _4512,
        _4518,
        _4523,
        _4527,
        _4529,
        _4531,
        _4534,
        _4537,
        _4545,
        _4547,
        _4554,
        _4557,
        _4561,
        _4564,
        _4567,
        _4570,
        _4573,
        _4582,
        _4588,
        _4591,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4752,
        _4754,
        _4758,
        _4761,
        _4766,
        _4771,
        _4773,
        _4776,
        _4779,
        _4782,
        _4784,
        _4787,
        _4789,
        _4793,
        _4795,
        _4797,
        _4803,
        _4808,
        _4812,
        _4814,
        _4816,
        _4819,
        _4822,
        _4830,
        _4832,
        _4839,
        _4842,
        _4846,
        _4849,
        _4852,
        _4855,
        _4858,
        _4867,
        _4873,
        _4876,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5012,
        _5014,
        _5018,
        _5021,
        _5026,
        _5031,
        _5033,
        _5036,
        _5039,
        _5042,
        _5044,
        _5047,
        _5049,
        _5053,
        _5055,
        _5057,
        _5063,
        _5068,
        _5072,
        _5074,
        _5076,
        _5079,
        _5082,
        _5090,
        _5092,
        _5099,
        _5102,
        _5106,
        _5109,
        _5112,
        _5115,
        _5118,
        _5127,
        _5133,
        _5136,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5271,
        _5273,
        _5277,
        _5280,
        _5285,
        _5290,
        _5292,
        _5295,
        _5298,
        _5301,
        _5303,
        _5306,
        _5308,
        _5312,
        _5314,
        _5316,
        _5322,
        _5327,
        _5331,
        _5333,
        _5335,
        _5338,
        _5341,
        _5349,
        _5351,
        _5358,
        _5361,
        _5365,
        _5368,
        _5371,
        _5374,
        _5377,
        _5386,
        _5392,
        _5395,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5553,
        _5555,
        _5559,
        _5562,
        _5567,
        _5572,
        _5574,
        _5577,
        _5580,
        _5583,
        _5585,
        _5588,
        _5590,
        _5594,
        _5596,
        _5598,
        _5604,
        _5609,
        _5613,
        _5615,
        _5617,
        _5620,
        _5623,
        _5631,
        _5633,
        _5640,
        _5643,
        _5647,
        _5650,
        _5653,
        _5656,
        _5659,
        _5668,
        _5674,
        _5677,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5903,
        _5905,
        _5909,
        _5912,
        _5917,
        _5922,
        _5924,
        _5927,
        _5930,
        _5933,
        _5935,
        _5938,
        _5940,
        _5944,
        _5946,
        _5948,
        _5954,
        _5959,
        _5963,
        _5965,
        _5967,
        _5970,
        _5973,
        _5981,
        _5983,
        _5990,
        _5993,
        _5997,
        _6000,
        _6003,
        _6006,
        _6009,
        _6018,
        _6024,
        _6027,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6163,
        _6165,
        _6169,
        _6172,
        _6177,
        _6182,
        _6184,
        _6187,
        _6190,
        _6193,
        _6195,
        _6198,
        _6200,
        _6204,
        _6206,
        _6208,
        _6214,
        _6219,
        _6223,
        _6225,
        _6227,
        _6230,
        _6233,
        _6241,
        _6243,
        _6250,
        _6253,
        _6257,
        _6260,
        _6263,
        _6266,
        _6269,
        _6278,
        _6284,
        _6287,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6432,
        _6434,
        _6438,
        _6441,
        _6446,
        _6451,
        _6453,
        _6456,
        _6459,
        _6462,
        _6464,
        _6467,
        _6469,
        _6473,
        _6475,
        _6477,
        _6483,
        _6488,
        _6492,
        _6494,
        _6496,
        _6499,
        _6502,
        _6510,
        _6512,
        _6519,
        _6522,
        _6526,
        _6529,
        _6532,
        _6535,
        _6538,
        _6547,
        _6553,
        _6556,
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6699,
        _6701,
        _6705,
        _6708,
        _6713,
        _6718,
        _6720,
        _6723,
        _6726,
        _6729,
        _6731,
        _6734,
        _6736,
        _6740,
        _6742,
        _6744,
        _6750,
        _6755,
        _6759,
        _6761,
        _6763,
        _6766,
        _6769,
        _6777,
        _6779,
        _6786,
        _6789,
        _6793,
        _6796,
        _6799,
        _6802,
        _6805,
        _6814,
        _6820,
        _6823,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7165,
        _7167,
        _7171,
        _7174,
        _7179,
        _7184,
        _7186,
        _7189,
        _7192,
        _7195,
        _7197,
        _7200,
        _7202,
        _7206,
        _7208,
        _7210,
        _7216,
        _7221,
        _7225,
        _7227,
        _7229,
        _7232,
        _7235,
        _7243,
        _7245,
        _7252,
        _7255,
        _7259,
        _7262,
        _7265,
        _7268,
        _7271,
        _7280,
        _7286,
        _7289,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7430,
        _7432,
        _7436,
        _7439,
        _7444,
        _7449,
        _7451,
        _7454,
        _7457,
        _7460,
        _7462,
        _7465,
        _7467,
        _7471,
        _7473,
        _7475,
        _7481,
        _7486,
        _7490,
        _7492,
        _7494,
        _7497,
        _7500,
        _7508,
        _7510,
        _7517,
        _7520,
        _7524,
        _7527,
        _7530,
        _7533,
        _7536,
        _7545,
        _7551,
        _7554,
    )
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundAnalysis")


class ConnectionCompoundAnalysis(_7564.DesignEntityCompoundAnalysis):
    """ConnectionCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundAnalysis")

    class _Cast_ConnectionCompoundAnalysis:
        """Special nested class for casting ConnectionCompoundAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
            parent: "ConnectionCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_2875.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(
                _2875.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(
                _2877.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2881.BeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2884.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(
                _2884.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2889.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2894.ClutchConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ClutchConnectionCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2896.CoaxialConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CoaxialConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2899.ConceptCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(
                _2899.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2902.ConceptGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2905.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.ConicalGearMeshCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2910.CouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2912.CVTBeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2916.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(
                _2916.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2918.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2920.CylindricalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2927.FaceGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2932.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2936.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.HypoidGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2938.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(
                _2938.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2940.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2943.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(
                _2943.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_2946.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(
                _2946.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2954.PartToPartShearCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(
                _2954.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2956.PlanetaryConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(_2956.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2963.RingPinsToDiscConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(
                _2963.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2966.RollingRingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2971.ShaftToMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2974.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2977.SpringDamperConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(
                _2977.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2980.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(
                _2980.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2983.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(
                _2983.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2992.TorqueConverterConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2992,
            )

            return self._parent._cast(
                _2992.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_2998.WormGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2998,
            )

            return self._parent._cast(_2998.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3001.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3001,
            )

            return self._parent._cast(_3001.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3142.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3146.BeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3149.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3154.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3159.ClutchConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3164.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3167.ConceptGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(
                _3167.ConceptGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3175.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3177.CVTBeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.CVTBeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3181.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3183.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3185.CylindricalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.CylindricalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3191.FaceGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.FaceGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3196.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3200.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3204.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3207.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3210.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3210,
            )

            return self._parent._cast(
                _3210.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3218.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(
                _3218.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3220.PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3227.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3230.RollingRingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.RollingRingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3237.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3240.SpringDamperConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3243.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3246.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3255.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3255,
            )

            return self._parent._cast(
                _3255.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3261.WormGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3261,
            )

            return self._parent._cast(
                _3261.WormGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3264.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3264,
            )

            return self._parent._cast(
                _3264.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3420,
            )

            return self._parent._cast(
                _3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3440.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3442.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3479.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3489.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3499.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3520,
            )

            return self._parent._cast(
                _3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3658.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3658,
            )

            return self._parent._cast(
                _3658.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3664.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3679.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3679,
            )

            return self._parent._cast(
                _3679.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3685.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3695.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3699.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3701.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3701,
            )

            return self._parent._cast(
                _3701.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3703.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3703,
            )

            return self._parent._cast(
                _3703.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3709.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3722.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3725.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3728.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3738.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3745.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3748.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3752.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3758.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3773,
            )

            return self._parent._cast(
                _3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3779.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3779,
            )

            return self._parent._cast(
                _3779.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3782,
            )

            return self._parent._cast(
                _3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3921.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(
                _3921.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3927.BeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3930.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(
                _3930.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3935.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3940.ClutchConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3942.CoaxialConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3945.ConceptCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3948.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3951.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3956.CouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3958.CVTBeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3962.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3964.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3966.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3972.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3977.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(_3977.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3981.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3983.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(
                _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_3999.PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4001.PlanetaryConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4008.RingPinsToDiscConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(
                _4008.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4011.RollingRingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(
                _4011.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4018.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4021.SpringDamperConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(
                _4021.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(
                _4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4027.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4036.TorqueConverterConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4036,
            )

            return self._parent._cast(
                _4036.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4042.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4042,
            )

            return self._parent._cast(_4042.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4045.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4191.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(
                _4191.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4193.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4197.BeltConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.BeltConnectionCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4200.BevelDifferentialGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4205.BevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelGearMeshCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4210.ClutchConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ClutchConnectionCompoundPowerFlow)

        @property
        def coaxial_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4212.CoaxialConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CoaxialConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4215.ConceptCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4218.ConceptGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4221.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.ConicalGearMeshCompoundPowerFlow)

        @property
        def connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4226.CouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4228.CVTBeltConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4232.CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4234.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
            )

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4236.CylindricalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(_4236.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4242.FaceGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.FaceGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4247.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.GearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4251.HypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.HypoidGearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4255.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(
                _4255.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4258.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(
                _4258.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4261.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4269.PartToPartShearCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(
                _4269.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4271.PlanetaryConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.PlanetaryConnectionCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4278.RingPinsToDiscConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4281.RollingRingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.RollingRingConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4285.ShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(
                _4285.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4288.SpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4291.SpringDamperConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.SpringDamperConnectionCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4294.StraightBevelDiffGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4297.StraightBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4306.TorqueConverterConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4306,
            )

            return self._parent._cast(_4306.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4312.WormGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4312,
            )

            return self._parent._cast(_4312.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4315.ZerolBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4315,
            )

            return self._parent._cast(_4315.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(
                _4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4473.BeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4476.BevelDifferentialGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(
                _4476.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4481.BevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4486.ClutchConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ClutchConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4488.CoaxialConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4491.ConceptCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(
                _4491.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4494.ConceptGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4497.ConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4499.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.ConnectionCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4502.CouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(
                _4502.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4504.CVTBeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(
                _4504.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4510.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4512.CylindricalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4518.FaceGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4523.GearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4527.HypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4529.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(
                _4529.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4531.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(
                _4531.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4534.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4537.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4545.PartToPartShearCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4547.PlanetaryConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4554.RingPinsToDiscConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.RingPinsToDiscConnectionCompoundParametricStudyTool
            )

        @property
        def rolling_ring_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4557.RollingRingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(
                _4557.RollingRingConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4564.SpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(
                _4564.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4567.SpringDamperConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4570.StraightBevelDiffGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4573.StraightBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(
                _4573.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4582.TorqueConverterConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4582,
            )

            return self._parent._cast(
                _4582.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4588.WormGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4588,
            )

            return self._parent._cast(_4588.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4591.ZerolBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4591,
            )

            return self._parent._cast(
                _4591.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4752.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(
                _4752.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(
                _4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4758.BeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4761.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(
                _4761.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4766.BevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4771.ClutchConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ClutchConnectionCompoundModalAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4773.CoaxialConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CoaxialConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4776.ConceptCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(
                _4776.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4779.ConceptGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4782.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.ConicalGearMeshCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4787.CouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4789.CVTBeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4793.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4795.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4797.CylindricalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(_4797.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4803.FaceGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4808.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4812.HypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.HypoidGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4814.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(
                _4814.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4816.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(
                _4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(
                _4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4830.PartToPartShearCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(
                _4830.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4832.PlanetaryConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4839.RingPinsToDiscConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4842.RollingRingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.RollingRingConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4846.ShaftToMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(
                _4846.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4849.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4852.SpringDamperConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4855.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(
                _4855.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4858.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4867.TorqueConverterConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4867,
            )

            return self._parent._cast(
                _4867.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4873.WormGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4873,
            )

            return self._parent._cast(_4873.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_4876.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4876,
            )

            return self._parent._cast(_4876.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5012.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5014.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5018.BeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5021.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5026.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(
                _5026.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5031.ClutchConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5033.CoaxialConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5036.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5039.ConceptGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5042.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5044.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5047.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(
                _5047.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5049.CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5049,
            )

            return self._parent._cast(
                _5049.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5053.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5055.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5057.CylindricalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5063.FaceGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(
                _5063.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5068.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(_5068.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5072.HypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5076.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(
                _5076.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5079.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(
                _5079.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5082.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5090.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5092.PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5099.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5102.RollingRingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5106.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5109.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5112.SpringDamperConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5115.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5118.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5127.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5127,
            )

            return self._parent._cast(
                _5127.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5133.WormGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5133,
            )

            return self._parent._cast(
                _5133.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5136.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5136,
            )

            return self._parent._cast(
                _5136.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5273.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(
                _5273.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5277.BeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5280.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5285.BevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5290.ClutchConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5292.CoaxialConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5295.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5298.ConceptGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5301.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(
                _5301.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5306.CouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(
                _5306.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5308.CVTBeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(
                _5308.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5312.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5314.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5316.CylindricalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(
                _5316.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5322.FaceGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5327.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(_5327.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5331.HypoidGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(
                _5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5335.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5338.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(
                _5338.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5341.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5349.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(
                _5349.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5351.PlanetaryConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5358.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5361.RollingRingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5365.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5368.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5371.SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5374.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5377.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5386.TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5386,
            )

            return self._parent._cast(
                _5386.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5392.WormGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5392,
            )

            return self._parent._cast(_5392.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5395.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5395,
            )

            return self._parent._cast(
                _5395.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5559.BeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5572.ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5577.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5585.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5588.CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5590.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5594.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5596.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5609.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(_5609.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(
                _5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5631.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5633.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5640.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5643.RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5653.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5668.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5668,
            )

            return self._parent._cast(
                _5668.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5674.WormGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5674,
            )

            return self._parent._cast(
                _5674.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5677,
            )

            return self._parent._cast(
                _5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(
                _5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(
                _5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5909.BeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(
                _5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5917.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5922.ClutchConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5924.CoaxialConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5927.ConceptCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(
                _5927.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5930.ConceptGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5933.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5938.CouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5940.CVTBeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5946.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5948.CylindricalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(_5948.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5954.FaceGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5959.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5963.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(
                _5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(
                _5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(
                _5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5981.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5983.PlanetaryConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5990.RingPinsToDiscConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5993.RollingRingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_5997.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(
                _5997.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6003.SpringDamperConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(
                _6003.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(
                _6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6009.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(
                _6009.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6018.TorqueConverterConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6018,
            )

            return self._parent._cast(
                _6018.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6024.WormGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6024,
            )

            return self._parent._cast(_6024.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6027,
            )

            return self._parent._cast(_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6163.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6165.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6169.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6172.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6177.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6182.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6184.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6187.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6187,
            )

            return self._parent._cast(
                _6187.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6190.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6193.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6198.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6200.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6204.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6206.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6208.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6214.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6219.GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6223.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6225.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6227.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6230.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6230,
            )

            return self._parent._cast(
                _6230.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6233.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6241.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6241,
            )

            return self._parent._cast(
                _6241.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6243.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6250.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6250,
            )

            return self._parent._cast(
                _6250.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6253.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6257.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6260.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6263.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6266.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6269.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6278.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6278,
            )

            return self._parent._cast(
                _6278.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6284.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6284,
            )

            return self._parent._cast(
                _6284.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6287.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6287,
            )

            return self._parent._cast(
                _6287.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6432.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(
                _6432.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(
                _6434.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6438.BeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6441.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(
                _6441.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6446.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6451.ClutchConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6453.CoaxialConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6456.ConceptCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(
                _6456.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6459.ConceptGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6462.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6467.CouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6469.CVTBeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6475.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6477.CylindricalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(_6477.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6483.FaceGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6488.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6492.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6494.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(
                _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6496.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(
                _6496.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6499.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6502.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(
                _6502.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6510.PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(
                _6510.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6512.PlanetaryConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6519.RingPinsToDiscConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(
                _6519.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6522.RollingRingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(
                _6522.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6526.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(
                _6526.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6529.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6532.SpringDamperConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(
                _6532.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(
                _6535.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6538.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(
                _6538.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6547.TorqueConverterConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6547,
            )

            return self._parent._cast(
                _6547.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6553.WormGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6553,
            )

            return self._parent._cast(_6553.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6556.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6556,
            )

            return self._parent._cast(_6556.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6699.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6701.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6705.BeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(_6705.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6713.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6718.ClutchConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6720.CoaxialConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(
                _6720.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6723.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6726.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6729.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(
                _6729.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6734.CouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6736.CVTBeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(
                _6736.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6740.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6742.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6744.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6750.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6755.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(_6755.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6763.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(
                _6763.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_6766.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6769.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(
                _6769.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6777.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6779.PlanetaryConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6786.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6789.RollingRingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6793.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(
                _6796.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6799.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6814.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6814,
            )

            return self._parent._cast(
                _6814.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6820.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6820,
            )

            return self._parent._cast(_6820.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6823,
            )

            return self._parent._cast(
                _6823.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7165.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7171.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7174.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7184.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7189.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7192.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7202.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7210.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7210,
            )

            return self._parent._cast(
                _7210.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7216.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7225.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7229.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7232.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7235.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7243.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7243,
            )

            return self._parent._cast(
                _7243.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7252.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7255.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7262.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7265.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7268.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7271.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7271,
            )

            return self._parent._cast(
                _7271.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7280.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7280,
            )

            return self._parent._cast(
                _7280.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7286.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7286,
            )

            return self._parent._cast(
                _7286.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7289.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7289,
            )

            return self._parent._cast(
                _7289.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7430.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7432.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7436.BeltConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7439.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7444.BevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(
                _7444.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7449.ClutchConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(
                _7449.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7451.CoaxialConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7454.ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7457.ConceptGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7460.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7462.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7465.CouplingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7467.CVTBeltConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(
                _7467.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7471.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7473.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7475.CylindricalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7481.FaceGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(
                _7481.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7486.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(_7486.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7490.HypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7492.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7494.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(
                _7494.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7497.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(
                _7497.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7500.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(
                _7500.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7508.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7510.PlanetaryConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7517.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7520.RollingRingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> (
            "_7524.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7527.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7530.SpringDamperConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7533.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7536.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7545.TorqueConverterConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7545,
            )

            return self._parent._cast(
                _7545.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7551.WormGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7551,
            )

            return self._parent._cast(
                _7551.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "_7554.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7554,
            )

            return self._parent._cast(
                _7554.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "ConnectionCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis":
        return self._Cast_ConnectionCompoundAnalysis(self)

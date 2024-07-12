"""ClampedSectionMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bolts import _1485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLAMPED_SECTION_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Bolts", "ClampedSectionMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("ClampedSectionMaterialDatabase",)


Self = TypeVar("Self", bound="ClampedSectionMaterialDatabase")


class ClampedSectionMaterialDatabase(
    _1485.BoltedJointMaterialDatabase["_1484.BoltedJointMaterial"]
):
    """ClampedSectionMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CLAMPED_SECTION_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClampedSectionMaterialDatabase")

    class _Cast_ClampedSectionMaterialDatabase:
        """Special nested class for casting ClampedSectionMaterialDatabase to subclasses."""

        def __init__(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
            parent: "ClampedSectionMaterialDatabase",
        ):
            self._parent = parent

        @property
        def bolted_joint_material_database(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
        ) -> "_1485.BoltedJointMaterialDatabase":
            return self._parent._cast(_1485.BoltedJointMaterialDatabase)

        @property
        def named_database(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
        ) -> "_1846.NamedDatabase":
            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def clamped_section_material_database(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
        ) -> "ClampedSectionMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClampedSectionMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase":
        return self._Cast_ClampedSectionMaterialDatabase(self)

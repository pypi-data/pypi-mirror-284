from typing import Dict
from typing import Type

from .versioning_format import VersioningFormat
from .versioning_format import VPrefixVersioning


class VersionedClass:
    versions: Dict[str, Type] = {}
    versioning_format: Type[VersioningFormat] = VPrefixVersioning

    @classmethod
    def register_version(cls, version):
        def decorator(klass):
            cls.versions[version] = klass
            return klass

        return decorator

    @classmethod
    def get_version(cls, version):
        return cls.versions[version]

    @classmethod
    def get_latest_version(cls) -> Type["VersionedClass"]:
        return cls.versions[
            cls.versioning_format().order_versions(cls.versions.keys())[-1]
        ]

    @classmethod
    def latest_version_before(cls, version: str) -> Type["VersionedClass"]:
        ordered_versions = cls.versioning_format().order_versions(cls.versions.keys())
        if version in ordered_versions:
            return cls.versions[ordered_versions[ordered_versions.index(version) - 1]]
        return cls.versions[ordered_versions[-1]]

    @classmethod
    def get_latest_version_instance(cls, *args, **kwargs) -> "VersionedClass":
        return cls.get_latest_version()(*args, **kwargs)

    @classmethod
    def latest_version_before_instance(
        cls, version: str, *args, **kwargs
    ) -> "VersionedClass":
        return cls.latest_version_before(version)(*args, **kwargs)

    @classmethod
    def get_version_instance(cls, version: str, *args, **kwargs) -> "VersionedClass":
        return cls.get_version(version)(*args, **kwargs)


def initial_version(version):
    def decorator(klass):
        klass.versions[version] = klass
        return klass

    return decorator

from abc import ABC
from abc import abstractmethod
from typing import Iterable
from typing import List


class VersioningFormat(ABC):
    @abstractmethod
    def order_versions(self, versions: Iterable[str]) -> List[str]:
        raise NotImplementedError


class SemanticVersioning(VersioningFormat):
    def order_versions(self, versions: Iterable[str]) -> List[str]:
        return sorted(versions, key=lambda x: tuple(map(int, x.split("."))))


class VPrefixVersioning(VersioningFormat):
    def order_versions(self, versions: Iterable[str]) -> List[str]:
        return sorted(
            versions, key=lambda x: tuple(map(int, x.split("v")[1].split(".")))
        )

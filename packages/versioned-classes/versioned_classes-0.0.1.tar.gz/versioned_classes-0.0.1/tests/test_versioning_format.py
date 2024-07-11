import pytest

from versioned_classes.versioning_format import SemanticVersioning
from versioned_classes.versioning_format import VPrefixVersioning


@pytest.mark.parametrize(
    "versions, expected",
    [
        (
            ["v2", "v2", "v1", "v7", "v4.3"],
            ["v1", "v2", "v2", "v4.3", "v7"],
        ),
        (
            ["v1", "v2", "v3", "v4", "v5"],
            ["v1", "v2", "v3", "v4", "v5"],
        ),
        (
            ["v0.0.1", "v1.0.5", "v0.0.2", "v3.0.0", "v2.0.0"],
            ["v0.0.1", "v0.0.2", "v1.0.5", "v2.0.0", "v3.0.0"],
        ),
    ],
)
def test_v_prefix_versioning(versions, expected):
    vpv = VPrefixVersioning()
    assert vpv.order_versions(versions) == expected


@pytest.mark.parametrize(
    "versions, expected",
    [
        (
            ["2", "2", "1", "7", "4.3"],
            ["1", "2", "2", "4.3", "7"],
        ),
        (
            ["1", "2", "3", "4", "5"],
            ["1", "2", "3", "4", "5"],
        ),
        (
            ["0.0.1", "1.0.5", "0.0.2", "3.0.0", "2.0.0"],
            ["0.0.1", "0.0.2", "1.0.5", "2.0.0", "3.0.0"],
        ),
    ],
)
def test_semantic_versioning(versions, expected):
    sv = SemanticVersioning()
    assert sv.order_versions(versions) == expected

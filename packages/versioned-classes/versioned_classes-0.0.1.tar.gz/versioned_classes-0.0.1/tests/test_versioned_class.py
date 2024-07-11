from versioned_classes.versioned_class import VersionedClass
from versioned_classes.versioned_class import initial_version


def test_create_versioned_calls():
    class Foo(VersionedClass):
        pass

    @Foo.register_version("v1")
    class Bar(Foo):
        pass

    @Foo.register_version("v2")
    class Baz(Foo):
        pass

    assert Foo.get_version("v1") == Bar
    assert Foo.get_version("v2") == Baz
    assert Foo.get_latest_version() == Baz
    assert Foo.latest_version_before("v2") == Bar
    assert isinstance(Foo.get_latest_version_instance(), Baz)
    assert isinstance(Foo.latest_version_before_instance("v2"), Bar)
    assert isinstance(Foo.get_version_instance("v1"), Bar)


def test_create_versioned_calls_with_initial_version():
    @initial_version("v1")
    class Foo(VersionedClass):
        pass

    assert Foo.get_version("v1") == Foo

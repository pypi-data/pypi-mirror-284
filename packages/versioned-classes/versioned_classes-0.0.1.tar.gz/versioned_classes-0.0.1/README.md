[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# Versioned Classes
A tool for managing versions of classes in a service.

## Installation
```bash
pip install versioned-classes
```


## Usage

If you have ever worked on an API which has a complex interdependency hierarchy, you might have faced the problem of managing versions of classes. When services grow large and multiple APIs are added, it becomes difficult to manage which versions of classes are being used by which API. Moreover, it can become cumbersome to ensure that all calls to a class are being kept up to date. The aim of this project is to provide a simple way to use the best version of a class in a service.

### Example
```python
from versioned_classes import VersionedClass
from versioned_classes import initial_version


@initial_version("v1")
class MyAPI(VersionedClass):
    pass


@MyAPI.register_version("v2")
class MyAPIV2(MyAPI):
    pass


MyAPI.get_latest_version()  # MyAPIV2

MyAPI.get_latest_version_instance(...)  # MyAPIV2(...)
```

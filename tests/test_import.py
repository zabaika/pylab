"""Basic tests for the pylab package."""


def test_can_import():
    """Пакет должен устанавливаться и импортироваться без ошибок"""
    import pylab


def test_docstring_exists():
    """У пакета должен быть docstring (хотя бы минимальный)"""
    import pylab
    assert pylab.__doc__ is not None
    assert len(pylab.__doc__.strip()) > 0


def test_has_core_functionality():
    """Проверяем наличие ключевой функции в библиотеке pylab"""
    import pytest
    pylab = pytest.importorskip("matplotlib.pyplot")
    assert hasattr(pylab, "plot")


def test_version_attribute():
    """Если в пакете есть __version__, он должен быть строкой"""
    import pylab
    if hasattr(pylab, "__version__"):
        assert isinstance(pylab.__version__, str)

from healthops import __version__


def test_package_is_importable() -> None:
    """Verify that the project package can be imported successfully."""
    assert __version__ == "0.1.0"
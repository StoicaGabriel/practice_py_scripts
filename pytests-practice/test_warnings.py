import warnings
import pytest


def deprecated_function():
    """Some sample deprecated function"""
    # Supposing the function is deprecated, send a warn message.
    warnings.warn(
        category=DeprecationWarning,
        message='This function is deprecated.')


def test_deprecated_function(recwarn):
    """Test the warning given by the deprecated function."""
    deprecated_function()
    assert len(recwarn) == 1
    warning = recwarn.pop()
    assert warning.category == DeprecationWarning
    assert str(warning.message) == 'This function is deprecated.'

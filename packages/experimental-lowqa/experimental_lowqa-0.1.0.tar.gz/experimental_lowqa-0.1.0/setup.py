# =====================================
# generator=datazen
# version=3.1.4
# hash=3f09e84d556b1ed96f16f6d9b23b95d4
# =====================================

"""
experimental-lowqa - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from experimental_lowqa_bootstrap.setup import setup  # type: ignore

# internal
from experimental_lowqa import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.11",
        "3.12",
    ],
}
setup(
    pkg_info,
    author_info,
)

"""""" # start delvewheel patch
def _delvewheel_patch_1_7_1():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_7_1()
del _delvewheel_patch_1_7_1
# end delvewheel patch

from .mecab import MeCab, MeCabError, mecabrc_path
from .types import Dictionary, Feature, Morpheme, Span

__version__ = "1.3.7"

__all__ = [
    "MeCab",
    "Morpheme",
    "Span",
    "Feature",
    "Dictionary",
    "MeCabError",
    "mecabrc_path",
]

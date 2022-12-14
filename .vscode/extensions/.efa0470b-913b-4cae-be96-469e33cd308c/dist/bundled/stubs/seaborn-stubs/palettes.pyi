"""
This type stub file was generated by pyright.
"""
from typing import Any
import matplotlib.colors as mcolors

__all__ = ["color_palette", "hls_palette", "husl_palette", "mpl_palette", "dark_palette", "light_palette", "diverging_palette", "blend_palette", "xkcd_palette", "crayon_palette", "cubehelix_palette", "set_color_codes"]
SEABORN_PALETTES: dict[str, list[str]] = ...
MPL_QUAL_PALS: dict[str, int]= ...
QUAL_PALETTE_SIZES: dict[str, int] = ...
QUAL_PALETTES: list[str] = ...

class _ColorPalette(list):
    def __enter__(self) -> _ColorPalette: ...
    
    def __exit__(self, *args) -> None: ...
    
    def as_hex(self) -> _ColorPalette: ...
    

def color_palette(palette=..., n_colors=..., desat=..., as_cmap=...) -> _ColorPalette | list[tuple[float, float, float]] | list[str] |mcolors.ListedColormap | mcolors.LinearSegmentedColormap: ...

def hls_palette(n_colors=..., h=..., l=..., s=..., as_cmap=...) -> _ColorPalette: ...

def husl_palette(n_colors=..., h=..., s=..., l=..., as_cmap=...) -> _ColorPalette: ...

def mpl_palette(name, n_colors=..., as_cmap=...) -> _ColorPalette: ...

def dark_palette(color, n_colors=..., reverse=..., as_cmap=..., input=...) -> _ColorPalette: ...

def light_palette(color, n_colors=..., reverse=..., as_cmap=..., input=...) -> _ColorPalette: ...

def diverging_palette(h_neg, h_pos, s=..., l=..., sep=..., n=..., center=..., as_cmap=...) -> _ColorPalette: ...

def blend_palette(colors, n_colors=..., as_cmap=..., input=...) -> _ColorPalette: ...

def xkcd_palette(colors) -> _ColorPalette | list[tuple[float, float, float]] | list[str]: ...

def crayon_palette(colors) -> _ColorPalette | list[tuple[float, float, float]] | list[str]: ...

def cubehelix_palette(n_colors=..., start=..., rot=..., gamma=..., hue=..., light=..., dark=..., reverse=..., as_cmap=...) -> _ColorPalette: ...

def set_color_codes(palette=...) -> None: ...


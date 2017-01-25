from typing import Union

from .price import Price


class PriceRange:
    min_price = ...  # Price
    max_price = ...  # Price

    def __init__(self, min_price: Price, max_price: Price) -> None: ...

    def __repr__(self) -> str: ...

    def __add__(self, other: Union[Price, PriceRange]) -> PriceRange: ...

    def __sub__(self, other: Union[Price, PriceRange]) -> PriceRange: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    def __contains__(self, item: Price) -> bool: ...

    @property
    def currency(self) -> str: ...

    def quantize(self, exp: str=None, rounding: str=None) -> PriceRange: ...

    def replace(self, min_price: Price=None, max_price: Price=None) -> PriceRange: ...

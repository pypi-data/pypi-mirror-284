# SPDX-FileCopyrightText: 2024-present Daniel Biehl <dbiehl@live.de>
#
# SPDX-License-Identifier: MIT
from typing import Any

from robot.api.deco import library
from robotlibcore import DynamicCore, keyword

from PlatynUI.technology.uiautomation import Locator

from .ButtonKeywords import ButtonKeywords
from .core.contextbase import ContextBase, ContextFactory
from .core.locatorbase import LocatorBase
from .TextKeywords import TextKeywords


def convert_locator(value) -> ContextBase:  # type: ignore
    if isinstance(value, ContextBase):
        return value

    if isinstance(value, LocatorBase):
        return ContextFactory.create_context(value)

    return ContextFactory.create_context(Locator(path=value))


@library(converters={ContextBase: convert_locator})
class PlatynUI(DynamicCore):
    def __init__(self) -> None:
        super().__init__([ButtonKeywords(), TextKeywords()])

    @keyword
    def blah(self) -> None:
        print("blah")

import re
import logging

from mkdocs.config import base, config_options as c
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

logger = logging.getLogger("mkdocs.plugins")

class LangPluginConfig(base.Config):
    global_enable = c.Type(bool, default=True)

class LangPlugin(BasePlugin[LangPluginConfig]):

    def check_lang_disable(self, page: Page) -> bool:
        if not self.config.global_enable and (not page.meta or not page.meta.get("lang", False)):
            return True

        if self.config.global_enable and page.meta and not page.meta.get("lang", True):
            return True

        return False

    def on_page_content(self, html: str, *, page: Page, config: MkDocsConfig, files: Files) -> str:
        if self.check_lang_disable(page):
            return html
        html = self.add_lang(page, html)

        return html

    def add_lang(self, page: Page, html: str) -> str:
        lang = page.meta.get("lang", "zh")  # Default to "zh" if not set
        regex = r'(.*)'
        result = f'<div lang="{lang}">\\1</div>'
        return re.sub(regex, result, html, flags=re.DOTALL)
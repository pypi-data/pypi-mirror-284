from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import re

class RenderStopperPlugin(BasePlugin):
    config_scheme = (
        ('tag', config_options.Type(str, default='[STOP]')),
    )

    def on_page_markdown(self, markdown, page, config, files):
        tag = self.config['tag']
        pattern = re.compile(re.escape(tag) + r'[\s\S]*', re.IGNORECASE)
        markdown = re.sub(pattern, '', markdown)
        return markdown
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import re

class RenderStopperPlugin(BasePlugin):
    config_scheme = (
        ('tag', config_options.Type(str, default='[STOP]')),
        ('placeholder', config_options.Type(str, default='À venir')),
    )

    def on_page_markdown(self, markdown, page, config, files):
        tag = self.config['tag']
        placeholder = self.config['placeholder']
        pattern = re.compile(re.escape(tag) + r'[\s\S]*', re.IGNORECASE)
        new_markdown = re.sub(pattern, '', markdown)

        # Si le document est vide après l'application du tag [STOP], insérer le message "À venir"
        if not new_markdown.strip():
            new_markdown = placeholder

        return new_markdown
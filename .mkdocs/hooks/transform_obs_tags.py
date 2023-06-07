import logging
import re
import string

import mkdocs.plugins

log = logging.getLogger("mkdocs")

@mkdocs.plugins.event_priority(100)
def on_page_markdown(markdown, page, **kwargs):
    """
    Заменяет obsidian теги (#тег) на front-matter-теги (tags: - tag)
    + Чекает что теги на английском
    """
    def _lines():
        lines = markdown.split('\n')

        for line in lines:
            if re.match('#([\w|-]+)', line):
                tags = re.findall(r'#([\w|-]+)', line)
                if not all(c in string.printable for tag in tags for c in tag):
                    log.warning(f'{page.file.abs_src_path}: Теги должны быть на английском: {tags}')
                page.meta['tags'] = tags
            else:
                yield line

    markdown = '\n'.join(_lines())

    return markdown

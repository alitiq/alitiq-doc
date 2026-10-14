"""
Lets a page point its canonical URL elsewhere via front matter.

Used for knowledge articles that moved to the alitiq.com blog, so search engines consolidate on
the blog version instead of indexing two competing copies:

    ---
    canonical: https://alitiq.com/en/blog/<slug>
    ---
"""

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page

CANONICAL_TAG = re.compile(r'<link rel="canonical" href="[^"]*">')


def on_post_page(output: str, page: Page, config: MkDocsConfig) -> str:
    """Replace (or add) the canonical link if the page sets `canonical` in its front matter."""
    canonical = page.meta.get("canonical")
    if not canonical:
        return output
    tag = f'<link rel="canonical" href="{canonical}">'
    output, replaced = CANONICAL_TAG.subn(tag, output, count=1)
    if not replaced:
        output = output.replace("</head>", f"{tag}</head>", 1)
    return output

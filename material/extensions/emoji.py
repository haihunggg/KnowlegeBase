from __future__ import annotations

import codecs
import functools
import material
import os

from glob import iglob
from inspect import getfile
from markdown import Markdown
from pymdownx import emoji, twemoji_db
from xml.etree.ElementTree import Element

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# Create twemoji index
def twemoji(options: object, md: Markdown):
    paths = options.get("custom_icons", [])[:]
    return _load_twemoji_index(tuple(paths))

# Create emoji or icon
def to_svg(
    index: str, shortname: str, alias: str, uc: str | None, alt: str,
    title: str, category: str, options: object, md: Markdown
):
    if not uc:
        icons = md.inlinePatterns["emoji"].emoji_index["emoji"]

        # Create and return element to host icon
        el = Element("span", { "class": options.get("classes", index) })
        el.text = md.htmlStash.store(_load(icons[shortname]["path"]))
        return el

    # Delegate to `pymdownx.emoji` extension
    return emoji.to_svg(
        index, shortname, alias, uc, alt, title, category, options, md
    )

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

# Load icon
@functools.lru_cache(maxsize = None)
def _load(file: str):
    with codecs.open(file, encoding = "utf-8") as f:
        return f.read()

# Load twemoji index and add icons
@functools.lru_cache(maxsize = None)
def _load_twemoji_index(paths):
    index = {
        "name": "twemoji",
        "emoji": twemoji_db.emoji,
        "aliases": twemoji_db.aliases
    }

    # Compute path to theme root and traverse all icon directories
    root = os.path.dirname(getfile(material))
    root = os.path.join(root, "templates", ".icons")
    for path in [*paths, root]:
        base = os.path.normpath(path)

        # Index icons provided by the theme and via custom icons
        glob = os.path.join(base, "**", "*.svg")
        glob = iglob(os.path.normpath(glob), recursive = True)
        for file in glob:
            icon = file[len(base) + 1:-4].replace(os.path.sep, "-")

            # Add icon to index
            name = f":{icon}:"
            if not any(name in index[key] for key in ["emoji", "aliases"]):
                index["emoji"][name] = { "name": name, "path": file }

    # Return index
    return index

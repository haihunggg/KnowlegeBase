import os

from mkdocs.plugins import BasePlugin, event_priority

from .config import OfflineConfig

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

# Offline plugin
class OfflinePlugin(BasePlugin[OfflineConfig]):

    # Set configuration for offline build
    def on_config(self, config):
        if not self.config.enabled:
            return

        # Ensure correct resolution of links when viewing the site from the
        # file system by disabling directory URLs
        config.use_directory_urls = False

        # Append iframe-worker to polyfills/shims
        config.extra["polyfills"] = config.extra.get("polyfills", [])
        if not any("iframe-worker" in url for url in config.extra["polyfills"]):
            script = "https://unpkg.com/iframe-worker/shim"
            config.extra["polyfills"].append(script)

    # Add support for offline search (run latest) - the search index is copied
    # and inlined into a script, so that it can be used without a server
    @event_priority(-100)
    def on_post_build(self, *, config):
        if not self.config.enabled:
            return

        # Ensure presence of search index
        path = os.path.join(config.site_dir, "search")
        file = os.path.join(path, "search_index.json")
        if not os.path.isfile(file):
            return

        # Obtain search index contents
        with open(file, encoding = "utf-8") as f:
            data = f.read()

        # Inline search index contents into script
        file = os.path.join(path, "search_index.js")
        with open(file, "w", encoding = "utf-8") as f:
            f.write(f"var __index = {data}")

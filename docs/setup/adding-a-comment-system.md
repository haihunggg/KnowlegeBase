# Adding a comment system

Material for MkDocs allows to easily add the third-party comment system of your
choice to the footer of any page by using [theme extension]. As an example,
we'll be integrating [Giscus], which is Open Source, free, and uses GitHub
discussions as a backend.

  [Giscus]: https://giscus.app/

## Customization

### Giscus integration

Before you can use [Giscus], you need to complete the following steps:

1.  __Install the [Giscus GitHub App]__ and grant access to the repository
    that should host comments as GitHub discussions. Note that this can be a
    repository different from your documentation.
2.  __Visit [Giscus] and generate the snippet__ through their configuration tool
    to load the comment system. Copy the snippet for the next step. The
    resulting snippet should look similar to this:

    ``` html
    <script
      src="https://giscus.app/client.js"
      data-repo="<username>/<repository>"
      data-repo-id="..."
      data-category="..."
      data-category-id="..."
      data-mapping="pathname"
      data-reactions-enabled="1"
      data-emit-metadata="1"
      data-theme="light"
      data-lang="en"
      crossorigin="anonymous"
      async
    >
    </script>
    ```

The [`comments.html`][comments] partial (empty by default) is the best place to
add the snippet generated by [Giscus]. Follow the guide on [theme extension]
and [override the `comments.html` partial][overriding partials] with:

``` html hl_lines="3"
{% if page.meta.comments %}
  <h2 id="__comments">{{ lang.t("meta.comments") }}</h2>
  <!-- Insert generated snippet here -->

  <!-- Synchronize Giscus theme with palette -->
  <script>
    var giscus = document.querySelector("script[src*=giscus]")

    // Set palette on initial load
    var palette = __md_get("__palette")
    if (palette && typeof palette.color === "object") {
      var theme = palette.color.scheme === "slate"
        ? "transparent_dark"
        : "light"

      // Instruct Giscus to set theme
      giscus.setAttribute("data-theme", theme) // (1)!
    }

    // Register event handlers after documented loaded
    document.addEventListener("DOMContentLoaded", function() {
      var ref = document.querySelector("[data-md-component=palette]")
      ref.addEventListener("change", function() {
        var palette = __md_get("__palette")
        if (palette && typeof palette.color === "object") {
          var theme = palette.color.scheme === "slate"
            ? "transparent_dark"
            : "light"

          // Instruct Giscus to change theme
          var frame = document.querySelector(".giscus-frame")
          frame.contentWindow.postMessage(
            { giscus: { setConfig: { theme } } },
            "https://giscus.app"
          )
        }
      })
    })
  </script>
{% endif %}
```

1.  This code block ensures that [Giscus] renders with a dark theme when the
    palette is set to `slate`. Note that multiple dark themes are available,
    so you can change it to your liking.

Replace the highlighted line with the snippet you generated with the [Giscus]
configuration tool in the previous step. If you copied the snippet from above,
you can enable comments on a page by setting the `comments` front matter
property to `true`:

``` yaml
---
comments: true
---

# Page title
...
```

If you wish to enable comments for an entire folder, you can use the
[built-in meta plugin].

  [Giscus GitHub App]: https://github.com/apps/giscus
  [theme extension]: ../customization.md#extending-the-theme
  [comments]: https://github.com/squidfunk/mkdocs-material/blob/master/src/templates/partials/comments.html
  [overriding partials]: ../customization.md#overriding-partials
  [built-in meta plugin]: ../plugins/meta.md




<div class="last-updated">Last updated on <strong>Feb 18, 2025</strong> by <strong>Trinh Hoai Nhat</strong></div>

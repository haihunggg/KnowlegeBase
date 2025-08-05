document$.subscribe(() => {
  document.querySelectorAll("nav.md-nav details").forEach((el) => {
    el.removeAttribute("open");
  });
});

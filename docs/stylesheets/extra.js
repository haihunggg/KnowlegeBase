document$.subscribe(() => {
  document.querySelectorAll("nav.md-nav details").forEach((el) => {
    el.removeAttribute("open");
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const headings = document.querySelectorAll(
    ".md-typeset h2[id], .md-typeset h4[id]"
  );

  headings.forEach((heading) => {
    const id = heading.id;
    if (!id) return;

    // Tạo button chứa SVG + tooltip
    const button = document.createElement("button");
    button.className = "copy-link-button";
    button.innerHTML = `
      <span class="tooltip">Copy link hướng dẫn</span>
      <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" viewBox="0 -960 960 960" fill="#666666">
        <path d="M440-280H280q-83 0-141.5-58.5T80-480q0-83 58.5-141.5T280-680h160v80H280q-50 0-85 35t-35 85q0 50 35 85t85 35h160v80ZM320-440v-80h320v80H320Zm200 160v-80h160q50 0 85-35t35-85q0-50-35-85t-85-35H520v-80h160q83 0 141.5 58.5T880-480q0 83-58.5 141.5T680-280H520Z"/>
      </svg>
    `;

    button.addEventListener("click", () => {
      const url = `${location.origin}${location.pathname}#${id}`;
      navigator.clipboard.writeText(url).then(() => {
        const tooltip = button.querySelector(".tooltip");
        tooltip.textContent = "✅ Copied!";
        setTimeout(() => (tooltip.textContent = "Copy link hướng dẫn"), 2000);
      });
    });

    heading.appendChild(button);
  });
});

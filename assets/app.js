/* Continental Reformed Bible Study — App Logic */
(function () {
  "use strict";

  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const menuBtn = document.getElementById("menu-toggle");
  const appShell = document.getElementById("app-shell");
  const progressBar = document.getElementById("progress-bar");
  const backTop = document.getElementById("back-top");
  const tocNav = document.getElementById("toc-nav");
  const tocSearch = document.getElementById("toc-search");
  const main = document.getElementById("main");

  const MQ_DESKTOP = window.matchMedia("(min-width: 1100px)");

  /* —— Build TOC from headings —— */
  function buildToc() {
    if (!tocNav || !main) return;
    const headings = main.querySelectorAll("h2[id], h3[id]");
    const frag = document.createDocumentFragment();
    headings.forEach((h) => {
      const a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent.replace(/^\d+[\.\s]*/, "").trim() || h.textContent;
      // Keep number prefix if present for clarity
      a.textContent = h.textContent.trim();
      a.dataset.target = h.id;
      if (h.tagName === "H3") a.classList.add("toc-h3");
      a.addEventListener("click", (e) => {
        e.preventDefault();
        document.getElementById(h.id)?.scrollIntoView({ behavior: "smooth" });
        history.replaceState(null, "", "#" + h.id);
        if (!MQ_DESKTOP.matches) closeSidebar();
      });
      frag.appendChild(a);
    });
    tocNav.appendChild(frag);
  }

  /* —— Sidebar —— */
  function openSidebar() {
    sidebar?.classList.add("open");
    sidebar?.classList.remove("collapsed");
    overlay?.classList.add("show");
    menuBtn?.setAttribute("aria-expanded", "true");
    if (MQ_DESKTOP.matches) appShell?.classList.add("sidebar-visible");
  }

  function closeSidebar() {
    sidebar?.classList.remove("open");
    overlay?.classList.remove("show");
    menuBtn?.setAttribute("aria-expanded", "false");
    if (MQ_DESKTOP.matches) {
      sidebar?.classList.add("collapsed");
      appShell?.classList.remove("sidebar-visible");
    }
  }

  function toggleSidebar() {
    const isOpen = sidebar?.classList.contains("open") ||
      (MQ_DESKTOP.matches && appShell?.classList.contains("sidebar-visible") && !sidebar?.classList.contains("collapsed"));
    if (MQ_DESKTOP.matches) {
      if (appShell?.classList.contains("sidebar-visible") && !sidebar?.classList.contains("collapsed")) {
        closeSidebar();
      } else {
        openSidebar();
      }
    } else {
      if (sidebar?.classList.contains("open")) closeSidebar();
      else openSidebar();
    }
  }

  function initSidebarState() {
    if (MQ_DESKTOP.matches) {
      sidebar?.classList.add("open");
      sidebar?.classList.remove("collapsed");
      appShell?.classList.add("sidebar-visible");
      overlay?.classList.remove("show");
      menuBtn?.setAttribute("aria-expanded", "true");
    } else {
      sidebar?.classList.remove("open");
      appShell?.classList.remove("sidebar-visible");
      menuBtn?.setAttribute("aria-expanded", "false");
    }
  }

  menuBtn?.addEventListener("click", toggleSidebar);
  overlay?.addEventListener("click", closeSidebar);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeSidebar();
  });

  MQ_DESKTOP.addEventListener("change", initSidebarState);

  /* —— TOC search —— */
  tocSearch?.addEventListener("input", () => {
    const q = tocSearch.value.trim().toLowerCase();
    tocNav?.querySelectorAll("a").forEach((a) => {
      const show = !q || a.textContent.toLowerCase().includes(q);
      a.style.display = show ? "" : "none";
    });
  });

  /* —— Scroll progress + active TOC + back-top —— */
  const headingEls = [];

  function onScroll() {
    const scrollTop = window.scrollY;
    const docH = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docH > 0 ? Math.min(100, (scrollTop / docH) * 100) : 0;
    document.documentElement.style.setProperty("--progress", pct + "%");

    if (backTop) {
      backTop.classList.toggle("show", scrollTop > 500);
    }

    // Active heading
    if (!headingEls.length) return;
    const offset = 80;
    let current = headingEls[0];
    for (const h of headingEls) {
      if (h.getBoundingClientRect().top <= offset) current = h;
      else break;
    }
    const id = current?.id;
    tocNav?.querySelectorAll("a").forEach((a) => {
      a.classList.toggle("active", a.dataset.target === id);
    });
  }

  let ticking = false;
  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        onScroll();
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  backTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* —— Expand / collapse all details —— */
  document.getElementById("expand-all")?.addEventListener("click", () => {
    document.querySelectorAll("details.fold").forEach((d) => { d.open = true; });
  });
  document.getElementById("collapse-all")?.addEventListener("click", () => {
    document.querySelectorAll("details.fold").forEach((d) => { d.open = false; });
  });

  /* —— Init Mermaid —— */
  function initMermaid() {
    if (typeof mermaid === "undefined") return;
    mermaid.initialize({
      startOnLoad: false,
      theme: "dark",
      themeVariables: {
        primaryColor: "#1a2b45",
        primaryTextColor: "#e8eef7",
        primaryBorderColor: "#c9a227",
        lineColor: "#d4af37",
        secondaryColor: "#152238",
        tertiaryColor: "#0f1a2e",
        background: "#0f1a2e",
        mainBkg: "#1a2b45",
        nodeBorder: "#c9a227",
        clusterBkg: "#152238",
        titleColor: "#f0d878",
        edgeLabelBackground: "#152238",
        fontFamily: "Noto Sans SC, sans-serif",
      },
      flowchart: { curve: "basis", padding: 12 },
      securityLevel: "loose",
    });
    mermaid.run({ querySelector: ".mermaid" }).catch((err) => {
      console.warn("Mermaid render issue:", err);
    });
  }

  /* —— Hash on load —— */
  function scrollToHash() {
    if (location.hash) {
      const el = document.getElementById(location.hash.slice(1));
      if (el) setTimeout(() => el.scrollIntoView({ behavior: "smooth" }), 100);
    }
  }

  /* —— Boot —— */
  function boot() {
    buildToc();
    headingEls.push(...main.querySelectorAll("h2[id], h3[id]"));
    initSidebarState();
    initMermaid();
    onScroll();
    scrollToHash();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

/* Continental Reformed Bible Study — App Logic (dark elegant theme) */
(function () {
  "use strict";

  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const menuBtn = document.getElementById("menu-toggle");
  const appShell = document.getElementById("app-shell");
  const backTop = document.getElementById("back-top");
  const tocNav = document.getElementById("toc-nav");
  const tocSearch = document.getElementById("toc-search");
  const main = document.getElementById("main");

  const MQ_DESKTOP = window.matchMedia("(min-width: 901px)");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function scrollBehavior() {
    return reduceMotion ? "auto" : "smooth";
  }

  /* —— Build TOC from headings —— */
  function buildToc() {
    if (!tocNav || !main) return;
    const headings = main.querySelectorAll("h2[id], h3[id]");
    const frag = document.createDocumentFragment();
    headings.forEach((h) => {
      const a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent.trim();
      a.dataset.target = h.id;
      if (h.tagName === "H3") a.classList.add("toc-h3");
      a.addEventListener("click", (e) => {
        e.preventDefault();
        document.getElementById(h.id)?.scrollIntoView({ behavior: scrollBehavior() });
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
    document.body.style.overflow = MQ_DESKTOP.matches ? "" : "hidden";
  }

  function closeSidebar() {
    sidebar?.classList.remove("open");
    overlay?.classList.remove("show");
    menuBtn?.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
    if (MQ_DESKTOP.matches) {
      sidebar?.classList.add("collapsed");
      appShell?.classList.remove("sidebar-visible");
    }
  }

  function toggleSidebar() {
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
    document.body.style.overflow = "";
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

  /* —— Swipe to close drawer (touch) —— */
  let touchStartX = 0;
  let touchStartY = 0;
  sidebar?.addEventListener("touchstart", (e) => {
    const t = e.changedTouches[0];
    touchStartX = t.screenX;
    touchStartY = t.screenY;
  }, { passive: true });
  sidebar?.addEventListener("touchend", (e) => {
    if (MQ_DESKTOP.matches || !sidebar.classList.contains("open")) return;
    const t = e.changedTouches[0];
    const dx = t.screenX - touchStartX;
    const dy = Math.abs(t.screenY - touchStartY);
    if (dx < -60 && dy < 80) closeSidebar();
  }, { passive: true });

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
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docH = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docH > 0 ? Math.min(100, (scrollTop / docH) * 100) : 0;
    document.documentElement.style.setProperty("--progress", pct + "%");

    if (backTop) {
      backTop.classList.toggle("show", scrollTop > 400);
    }

    if (!headingEls.length) return;
    const offset = (parseInt(getComputedStyle(document.documentElement).getPropertyValue("--header-h"), 10) || 56) + 24;
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
  window.addEventListener("resize", () => {
    onScroll();
  }, { passive: true });

  backTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: scrollBehavior() });
  });

  /* —— Expand / collapse ALL folds —— */
  document.getElementById("expand-all")?.addEventListener("click", () => {
    document.querySelectorAll("details.fold").forEach((d) => { d.open = true; });
  });
  document.getElementById("collapse-all")?.addEventListener("click", () => {
    document.querySelectorAll("details.fold").forEach((d) => { d.open = false; });
  });

  /* —— Init Mermaid (dark elegant) —— */
  function initMermaid() {
    if (typeof mermaid === "undefined") return;
    mermaid.initialize({
      startOnLoad: false,
      theme: "dark",
      themeVariables: {
        darkMode: true,
        background: "#152238",
        primaryColor: "#1a2b45",
        primaryTextColor: "#e8e4d9",
        primaryBorderColor: "#d4af37",
        secondaryColor: "#0f172a",
        tertiaryColor: "#1e334f",
        lineColor: "#d4af37",
        textColor: "#e8e4d9",
        mainBkg: "#1a2b45",
        nodeBorder: "#c9a227",
        clusterBkg: "#152238",
        clusterBorder: "#2a3f5f",
        titleColor: "#f0d878",
        edgeLabelBackground: "#152238",
        nodeTextColor: "#e8e4d9",
        fontFamily: "system-ui, Noto Sans SC, sans-serif",
      },
      flowchart: { curve: "basis", padding: 12, useMaxWidth: true, htmlLabels: true },
      mindmap: { useMaxWidth: true },
      securityLevel: "loose",
    });
    mermaid.run({ querySelector: ".mermaid" }).catch((err) => {
      console.warn("Mermaid render issue:", err);
    });
  }

  /* —— Wrap mermaid after render for scroll safety —— */
  function enhanceDiagramScroll() {
    document.querySelectorAll(".mermaid-wrap").forEach((wrap) => {
      wrap.classList.add("diagram-scroll");
    });
    document.querySelectorAll(".table-wrap").forEach((wrap) => {
      wrap.classList.add("table-scroll");
    });
  }

  /* —— Hash on load —— */
  function scrollToHash() {
    if (location.hash) {
      const el = document.getElementById(location.hash.slice(1));
      if (el) setTimeout(() => el.scrollIntoView({ behavior: scrollBehavior() }), 120);
    }
  }

  /* —— Viewport meta safe-area helper (viewport-fit) —— */
  function ensureViewportFit() {
    const meta = document.querySelector('meta[name="viewport"]');
    if (meta && !/viewport-fit/.test(meta.content)) {
      meta.content = meta.content + ", viewport-fit=cover";
    }
  }

  /* —— Boot —— */
  function boot() {
    ensureViewportFit();
    buildToc();
    headingEls.push(...main.querySelectorAll("h2[id], h3[id]"));
    initSidebarState();
    enhanceDiagramScroll();
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

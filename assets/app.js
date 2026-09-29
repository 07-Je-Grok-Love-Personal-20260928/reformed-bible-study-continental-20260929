/* Continental Reformed Bible Study — App Logic (premium dark elegant) */
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
    const offset = (parseInt(getComputedStyle(document.documentElement).getPropertyValue("--header-h"), 10) || 64) + 24;
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

  /* —— High-contrast Mermaid theme (cream/gold nodes, dark text, gold edges) —— */
  const MERMAID_THEME = {
    darkMode: false,
    background: "#0f1a2c",
    primaryColor: "#f5e6c4",
    primaryTextColor: "#1a1a1a",
    primaryBorderColor: "#d4af37",
    secondaryColor: "#e8d5a3",
    tertiaryColor: "#1e3a5f",
    secondaryTextColor: "#1a1a1a",
    tertiaryTextColor: "#f0d878",
    lineColor: "#d4af37",
    textColor: "#1a1a1a",
    mainBkg: "#f5e6c4",
    nodeBorder: "#c9a227",
    clusterBkg: "#152238",
    clusterBorder: "#c9a227",
    titleColor: "#f0d878",
    edgeLabelBackground: "#f5e6c4",
    nodeTextColor: "#1a1a1a",
    fontFamily: "system-ui, Noto Sans SC, sans-serif",
    fontSize: "16px",
  };

  function forceMermaidContrast() {
    document.querySelectorAll(".mermaid svg").forEach((svg) => {
      svg.querySelectorAll(".node rect, .node polygon, .node circle, .node path").forEach((el) => {
        const fill = (el.getAttribute("fill") || "").toLowerCase();
        if (!fill || fill === "none" || fill === "#0f172a" || fill === "#152238" || fill === "#1a2b45" || fill === "#1e334f") {
          el.setAttribute("fill", "#f5e6c4");
        }
        if (!el.getAttribute("stroke") || el.getAttribute("stroke") === "none") {
          el.setAttribute("stroke", "#d4af37");
        }
      });
      svg.querySelectorAll("text, .nodeLabel, tspan").forEach((el) => {
        el.setAttribute("fill", "#1a1a1a");
        if (el.style) el.style.color = "#1a1a1a";
      });
      svg.querySelectorAll("foreignObject div, foreignObject span, foreignObject p").forEach((el) => {
        el.style.color = "#1a1a1a";
      });
      svg.querySelectorAll(".edgePath path, .flowchart-link").forEach((el) => {
        el.setAttribute("stroke", "#d4af37");
      });
      svg.querySelectorAll(".marker, defs marker path").forEach((el) => {
        el.setAttribute("fill", "#d4af37");
        el.setAttribute("stroke", "#d4af37");
      });
    });
  }

  function initMermaid() {
    if (typeof mermaid === "undefined") {
      setTimeout(initMermaid, 80);
      return;
    }
    // Re-init after theme so every diagram picks up high-contrast vars
    mermaid.initialize({
      startOnLoad: false,
      theme: "base",
      themeVariables: MERMAID_THEME,
      flowchart: {
        curve: "basis",
        padding: 14,
        useMaxWidth: true,
        htmlLabels: true,
        nodeSpacing: 28,
        rankSpacing: 36,
      },
      mindmap: { useMaxWidth: true, padding: 12 },
      securityLevel: "loose",
    });
    mermaid.run({ querySelector: ".mermaid" })
      .then(() => {
        forceMermaidContrast();
        // Second pass after layout settles
        setTimeout(forceMermaidContrast, 120);
      })
      .catch((err) => {
        console.warn("Mermaid render issue:", err);
        forceMermaidContrast();
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

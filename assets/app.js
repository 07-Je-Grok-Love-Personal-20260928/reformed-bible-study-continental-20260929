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
    overlay?.setAttribute("aria-hidden", "false");
    sidebar?.setAttribute("aria-hidden", "false");
    menuBtn?.setAttribute("aria-expanded", "true");
    if (MQ_DESKTOP.matches) {
      appShell?.classList.add("sidebar-visible");
      document.body.classList.remove("nav-open");
      document.body.style.overflow = "";
    } else {
      document.body.classList.add("nav-open");
      document.body.style.overflow = "hidden";
      // Focus close button for a11y without stealing if user tapped hamburger again
      try { document.getElementById("sidebar-close")?.focus({ preventScroll: true }); } catch (_) {}
    }
  }

  function closeSidebar() {
    sidebar?.classList.remove("open");
    overlay?.classList.remove("show");
    overlay?.setAttribute("aria-hidden", "true");
    menuBtn?.setAttribute("aria-expanded", "false");
    document.body.classList.remove("nav-open");
    document.body.style.overflow = "";
    if (MQ_DESKTOP.matches) {
      sidebar?.classList.add("collapsed");
      appShell?.classList.remove("sidebar-visible");
    } else {
      sidebar?.setAttribute("aria-hidden", "true");
      try { menuBtn?.focus({ preventScroll: true }); } catch (_) {}
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
    document.body.classList.remove("nav-open");
    if (MQ_DESKTOP.matches) {
      sidebar?.classList.add("open");
      sidebar?.classList.remove("collapsed");
      appShell?.classList.add("sidebar-visible");
      overlay?.classList.remove("show");
      menuBtn?.setAttribute("aria-expanded", "true");
    } else {
      sidebar?.classList.remove("open");
      sidebar?.setAttribute("aria-hidden", "true");
      appShell?.classList.remove("sidebar-visible");
      overlay?.classList.remove("show");
      overlay?.setAttribute("aria-hidden", "true");
      menuBtn?.setAttribute("aria-expanded", "false");
    }
  }

  menuBtn?.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    toggleSidebar();
  });
  overlay?.addEventListener("click", (e) => {
    e.preventDefault();
    closeSidebar();
  });
  document.getElementById("sidebar-close")?.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    closeSidebar();
  });

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
  function setAllFolds(open) {
    document.querySelectorAll("details.fold").forEach((d) => { d.open = open; });
  }
  ["expand-all", "expand-all-hero"].forEach((id) => {
    document.getElementById(id)?.addEventListener("click", () => setAllFolds(true));
  });
  ["collapse-all", "collapse-all-hero"].forEach((id) => {
    document.getElementById(id)?.addEventListener("click", () => setAllFolds(false));
  });

  /* —— High-contrast Mermaid theme (multi-color storyline branches, dark text) —— */
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
    /* Branch palette — chip colors: gold/blue/purple/green/teal/rose/amber */
    git0: "#f0d878",
    gitBranchLabel0: "#1a1a1a",
    git1: "#d6e8f8",
    gitBranchLabel1: "#1a1a1a",
    git2: "#e6dcf5",
    gitBranchLabel2: "#1a1a1a",
    git3: "#d4eedf",
    gitBranchLabel3: "#1a1a1a",
    cScale0: "#f5e6c4",
    cScaleLabel0: "#1a1a1a",
    cScaleInv0: "#d4af37",
    cScale1: "#d6e8f8",
    cScaleLabel1: "#1a1a1a",
    cScaleInv1: "#6ba3e0",
    cScale2: "#e6dcf5",
    cScaleLabel2: "#1a1a1a",
    cScaleInv2: "#b39ddb",
    cScale3: "#d4eedf",
    cScaleLabel3: "#1a1a1a",
    cScaleInv3: "#3d9a6a",
    cScale4: "#d4f0ee",
    cScaleLabel4: "#1a1a1a",
    cScaleInv4: "#5ec4c0",
    cScale5: "#f5d6d6",
    cScaleLabel5: "#1a1a1a",
    cScaleInv5: "#c45c5c",
    cScale6: "#f5e0c8",
    cScaleLabel6: "#1a1a1a",
    cScaleInv6: "#e8a85c",
    cScale7: "#f5e6c4",
    cScaleLabel7: "#1a1a1a",
    cScaleInv7: "#d4af37",
    cScale8: "#d6e8f8",
    cScaleLabel8: "#1a1a1a",
    cScaleInv8: "#6ba3e0",
    cScale9: "#e6dcf5",
    cScaleLabel9: "#1a1a1a",
    cScaleInv9: "#b39ddb",
    cScale10: "#d4eedf",
    cScaleLabel10: "#1a1a1a",
    cScaleInv10: "#3d9a6a",
    cScale11: "#d4f0ee",
    cScaleLabel11: "#1a1a1a",
    cScaleInv11: "#5ec4c0",
  };

  const MINDMAP_BRANCH_COLORS = [
    { fill: "#f5e6c4", stroke: "#d4af37" }, // gold
    { fill: "#d6e8f8", stroke: "#6ba3e0" }, // blue
    { fill: "#e6dcf5", stroke: "#b39ddb" }, // purple
    { fill: "#d4eedf", stroke: "#3d9a6a" }, // green
    { fill: "#d4f0ee", stroke: "#5ec4c0" }, // teal
    { fill: "#f5d6d6", stroke: "#c45c5c" }, // rose
    { fill: "#f5e0c8", stroke: "#e8a85c" }, // amber
  ];
  const MINDMAP_ROOT_COLOR = { fill: "#f0d878", stroke: "#c9a227" };

  function mindmapColorForNode(el) {
    const host = el.closest("[class*=\"section-\"]") || el.parentElement;
    const cls = (host && host.getAttribute("class")) || el.getAttribute("class") || "";
    if (/\bsection-root\b/.test(cls)) return MINDMAP_ROOT_COLOR;
    const m = cls.match(/\bsection-(\d+)\b/);
    if (m) return MINDMAP_BRANCH_COLORS[Number(m[1]) % MINDMAP_BRANCH_COLORS.length];
    return MINDMAP_BRANCH_COLORS[0];
  }

  function forceMermaidContrast() {
    document.querySelectorAll(".mermaid svg").forEach((svg) => {
      // Flowchart nodes
      svg.querySelectorAll(".node rect, .node polygon, .node circle, .node path").forEach((el) => {
        const fill = (el.getAttribute("fill") || "").toLowerCase();
        if (!fill || fill === "none" || fill === "#0f172a" || fill === "#152238" || fill === "#1a2b45" || fill === "#1e334f" || fill === "#000" || fill === "#000000" || fill === "rgb(0, 0, 0)" || fill === "black") {
          el.setAttribute("fill", "#f5e6c4");
        }
        if (!el.getAttribute("stroke") || el.getAttribute("stroke") === "none") {
          el.setAttribute("stroke", "#d4af37");
        }
      });
      // Mindmap nodes — chip palette by section-N; root stays gold
      svg.querySelectorAll(".mindmap-node rect, .mindmap-node polygon, .mindmap-node circle, .mindmap-node path, [class*=\"section-\"] rect, [class*=\"section-\"] polygon, [class*=\"section-\"] circle, [class*=\"section-\"] path").forEach((el) => {
        const { fill, stroke } = mindmapColorForNode(el);
        el.setAttribute("fill", fill);
        el.setAttribute("stroke", stroke);
        if (el.style) {
          el.style.fill = fill;
          el.style.stroke = stroke;
        }
      });
      svg.querySelectorAll("text, .nodeLabel, tspan, .mindmap-node-label").forEach((el) => {
        el.setAttribute("fill", "#1a1a1a");
        if (el.style) el.style.color = "#1a1a1a";
      });
      svg.querySelectorAll("foreignObject div, foreignObject span, foreignObject p").forEach((el) => {
        el.style.color = "#1a1a1a";
      });
      // Colors only — never touch path d= or node transform (layout geometry)
      svg.querySelectorAll(".edgePath path, .flowchart-link, .mindmap-edges path, .mindmap-edges line, .edge, [class*=\"section-edge-\"]").forEach((el) => {
        const host = el.closest("[class*=\"section-edge-\"]") || el;
        const cls = (host.getAttribute("class") || "") + " " + (el.getAttribute("class") || "");
        const m = cls.match(/section-edge-(\d+)/);
        const stroke = m
          ? MINDMAP_BRANCH_COLORS[Number(m[1]) % MINDMAP_BRANCH_COLORS.length].stroke
          : "#d4af37";
        el.setAttribute("stroke", stroke);
        if (el.style) el.style.stroke = stroke;
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
        padding: 16,
        useMaxWidth: true,
        htmlLabels: true,
        nodeSpacing: 24,
        rankSpacing: 40,
      },
      mindmap: { useMaxWidth: false, padding: 28 },
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

// ========= START OF FILE data/floodlamp/_exclude-from-archive/_code-floodlamp-archive/webcode/floodlamp_archive_item_template.js =========
// deploy: copy to the FloodLAMP archive item template page > Page Settings > Custom Code > Before </body> between script tags
// contains: archive item template rendering logic for CMS-driven archive item pages,
//           including field extraction, link handling, and dynamic HTML output

var fileInfo = 'floodlamp_archive_item_template.js  3-27 1243 fix capitalization on metadata rows values displayed';

(function () {
  const ROOT_SELECTOR = "#fl-archive-template-root, [data-fl-archive-template-root='true']";
  const DATA_SELECTOR = "[data-fl-archive-template-data='true']";
  const LINK_FIELD_NAMES = [
    "gfile-url",
    "xfile-github-download-url",
    "pdf-gdrive-url",
    "pdf-github-url",
    "github-markdown-url",
    "github-markdown-download-url",
    "web-pdf-url",
    "web-slides-url",
    "youtube-url",
    "web-url"
  ];
  const FIELD_NAMES = [
    "title",
    "summary-short",
    "archive-item-type",
    "archive-scope",
    "category",
    "subcategory",
    "source-file-name",
    "source-rel-path",
    "file-date",
    "notes",
    "tags",
    "source-file-type",
    "xfile-type",
    "license",
    "gfile-url",
    "xfile-github-download-url",
    "pdf-gdrive-url",
    "pdf-github-url",
    "github-markdown-url",
    "github-markdown-download-url",
    "words",
    "tokens",
    "web-pdf-url",
    "web-slides-url",
    "youtube-url",
    "audio-file-name",
    "web-url"
  ];
  // Template styling now lives in floodlamp_archive_site_head.html for Webflow site head deployment.
  function init() {
    console.log('Loading JavaScript for Archive Item Template: ', fileInfo);
    const root = document.querySelector(ROOT_SELECTOR);
    if (!root) {
      return;
    }
    const dataRoot = root.querySelector(DATA_SELECTOR);
    if (!dataRoot) {
      renderState(root, "Archive template data is missing.");
      return;
    }
    const record = readRecord(dataRoot);
    if (!record.title) {
      renderState(root, "Archive template could not find the CMS title field.");
      return;
    }
    renderTemplate(root, record);
    attachDownloadHandlers(root);
    console.log("FloodLAMP archive item template loaded:", fileInfo, record.slug || record.title);
  }
  function readRecord(dataRoot) {
    const record = {};
    FIELD_NAMES.forEach((fieldName) => {
      record[fieldName] = readFieldValue(dataRoot, fieldName);
    });
    LINK_FIELD_NAMES.forEach((fieldName) => {
      record[fieldName] = normalizeUrl(record[fieldName]);
    });
    record.slug = slugify(record.title);
    return record;
  }
  function readFieldValue(dataRoot, fieldName) {
    const node = dataRoot.querySelector(`[data-fl-field="${fieldName}"]`);
    if (!node) {
      return "";
    }
    if (node.tagName === "A") {
      const href = node.getAttribute("href") || "";
      return cleanValue(href);
    }
    return cleanValue(node.textContent || "");
  }
  function cleanValue(value) {
    const cleanedValue = String(value || "").replace(/\u00a0/g, " ").trim();
    if (!cleanedValue || cleanedValue === "#" || cleanedValue.toUpperCase() === "NA" || /^REPLACE_WITH_/i.test(cleanedValue)) {
      return "";
    }
    return cleanedValue;
  }
  function normalizeUrl(value) {
    const cleanedValue = cleanValue(value);
    if (!cleanedValue || !/^https?:\/\//i.test(cleanedValue)) {
      return "";
    }
    try {
      const urlObject = new URL(cleanedValue);
      if (typeof window !== "undefined" && urlObject.origin === window.location.origin && urlObject.pathname === window.location.pathname && !urlObject.search && !urlObject.hash) {
        return "";
      }
      return urlObject.toString();
    } catch (error) {
      return "";
    }
  }
  function slugify(value) {
    return cleanValue(value)
      .toLowerCase()
      .replace(/&/g, " and ")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/-{2,}/g, "-")
      .replace(/^-|-$/g, "");
  }
  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
  function titleCase(value) {
    return cleanValue(value)
      .split(/[\s_-]+/)
      .filter(Boolean)
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
      .join(" ");
  }
  function formatDate(value) {
    const cleanedValue = cleanValue(value);
    if (!cleanedValue) {
      return "";
    }
    const match = cleanedValue.match(/^(\d{4})[-_](\d{2})[-_](\d{2})$/);
    if (!match) {
      return cleanedValue;
    }
    return `${match[1]}-${match[2]}-${match[3]}`;
  }
  function formatNumber(value) {
    const cleanedValue = cleanValue(value);
    if (!cleanedValue) {
      return "";
    }
    const numberValue = Number(cleanedValue);
    if (Number.isNaN(numberValue)) {
      return cleanedValue;
    }
    return numberValue.toLocaleString();
  }
  function formatLabel(value) {
    return titleCase(String(value || "").replace(/\//g, " "));
  }
  function getCategoryPageHref(record) {
    const categorySlug = slugify(record.category);
    if (!categorySlug) {
      return "";
    }
    return `/cat-${categorySlug}`;
  }
  function getSubcategoryPageHref(record) {
    const categoryHref = getCategoryPageHref(record);
    const subcategorySlug = slugify(record.subcategory);
    if (!categoryHref || !subcategorySlug) {
      return "";
    }
    return `${categoryHref}#${subcategorySlug}`;
  }
  function makeKickerDetailHtml(label, value, href) {
    const cleanedValue = cleanValue(value);
    if (!cleanedValue) {
      return "";
    }
    const formattedValue = escapeHtml(formatLabel(cleanedValue));
    if (!href) {
      return `<div class="fl-archive-kicker fl-archive-kicker-detail">${escapeHtml(label)}: ${formattedValue}</div>`;
    }
    return `<div class="fl-archive-kicker fl-archive-kicker-detail">${escapeHtml(label)}: <a class="fl-archive-kicker-link" href="${escapeHtml(href)}">${formattedValue}</a></div>`;
  }
  function getGoogleLabel(record) {
    const sourceType = cleanValue(record["source-file-type"]).toLowerCase();
    const labelMap = {
      gdoc: "Open Google Doc",
      gsheet: "Open Google Sheet",
      gslide: "Open Google Slides"
    };
    return labelMap[sourceType] || "Open Google File";
  }
  function getOriginalDownloadLabel(record) {
    const originalType = cleanValue(record["xfile-type"] || record["source-file-type"]).toUpperCase();
    if (!originalType) {
      return "Download Original File";
    }
    return `Download Original ${originalType}`;
  }
  function getMarkdownFilename(record) {
    const sourceFileName = cleanValue(record["source-file-name"]);
    if (sourceFileName) {
      return sourceFileName.replace(/\.[^.]+$/, ".md");
    }
    const markdownUrl = cleanValue(record["github-markdown-download-url"]);
    if (!markdownUrl) {
      return `${record.slug || "archive-file"}.md`;
    }
    try {
      const urlObject = new URL(markdownUrl);
      const fileName = decodeURIComponent(urlObject.pathname.split("/").pop() || "");
      return fileName || `${record.slug || "archive-file"}.md`;
    } catch (error) {
      return `${record.slug || "archive-file"}.md`;
    }
  }
  function makeActionCard(action, variant) {
    const attributes = [
      `class="w-button fl-archive-action-button fl-archive-action-button-${variant}"`,
      `href="${escapeHtml(action.url)}"`
    ];
    if (action.downloadUrl) {
      attributes.push(`data-download-url="${escapeHtml(action.downloadUrl)}"`);
      attributes.push(`data-download-filename="${escapeHtml(action.downloadFilename || "")}"`);
    } else {
      attributes.push(`target="_blank"`);
      attributes.push(`rel="noopener noreferrer"`);
    }
    return [
      `<a ${attributes.join(" ")}>`,
      `<span class="fl-archive-action-title">${escapeHtml(action.title)}</span>`,
      `</a>`
    ].join("");
  }
  function makeInlineLink(action) {
    const attributes = [
      `class="fl-archive-inline-link"`,
      `href="${escapeHtml(action.url)}"`
    ];
    if (action.downloadUrl) {
      attributes.push(`data-download-url="${escapeHtml(action.downloadUrl)}"`);
      attributes.push(`data-download-filename="${escapeHtml(action.downloadFilename || "")}"`);
    } else {
      attributes.push(`target="_blank"`);
      attributes.push(`rel="noopener noreferrer"`);
    }
    return [
      `<a ${attributes.join(" ")}>`,
      `<span class="fl-archive-inline-link-label">${escapeHtml(action.title)}</span>`,
      `</a>`
    ].join("");
  }
  function buildPrimaryActions(record) {
    const actions = [
      {
        url: record["gfile-url"],
        title: getGoogleLabel(record)
      },
      {
        url: record["github-markdown-url"],
        title: "Open Markdown on GitHub"
      },
      {
        url: record["xfile-github-download-url"],
        title: getOriginalDownloadLabel(record)
      }
    ];
    return actions.filter((action) => action.url);
  }
  function buildSecondaryActions(record) {
    const actions = [
      {
        url: record["github-markdown-download-url"],
        title: "Download Markdown",
        downloadUrl: record["github-markdown-download-url"],
        downloadFilename: getMarkdownFilename(record)
      },
      {
        url: record["pdf-github-url"],
        title: "Open PDF on GitHub"
      },
      {
        url: record["pdf-gdrive-url"],
        title: "Open PDF in Google Drive"
      },
      {
        url: record["web-pdf-url"],
        title: "Open Website PDF"
      },
      {
        url: record["web-slides-url"],
        title: "Open Website Slides"
      },
      {
        url: record["web-url"],
        title: "Open Web Version"
      },
      {
        url: record["youtube-url"],
        title: "Open YouTube"
      }
    ];
    return actions.filter((action) => action.url);
  }
  function buildMetadataRows(record) {
    const rows = [
      { label: "File date", value: formatDate(record["file-date"]) },
      { label: "Source type", value: cleanValue(record["source-file-type"]) },
      { label: "Original file type", value: formatLabel(record["xfile-type"]) },
      { label: "License", value: cleanValue(record.license) },
      { label: "Words", value: formatNumber(record.words) },
      { label: "Tokens", value: formatNumber(record.tokens) },
      { label: "Source file name", value: cleanValue(record["source-file-name"]) },
      { label: "Archive path", value: cleanValue(record["source-rel-path"]) },
      { label: "Archive item type", value: cleanValue(record["archive-item-type"]) },
      { label: "Archive scope", value: cleanValue(record["archive-scope"]) },
      { label: "Notes", value: cleanValue(record.notes) }
    ];
    return rows.filter((row) => row.value);
  }
  function renderTemplate(root, record) {
    const primaryActions = buildPrimaryActions(record);
    const secondaryActions = buildSecondaryActions(record);
    const metadataRows = buildMetadataRows(record);
    const summaryShort = cleanValue(record["summary-short"]);
    const isPrimaryItem = cleanValue(record["archive-item-type"]).toLowerCase() === "primary";
    const summaryHtml = summaryShort
      ? `<p class="fl-archive-paragraph fl-archive-summary">${escapeHtml(summaryShort)}</p>`
      : `<p class="fl-archive-paragraph fl-archive-summary fl-archive-summary-empty">Summary not available yet for this archive item.</p>`;
    const statusHtml = isPrimaryItem
      ? ""
      : `<div class="fl-archive-beta-note">This first template version is tuned for primary archive files. This item is still rendered, but some links or metadata groupings may need a later pass.</div>`;
    const primaryActionsHtml = primaryActions.length
      ? primaryActions.map((action) => makeActionCard(action, "default")).join("")
      : `<div class="fl-archive-paragraph fl-archive-empty-block">Primary access links are not available on this item yet.</div>`;
    const secondaryActionsHtml = secondaryActions.length
      ? [
          `<section class="fl-archive-section">`,
          `<div class="title-section-3 fl-archive-section-header">`,
          `<h2 class="sub-page-titles sub-page-sub-headings fl-archive-section-title">Other Access Options</h2>`,
          `</div>`,
          `<div class="fl-archive-inline-links">${secondaryActions.map(makeInlineLink).join("")}</div>`,
          `</section>`
        ].join("")
      : "";
    const metadataHtml = metadataRows.length
      ? [
          `<section class="fl-archive-section">`,
          `<div class="title-section-3 fl-archive-section-header">`,
          `<h2 class="sub-page-titles sub-page-sub-headings fl-archive-section-title">Archive File Metadata</h2>`,
          `</div>`,
          `<dl class="fl-archive-metadata">${metadataRows.map((row) => `<div class="fl-archive-metadata-row"><dt>${escapeHtml(row.label)}</dt><dd>${escapeHtml(row.value)}</dd></div>`).join("")}</dl>`,
          `</section>`
        ].join("")
      : "";
    root.innerHTML = [
      `<section class="hero-stack-3 fl-archive-shell-section">`,
      `<div class="small-container-5 fl-archive-shell">`,
      `<div class="title-section-3 fl-archive-hero">`,
      `<div class="section-title-3 fl-archive-hero-copy">`,
      `<div class="fl-archive-kicker-row">`,
      `<div class="fl-archive-kicker">FloodLAMP archive file</div>`,
      makeKickerDetailHtml("Category", record.category, getCategoryPageHref(record)),
      makeKickerDetailHtml("Subcategory", record.subcategory, getSubcategoryPageHref(record)),
      `</div>`,
      `<h1 class="heading fl-archive-title">${escapeHtml(record.title)}</h1>`,
      summaryHtml,
      statusHtml,
      `<section class="fl-archive-section fl-archive-section-actions">`,
      `<div class="title-section-3 fl-archive-section-header">`,
      `<h2 class="sub-page-titles sub-page-sub-headings fl-archive-section-title">Open Or Download</h2>`,
      `</div>`,
      `<div class="fl-archive-actions-grid">${primaryActionsHtml}</div>`,
      `</section>`,
      `</div>`,
      secondaryActionsHtml,
      metadataHtml,
      `</div>`,
      `</section>`
    ].join("");
  }
  function attachDownloadHandlers(root) {
    const downloadLinks = root.querySelectorAll("[data-download-url]");
    downloadLinks.forEach((link) => {
      link.addEventListener("click", async (event) => {
        event.preventDefault();
        const downloadUrl = cleanValue(link.getAttribute("data-download-url"));
        const downloadFilename = cleanValue(link.getAttribute("data-download-filename")) || "download";
        if (!downloadUrl) {
          return;
        }
        try {
          const response = await fetch(downloadUrl);
          if (!response.ok) {
            throw new Error(`Download failed with status ${response.status}`);
          }
          const blob = await response.blob();
          const objectUrl = window.URL.createObjectURL(blob);
          const temporaryLink = document.createElement("a");
          temporaryLink.href = objectUrl;
          temporaryLink.download = downloadFilename;
          document.body.appendChild(temporaryLink);
          temporaryLink.click();
          temporaryLink.remove();
          window.URL.revokeObjectURL(objectUrl);
        } catch (error) {
          console.error("FloodLAMP markdown download failed:", error);
          window.open(downloadUrl, "_blank", "noopener,noreferrer");
        }
      });
    });
  }
  function badgeHtml(value, label) {
    const cleanedValue = cleanValue(value);
    if (!cleanedValue) {
      return "";
    }
    return `<span class="fl-archive-badge" title="${escapeHtml(label)}">${escapeHtml(formatLabel(cleanedValue).toLowerCase())}</span>`;
  }
  function renderState(root, message) {
    root.innerHTML = [
      `<section class="hero-stack-3 fl-archive-shell-section">`,
      `<div class="small-container-5 fl-archive-shell">`,
      `<div class="fl-archive-paragraph fl-archive-state">${escapeHtml(message)}</div>`,
      `</div>`,
      `</section>`
    ].join("");
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
    return;
  }
  init();
})();

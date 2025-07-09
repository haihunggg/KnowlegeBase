---
hide:
  - toc
---

<!-- Style -->
<style>
  :root {
    --bg-table: #ffffff;
    --text-color: #1a1a1a;
    --bg-header: #4b52c1;
    --bg-row-alt: #f9f9f9;
    --bg-hover: #eef3ff;
    --border-color: #ccc;
    --highlight-color: #ffff99;
    --filter-bg: #fff;
    --spinner-color: #4b52c1;
  }

  html[data-theme='dark'] {
    --bg-table: #1e1e1e;
    --text-color: #f0f0f0;
    --bg-header: #4b52c1;
    --bg-row-alt: #2a2a2a;
    --bg-hover: #313a54;
    --border-color: #444;
    --highlight-color: #ffd700;
    --filter-bg: #2a2a2a;
    --spinner-color: #c2c6ff;
  }

  #sheet-table-container {
    width: 100%;
    overflow-x: auto;
    max-width: 100%;
    padding: 16px;
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 16px;
    color: var(--text-color);
  }

  #sheet-table-container table {
    min-width: 900px;
    width: fit-content;
    display: block;
    border-collapse: collapse;
    background: var(--bg-table);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }

  th, td {
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
    word-break: break-word;
    white-space: normal;
    color: var(--text-color);
  }

  th {
    background-color: var(--bg-header);
    color: #fff;
    font-weight: 600;
    position: sticky;
    top: 0;
    z-index: 2;
    font-size: 15px;
  }

  tr:nth-child(even) td {
    background-color: var(--bg-row-alt);
  }

  tr:hover td {
    background-color: var(--bg-hover);
  }

  .filter-row input,
  .filter-row select {
    width: 100%;
    padding: 8px;
    font-size: 14px;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    background-color: var(--filter-bg);
    color: var(--text-color);
  }

  .highlight {
    background-color: var(--highlight-color);
    font-weight: bold;
  }

  /* Spinner */
  #loading-spinner {
    display: none;
    margin: 40px auto;
    width: 48px;
    height: 48px;
    border: 6px solid rgba(0,0,0,0.1);
    border-top: 6px solid var(--spinner-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .loading-message {
    text-align: center;
    font-style: italic;
    color: var(--text-color);
    margin-top: 10px;
  }

  .export-buttons {
    margin: 16px 0;
    text-align: left;
  }

  .export-buttons input {
    padding: 8px 12px;
    font-size: 14px;
    width: 60%;
    max-width: 400px;
    margin-right: 10px;
  }
</style>

<!-- Spinner -->
<div id="loading-spinner"></div>
<div class="loading-message" id="loading-text">Đang tải dữ liệu, vui lòng chờ...</div>

<!-- Tìm kiếm nâng cao -->
<div class="export-buttons">
  <input type="text" id="globalSearch" placeholder="🔍 Tìm kiếm tất cả bảng..." oninput="applyFilter()">
</div>

<!-- Bảng -->
<div id="sheet-table-container"></div>

<!-- Scripts -->
<script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>

<script>
  let rawRows = [];
  let headers = [];

  function getColumnWidth(index) {
    const widths = {
      0: '60px', 1: '150px', 2: '200px', 3: '250px',
      4: '300px', 5: '350px', 6: '180px', 7: '150px',
      8: '200px', 9: '150px'
    };
    return widths[index] || '120px';
  }

  async function loadSheetData() {
    const url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTbKF-N9-xBzwenpr5H5ZkwASlMbnhXhvsbmyugWwt7t-W9JJogi4wOP3ArE5xL_mr7reem2ZN_inU4/pub?gid=0&single=true&output=csv';

    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('loading-text').style.display = 'block';
    document.getElementById('sheet-table-container').innerHTML = '';

    try {
      const response = await fetch(url);
      const text = await response.text();
      const results = Papa.parse(text, { header: false, skipEmptyLines: true });
      rawRows = results.data;
      headers = rawRows[0];
      renderTable(rawRows);
    } catch (err) {
      document.getElementById('sheet-table-container').innerHTML = `<p style="color:red; text-align:center;">Không thể tải dữ liệu.</p>`;
    } finally {
      document.getElementById('loading-spinner').style.display = 'none';
      document.getElementById('loading-text').style.display = 'none';
    }
  }

  function renderTable(data) {
    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const trHead = document.createElement('tr');
    const trFilter = document.createElement('tr');
    trFilter.classList.add('filter-row');

    headers.forEach((header, colIndex) => {
      const th = document.createElement('th');
      th.textContent = header;
      th.style.width = getColumnWidth(colIndex);
      trHead.appendChild(th);

      const tdFilter = document.createElement('td');
      tdFilter.style.width = getColumnWidth(colIndex);

      const sampleValues = data.slice(1).map(r => r[colIndex]);
      const isNumeric = sampleValues.every(v => !isNaN(v));
      const uniqueVals = [...new Set(sampleValues.filter(v => v !== ''))];

      if (uniqueVals.length <= 10 && !isNumeric) {
        const select = document.createElement('select');
        const optAll = document.createElement('option');
        optAll.value = '';
        optAll.textContent = '-- Tất cả --';
        select.appendChild(optAll);
        uniqueVals.sort().forEach(val => {
          const opt = document.createElement('option');
          opt.value = val;
          opt.textContent = val;
          select.appendChild(opt);
        });
        select.onchange = applyFilter;
        tdFilter.appendChild(select);
      } else {
        const input = document.createElement('input');
        input.placeholder = 'Lọc...';
        input.oninput = applyFilter;
        tdFilter.appendChild(input);
      }

      trFilter.appendChild(tdFilter);
    });

    thead.appendChild(trHead);
    thead.appendChild(trFilter);
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    table.appendChild(tbody);

    const container = document.getElementById('sheet-table-container');
    container.innerHTML = '';
    container.appendChild(table);

    applyFilter();
  }

  function highlightMatch(text, keyword) {
    if (!keyword) return text;
    const pattern = new RegExp(`(${keyword})`, 'gi');
    return text.replace(pattern, `<span class="highlight">$1</span>`);
  }

  function applyFilter() {
    const table = document.querySelector('#sheet-table-container table');
    if (!table) return;

    const filters = Array.from(table.querySelectorAll('.filter-row td')).map(td => {
      const input = td.querySelector('input, select');
      return input ? input.value.trim().toLowerCase() : '';
    });

    const globalSearchValue = document.getElementById('globalSearch')?.value?.toLowerCase() ?? '';

    const tbody = table.querySelector('tbody');
    tbody.innerHTML = '';

    rawRows.slice(1).forEach(row => {
      const matchColumnFilters = row.every((cell, idx) => {
        const filterVal = filters[idx];
        if (!filterVal) return true;
        return cell.toLowerCase().includes(filterVal);
      });

      const matchGlobal = globalSearchValue
        ? row.some(cell => cell.toLowerCase().includes(globalSearchValue))
        : true;

      if (matchColumnFilters && matchGlobal) {
        const tr = document.createElement('tr');
        row.forEach((cell, idx) => {
          const td = document.createElement('td');
          td.innerHTML = highlightMatch(cell, filters[idx] || globalSearchValue);
          td.style.width = getColumnWidth(idx);
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      }
    });
  }

  function runWhenPageReady() {
    const container = document.getElementById('sheet-table-container');
    if (container && container.innerHTML.trim() === '') {
      loadSheetData();
    }
  }

  document.addEventListener("DOMContentLoaded", runWhenPageReady);
  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => {
      runWhenPageReady();
    });
  }
</script>

<div class="last-updated">Last updated on <strong>July 8, 2025</strong> by <strong>nhatth</strong></div>

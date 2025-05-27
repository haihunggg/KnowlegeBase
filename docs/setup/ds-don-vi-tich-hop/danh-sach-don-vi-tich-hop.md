---
hide:
  - toc
---

<style>
  :root {
    --bg-table: #ffffff;
    --text-color: #000000;
    --bg-header: #007acc;
    --bg-row-alt: #fafafa;
    --bg-hover: #e8f4ff;
    --border-color: #ddd;
    --highlight-color: yellow;
    --filter-bg: #fff;
  }

  html[data-theme='dark'] {
    --bg-table: #1e1e1e;
    --text-color: #eeeeee;
    --bg-header: #007acc;
    --bg-row-alt: #2a2a2a;
    --bg-hover: #2d3c4d;
    --border-color: #444;
    --highlight-color: #ffd700;
    --filter-bg: #2a2a2a;
  }

  #sheet-table-container {
    width: 100%;
    overflow-x: auto;
    padding: 16px;
    box-sizing: border-box;
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
    background-color: var(--bg-row-alt);
    color: var(--text-color);
  }

  #sheet-table-container table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
    background: var(--bg-table);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    table-layout: auto;
  }

  th,
  td {
    padding: 10px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
    vertical-align: top;
    word-break: break-word;
    color: var(--text-color);
  }

  th {
    background-color: var(--bg-header);
    color: #ffffff;
    font-weight: 600;
    position: sticky;
    top: 0;
    z-index: 2;
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
    padding: 5px;
    font-size: 0.85em;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background-color: var(--filter-bg);
    color: var(--text-color);
  }

  .highlight {
    background-color: var(--highlight-color);
    font-weight: bold;
  }
</style>

<div id="sheet-table-container">
  <p>Đang tải dữ liệu...</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>

<script>
  const hiddenCols = [2, 7, 8, 9, 10, 11];
  let rawRows = [];
  let headers = [];

  async function loadSheetData() {
    const url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQmQYH5j8ruAENtaIj8LXF_2wlYDnznZhRi0urxGWo8HBqRK4huxRICTQRl54e_wdKuGV-KfTE1-IQY/pub?output=csv';

    try {
      const response = await fetch(url);
      const text = await response.text();
      const results = Papa.parse(text, { header: false, skipEmptyLines: true });
      rawRows = results.data;
      headers = rawRows[0].filter((_, idx) => !hiddenCols.includes(idx));
      renderTable(rawRows);
    } catch (err) {
      document.getElementById('sheet-table-container').innerHTML = `<p style="color:red;">Không thể tải dữ liệu.</p>`;
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
      trHead.appendChild(th);

      const tdFilter = document.createElement('td');

      const sampleValues = data.slice(1).map(r => r.filter((_, idx) => !hiddenCols.includes(idx))[colIndex]);
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

    applyFilter(); // ban đầu render hết
  }

  function highlightMatch(text, keyword) {
    if (!keyword) return text;
    const pattern = new RegExp(`(${keyword})`, 'gi');
    return text.replace(pattern, `<span class="highlight">$1</span>`);
  }

  function applyFilter() {
    const table = document.querySelector('#sheet-table-container table');
    const filters = Array.from(table.querySelectorAll('.filter-row td')).map(td => {
      const input = td.querySelector('input, select');
      return input ? input.value.trim().toLowerCase() : '';
    });

    const tbody = table.querySelector('tbody');
    tbody.innerHTML = '';

    rawRows.slice(1).forEach(row => {
      const visibleRow = row.filter((_, idx) => !hiddenCols.includes(idx));
      const match = visibleRow.every((cell, idx) => {
        const filterVal = filters[idx];
        if (!filterVal) return true;
        return cell.toLowerCase().includes(filterVal);
      });

      if (match) {
        const tr = document.createElement('tr');
        visibleRow.forEach((cell, idx) => {
          const td = document.createElement('td');
          const keyword = filters[idx];
          td.innerHTML = highlightMatch(cell, keyword);
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      }
    });
  }

  loadSheetData();
</script>

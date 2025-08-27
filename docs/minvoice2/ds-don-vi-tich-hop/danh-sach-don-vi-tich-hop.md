---
hide:
  - toc
---

<style>
:root {
  --bg-table: #ffffff;
  --text-color: #222222;
  --bg-header-gradient: linear-gradient(90deg, #4a4fc1 0%, #6c73e6 100%);
  --bg-row-alt: #fafafa;
  --bg-hover: #eef4ff;
  --border-color: #ddd;
  --highlight-color: #ffeb3b;
  --filter-bg: #f9f9ff;
  --caption-bg: #f9f9ff;
  --caption-color: #363793;
}

html[data-theme='dark'] {
  --bg-table: #1f2127;
  --text-color: #eee;
  --bg-header-gradient: linear-gradient(90deg, #363793 0%, #4a4fc1 100%);
  --bg-row-alt: #2a2a2a;
  --bg-hover: #313a54;
  --border-color: #444;
  --highlight-color: #ffd700;
  --filter-bg: #2a2a2a;
  --caption-bg: #2a2a2a;
  --caption-color: #cfcfff;
}

#sheet-table-container {
  width: 100%;
  overflow-x: auto;
  padding: 16px;
  box-sizing: border-box;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
  color: var(--text-color);
  background-color: var(--bg-row-alt);
}

#sheet-table-container table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.8.5em;
  background: var(--bg-table);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  table-layout: auto;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

#sheet-table-container table caption {
  caption-side: top;
  text-align: center;
  font-size: 1.15em;
  font-weight: 600;
  padding: 12px 0;
  color: var(--caption-color);
  background-color: var(--caption-bg);
  border-bottom: 1px solid var(--border-color);
}

th {
  background-color: #3a3f9f; /* nền đậm, đơn giản */
  color: #ffffff;
  font-weight: 600;
  font-size: 0.92em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  position: sticky;
  top: 0;
  z-index: 5;
  border-bottom: 2px solid #2e3280; /* tạo độ phân biệt với row */
  padding: 12px 16px;
  text-align: left;
  transition: background 0.2s ease;
}

th:hover {
  background-color: #4e53d1; /* nổi bật khi hover */
  cursor: default;
}

/*
tr:nth-child(even) td {
  background-color: var(--bg-row-alt);
}
*/

tr:hover td {
  background-color: var(--bg-hover);
  transition: background 0.2s ease-in-out;
}

td {
  padding: 10px 16px;
  vertical-align: top;
  word-break: break-word;
}

.filter-row input,
.filter-row select {
  width: 100%;
  padding: 6px 8px;
  font-size: 0.85em;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background-color: var(--filter-bg);
  color: var(--text-color);
  transition: all 0.2s ease;
}

.filter-row input:focus,
.filter-row select:focus {
  border-color: #4a4fc1;
  box-shadow: 0 0 0 2px rgba(74,79,193,0.2);
  outline: none;
}

.highlight {
  background-color: var(--highlight-color);
  font-weight: bold;
}

.status {
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.75em;
  display: inline-block;
}

.status.new {
  background: #d1fadd;
  color: #0f9d58;
  border: 1px solid #81c995;
}

.status.edit {
  background: #d6e9ff;
  color: #1a73e8;
  border: 1px solid #8ab4f8;
}

a.guide-link {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 6px;
  background-color: #f1f5f9;
  color: #1a73e8;
  font-size: 0.9em;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s ease;
}

a.guide-link:hover {
  background-color: #e8f0fe;
  color: #174ea6;
}

.last-updated {
  margin-top: 14px;
  font-size: 0.8em;
  color: #777;
  text-align: right;
}

/* CSS để chữ đậm cho các cột */
.bold-column {
  font-weight: 700;
}
.status-cell span {
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.75em;
  display: inline-block; /* tạo hiệu ứng nút */
}

/* các trạng thái */
.status-golive {
  background-color: #d1fadd;
  color: #0f9d58;
  border: 1px solid #81c995;
}

.status-stopped {
  background-color: #f0f0f0;
  color: #888888;
  border: 1px solid #cccccc;
}

.status-inprogress {
  background-color: #fff4cc;
  color: #fbbc04;
  border: 1px solid #fbbc04;
}

.status-checking {
  background-color: #d6e9ff;   /* nền xanh nhạt */
  color: #1a73e8;             /* chữ xanh dương */
  border: 1px solid #8ab4f8;  /* viền xanh */
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

/**
async function getCsvUrlFromConfig() {
  const configCsvUrl = "https://docs.google.com/spreadsheets/d/1_WP9zofpMODLm1jvA2MLOi9m1Y5Vs-2JC_PEBXnCazQ/export?format=csv&gid=0";
  const response = await fetch(configCsvUrl);
  const text = await response.text();
  const results = Papa.parse(text, { header: true, skipEmptyLines: true });
  // Giả sử Key là 'csv_url'
  const csvRow = results.data.find(r => r.Key === "csv_url_tichhop");
  return csvRow ? csvRow.Value : null;
}

async function loadSheetData() {
  const url = await getCsvUrlFromConfig();
  if (!url) {
    document.getElementById('sheet-table-container').innerHTML = `<p style="color:red;">Không tìm thấy CSV URL trong config.</p>`;
    return;
  }

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

**/

  async function loadSheetData() {
    const url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQmQYH5j8ruAENtaIj8LXF_2wlYDnznZhRi0urxGWo8HBqRK4huxRICTQRl54e_wdKuGV-KfTE1-IQY/pub?gid=1990243708&single=true&output=csv';

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

  // ---- Thêm đoạn xử lý trạng thái ----
  const colName = headers[idx].toLowerCase();
if (colName.includes("trạng thái")) {
    td.classList.add("status-cell");
    const val = cell.trim();

    const span = document.createElement("span");
    span.textContent = val;

    // gán class trạng thái
    const valLower = val.toLowerCase();
    if (valLower === "đã golive") span.classList.add("status-golive");
    else if (valLower === "ngưng hợp tác") span.classList.add("status-stopped");
    else if (valLower === "đang thực hiện") span.classList.add("status-inprogress");
    else if (valLower === "đang kiểm thử") span.classList.add("status-checking"); 

    td.innerHTML = "";
    td.appendChild(span);
}



  // ---- Thêm đoạn in đậm cho tên nhà cung cấp & sản phẩm ----
  if (colName.includes("tên nhà cung cấp") || colName.includes("tên sản phẩm")) {
    td.style.fontWeight = "700";
  }

  tr.appendChild(td);
});

        tbody.appendChild(tr);
      }
    });
  }

  loadSheetData();
</script>

<div class="last-updated">Last updated on <strong>May 27, 2025</strong> by <strong>nhatth</strong></div>

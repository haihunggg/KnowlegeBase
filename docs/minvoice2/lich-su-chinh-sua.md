---
hide:
  - toc
---

<style>
  :root {
    --bg-table: #fff;
    --text-color: #222;
    --bg-header: linear-gradient(90deg, #363793, #4a4fc1); /* Gradient nhẹ */
    --bg-hover: #f9faff;
    --border-color: #eee;
    --highlight-color: #ffeb3b;
    --filter-bg: #fafafa;
  }

  body[data-md-color-scheme="slate"] {
    --bg-table: #1f2127;
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
    padding: 16px;
    box-sizing: border-box;
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
  }

  #sheet-table-container table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.8em;
    background: var(--bg-table);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04); /* shadow nhẹ */
  }

  th, td {
    padding: 10px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
    word-break: break-word;
    color: var(--text-color);
  }

  th {
    background: var(--bg-header);
    color: #fff;
    font-weight: 600;
    font-size: 0.85em;
    letter-spacing: 0.3px;
    position: sticky;
    top: 0;
    z-index: 2;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover td {
    background-color: var(--bg-hover);
    transition: background 0.2s ease-in-out;
  }

  .filter-row input,
  .filter-row select {
    width: 100%;
    padding: 6px 8px;
    font-size: 0.8em;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    background-color: var(--filter-bg);
    color: var(--text-color);
    outline: none;
    transition: border 0.2s ease, box-shadow 0.2s ease;
  }

  .filter-row input:focus,
  .filter-row select:focus {
    border-color: #363793;
    box-shadow: 0 0 0 2px rgba(54,55,147,0.15);
  }

  .filter-row input::placeholder {
    color: #aaa;
    font-style: italic;
  }

  .highlight {
    background-color: var(--highlight-color);
    padding: 0 2px;
    border-radius: 2px;
  }

  .loading {
    padding: 16px;
    font-style: italic;
    text-align: center;
    color: var(--text-color);
    font-size: 0.9em;
  }

  .last-updated {
    margin-top: 14px;
    font-size: 0.8em;
    color: #777;
    text-align: right;
  }
  #sheet-table-container table caption {
  caption-side: top;
  text-align: center;
  font-size: 1.1em;
  font-weight: 600;
  padding: 14px 10px;
  color: #363793;
  background: linear-gradient(90deg, #f9f9ff, #eef0ff);
  border-bottom: 1px solid var(--border-color);
  border-radius: 8px 8px 0 0;
  letter-spacing: 0.3px;
}

.status {
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.75em;
  display: inline-block;
}

.status.new {
  background: #d1fadd;   /* xanh nền nhạt hơn */
  color: #0f9d58;        /* xanh lá tươi */
  border: 1px solid #81c995;
}

.status.edit {
  background: #d6e9ff;   /* xanh nền nhạt */
  color: #1a73e8;        /* xanh dương tươi */
  border: 1px solid #8ab4f8;
}
a.guide-link {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 6px;
  background-color: #f1f5f9; /* xám nhạt */
  color: #1a73e8;           /* xanh Google */
  font-size: 0.9em;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s ease;
}

a.guide-link:hover {
  background-color: #e8f0fe; /* xanh nhạt khi hover */
  color: #174ea6;           
}

</style>

<div id="sheet-table-container">
  <p class="loading">⏳ Đang tải dữ liệu Release Notes...</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>

<script>
  const hiddenCols = [1];
  let rawRows = [];
  let headers = [];

  async function loadSheetData() {
const url = "https://script.google.com/macros/s/AKfycbxSE-C-fcy66BwR6AEm3hsjJO70h9zAraVk_SRPHv9aKnpWfrwvs-DzUbb-FYT-ffeXKQ/exec?ts=" + Date.now();

    try {
      const response = await fetch(url);
      const text = await response.text();
      const results = Papa.parse(text, { header: false, skipEmptyLines: true });
      rawRows = results.data;

      if (!rawRows.length) throw new Error("Không có dữ liệu");

      headers = rawRows[0].filter((_, idx) => !hiddenCols.includes(idx));
      renderTable(rawRows);
    } catch (err) {
      document.getElementById('sheet-table-container').innerHTML =
        `<p style="color:red; text-align:center;">⚠️ Không thể tải dữ liệu Release Notes.</p>`;
    }
  }

  function renderTable(data) {
    const table = document.createElement('table');
    const caption = document.createElement('caption');
    caption.textContent = "Danh sách các chỉnh sửa & cập nhật phần mềm (Release Notes Effective August 1, 2025)";
    table.appendChild(caption);

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

     if (
  uniqueVals.length > 0 && 
  uniqueVals.length <= 10 && 
  !isNumeric && 
  uniqueVals.every(v => v.length <= 30) // nếu tất cả giá trị <= 30 ký tự
) {
  // Nếu ít giá trị và không quá dài thì dùng combobox
  const select = document.createElement('select');
  const optAll = new Option("-- Tất cả --", "");
  select.appendChild(optAll);
  uniqueVals.sort().forEach(val => select.appendChild(new Option(val, val)));
  select.onchange = applyFilter;
  tdFilter.appendChild(select);
} else {
  // Nếu nhiều giá trị hoặc chuỗi dài thì dùng textbox
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
    document.getElementById('sheet-table-container').innerHTML = '';
    document.getElementById('sheet-table-container').appendChild(table);

    applyFilter();
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
      const headerText = headers[idx].toLowerCase();
      const cellVal = cell.trim();

      // Nếu đây là cột "Tiêu đề hướng dẫn"
   if (headerText.includes("tiêu đề hướng dẫn")) {
  const linkVal = row[1] ? row[1].trim() : ""; // cột Link ở index 1
  if (linkVal.startsWith("http")) {
    td.innerHTML = `<a href="${linkVal}" target="_blank" rel="noopener" 
                      style="text-decoration: underline; color: blue;"
                      class="guide-link" 
                      title="Bấm vào để xem hướng dẫn">${cellVal}</a>`;
  } else {
    td.textContent = cellVal;
  }
}
      // Nếu là cột "Tạo mới / Chỉnh sửa"
      else if (headerText.includes("tạo mới") || headerText.includes("chỉnh sửa")) {
        if (cellVal.toLowerCase().includes("tạo mới")) {
          td.innerHTML = `<span class="status new">${cellVal}</span>`;
        } else if (cellVal.toLowerCase().includes("chỉnh sửa")) {
          td.innerHTML = `<span class="status edit">${cellVal}</span>`;
        } else {
          td.textContent = cellVal;
        }
      }
      // Còn lại highlight bình thường
      else {
        td.innerHTML = highlightMatch(cellVal, keyword);
      }

      tr.appendChild(td);
    });

    tbody.appendChild(tr);
  }
});

  }

  loadSheetData();

</script>

<div class="last-updated">📅 Last updated on <strong>Aug 21, 2025</strong> — 👤 <strong>NHATTH</strong></div>

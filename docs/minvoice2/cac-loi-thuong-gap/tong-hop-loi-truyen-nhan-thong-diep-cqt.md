---
hide:
  - toc
---

**Chi tiết các bước hướng dẫn khắc phục các lỗi truyền nhận từ CQT**

??? info "Cách để xem mã lỗi và mô tả lỗi ở phiên bản 1.0 - Bấm vào đấy để xem"

    **Bước 1: Bấm vào chữ đã gửi màu đỏ ở hóa đơn để kiểm tra**

    ![Hình 1](../../assets/images/invoice2/cac-loi-thuong-gap/loi-truyen-nhan-cqt-v1-1.png "Hãy bấm vào để xem rõ hơn")

    **Bước 2: Đọc mô tả lỗi, mã lỗi**

    ![Hình 1](../../assets/images/invoice2/cac-loi-thuong-gap/loi-truyen-nhan-cqt-v1-2.png "Hãy bấm vào để xem rõ hơn")

    <span style="color:red;"><strong>1: Mã lỗi</strong></span>

    <span style="color:red;"><strong>2: Mô tả lỗi</strong></span>

    **Bước 3: Tra cứu lỗi + hướng xử lý ở dưới đây**

???+ info "Cách để xem mã lỗi và mô tả lỗi ở phiên bản 2.0"

    **Bước 1: Bấm vào chữ có lỗi màu đỏ ở hóa đơn bị lỗi**

    ![Hình 1](../../assets/images/invoice2/cac-loi-thuong-gap/loi-truyen-nhan-cqt-1.png "Hãy bấm vào để xem rõ hơn")

    **Bước 2: Đọc mô tả lỗi, mã lỗi**

    ![Hình 1](../../assets/images/invoice2/cac-loi-thuong-gap/loi-truyen-nhan-cqt-2.png "Hãy bấm vào để xem rõ hơn")

    <span style="color:red;"><strong>1: Mã lỗi</strong></span>

    <span style="color:red;"><strong>2: Mô tả lỗi</strong></span>

**Bước 3: Tra cứu lỗi + hướng xử lý ở dưới đây**

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
  th:nth-child(1),
  td:nth-child(1),
    th:nth-child(3),
  td:nth-child(3),
      th:nth-child(5),
  td:nth-child(5),
  th:nth-child(6),
  td:nth-child(6) {
    display: none;
  }

.custom-tooltip-trigger {
  position: relative;
  color: red;
  text-decoration: underline;
  cursor: pointer;
  display: inline-block;
  max-width: 100%;
}

.custom-tooltip-text {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  top: 50%;
  right: 100%; /* 👈 đưa tooltip sang trái hoàn toàn */
  transform: translateY(-50%); /* 👈 căn giữa theo chiều dọc */
  margin-right: 12px; /* 👈 khoảng cách giữa tooltip và chữ “Lưu ý” */
  min-width: 250px;
  max-width: 400px;
  background-color: #333;
  color: #fff;
  text-align: left;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 14px;
  line-height: 1.4;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  transition: opacity 0.3s ease;
  word-break: break-word;
  white-space: normal;
  overflow-wrap: break-word;
  box-sizing: border-box;
  z-index: 999;
}

.custom-tooltip-trigger:hover .custom-tooltip-text {
  visibility: visible;
  opacity: 1;
}


.toggle-button {
    background: none;
    border: none;
    color: #007bff;
    cursor: pointer;
    padding: 0;
    margin-left: 5px;
    font-size: 0.85em;
  }

  .toggle-button:hover {
    text-decoration: underline;
  }

  .truncated-text, .full-text {
  
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
      0: '60px', 1: '150px', 2: '200px', 3: '210px',
      4: '300px', 5: '350px', 6: '210px', 7: '250px',
      8: '200px', 9: '25px'
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

  const styledColumns = [0, 1, 2, 3, 4, 5]; // Áp dụng định dạng đặc biệt cho các cột này

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

        if (headers[idx].toLowerCase().includes("lưu ý")) {
          if (cell.trim() !== "") {
            const safeText = cell
              .replace(/&/g, "&amp;")
              .replace(/</g, "&lt;")
              .replace(/>/g, "&gt;")
              .replace(/"/g, "&quot;")
              .replace(/'/g, "&#39;");
            td.innerHTML = `
              <span class="custom-tooltip-trigger">Lưu ý
                <span class="custom-tooltip-text">${safeText}</span>
              </span>
            `;
          } else {
            td.innerHTML = "";
          }
        } else {
          // Xử lý định dạng các cột được chọn
          let formatted = cell;

          if (styledColumns.includes(idx)) {
            let parts = cell.split(' - ');
            if (parts.length >= 2 && !isNaN(parts[0].trim())) {
              const numberPart = `<span style="color:red">${parts[0].trim()}</span>`;
              const textPart = `<strong>${parts.slice(1).join(' - ').trim()}</strong>`;
              formatted = `${numberPart} - ${textPart}`;
            } else {
              formatted = `<strong>${cell}</strong>`;
            }
          }

// Nếu là cột "Cách kiểm tra phát hiện lỗi" thì tự động xuống dòng theo số
if (headers[idx].toLowerCase().includes("cách kiểm tra") && cell.trim() !== "") {
  formatted = cell.replace(/(\d+)\./g, '<br>$1.').trim();
  // Xoá <br> đầu nếu có
  formatted = formatted.replace(/^<br>/, '');
}

      const plainText = cell.trim();

if (plainText.length > 109) {
  let shortPart = plainText.slice(0, 109);
  let fullPart = plainText;

  // Nếu là cột "cách kiểm tra", thêm <br> xuống dòng
  const isCheckColumn = headers[idx].toLowerCase().includes("cách kiểm tra");
  if (isCheckColumn) {
    shortPart = shortPart.replace(/(\d+)\./g, '<br>$1.').replace(/^<br>/, '');
    fullPart = fullPart.replace(/(\d+)\./g, '<br>$1.').replace(/^<br>/, '');
  }

  // Highlight
  const highlightedShort = highlightMatch(shortPart, filters[idx] || globalSearchValue);
  const highlightedFull = highlightMatch(fullPart, filters[idx] || globalSearchValue);

  let formattedShort = highlightedShort;
  let formattedFull = highlightedFull;

  // Áp dụng định dạng đặc biệt nếu là cột cần thiết
  if (styledColumns.includes(idx)) {
    let partsShort = shortPart.replace(/<br>/g, '').split(' - ');
    let partsFull = fullPart.replace(/<br>/g, '').split(' - ');

    if (partsShort.length >= 2 && !isNaN(partsShort[0].trim())) {
      formattedShort = `<span style="color:red">${partsShort[0].trim()}</span> - <strong>${partsShort.slice(1).join(' - ').trim()}</strong>`;
    }

    if (partsFull.length >= 2 && !isNaN(partsFull[0].trim())) {
      formattedFull = `<span style="color:red">${partsFull[0].trim()}</span> - <strong>${partsFull.slice(1).join(' - ').trim()}</strong>`;
    }
  }

  td.innerHTML = `
    <span class="truncated-text">${formattedShort}...</span>
    <span class="full-text" style="display:none;">${formattedFull}</span>
    <button class="toggle-button" onclick="toggleText(this)">Xem thêm</button>
  `;
} else {
  let finalFormatted = cell;

  if (styledColumns.includes(idx)) {
    let parts = cell.split(' - ');
    if (parts.length >= 2 && !isNaN(parts[0].trim())) {
      finalFormatted = `<span style="color:red">${parts[0].trim()}</span> - <strong>${parts.slice(1).join(' - ').trim()}</strong>`;
    } else {
      finalFormatted = `<strong>${cell}</strong>`;
    }
  }

  // Nếu là cột cách kiểm tra, xử lý xuống dòng
  if (headers[idx].toLowerCase().includes("cách kiểm tra") && cell.trim() !== "") {
    finalFormatted = cell.replace(/(\d+)\./g, '<br>$1.').replace(/^<br>/, '');
  }

  td.innerHTML = highlightMatch(finalFormatted, filters[idx] || globalSearchValue);
}


        }

        td.style.width = getColumnWidth(idx);
        tr.appendChild(td);
      });

      tbody.appendChild(tr);
    }
  });
}

function toggleText(button) {
  const td = button.parentElement;
  const truncated = td.querySelector('.truncated-text');
  const full = td.querySelector('.full-text');

  const isExpanded = full.style.display === 'inline';

  if (isExpanded) {
    full.style.display = 'none';
    truncated.style.display = 'inline';
    button.textContent = 'Xem thêm';
  } else {
    full.style.display = 'inline';
    truncated.style.display = 'none';
    button.textContent = 'Thu gọn';
  }
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

<div class="last-updated">Last updated on <strong>Aug 6, 2025</strong> by <strong>NHATTH</strong></div>

---
hide:
  - toc
---

<style>
  #sheet-table-container {
    width: 100vw;
    overflow-x: auto;
    padding: 12px;
    box-sizing: border-box;
    font-family: "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  #sheet-table-container table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.8em;
    background: white;
    border: 1px solid #ddd;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0.04);
  }

  #sheet-table-container th,
  #sheet-table-container td {
    padding: 6px 10px; /* ↓ nhỏ lại so với trước */
    text-align: left;
    border-bottom: 1px solid #eee;
  }

  #sheet-table-container th {
    background-color: #007acc;
    color: white;
    font-weight: 600;
  }

  #sheet-table-container tr:nth-child(even) td {
    background-color: #f9f9f9;
  }

  #sheet-table-container tr:hover td {
    background-color: #f1f8ff;
  }

  #sheet-table-container td:first-child:not(:has(th)) {
    font-weight: bold;
    color: #333;
  }
</style>

<div id="sheet-table-container">
  <p>Đang tải dữ liệu...</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>

<script>
  async function loadSheetData() {
    const url =
      'https://docs.google.com/spreadsheets/d/e/2PACX-1vQmQYH5j8ruAENtaIj8LXF_2wlYDnznZhRi0urxGWo8HBqRK4huxRICTQRl54e_wdKuGV-KfTE1-IQY/pub?output=csv';
    const hiddenCols = [2, 4, 7, 8, 9, 10, 11];

    try {
      const response = await fetch(url);
      const text = await response.text();
      const results = Papa.parse(text, {
        header: false,
        skipEmptyLines: true
      });
      const rows = results.data;

      const table = document.createElement('table');

      rows.forEach((row, rowIndex) => {
        const tr = document.createElement('tr');
        row.forEach((cell, colIndex) => {
          if (hiddenCols.includes(colIndex)) return;

          const isHeader = rowIndex === 0;
          const cellElement = document.createElement(isHeader ? 'th' : 'td');
          cellElement.textContent = cell;

          // In đậm cột đầu tiên nếu không phải tiêu đề
          if (!isHeader && colIndex === 0) {
            cellElement.style.fontWeight = 'bold';
            cellElement.style.color = '#333';
          }

          tr.appendChild(cellElement);
        });
        table.appendChild(tr);
      });

      const container = document.getElementById('sheet-table-container');
      container.innerHTML = '';
      container.appendChild(table);
    } catch (err) {
      document.getElementById('sheet-table-container').innerHTML =
        `<p style="color:red;">Không thể tải dữ liệu.</p>`;
      console.error('Lỗi tải sheet:', err);
    }
  }

  loadSheetData();
</script>

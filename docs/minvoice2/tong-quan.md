# Sections

#### Sections

<div class="card-grid">

<a class="card" href="../../minvoice2/huong-dan/plugin/">
  <div class="card-icon" style="
  width: 58px;
  height: 58px;
  background-image: url('../../assets/icons/plugin_v2.ico');
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  border-radius: 8px;"></div>
  <div>
    <h2 class="card-title">Plugin ký</h2>
    <p class="card-desc">Tải xuống công cụ hỗ trợ ký số USB và in hóa đơn hàng loạt từ M-Invoice.</p>
  </div>
  <div class="card-overlay">
    <button class="icon-btn"
      title="Xem hướng dẫn">
      <svg xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px" fill="#363793"><path d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>
    </button>
   <button class="icon-btn" style="margin-left: 8px;" onclick="downloadFile()" title="Tải xuống">
  <svg xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px" fill="#363793">
    <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"/>
  </svg>
</button>

<script>
function downloadFile() {
  const link = document.createElement('a');
  link.href = "https://plugin.minvoice.com.vn/MinvoicePlugin_NewApp/setup.exe";
  link.download = "setup.exe"; // gợi ý tên file
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
</script>
  </div>
</a>

<a class="card" href="../../minvoice2/huong-dan/dang-nhap">
  <div class="card-icon" style="mask-image: url('../../assets/icons/huong-dan-su-dung.svg');"></div>
  <div>
    <h2 class="card-title">Hướng dẫn sử dụng</h2>
    <p class="card-desc">Hướng dẫn thao tác lần đầu các chức năng chính của hóa đơn điện tử.</p>
  </div>
  <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>
</a>

<a class="card" href="../../minvoice2/huong-dan/in-hang-loat">
  <div class="card-icon" style="mask-image: url('../../assets/icons/chung-nang-hay-su-dung.svg');"></div>
  <div>
    <h2 class="card-title">Chức năng hay sử dụng</h2>
    <p class="card-desc">Hướng dẫn chi tiết các chức năng như (Tải PDF XML hàng loạt, nhập excel, chỉnh số thập phân, ...)</p>
  </div>
   <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>

</a>

<a class="card" href="../../minvoice2/cac-cau-hoi-thuong-gap/cau-hoi-thuong-gap-ve-hoa-don-dien-tu/">
  <div class="card-icon" style="mask-image: url('../../assets/icons/cac-loi-thuong-gap.svg');"></div>
  <div>
    <h2 class="card-title">Câu hỏi & lỗi thường gặp khi dùng phần mềm</h2>
    <p class="card-desc">Tổng hợp các câu hỏi và lỗi phổ biến khi sử dụng hóa đơn điện tử, kèm cách xử lý nhanh chóng.</p>
  </div>
  <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>

</a>

<a class="card" href="../../minvoice2/xu-ly-sai-sot/thay-the-hoa-don/">
  <div class="card-icon" style="mask-image: url('../../assets/icons/nghiep-vu-sai-sot.svg');"></div>
  <div>
    <h2 class="card-title">Nghiệp vụ hóa đơn điện tử - xử lý sai sót</h2>
    <p class="card-desc">Hướng dẫn xử lý các tình huống sai sót khi xuất hóa đơn.</p>
  </div>
   <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>

</a>

<a class="card" href="../../minvoice2/xang-dau/huong-dan-xang-dau/">
  <div class="card-icon" style="mask-image: url('../../assets/icons/xang-dau.svg');"></div>
  <div>
    <h2 class="card-title">Xăng dầu</h2>
    <p class="card-desc">Hướng dẫn lập hóa đơn điện tử trong lĩnh vực kinh doanh xăng dầu theo đúng quy định.</p>
  </div>
  <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>

</a>

<a class="card" href="../../minvoice2/danh-muc-bao-cao/bao-cao-tong-hop/">
  <div class="card-icon" style="mask-image: url('../../assets/icons/bao-cao.svg');"></div>
  <div>
    <h2 class="card-title">Danh mục báo cáo</h2>
    <p class="card-desc">Giới thiệu các loại báo cáo liên quan đến hóa đơn, tra cứu, và quản lý dữ liệu.</p>
  </div>
  <div class="card-overlay"><button><i class="fa fa-eye"></i> Xem chi tiết</button></div>

</a>

</div>

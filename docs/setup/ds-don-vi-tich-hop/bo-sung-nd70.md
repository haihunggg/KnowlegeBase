## **Thông tin và các trường bổ sung theo NGHỊ ĐỊNH 70/2025/NĐ-CP (áp dụng từ ngày 01/06/2025)**

???+ Danger "📢 THÔNG BÁO VỀ VIỆC BỎ PHƯƠNG THỨC HỦY HÓA ĐƠN THEO NGHỊ ĐỊNH 70/2025/NĐ-CP"

    Căn cứ theo quy định mới tại Nghị định số 70/2025/NĐ-CP sửa đổi, bổ sung Nghị định 123/2020/NĐ-CP về hóa đơn, chúng tôi xin thông báo:

    🔸 Từ thời điểm Nghị định có hiệu lực, phương thức "HUỶ HOÁ ĐƠN” chính thức bị bãi bỏ. Việc xử lý sai sót về hóa đơn sẽ được thực hiện thông qua hình thức “ĐIỀU CHỈNH” (API `api/InvoiceApi78/DieuChinh`) hoặc “THAY THẾ” (API `api/InvoiceApi78/ThayThe`) hóa đơn theo đúng quy định hiện hành.

    🔸 Đồng thời, phương thức gọi API hủy hóa đơn (API `/api/InvoiceApi78/HuyHoaDon`) cũng sẽ bị ngưng sử dụng. Đối với các hệ thống tích hợp, Quý đối tác vui lòng cập nhật để tránh gặp gián đoạn trong quá trình xử lý nghiệp vụ.

???+ Info "Bổ sung loại hóa đơn"

    Bổ sung 2 loại hóa đơn:

    <span style="color:red">Hóa đơn bán tài sản công</span>

    <span style="color:red">Hóa đơn bán hàng dự trữ quốc gia</span>

??? Info "Bổ sung thông tin người bán và người mua"

    Người bán

    <table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%;">
    <thead>
    <tr>
      <th style="width: 150px; text-align: left;">Tên trường</th>
      <th style="text-align: left;">Kiểu dữ liệu</th>
      <th style="text-align: left;">Độ dài</th>
      <th style="text-align: left;">Bắt buộc</th>
      <th style="width: 200px; text-align: left;">Ghi chú</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><code>ma_ch</code></td>
      <td>string</td>
      <td>250</td>
      <td></td>
      <td>Mã cửa hàng</td>
    </tr>
    <tr>
      <td><code>ten_ch</code></td>
      <td>string</td>
      <td>250</td>
      <td></td>
      <td>Tên cửa hàng</td>
    </tr>
    <tr>
      <td><code>dchicuahang</code></td>
      <td>string</td>
      <td>250</td>
      <td></td>
      <td>Địa chỉ cửa hàng</td>
    </tr>
    </tbody>
    </table>


    Người mua

    <table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%;">
    <thead>
    <tr>
      <th style="width: 170px; text-align: left;">Tên trường</th>
      <th style="text-align: left;">Kiểu dữ liệu</th>
      <th style="text-align: left;">Độ dài</th>
      <th style="text-align: left;">Bắt buộc</th>
      <th style="width: 200px; text-align: left;">Ghi chú</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><code>mdvqhnsach_nmua</code></td>
      <td>string</td>
      <td>7</td>
      <td>Bắt buộc</td>
      <td>Mã đơn vị Quan hệ Ngân sách (Theo Khoản 7 điều 1 NĐ 70)</td>
    </tr>
    <tr>
      <td><code>so_hchieu</code></td>
      <td>string</td>
      <td>20</td>
      <td></td>
      <td>Số hộ chiếu người mua</td>
    </tr>
    <tr>
      <td><code>cccdan</code></td>
      <td>string</td>
      <td>20</td>
      <td></td>
      <td>Căn cước công dân người mua</td>
    </tr>
    <tr>
      <td><code>socialDeductionAmount</code></td>
      <td>decimal</td>
      <td>21,6</td>
      <td></td>
      <td>Phí vận chuyển <em>(Liên hệ Kỹ thuật để cấu hình thêm)</em></td>
    </tr>
    <tr>
      <td><code>ratioOrtherTax</code></td>
      <td>decimal</td>
      <td>21,6</td>
      <td></td>
      <td>Thuế Tiêu thụ đặc biệt <em>(Liên hệ Kỹ thuật để cấu hình)</em></td>
    </tr>
    <tr>
      <td><code>ortherFee</code></td>
      <td>decimal</td>
      <td>21,6</td>
      <td></td>
      <td>Tiền thuế Tiêu thụ đặc biệt <em>(Liên hệ Kỹ thuật để cấu hình)</em></td>
    </tr>
    </tbody>
    </table>

??? Info "Bổ sung thêm các trường thông tin (áp dụng hóa đơn bán tài sản công)"

    <table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%;">
    <thead>
    <tr>
      <th style="width: 170px; text-align: left;">Tên trường</th>
      <th style="text-align: left;">Kiểu dữ liệu</th>
      <th style="text-align: left;">Độ dài</th>
      <th style="text-align: left;">Bắt buộc</th>
      <th style="width: 200px; text-align: left;">Ghi chú</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><code>mdvqhnsach_nban</code></td>
      <td>string</td>
      <td>7</td>
      <td>Bắt buộc</td>
      <td>Mã đơn vị quan hệ ngân sách (Mã số đơn vị có quan hệ với ngân sách của đơn vị bán tài sản công)</td>
    </tr>
    <tr>
      <td><code>so_qdinh</code></td>
      <td>string</td>
      <td>50</td>
      <td></td>
      <td>Số quyết định (Số quyết định bán tài sản)</td>
    </tr>
    <tr>
      <td><code>ngay_qdinh</code></td>
      <td>date</td>
      <td>–</td>
      <td></td>
      <td>Ngày quyết định (Ngày quyết định bán tài sản)</td>
    </tr>
    <tr>
      <td><code>cqbhanh_qdinh</code></td>
      <td>string</td>
      <td>200</td>
      <td></td>
      <td>Cơ quan ban hành quyết định</td>
    </tr>
    <tr>
      <td><code>hthuc_ban</code></td>
      <td>string</td>
      <td>200</td>
      <td></td>
      <td>Hình thức bán</td>
    </tr>
    <tr>
      <td><code>dd_vchuyen</code></td>
      <td>string</td>
      <td>400</td>
      <td></td>
      <td>Địa điểm vận chuyển hàng đến</td>
    </tr>
    <tr>
      <td><code>tg_vchuyen</code></td>
      <td>date</td>
      <td>–</td>
      <td></td>
      <td>Ngày bắt đầu vận chuyển</td>
    </tr>
    <tr>
      <td><code>tg_vchuyen_den</code></td>
      <td>date</td>
      <td>–</td>
      <td></td>
      <td>Ngày vận chuyển đến</td>
    </tr>
    </tbody>
    </table>

??? Info "Bổ sung các trường thông tin đối với phần chi tiết hóa đơn"

    Bổ sung thêm tính chất `HÀNG HÓA ĐẶC TRƯNG` giá trị tính chất là `5`

    Tính chất hàng hóa đặc trưng sẽ thêm các trường sau

    <table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%;">
    <thead>
    <tr>
      <th style="width: 150px; text-align: left;">Tên trường</th>
      <th style="text-align: left;">Kiểu dữ liệu</th>
      <th style="text-align: left;">Độ dài</th>
      <th style="text-align: left;">Bắt buộc</th>
      <th style="width: 200px; text-align: left;">Ghi chú</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><code>skhung</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Số khung<br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span></td>
    </tr>
    <tr>
      <td><code>smay</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Số Máy<br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span></td>
    </tr>
    <tr>
      <td><code>bien_sxe</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Biển số xe<br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span></td>
    </tr>
    <tr>
      <td><code>ten_ngui</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Tên người gửi hàng<br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span></td>
    </tr>
    <tr>
      <td><code>dc_ngui</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Địa chỉ người gửi hàng<br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span></td>
    </tr>
    <tr>
      <td><code>mst_ngui</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>MST người gửi hàng<br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span></td>
    </tr>
    <tr>
      <td><code>sddanh_ngui</code></td>
      <td>string</td>
      <td>200</td>
      <td>Bắt buộc</td>
      <td>Căn cước công dân người gửi<br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span></td>
    </tr>
    </tbody>
    </table>

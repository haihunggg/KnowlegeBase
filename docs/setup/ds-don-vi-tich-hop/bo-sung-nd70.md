## **Thông tin và các trường bổ sung theo ND70 (áp dụng từ ngày 01/06/2025)**

???+ Danger "📢 THÔNG BÁO VỀ VIỆC BỎ PHƯƠNG THỨC HỦY HÓA ĐƠN THEO NGHỊ ĐỊNH 70/2025/NĐ-CP"

    Căn cứ theo quy định mới tại Nghị định số 70/2025/NĐ-CP sửa đổi, bổ sung Nghị định 123/2020/NĐ-CP về hóa đơn, chứng từ điện tử, chúng tôi xin thông báo:

    🔸 Từ thời điểm Nghị định có hiệu lực, phương thức “hủy hóa đơn” chính thức bị bãi bỏ. Việc xử lý sai sót về hóa đơn sẽ được thực hiện thông qua hình thức “điều chỉnh” hoặc “thay thế” hóa đơn theo đúng quy định hiện hành.

    🔸 Đồng thời, phương thức gọi API hủy hóa đơn (API `/HuyHoaDon`) cũng sẽ bị ngừng hỗ trợ. Đối với các hệ thống tích hợp, Quý khách vui lòng cập nhật lại quy trình xử lý hóa đơn để đảm bảo tuân thủ.

???+ Info "Bổ sung loại hóa đơn"

    Bổ sung 2 loại hóa đơn:

    <span style="color:red">Hóa đơn bán tài sản công</span>

    <span style="color:red">Hóa đơn bán hàng dự trữ quốc gia</span>

??? Info "Bổ sung thông tin người bán và người mua"

    Người bán

    | Tên trường              | Kiểu dữ liệu | Độ dài | Bắt buộc | Ghi chú                                                  |
    |--------------------------|--------------|--------|-----------|-----------------------------------------------------------|
    | `ma_ch`                  | string       | 250    |           | Mã cửa hàng                                              |
    | `ten_ch`                 | string       | 250    |           | Tên cửa hàng                                              |
    | `dchicuahang`            | string       | 250    |           | Địa chỉ cửa hàng                                          |


    Người mua

    | Tên trường              | Kiểu dữ liệu | Độ dài | Bắt buộc | Ghi chú                                                  |
    |--------------------------|--------------|--------|-----------|-----------------------------------------------------------|
    | `mdvqhnsach_nmua`        | string       | 7      | Bắt buộc  | Mã đơn vị Quan hệ Ngân sách (Theo Khoản 7 điều 1 NĐ 70)   |
    | `so_hchieu`              | string       | 20     |           | Số hộ chiếu người mua                                     |
    | `cccd`                   | string       | 20     |           | Căn cước công dân người mua                               |
    | `socialDeductionAmount` | decimal      | 21,6   |           | Phí vận chuyển *(Liên hệ Kỹ thuật để cấu hình thêm)*     |
    | `ratioOrtherTax`        | decimal      | 21,6   |           | Thuế Tiêu thụ đặc biệt *(Liên hệ Kỹ thuật để cấu hình)*  |
    | `ortherFee`             | decimal      | 21,6   |           | Tiền thuế Tiêu thụ đặc biệt *(Liên hệ Kỹ thuật để cấu hình)* |

??? Info "Bổ sung hóa đơn bán tài sản công"

    | Tên trường         | Kiểu dữ liệu | Độ dài | Bắt buộc | Ghi chú                                                               |
    |--------------------|--------------|--------|-----------|------------------------------------------------------------------------|
    | `mdvqhnsach_nban`  | string       | 7      | Bắt buộc  | Mã đơn vị quan hệ ngân sách (Mã số đơn vị có quan hệ với ngân sách của đơn vị bán tài sản công) |
    | `so_qdinh`         | string       | 50     |           | Số quyết định (Số quyết định bán tài sản)                             |
    | `ngay_qdinh`       | date         | –      |           | Ngày quyết định (Ngày quyết định bán tài sản)                         |
    | `cqbhanh_qdinh`    | string       | 200    |           | Cơ quan ban hành quyết định                                           |
    | `hthuc_ban`        | string       | 200    |           | Hình thức bán                                                          |
    | `dd_vchuyen`       | string       | 400    |           | Địa điểm vận chuyển hàng đến                                          |
    | `tg_vchuyen`       | date         | –      |           | Ngày bắt đầu vận chuyển                                               |
    | `tg_vchuyen_den`   | date         | –      |           | Ngày vận chuyển đến                                                   |

??? Info "Bổ sung các trường đối với phần chi tiết hóa đơn"

    Bổ sung thêm `Hàng hóa đặc trưng` giá trị tính chất là `5`

    Tính chất hàng hóa đặc trưng sẽ thêm các trường sau

    | Tên trường     | Kiểu dữ liệu | Độ dài | Bắt buộc | Ghi chú                                                                                   |
    |----------------|--------------|--------|-----------|--------------------------------------------------------------------------------------------|
    | `skhung`       | string       | 200    | Bắt buộc  | Số khung <br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span> |
    | `smay`         | string       | 200    | Bắt buộc  | Số Máy <br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span>   |
    | `bien_sxe`     | string       | 200    | Bắt buộc  | Biển số xe <br><span style="color:red">(Đối với hóa đơn đặc trưng Bán mô tô, xe mô tô)</span>|
    | `ten_ngui`     | string       | 200    | Bắt buộc  | Tên người gửi hàng <br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span> |
    | `dc_ngui`      | string       | 200    | Bắt buộc  | Địa chỉ người gửi hàng <br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span> |
    | `mst_ngui`     | string       | 200    | Bắt buộc  | MST người gửi hàng <br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span> |
    | `sddanh_ngui`  | string       | 200    | Bắt buộc  | Căn cước công dân người gửi <br><span style="color:red">(Đối với Dịch vụ vận chuyển trên nền tảng số, TMĐT)</span> |

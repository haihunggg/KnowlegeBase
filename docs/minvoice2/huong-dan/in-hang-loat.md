# **Tải hàng loạt hóa đơn PDF và XML**

Dưới đây là những hướng dẫn thao tác cơ bản trên phần mềm hóa đơn điện tử M-Invoice ở phiên bản 2.0 vô cùng mạch lạc và dễ hiểu.

<script>
function activateTabFromUrlFragment() {
  // 1. Get the fragment from the URL (e.g., #tab2-h1)
  const fragment = window.location.hash;

  if (fragment) {
    // 2. Find the element with the matching ID
    // We remove the '#' from the fragment to get the pure ID
    const targetElement = document.getElementById(fragment.substring(1));

    if (targetElement) {
      // 3. Find the parent .tabbed-block of the target element
      const parentBlock = targetElement.closest(".tabbed-block");

      // 4. Find the main container for all tab content blocks
      const contentContainer = targetElement.closest(".tabbed-content");

      if (parentBlock && contentContainer) {
        // 5. Get all tab blocks to determine the index of our target
        const allBlocks = Array.from(
          contentContainer.querySelectorAll(".tabbed-block"),
        );
        const targetIndex = allBlocks.indexOf(parentBlock);

        // 6. Navigate up to the main component container
        const mainContainer = contentContainer.parentElement;

        if (mainContainer) {
          // 7. Find all the labels for the tabs within that container
          const allLabels = mainContainer.querySelectorAll(
            ".tabbed-labels label",
          );

          if (allLabels[targetIndex]) {
            // 8. First, activate the correct tab by clicking its label
            allLabels[targetIndex].click();

            // 9. Now that the element is visible, scroll it into view
            targetElement.scrollIntoView({
              behavior: "smooth", // Use a smooth scrolling animation
              block: "start", // Align the top of the element with the top of the visible area
            });
          }
        }
      }
    }
  }
}

document.addEventListener('DOMContentLoaded', activateTabFromUrlFragment);
</script>

## **Hướng dẫn In hàng loạt PDF và XML**

Trong quá trình phát hành hóa đơn người dùng sẽ có nhu cầu in hoá đơn PDF và XML. M-invoice xin giới thiệu với khách hàng và người sử dụng tính năng in hoá đơn PDF và XML

=== "Cách 1: In nhiều hoá đơn PDF"

    #### Cách 1: In nhiều hoá đơn PDF

    ???+ Note "Ghi chú"
        In bằng cách này sẽ tách file PDF và sẽ lâu hơn cách 2

        **Cách này bạn cần phải cài plugin thì mới tải được** [Hướng dẫn cài đặt plugin](plugin.md#attribute-lists){ data-preview }

        Trường hợp không in được load lâu, quý khách hàng cần cập nhật lên plugin mới nhất (Chuột phải vào biểu tượng plugin ở ảnh trên bấn cập nhật phần mềm)

    **Bước 1: Lọc những hoá đơn muốn tải (theo quý hoặc tháng)**

    ![Hình 1](../../assets/images/invoice2/2.0_in-hang-loat_1.png "Hãy bấm vào để xem rõ hơn")

    **Bước 2: Tích chọn hoá đơn muốn tải hoặc chọn tất cả**

    ![Hình 15](../../assets/images/invoice2/2.0_in-hang-loat_7.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 2](../../assets/images/invoice2/2.0_in-hang-loat_2.png "Hãy bấm vào để xem rõ hơn")

    **Bước 3: Bấm "tải hoá đơn PDF"**

    ![Hình 3](../../assets/images/invoice2/2.0_in-hang-loat_3.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 4](../../assets/images/invoice2/2.0_in-hang-loat_7.png "Hãy bấm vào để xem rõ hơn")

=== "Cách 2: In nhiều hoá đơn PDF"

    #### Cách 2: In nhiều hoá đơn PDF

    ???+ Note "Ghi chú"
        In bằng cách này sẽ liền file PDF và sẽ nhanh hơn cách 1
    **Bước 1: Lọc những hoá đơn muốn tải (theo quý hoặc tháng)**

    ![Hình 5](../../assets/images/invoice2/2.0_in-hang-loat_1.png "Hãy bấm vào để xem rõ hơn")

    **Bước 2: Tích chọn hoá đơn muỗn tải hoặc chọn tất cả**

    ![Hình 16](../../assets/images/invoice2/2.0_in-hang-loat_7.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 6](../../assets/images/invoice2/2.0_in-hang-loat_2.png "Hãy bấm vào để xem rõ hơn")

    **Bước 3: Bấm "Xem in"**

    ![Hình 7](../../assets/images/invoice2/2.0_in-hang-loat_4.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 8](../../assets/images/invoice2/2.0_in-hang-loat_5.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 9](../../assets/images/invoice2/2.0_in-hang-loat_6.png "Hãy bấm vào để xem rõ hơn")
    Chọn A4 để khi in không bị lỗi khung

=== "In nhiều XML"

    #### In nhiều XML

    ???+ Note "Ghi chú"

        **Cách này bạn cần phải cài plugin thì mới tải được** [Hướng dẫn cài đặt plugin](plugin.md#attribute-lists){ data-preview }

        Trường hợp không in được load lâu, quý khách hàng cần cập nhật lên plugin mới nhất (Chuột phải vào biểu tượng plugin ở ảnh trên bấn cập nhật phần mềm)

    **Bước 1: Lọc những hoá đơn muốn tải (theo quý hoặc tháng)**

    ![Hình 10](../../assets/images/invoice2/2.0_in-hang-loat_1.png "Hãy bấm vào để xem rõ hơn")

    **Bước 2: Tích chọn hoá đơn muỗn tải hoặc chọn tất cả**

    ![Hình 17](../../assets/images/invoice2/2.0_in-hang-loat_7.png "Hãy bấm vào để xem rõ hơn")

    ![Hình 11](../../assets/images/invoice2/2.0_in-hang-loat_2.png "Hãy bấm vào để xem rõ hơn")

    **Bước 3: Chọn chức năng tải XML**

    ![Hình 12](../../assets/images/invoice2/2.0_in-hang-loat-xml_3.png "Hãy bấm vào để xem rõ hơn")

    **Anh chị vui lòng chờ để quá trình tải về được hoàn tất**

    ![Hình 13](../../assets/images/invoice2/2.0_plugin_7.png "Hãy bấm vào để xem rõ hơn")

???+ info "Xin chân thành cảm ơn quý khách hàng đã tin dùng sản phẩm của M-Invoice"

    Có bất kỳ vướng mắc nào trong quá trình sử dụng hãy liên hệ với M-Invoice tại mục Hỗ trợ kỹ thuật góc phải bên dưới màn hình hoặc gọi tổng đài kỹ thuật của M-Invoice (1900.955.557 Nhánh 1)

![Hình 14](../../assets/images/invoice2/hotro.png "Hãy bấm vào để xem rõ hơn")

<div class="last-updated">Last updated on <strong>Aug 9, 2025</strong> by <strong>nhatth</strong></div>

document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll("article img");

  images.forEach((img) => {
    // Bỏ qua ảnh nếu đã có title rồi (không đè lên)
    if (!img.title) {
      img.title = "Hãy bấm vào để xem rõ hơn";
    }

    // Bọc ảnh trong thẻ <a> để khi click vào mở ảnh to
    if (!img.closest("a")) {
      const link = document.createElement("a");
      link.href = img.src;
      link.target = "_blank";
      link.title = img.title;
      img.parentNode.insertBefore(link, img);
      link.appendChild(img);
    }
  });
});

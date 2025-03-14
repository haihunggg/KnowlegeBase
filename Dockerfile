FROM squidfunk/mkdocs-material

# Cài đặt các plugin bổ sung (nếu cần)
RUN pip install --no-cache-dir mkdocs-glightbox

# Đặt thư mục làm việc
WORKDIR /docs

COPY . /docs
# Mở cổng 8000
EXPOSE 8000

# Đảm bảo sử dụng đúng entrypoint
ENTRYPOINT ["mkdocs"]
CMD ["serve", "-a", "0.0.0.0:8000"]
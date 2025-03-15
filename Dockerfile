FROM python:3.10-slim

# Cài đặt các plugin bổ sung (nếu cần)
# RUN pip install --no-cache-dir mkdocs-glightbox
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Đặt thư mục làm việc
WORKDIR /docs

RUN pip install --no-cache-dir \
    mkdocs \
    mkdocs-material

#COPY ./material/overrides /docs/material/overrides
COPY . .
# Mở cổng 8000
EXPOSE 8000

# Đảm bảo sử dụng đúng entrypoint
ENTRYPOINT ["mkdocs"]
CMD ["serve", "-a", "0.0.0.0:8000"]
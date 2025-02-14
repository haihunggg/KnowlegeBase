# **Hướng dẫn hủy hóa đơn theo NĐ123**

<!-- [^1]:
    In 2016, Material for MkDocs started out as a simple theme for MkDocs, but
    over the course of several years, it's now much more than that – with the
    many built-in plugins, settings, and countless customization abilities,
    Material for MkDocs is now one of the simplest and most powerful frameworks
    for creating documentation for your project.

[MkDocs]: https://www.mkdocs.org
[pip]: #with-pip
[docker]: #with-docker -->
!!! note "Người sử dụng có thể sử dụng Nghiệp vụ này trước khi có quyết định thanh kiểm tra của CQT và chỉ được phép sử dụng nghiệp vụ Hủy hóa đơn với các điều kiện sau:"
    1, Hóa đơn cần hủy đã được gửi CQT thành công hoặc hóa đơn đã có mã CQT cấp;
    2, Hóa đơn cần hủy ở Trạng thái Gốc (Mới)

!!! warning "Lưu ý"  
        Nếu đã lựa chọn nghiệp vụ hủy thì không được điều chỉnh hoặc thay thế hóa đơn đã bị hủy.
        Nghiệp vụ này bắt buộc phải lập 04/SS

<iframe width="640" height="360" 
    src="https://www.youtube.com/embed/WSA0CrIhZFM" 
    frameborder="0" allowfullscreen>
</iframe>

### Bước 1: Kiểm tra trong phần hệ thống đã điền cơ quan thuế cấp tình và chi cục thuế quản lý hay chưa

![Hình 1](../../assets/images/invoice1/1.0_huy_1.png)

Truy cập vào phần Hệ thống >> Quản lý doanh nghiệp >> Thông tin doanh nghiệp
Nếu chưa điền bạn sẽ phải điền vào và sau đó nhấn lưu lại 

### Bước 2: Quay trở lại phần mềm, chọn hóa đơn cần hủy, chọn nghiệp vụ chọn hủy hóa đơn 

![Hình 2](../../assets/images/invoice1/1.0_huy_2.png)

### Bước 3 : Sau khi nhấn hủy phần mềm sẽ tự động sinh ra 1 form để lập mẫu 04ss

![Hình 3](../../assets/images/invoice1/1.0_huy_3.png)

Các bạn chỉ cần kiểm tra lại thông tin, sau đó điền vào phần lý do 
Khi nhập lý do xong hãy nhấn phím tab để pm lưu lại được mục lý do, sau đó nhấn Ghi(F10)

### Bước 4 : Ký gửi 04ss  thông báo sai sót đến CQT

![Hình 3](../../assets/images/invoice1/1.0_huy_4.png)

Trên pm truy cập vào phần Hóa đơn NĐ123  >> quản lý thông báo 04/SS-HDDT 
Chọn tờ 04ss vừa mới lập ở bước trên nhấn Ký 04/SS - HDDT , sau khi ký xong nhấn gửi CQT

Ở mục trạng thái CQT, nếu cơ quan thuế đồng ý về việc hủy hóa đơn thì phần trạng thái sẽ chuyển về chấp nhận và ngược lại

!!! info "Xin chân thành cảm ơn Quý khách hàng đã tin dùng sản phẩm của M-Invoice"
    Có bất kỳ vướng mắc nào trong quá trình sử dụng hãy liên hệ với M-Invoice tại mục Hỗ trợ kỹ thuật góc phải bên dưới màn hình hoặc gọi tổng đài kỹ thuật của M-Invoice (1900.955.557 Nhánh 1)

![Hình 5](../../assets/images/invoice1/1.0_suaTienBangTay_5.png)

<!-- === "Latest"

    ``` sh
    pip install mkdocs-material
    ```

=== "9.x"

    ``` sh
    pip install mkdocs-material=="9.*" # (1)!
    ```

    1.  Material for MkDocs uses [semantic versioning][^2], which is why it's a
        good idea to limit upgrades to the current major version.

        This will make sure that you don't accidentally [upgrade to the next
        major version], which may include breaking changes that silently corrupt
        your site. Additionally, you can use `pip freeze` to create a lockfile,
        so builds are reproducible at all times:

        ```
        pip freeze > requirements.txt
        ```

        Now, the lockfile can be used for installation:

        ```
        pip install -r requirements.txt
        ```

[^2]:
    Note that improvements of existing features are sometimes released as
    patch releases, like for example improved rendering of content tabs, as
    they're not considered to be new features.

This will automatically install compatible versions of all dependencies:
[MkDocs], [Markdown], [Pygments] and [Python Markdown Extensions]. Material for
MkDocs always strives to support the latest versions, so there's no need to
install those packages separately.

---

:fontawesome-brands-youtube:{ style="color: #EE0F0F" }
**[How to set up Material for MkDocs]** by @james-willett – :octicons-clock-24:
27m – Learn how to create and host a documentation site using Material for
MkDocs on GitHub Pages in a step-by-step guide.

[How to set up Material for MkDocs]: https://www.youtube.com/watch?v=xlABhbnNrfI

---

!!! tip

    If you don't have prior experience with Python, we recommend reading
    [Using Python's pip to Manage Your Projects' Dependencies], which is a
    really good introduction on the mechanics of Python package management and
    helps you troubleshoot if you run into errors.

[Python package]: https://pypi.org/project/mkdocs-material/
[virtual environment]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment
[semantic versioning]: https://semver.org/
[upgrade to the next major version]: upgrade.md
[Markdown]: https://python-markdown.github.io/
[Pygments]: https://pygments.org/
[Python Markdown Extensions]: https://facelessuser.github.io/pymdown-extensions/
[Using Python's pip to Manage Your Projects' Dependencies]: https://realpython.com/what-is-pip/

### with docker

The official [Docker image] is a great way to get up and running in a few
minutes, as it comes with all dependencies pre-installed. Open up a terminal
and pull the image with:

=== "Latest"

    ```
    docker pull squidfunk/mkdocs-material
    ```

=== "9.x"

    ```
    docker pull squidfunk/mkdocs-material:9
    ```

The `mkdocs` executable is provided as an entry point and `serve` is the
default command. If you're not familiar with Docker don't worry, we have you
covered in the following sections.

The following plugins are bundled with the Docker image:

- [mkdocs-minify-plugin]
- [mkdocs-redirects]

  [Docker image]: https://hub.docker.com/r/squidfunk/mkdocs-material/
  [mkdocs-minify-plugin]: https://github.com/byrnereese/mkdocs-minify-plugin
  [mkdocs-redirects]: https://github.com/datarobot/mkdocs-redirects

??? question "How to add plugins to the Docker image?"

    Material for MkDocs only bundles selected plugins in order to keep the size
    of the official image small. If the plugin you want to use is not included,
    you can add them easily:

    === "Material for MkDocs"

        Create a `Dockerfile` and extend the official image:

        ``` Dockerfile title="Dockerfile"
        FROM squidfunk/mkdocs-material
        RUN pip install mkdocs-macros-plugin
        RUN pip install mkdocs-glightbox
        ```

    === "Insiders"

        Clone or fork the Insiders repository, and create a file called
        `user-requirements.txt` in the root of the repository. Then, add the
        plugins that should be installed to the file, e.g.:

        ``` txt title="user-requirements.txt"
        mkdocs-macros-plugin
        mkdocs-glightbox
        ```

    Next, build the image with the following command:

    ```
    docker build -t squidfunk/mkdocs-material .
    ```

    The new image will have additional packages installed and can be used
    exactly like the official image.

### with git

Material for MkDocs can be directly used from [GitHub] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

```
git clone https://github.com/squidfunk/mkdocs-material.git
```

Next, install the theme and its dependencies with:

```
pip install -e mkdocs-material
```

[GitHub]: https://github.com/squidfunk/mkdocs-material -->

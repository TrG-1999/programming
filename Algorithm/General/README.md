# General 

## Harr Wavelet Transform
### Các bước thực hiện thuật toán tách sóng con theo phương pháp của harr
![Image of step harr](https://raw.githubusercontent.com/TrG-1999/programming/master/Algorithm/General/DWT_Harr_wavelet_transform.PNG)

####[Code dựa trên các bước Harr](https://github.com/TrG-1999/programming/tree/master/Algorithm/General/dwt_function.py)
>kết quả sẽ khá tương tự như hình dưới.
![Image of example harr](https://raw.githubusercontent.com/TrG-1999/programming/master/Algorithm/General/example_DWT_harr.PNG)

### Ứng dụng vào Hình ảnh RGB có kích thước chẵn
>Hình Gốc...
![Image of original watemark](https://raw.githubusercontent.com/TrG-1999/programming/master/Algorithm/General/Lena-convert.png)

####[Code Thực hiện DWT hình ảnh](https://github.com/TrG-1999/programming/tree/master/Algorithm/General/using-dwt-harr-in-image.py)
>Hình ảnh sau khi được phân tách sóng con mức 1
![Image of DWT Lv1](https://raw.githubusercontent.com/TrG-1999/programming/master/Algorithm/General/Lena-convert-Dwt.png)
>Sau khi Invert lại hình sẽ trở lại giống như hình gốc... Các kĩ thuật chuyển sóng con này được áp dụng vào Nhúng thủy vân.
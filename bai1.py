# Phân tích lỗi
# Nguyên nhân: Trong code ban đầu, vòng lặp ngoài duyệt theo tháng
#  vòng lặp trong duyệt theo chi nhánh. Điều này khiến dữ liệu được in ra theo thứ tự tháng -> chi nhánh
# tức gom theo tháng chứ không gom theo chi nhánh.
# Theo yêu cầu nghiệp vụ: Báo cáo cần gom dữ liệu theo từng chi nhánh.
# -> Vòng lặp ngoài phải duyệt theo chi nhánh.
# -> Vòng lặp trong phải duyệt theo tháng.

# Sửa lỗi
# Báo cáo doanh thu theo chi nhánh - Rikkei Store

branches_number = int(input("Nhập số lượng chi nhánh: "))
month_number = 3

print("-------------- Kết quả --------------")
for branch in range(1, branches_number + 1):
    print(f"--- Doanh thu Chi nhánh {branch} ---")
    total = 0
    for month in range(1, month_number + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        print(f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng")
        total += revenue
    print(f"Tổng doanh thu Chi nhánh {branch}: {total} triệu đồng\n")
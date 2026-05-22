# # CAU 1
# price = float(input("Moi ban nhap vao don gia: "))
# quantity = int(input("Moi bannhap vao so luong: "))

# total_money = price * quantity

# if(total_money >= 1000000):
#     total_money = total_money - (total_money * 0.1)
#     print("Ban duoc giam gia 10%")
#     print(f"So tien sau khi duoc giam la {total_money} nghin dong")
# else:
#     print("Ban khong duoc giam gia!!!")


# CAU 2
# password = 123456
# for i in range(1,4):
#     input_pass = input("Nhap mat khau: ")
#     if(input_pass == password):
#         print("Đăng nhập thành công!")
#         break
#     else:
#         if(i >= 3):
#             print("Tài khoản đã bị khóa!")
#             break
#         else:
#             print("Mật khẩu sai, vui lòng nhập lại!")


# CAU 3
total_product = 0
box_quantity = 0
while True:
        a = int(input("Nhap so luong san pham: "))
        if a < 0:
            print("Số lượng không hợp lệ, bỏ qua thùng này!")
            continue

        if a == 0:
            print("Đã kiểm đếm xong và kết thúc quá trình nhập")
            break

        total_product += a
        box_quantity += 1

        print("Đã thêm số lượng sản phẩm thành công")

print(f"số thùng hàng hợp lệ đã đếm {box_quantity}")
print(f"số lượng sản phẩm thu được {total_product}")


    

    
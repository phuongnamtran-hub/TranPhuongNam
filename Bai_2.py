try:
    thang = int(input("Nhập tháng"))
except:
    print("Dữ liệu không hợp lệ")
else:
    if thang <= 12:
        print(f"{thang} là Tháng hợp lệ")
    else:
        print(f"{thang} là Tháng không hợp lệ")
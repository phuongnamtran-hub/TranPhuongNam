try:
    NamDL = int(input("Nhập năm của bạn: "))
except:
    print("Năm không hợp lệ!")
else:
    DuCan = NamDL % 10
    DuChi = NamDL % 12
    match DuCan:
        case 0:
            print("Canh") 
        case 1:
            print("Tân") 
        case 2:
            print("Nhâm") 
        case 3:
            print("Quý") 
        case 4:
            print("Giáp") 
        case 5:
            print("Ất") 
        case 6:
            print("Bính") 
        case 7:
            print("Đinh") 
        case 8:
            print("Mậu") 
        case 9:
            print("Kỷ") 

    match DuChi:
        case 0:
            print("Thân") 
        case 1:
            print("Dậu") 
        case 2:
            print("Tuất") 
        case 3:
            print("Hợi") 
        case 4:
            print("Tí") 
        case 5:
            print("Sửu") 
        case 6:
            print("Dầu") 
        case 7:
            print("Mẹo") 
        case 8:
            print("Thìn") 
        case 9:
            print("Tỵ") 
        case 10:
            print("Ngọ") 
        case 11:
            print("Mùi") 
    print(f"năm Âm Lịch của bạn là {DuCan + DuChi}")
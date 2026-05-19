ovqatlar = {
    "osh" : 20,
    "somsa" : 20,
    "plemen" : 20,
    "chuchvara" : 20,
    "galupsiy" : 20
}

while True:
    menyu = f"""
Oshxona menyu
1) Osh {ovqatlar["osh"]} 
2) Somsa {ovqatlar["somsa"]}
3) Plemen {ovqatlar["plemen"]}
4) Chuchvara {ovqatlar["chuchvara"]}
5) Galupsiy {ovqatlar["galupsiy"]}
0) Chiqish"""
    print(menyu)
    menyu_tanlash = int(input("Menyulardan birini tanlang: "))
    if menyu_tanlash == 1:
        dona = int(input("Necha dona osh olasiz: "))
        if dona > 0:
            if dona <= ovqatlar["osh"]:
                ovqatlar["osh"] -= dona
                print(f"{dona} dona osh oldiz. Qoldiq -> {ovqatlar["osh"]} ta qoldi")
            else:
                print("Buncha miqdorda osh yoq")
        else:
            print("Miqdor 0 dan katta bo'lishi kerak")
    elif menyu_tanlash == 2:
        dona = int(input("Necha dona somsa olasiz: "))
        if dona > 0:
            if dona <= ovqatlar["somsa"]:
                ovqatlar["somsa"] -= dona
                print(f"{dona} dona somsa oldiz. Qoldiq -> {ovqatlar["somsa"]} ta qoldi")
            else:
                print("Buncha miqdorda somsa yoq")
        else:
            print("Miqdor 0 dan katta bo'lishi kerak")
    elif menyu_tanlash == 3:
        dona = int(input("Necha dona plemen olasiz: "))
        if dona > 0:
            if dona <= ovqatlar["plemen"]:
                ovqatlar["plemen"] -= dona
                print(f"{dona} dona plemen oldiz. Qoldiq -> {ovqatlar["plemen"]} ta qoldi")
            else:
                print("Buncha miqdorda osh yoq")
        else:
            print("Miqdor 0 dan katta bo'lishi kerak")
    elif menyu_tanlash == 4:
        dona = int(input("Necha dona chuchvara olasiz: "))
        if dona > 0:
            if dona <= ovqatlar["chuchvara"]:
                ovqatlar["chuchvara"] -= dona
                print(f"{dona} dona chuchvara oldiz. Qoldiq -> {ovqatlar["chuchvara"]} ta qoldi")
            else:
                print("Buncha miqdorda chuchvara yoq")
        else:
            print("Miqdor 0 dan katta bo'lishi kerak")
    elif menyu_tanlash == 5:
        dona = int(input("Necha dona galupsiy olasiz: "))
        if dona > 0:
            if dona <= ovqatlar["galupsiy"]:
                ovqatlar["galupsiy"] -= dona
                print(f"{dona} dona galupsiy oldiz. Qoldiq -> {ovqatlar["galupsiy"]} ta qoldi")
            else:
                print("Buncha miqdorda galupsiy yoq")
        else:
            print("Miqdor 0 dan katta bo'lishi kerak")
    elif menyu_tanlash == 0:
        print("Tashrifingiz uchun rahmat!")
        break
    else:
        print("Bunday menyu yoq!")

height=float(input("키를 입력하세요(cm): "))
weight=float(input("몸무게를 입력하세요(kg): "))
height_m= height/100
bmi= weight/(height_m **2)

if bmi< 18.5:
    print("저체중")
elif bmi<23:
    print("정상")
elif bmi<25:
    print("과체중")
else:
    print("비만")


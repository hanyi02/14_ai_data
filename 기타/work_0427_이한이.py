import pandas as pd

# =========================
# 문제 1. Series 생성하기
# =========================

name_list= ["김민수", "이서연", "박지훈", "최유진"]
score_list= [85, 92, 78, 95]

score= pd.Series(score_list, index=name_list)

print("문제 1")
print(score)

# =========================
# 문제 2. Series 속성 출력하기
# =========================
print("\n문제 2")
print(score.values)
print(score.index)
print(score.dtype)
print(score.size)
print(score.ndim)



# =========================
# 문제 3. Series 원소 1개 선택하기
# =========================
print("\n문제 3")
print(score["김민수"])
print(score["최유진"])
print(score.iloc[0]) #위치 기준이라 iloc
print(score.iloc[-1])



# =========================
# 문제 4. Series 원소 여러 개 선택하기
# =========================
print("\n문제 4")
print(score[["김민수", "박지훈"]])
print(score[["이서연", "최유진"]])
print(score.iloc[0:2])
print(score.iloc[1:])


# =========================
# 문제 5. DataFrame 생성하기
# =========================

# 딕셔너리 사용!
students= pd.DataFrame({
    "이름": ["김민수", "이서연", "박지훈", "최유진"],
    "나이": [20, 21, 20, 22],
    "국어": [85, 92, 78, 95],
    "영어": [90, 87, 80, 93],
    "수학": [88, 95, 76, 97]
})

print("\n문제 5")
print(students)


# =========================
# 문제 6. DataFrame 속성 출력하기
# =========================
print("\n문제 6")
print(students)
print(students.shape)
print(students.columns)
print(students.index)
print(students.dtypes)
print(students.size)
print(students.ndim)


# =========================
# 문제 7. DataFrame 열 1개 선택하기
# =========================
print("\n문제 7")
print(students["이름"])
print(students["국어"])
print(students["수학"])


# =========================
# 문제 8. DataFrame 열 여러 개 선택하기
# =========================
print("\n문제 8")
print(students[["이름", "나이"]])
print(students[["이름", "국어", "영어"]])
print(students[["국어", "영어", "수학"]])


# =========================
# 문제 9. DataFrame 행 1개 선택하기
# =========================
print("\n문제 9")
print(students.iloc[0])
print(students.iloc[1])
print(students.iloc[-1])


# =========================
# 문제 10. DataFrame 행 여러 개 선택하기
# =========================
print("\n문제 10")
print(students.iloc[0:2])
print(students.iloc[1:])
print(students.iloc[[0, 2]])


# =========================
# 문제 11. DataFrame 행 선택
# =========================

new_students = pd.DataFrame({
    '나이': [20, 21, 20, 22],
    '국어': [85, 92, 78, 95],
    '영어': [90, 87, 80, 93],
    '수학': [88, 95, 76, 97]
}, index=['김민수', '이서연', '박지훈', '최유진'])

print(new_students.loc['김민수'])
print(new_students.loc['최유진'])
print(new_students.loc[['김민수', '박지훈']])
print(new_students.loc['이서연':'최유진'])
 
 
# =========================
# 문제 12. DataFrame 행과 열 선택하기
# =========================
print("\n문제 12")
print(new_students.loc["김민수", "국어"])
print(new_students.loc["이서연", "수학"])
print(new_students.loc["박지훈", "영어"])
print(new_students.loc["최유진", "나이"])


# =========================
# 문제 13. 여러 행과 여러 열 선택
# =========================
print("\n문제 13")
print(new_students.loc[["김민수", "이서연"], ["국어", "영어"]])
print(new_students.loc[["박지훈", "최유진"], ["영어", "수학"]])
print(new_students.loc[:, ["국어", "영어", "수학"]])
print(new_students.loc["김민수":"박지훈", ["나이", "국어"]])


# =========================
# 문제 14. 특정 위치의 값 선택
# =========================
print("\n문제 14")
print(students.iloc[0, 0])
print(students.iloc[1, 3])
print(students.iloc[2, 4])
print(students.iloc[3, 1])


# =========================
# 문제 15. 종합 문제
# =========================
products = pd.DataFrame({
    "상품명": ["노트북", "마우스", "의자", "책상", "키보드"],
    "가격": [1200000, 25000, 85000, 150000, 45000],
    "재고": [5, 30, 12, 7, 20],
    "카테고리": ["전자제품", "전자제품", "가구", "가구", "전자제품"]
})

print("\n문제 15-1")
print(products)

print("\n문제 15-2")
print(products.shape)

print("\n문제 15-3")
print(products.columns)

print("\n문제 15-4")
print(products["상품명"])

print("\n문제 15-5")
print(products[["상품명", "가격"]])

print("\n문제 15-6")
print(products.iloc[0])

print("\n문제 15-7")
print(products.iloc[-1])

print("\n문제 15-8")
print(products.iloc[1:4])

print("\n문제 15-9")
products2 = products.set_index("상품명")
print(products2)

print("\n문제 15-10")
print(products2.loc["노트북"])

print("\n문제 15-11")
print(products2.loc["마우스", "가격"])

print("\n문제 15-12")
print(products2.loc[["의자", "책상"], ["가격", "재고"]])
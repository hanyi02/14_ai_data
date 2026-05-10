## =========================================
## 컨테이너 자료형- [4] Dict 자료형
##
## Dict와 추가 메서드들 살펴보기
## =========================================
## -------------------------------------------
## dict에 원소/ 요소 추가 메서드=> 형태: 키와 값 쌍으로 추가
## -> setdefault() 메서드
## -> update() 메서드
## -------------------------------------------

## 예시 dict 생성
strDict = {"홍": 3.9, "마": 4.1, "권": 2.7}

## 원소 추가하기
strDict.setdefault("박")
print(f"원소:{len(strDict)}개, {strDict}")

strDict.setdefault("배", 3.3)
print(f"원소:{len(strDict)}개, {strDict}")

strDict.setdefault("배", 4.3)
print(f"원소:{len(strDict)}개, {strDict}")

# ======> 처음 추가된 키 값으로 고정됨. 이미 키가 있으면 바뀌지 않음


## => 원소 추가하기(2)
## 존재하지 않는 키 추가, 1개~여러 개 추가 가능

## 키워드 인자 방식으로 추가
strDict.update(K=2.9, P=3.1, C=4.0)
print(f"원소: {len(strDict)}개, {strDict}")

## dict 형식 / (키,값) 쌍 묶음으로 추가
strDict.update([('김', 3.2), ('이', 4.4)])
print(f"원소: {len(strDict)}개, {strDict}")

## zip 형식으로 추가
strDict.update(zip(['최', '제갈', '남궁'], [3.0, 2.9, 2.8]))
print(f"원소: {len(strDict)}개, {strDict}")


## ============================================================
## dict 에 원소/ 요소 값 변경 메서드 => update(키와 값 묶음) 메서드
## 존재하는 키면 값을 수정해줌
## 여러 개 변경도 가능함
## ============================================================

strDict['홍'] = 3.9
strDict['마'] = 4.4
strDict['권'] = 3.7
strDict['박'] = 1.3
print(f"원소: {len(strDict)}개, {strDict}")

# 여러 개 한꺼번에 변경/업데이트
strDict.update(zip(['홍', '마', '권', '박'], [2.2, 3.4, 4.4, 2.3]))
print(f"원소: {len(strDict)}개, {strDict}")


## ==============================================================
## dict에 원소/ 요소 삭제 메서드
## pop(키) : 키에 해당하는 원소를 꺼내서 값만 반환
## popitem() : 마지막 원소를 꺼내서 (키, 값) 형태 반환
## ==============================================================




## zip 형식으로 추가
#strDict.update(zip(['최', '제갈', '남궁'], [3.0, 2.9, 2.8]))
#print(f"원소: {len(strDict)}개, {strDict}")


## (1) 특정 키의 원소 꺼내서 값만 가져오기
value = strDict.pop('홍')
print(f"원소: {len(strDict)}개, \n꺼낸 원소 값:{value}")

## (2) 마지막 원소 꺼내서 (키, 값) 형태로 가져오기
result= strDict.popitem()
print(f"원소: {len(strDict)}개, \n꺼낸 원소 값:{result}")

result= strDict.popitem()
print(f"원소: {len(strDict)}개, \n꺼낸 원소 값:{result}")

result= strDict.popitem()
print(f"원소: {len(strDict)}개, \n꺼낸 원소 값:{result}")


## (3) 특정 키의 원소 삭제 명령어: del 변수명[키], del(변수명[키])
del strDict['권']
del strDict['마']
print(f"원소: {len(strDict)}개, {strDict}")


## (4) 모든 원소 삭제 메서드: clear()=> 빈 dict 남음!
strDict.clear()
print(f"원소: {len(strDict)}개, {strDict}") 
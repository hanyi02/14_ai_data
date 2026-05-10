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

dataDict={1:100, 2:98, 3:100}

print(f"dataDict: {len(dataDict)}개, {dataDict}")

## => 키 존재 할 경우
value= dataDict.get(2)
print(f"get(2): {value}| {dataDict}")
print(f"dataDict[2]: {dataDict[2]}| {dataDict}")


## => 키 존재 하지 않는 경우
value= dataDict.get('A')
print(f"get('A'): {value}| {dataDict}")
print(f"dataDict['A']: {dataDict['A']}| {dataDict}")

# 에러발생




## -------------------------------------------
## 키 정보만 가지고 dict 생성 메서드: fromkeys()
## -------------------------------------------
keys= range(10, 101, 10)
dataDict= dict.fromkeys(keys)

print(f"dataDict: {len(dataDict)}개, {dataDict}")


dataDict= dict.fromkeys(keys, 0)
print(f"dataDict: {len(dataDict)}개, {dataDict}")


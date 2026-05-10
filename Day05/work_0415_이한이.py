## ===========================================================
## 25장 딕셔너리 응용하기
## - 25.3 딕셔너리 표현식 사용하기 제외
## - confrehension, 조건부 표현식 문제 제외
## ===========================================================

# <딕셔너리에서 키 값 수정하기>
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.update(a=90)) #{'a': 90, 'b': 20, 'c': 30, 'd': 40}

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.update(a=90)) # None

# 한꺼번에
x.update(a=900, f=60)
print(x) #{'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# ** update(키=값)은 키가 문자열일 때만 사용가능/ 숫자일 경우에는 update처럼 딕셔너리를 넣어서 값을 수정할 수 있음

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y) #{1: 'ONE', 2: 'two', 3: 'THREE'}


# 방법2
# update(리스트), update(튜플) 
# 여기서 리스트는 [[키1, 값1], [키2, 값2]] 형식으로 키와 값을 리스트로 만들고 이 리스트를 다시 리스트 안에 넣어서 키-값 쌍 나열(튜플도 같은 형식).

y.update([[2, 'TWO'], [4, 'FOUR']])
print(y) #{1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}

"""
setdefault와 update 차이


setdefault는 키-값 쌍 추가만 할 수 있고 이미 들어있는 키의 값은 수정할 수 XX
하지만 update는 키-값 쌍 추가와 값 수정이 모두 가능


"""

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90)
print(x) #{'a': 10, 'b': 20, 'c': 30, 'd': 40}




# 딕셔너리에서 임의의 키-값 쌍 삭제하기

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem() #('d', 40)

print(x) #{'a': 10, 'b': 20, 'c': 30}



# 딕셔너리에서 키 값 가져오기

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a') #10

# get(키, 기본값)처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 
# 해당 키의 값을 반환하지만 키가 없을 때는 기본값을 반환
x.get('z', 0) # 0



# 딕셔너리에서 키-값 쌍 모두 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

x.keys()
dict_keys(['a', 'b', 'c', 'd'])

x.values()
dict_values([10, 20, 30, 40])


# 리스트와 튜플로 딕셔너리 만들기
''' dict.fromkeys(키리스트): 키 리스트로 딕셔너리를 생성하며 값은 모두 None '''

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x) #{'a': None, 'b': None, 'c': None, 'd': None}


y = dict.fromkeys(keys, 100)
print(y) # {'a': 100, 'b': 100, 'c': 100, 'd': 100}






# 반복문으로 딕셔너리의 키-값 쌍 모두 출력하기

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')

# a 10
# b 20
# c 30
# d 40


# 딕셔너리 안에서 딕셔너리 사용하기

# 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}


terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

"""
# 딕셔너리의 할당과 복사 #################################### 헷갈림

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x

# =====> 
# 딕셔너리를 다른 변수에 할당하면 딕셔너리는 두 개가 될 것 같지만 
# 실제로는 딕셔너리가 한 개
"""

print(x is y) #True


# x와 y는 같으므로 y['a'] = 99와 같이 키 'a'의 값을 변경하면 
# 딕셔너리 x와 y에 모두 반영

y['a'] = 99
print(x) #{'a': 99, 'b': 0, 'c': 0, 'd': 0}

print(y) #{'a': 99, 'b': 0, 'c': 0, 'd': 0}



# 딕셔너리 x와 y를 완전히 두 개로 만들려면 copy 메서드
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy
print(x is y) #False
print(x == y) #True



# 25.5.1  중첩 딕셔너리의 할당과 복사

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()


y['a']['python'] = '2.7.15'
print(x) #{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}

print(y) #{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}



# 중첩 딕셔너리를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수 

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy             # copy 모듈을 가져옴
y = copy.deepcopy(x)    # copy.deepcopy 함수를 사용하여 깊은 복사
y['a']['python'] = '2.7.15'
print(x) #{'a': {'python': '2.7'}, 'b': {'python': '3.6'}}

print(y) #{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}





# ===================================================================================

#                                   퀴즈 

# ===================================================================================

"""

1.

다음 중 딕셔너리 x에서 키 'python'과 해당 값을 삭제하는 방법으로 올바른 것을 모두 고르세요.

a. x.pop()
b. x.popitem()
c. x.pop('python', 100)
d. x.remove('python')
e. del x['python']

=====>  c, e



2.

다음 중 딕셔너리의 메서드에 대한 설명으로 올바르지 않은 것을 모두 고르세요.

a. setdefault는 딕셔너리에 키-값 쌍을 추가한다.
b. setdefault는 키만 지정하면 값은 0으로 저장한다.
c. keys는 딕셔너리의 키-값 쌍을 모두 가져온다.
d. clear는 딕셔너리의 모든 키-값 쌍을 삭제한다.
e. update는 딕셔너리에서 키의 값을 수정한다.

=====>  b, c



3.

다음 중 반복문으로 딕셔너리 x의 모든 키를 출력하는 방법으로 올바른 것을 모두 고르세요.

a.

for key, value in x:
    print(key)

b.

for key in x:
    print(key)

c.

for key in x.keys():
    print(key)

d.

for value in x.values():
    print(value)

e.

for key, value in x.items():
    print(key)

=====>  b, c, e

4.

다음 중 딕셔너리
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
에서 값이 40인 키-값 쌍을 삭제하는 방법으로 바른 것을 고르세요.

a.

for key, value in x.items():
    if value == 40:
        del x[key]

b. del x[40]

=====>  d


5.

다음 코드에서 딕셔너리 terrestrial_planets의 키 'satellites'에 접근하는 방법으로 올바른 것을 고르세요.



a. terrestrial_planet('Earth')('orbital_characteristics')('satellites')
b. terrestrial_planet['satellites']
c. terrestrial_planet['Earth']['satellites']
d. terrestrial_planet['Earth']['orbital_characteristics']['satellites']
e. terrestrial_planet['Mars']['physical_characteristics']['mass']

====>  d



6.

다음 코드의 실행 결과로 올바른 것을 고르세요.

import copy

x = {'python': {'version': '2.7'}, 'script': {'name': 'hello.py'}}

a = x
b = x.copy()
c = copy.deepcopy(x)

x['python']['version'] = '3.6'

print(a['python']['version'], b['python']['version'], c['python']['version'])

a. 2.7 2.7 2.7
b. 3.6 2.7 2.7
c. 3.6 3.6 2.7
d. 3.6 3.6 3.6

====>  c


"""


# ================================================================
# 연습문제: 평균 점수 구하기 
# ================================================================

maria= {'korean': 94, 'english': 91, 'math': 89, 'science': 83}
average= sum(maria.values)/len(maria)
print(average)








## ===========================================================
## 26장 세트 사용하기
##  - 26.6 세트 표현식 사용하기 제외
## =======================================================



# 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits) #{'pineapple', 'orange', 'grape', 'strawberry', 'cherry'}

# 세트는 요소의 순서가 정해져 있지 않음
# 세트에 들어가는 요소는 중복될 수 없음
# 세트에 'orange'를 두 개 넣어도 실제로는 한 개만 들어감

# 특히 세트는 리스트, 튜플, 딕셔너리와는 달리 [ ](대괄호)로 특정 요소만 출력할 수 X

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits[0])

"""
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(fruits[0])
TypeError: 'set' object does not support indexing
>>> fruits['strawberry']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    fruits['strawberry']
TypeError: 'set' object is not subscriptable
"""






# 세트에 특정 값이 있는지 확인하기
# 리스트, 튜플, 딕셔너리에 사용했던 in 연산자 

# 값 in 세트
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits) #True

print('peach' in fruits)  #False






# 한글 문자열을 세트로 만들기

set('안녕하세요') #{'녕', '요', '안', '세', '하'}

# 세트 안에 세트 넣기
# ===> 세트는 리스트, 딕셔너리와 달리 세트 안에 세트를 넣을 수 없음
"""
a = {{1, 2}, {3, 4}}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a = {{1, 2}, {3, 4}}
TypeError: unhashable type: 'set'



프로즌세트 = frozenset(반복가능한객체)

a = frozenset(range(10))
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

frozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없음
=>  즉, 다음과 같이 frozenset의 요소를 변경하려고 하면 에러 발생 

a = frozenset(range(10))
a |= 10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a |= 10
TypeError: unsupported operand type(s) for |=: 'frozenset' and 'int'
a.update({10})
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update({10})
AttributeError: 'frozenset' object has no attribute 'update'
frozenset는 세트 안에 세트를 넣고 싶을 때 사용
-> 다음과 같이 frozenset는 frozenset를 중첩해서 넣을 수 있음 단, frozenset만 넣을 수 있고, 일반 set는 넣을 수 없음

frozenset({frozenset({1, 2}), frozenset({3, 4})})
frozenset({frozenset({1, 2}), frozenset({3, 4})})

"""

"""
1. 합집합
세트1 | 세트2
set.union(세트1, 세트2)

2. 교집합
세트1 & 세트2
set.intersection(세트1, 세트2)

3. 차집합
세트1 - 세트2
set.difference(세트1, 세트2)

4. 대칭차집합
세트1 ^ 세트2
set.symmetric_difference(세트1, 세트2)

5. 상위집합 확인 
현재세트 < 다른세트
현재세트.issubset(다른세트)


현재세트 > 다른세트
현재세트.issuperset(다른세트)


현재세트.isdisjoint(다른세트)
"""




# ===================================================================================

#                                   퀴즈 

# ===================================================================================

"""

1. 다음 중 세트를 만드는 방법으로 올바르지 않은 것을 고르세요.

a. a = {1, 2, 3, 4, 5}
b. a = {}
c. a = set('hello')
d. a = set(range(10))
e. a = set()

===>  b: 빈딕셔너리 만드는 것

2. 세트 a = {1, 2, 3}, b = {3, 4, 5}가 있을 때 집합 연산의 결과로 잘못된 것을 모두 고르세요.

a. set.union(a, b)는 {1, 2, 3, 4, 5}
b. a ^ b는 {1, 3, 5}
c. a - b는 {1, 2}
d. a & b는 {3}
e. set.difference(b, a)는 {4}

===>  b, e
b: 안 겹치는 요소 출력임
e: 차집합임



3. 다음 중 부분집합, 상위집합에 대한 설명으로 잘못된 것을 모두 고르세요.

a. 부분집합은 <=와 issubset로 구할 수 있고, 두 세트가 같을 때 참이다.
b. 진부분집합은 <와 issubset로 구할 수 있고, 두 세트가 다를 때 참이다.
c. 상위집합은 >=와 issuperset로 구할 수 있고, 두 세트가 같을 때 참이다.
d. 진상위집합은 >로 구할 수 있고, 두 세트가 같을 때 참이다.
e. 진부분집합과 진상위집합을 구하는 메서드는 없다.

===>  b, d



4. 다음 중 세트 메서드에 대한 설명으로 올바른 것을 모두 고르세요.

a. intersection_update는 현재 세트와 다른 세트에서 겹치는 요소만 현재 세트에 저장한다.
b. symmetric_difference는 두 세트의 대칭차집합을 구한다.
c. isdisjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인한다.
d. discard는 현재 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킨다.
e. pop은 현재 세트에서 지정된 요소를 삭제하고 요소가 없으면 에러를 발생시킨다.

===>  a, b, c




5. 다음 중 메서드와 연산자의 기능이 잘못 짝지어진 것을 고르세요.

a. set.intersection은 &와 같다.
b. set.update는 |=와 같다.
c. symmetric_difference_update는 -=와 같다.

===>  c, d

"""
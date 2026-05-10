## ===========================================================
## 29장 함수 사용하기
## ===========================================================


def add(a, b):
    """ 독스트링: 함수에 대한 설명,
    함수이름.__doc__ 으로 호출 가능 => 무조건 함수 본문 첫 번째 문장이여야 출력됨"""
    return a+b


print(add(3, 4)) #7
print(add.__doc__)

# 매개변수는 없고 반환값만 있는 함수
def one():
    return 1
print(one()) # 1

# return으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep='')

print(not_ten(5)) #5입니다. \nNone 나옴=> 

'''
1. not_ten(5) 실행
2. 함수 안에서 5입니다. 출력
3. 함수는 반환값이 없으므로 None 반환
4. 바깥 print()가 그 None을 또 출력
'''
# print(not_ten(10)) # None

# 여러개 값 반환하기
def add_sub(a, b):
    return a + b, a - b   

x, y = add_sub(10, 20)
x  #=> 30
y  #=> -10

# 곱셈함수 mul

def mul(a, b):
    c = a * b
    return c
 
def add(a, b):
    c = a + b   # 여기 c가 나오지만 위에 mul 호출 안됨==>  a+b값 저장
    print(c)
    d = mul(a, b)
    print(d)
 
x = 10
y = 20
add(x, y)


## ==========================================================================
##                                  퀴즈
## ==========================================================================


"""
29.6 퀴즈
1. 다음 중 매개변수가 없는 hello 함수를 호출하는 방법으로 올바른 것을 고르세요. C
a. def hello     
b. hello     
c. hello()      
d. hello[]     
e. def hello:    

==> C
a: 함수 정의
b: X
d: 리스트 생성/ 인덱싱
e: 함수 정의

---------------------------------------------------------------------
2. 두 수를 받은 뒤 곱한 결과를 반환하는 함수를 만들려고 합니다. 올바른 코드를 고르세요. d
a. def mul(): a * b            
b. def mul(a, b): a * b        
c. mul(a, b): return a * b     
d. def mul(a, b): return a * b    
e. mul(a, b): a * b     

==> D

a: 매개변수, return X
b: return X
c: 함수 정의 X
e: def와 return이 X


---------------------------------------------------------------------
3. 다음 중 값을 세 개 반환하는 함수를 만들려고 합니다. 올바른 코드를 모두 고르세요. a,c,d
a. def three(): return 1, 2, 3       
b. def three(): return 1 return 2 return 3 
c. def three(): return (1, 2, 3)     
d. def three(): return [1, 2, 3]     
e. def three(): return 1, return 2, return 3 

===> a, c, d

"""

## ==========================================================================
##                  연습문제: 몫과 나머지를 구하는 함수 만들기
## ==========================================================================
x = 10
y = 3

def  get_quotient_remainder(a, b):
    return a//b, a%b

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))



## ==========================================================================
##                  심사문제: 사칙 연산 함수 만들기
## ==========================================================================

# 표준 입력으로 숫자 두 개가 입력됩니다. 다음 소스 코드를 완성하여 
# 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요.
# 나눗셈의 결과는 실수여야 합니다.

# 입력 예시: 10 20 | 출력 예시: 덧셈: 30, 뺄셈: -10, 곱셈: 200, 나눗셈: 0.5
# 입력 예시: 40 8  | 출력 예시: 덧셈: 48, 뺄셈: 32, 곱셈: 320, 나눗셈: 5.0

# x, y = map(int, input().split()) # 실제 입력 시 주석 해제

def calc(a, b):
    return a + b, a - b, a * b, float(a / b)

# a, s, m, d = calc(x, y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))





## ===========================================================
## 30장 함수에서 위치 인수와 키워드 인수 사용하기
## ===========================================================


#위치인수를 사용하는 함수 만들고 호출
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(10,20,30)
# 10
# 20
# 30

# * 붙여서 리스트나 튜플 언팩킹하기
x = [10, 20, 30]

print_numbers(*x)
# 10
# 20
# 30

print_numbers(*[10, 20, 30]) # 이거도 가능

# 인수의 개수가 정해지지 않은 가변 인수 사용.

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10) # 10


# 고정인수와 가변인수 함께 사용
def print_numbers(a, *args):
     print(a)
     print(args)

print_numbers(1)
# 1
# ()
print_numbers(1, 10, 20)
# 1
# (10, 20)
print_numbers(*[10, 20, 30])   # * 이거 안하면 덩어리 하나로 친다.
# 10
# (20, 30)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


# 키워드 인수 방식으로 호출
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동


# ** 딕셔너리 언패킹
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동

personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
# 이렇게도 가능

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# name: 홍길동
# age: 30
# address: 서울시 용산구 이촌



#초깃값이 지정된 매개변수 위치
def personal_info(name, address='비공개', age=22):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

#   File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument  에러 발생
# => age 초깃값 설정하면 됨


# 초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 된다.
# def personal_info(name, age, address='비공개'):
# def personal_info(name, age=0, address='비공개'):
# def personal_info(name='비공개', age=0, address='비공개'):




## ==========================================================================
##                                  퀴즈
## ==========================================================================


"""
1. 함수를 def print_numbers(a, b, c): 처럼 만들었을 때 이 함수를 호출하는 방법으로 잘못된 것을 고르세요. 
a. print_numbers(1, 3, 5)            
b. print_numbers(a=1, b=2, c=3)     
c. a = [5, 0, 2]; print_numbers(*a)   
d. a = [3, 7, 9]; print_numbers(**a)
e. print_numbers(*(9, 1, 2))       


=> d
**는 딕셔너리 언패킹에 사용. a가 리스트라서 에러 발생

--------------------------------------------------------------------------------

2. 다음 중 print_numbers(*(10, 20, 30))으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.
a. def print_numbers(args):       
b. def print_numbers(a, b, c):       
c. def print_numbers(*args):  
d. def print_numbers(a, b):    
e. def print_numbers():    


==>  b,c


--------------------------------------------------------------------------------

3. 다음 중 personal_info(**{'name': '홍길동', 'age': 30})으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.  
a. def personal_info(**kwargs):    
b. def personal_info(*args):    
c. def personal_info(name='미공개', age=0): 
d. def personal_info(name, address):   
e. def personal_info(kwargs):       


==> a, c

b:  딕셔너리 언패킹(**)은  *args로 받을 수 없다.
d:'age' 키워드 대응 매개변수 없음.
e: 일반 매개변수 하나만

--------------------------------------------------------------------------------
"""

## ==========================================================================
##                  연습문제: 가장 높은 점수를 구하는 함수 만들기
## ==========================================================================
 
korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# 실행 결과:
# 높은 점수: 100
# 높은 점수: 91


## ===================================================================================================================
##                        심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
## ===================================================================================================================

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요.
# 평균 점수는 실수여야 합니다.

# 입력 예시: 76 82 89 84 | 출력 예시: 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 입력 예시: 89 92 73 83 | 출력 예시: 낮은 점수: 73.00, 높은 점수: 92.00, 평균 점수: 84.25

# [테스트용 데이터] - 실제 제출 시에는 input()을 사용하세요.
korean, english, mathematics, science = 76, 82, 89, 84 



def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    return sum(kwargs.values()) / len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

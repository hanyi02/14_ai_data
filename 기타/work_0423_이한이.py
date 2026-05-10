## ===========================================================================================================
##                                    34장 클래스 사용하기
## ===========================================================================================================

#  용어 정리
#  1. 클래스(Class): 속성(데이터)와 메서드(기능)을 묶은 틀
#               -> 사용자 정의 자료형
#
#  2. 객체(Object): 메모리에 실제로 올라간 데이터 덩어리
#               -> 보통 클래스 이용해서 생성
#                   class Object:
#                           def Object 기능함수:
#                               ~~~~~~~~~~~
#               -> 실제로 사용할 수 있는 상태(책상, 버튼, 체크박스) 같이 특정한 개념이나 모양으로 존재하는 것
#
#  3. 인스턴스(Instance): 특정 클래스에서 만들어진 객체
#                       -> 객체랑 거의 같은 의미지만 "어느 클래스의 객체냐"를 강조
#                       p1=Person(...)일 때 p1은 Person의 인스턴스
#
#  4. 속성(Attribute): 객체가 가지고 있는 데이터
#                      -> self.name= name
#                      -> self.age= age
#                      -> 이때 age, name은 속성임
#                      사용=> p1.name // 인스턴스(객체)의 정보를 뜻함
#
#  5. 메서드(Method): 객체가 할 수 있는 행동(함수)
#                   def info(self):
#                       print(self.name)
#                      라고 정의하고, 사용은 p1.info()
#
# ------------------------------------------------------------------------------------------------------------
## 정리

class Person:                # 클래스
    def __init__(self, name):
        self.name = name    # 속성: 객체가 가진 데이터(여기서는 이름)

    def info(self):         # 메서드: 행동
        print(self.name)

p1 = Person("홍길동")       # 객체(= 인스턴스)

p1.info() # 호출

# 클래스 사용

class Person:
    def greeting(self): # 메서드
        print('Hello')

james= Person() #여기서는 james가 Person의 인스턴스(객체)
# ----> 클래스는 특정 기능을 표현할 뿐이지 사용하려면 인스턴스 생성을 해야함

james.greeting() # 메서드 호출(이 경우에는 인스턴스를 이용해 매서드를 호출하므로 인스턴스 매서드라고 함)


### int, dict, list도 일종의 클래스!!!!!!!!!!!! 
#                           --> 클래스: 특정 개념 표현
#   int, dict, list를 사용하려면 객체를 불러야함
a= int("15") # 클래스를 사용하려면 인스턴스에 할당을 해야함

# 특정 클래스의 인스턴스인지 확인하는 법
isinstance(james, Person) #True
# ------------------------------------------------------------------------------------------------------------

# 속성 사용하기
# -> 속성(attribute)을 만들 때는 __init__ 매서드 안에서 self.속성에 값을 할당함
# -> 속성: 객체가 가지고 있는 데이터

class Car:
    def __init__(self):
        self.go= "5칸 전진"

    def start(self):
        print(self.go)

car=Car()
car.start() # 5칸 전진

# __init__ 매서드는 car=Car() 처럼 클래스에 ()를 붙여서 인스턴스를 만들 때 호출되는 특별한 매서드임
# ===> init은 initialize의 준말로 초기화를 뜻함

# ------------------------------------------------------------------------------------------------------------
# 인스턴스 받을 때 값 받기
class Bus:
    def __init__(self, color, number): #매개변수 정의
        self.color= color #self.속성= 매개변수
        self.number= number

    def alarm(self):
        print('{0}버스 {1}번 도착.'.format(self.color, self.number))

bus= Bus('파란색', 836)
bus.alarm()

''' 클래스로 인스턴스 만들 때 위치인수와 키워드 인수 사용이 가능하다 '''
# 위치 인수와 리스트 언패킹 사용--> *arg 사용, 매개변수 값 가져오려면 args[n]

# 1. 위치인수
class Bus:
    def __init__(self, *arg): #매개변수 정의
        self.color= args[0] #self.속성= 매개변수
        self.number= args[1]

    def alarm(self):
        print('{0}버스 {1}번 도착.'.format(self.color, self.number))
bus=Bus(*['초록색', 500])

# 2. 키워드 인수+ 딕셔너리 언패킹--> **kwargs
class Bus:
    def __init__(self, **kwarg): #매개변수 정의
        self.color= kwargs['color'] #self.속성= 매개변수
        self.number= kwargs['number']

    def alarm(self):
        print('{0}버스 {1}번 도착.'.format(self.color, self.number))

bus=Bus(**{'color':'초록색', 'number': 500})


# 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
class Person:
    pass
maria = Person()         # 인스턴스 생성
maria.name = '마리아'
## => 이렇게 인스터스 생성 후 추가한 속성은 해당 인스턴스 내에서만 생성이 됨
##    그래서 클래스로 다른 인스턴스 만들면 추가 속성 생성이 안 됨
james=Person()
# james.name==> 마리아에 추가했기 때문에 제임스에는 네임속성이 없음

# -------------------------------------------------------------------------------------------
# 비공개 속성 사용
class 클래스이름:
    def __init__(self, 매개변수):
        self.__속성 = 값 # __ 을 앞에 써줘야함

## ============================================================================================
##                                           퀴즈
## ============================================================================================
"""
1. 다음 클래스의 greeting 메서드를 호출하기 위한 방법으로 올바른 것을 고르세요.

a. Person.greeting()
b. greeting()
c. maria = Person
   maria.greeting()
d. maria = Person() 
   maria.greeting()
e. Person(greeting)
===> d


2. 클래스로 인스턴스를 만들 때 호출되는 메서드는 무엇인가요? (메서드 뒤의 괄호는 생략하고 메서드 이름만 입력)

===> __init__


3. 다음과 같이 Person 클래스가 있습니다. 클래스에서 다른 메서드를 만들었을 때 인스턴스 속성 name에 접근하기 위한 방법으로 올바른 것을 고르세요.
a. name
b. self
c. Person.name
d. self[name]
e. self.name
==> e


4. 클래스의 메서드 def __init__(self):에서 속성을 만들려고 합니다. 다음 중 비공개 속성을 고르세요.
a. self.name
b. self._name
c. self.__name 
d. self.__name__
e. self.name__
===> c


"""
## ============================================================================================
##                              연습문제: 게임 캐릭터 클래스 만들기
## ============================================================================================
# 다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.
class Knight:
    
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print("베기")
        
x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

## ============================================================================================
##                              심사문제: 게임 캐릭터 클래스 만들기
## ============================================================================================
#  표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다. 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의 피해량이 출력되게 만드세요. 티버의 피해량은 AP * 0.65 + 400이며 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print(f"티버: 피해량 {ability_power* 0.65+ 400}")

health, mana, ability_power = map(float, input().split())
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()


## ============================================================================================
##                                    35장 퀴즈 
## ============================================================================================
"""

1. 다음 중 클래스 바깥에서 클래스 속성 x에 접근하는 방법으로 올바른 것을 고르세요.
class Person:
    x = {}
a. Person.x
b. Person(x)
c. x
d. self.x
e. Person['x']
===> a

2. 다음 중 정적 메서드로 올바른 것을 고르세요.
a. def print_count(self):
    print(self.count)
b. @staticmethod
def sub(self, a, b):
    print(a - b)
c. @staticmethod
def div(a, b):
    print(a / b)
d. @staticmethod
def add(cls, a, b)
    print(a + b)
e. def print_count(cls):
    print(cls.count)

===> c

3. 다음 중 클래스 메서드에 대한 설명으로 잘못된 것을 고르세요.
a. 클래스 메서드는 클래스.메서드() 형식으로 호출한다.
b. 클래스 메서드는 위에 @classmethod를 붙여서 만든다.
c. 클래스 메서드의 첫 번째 매개변수는 self이며 현재 인스턴스가 들어온다.
d. 클래스 메서드는 인스턴스 없이 호출할 수 있다.
e. 클래스 메서드는 위에 @staticmethod를 붙여서 만든다.

===> c,e



"""

## ============================================================================================
##                                      연습문제
## ============================================================================================
# 다음 소스 코드에서 Date 클래스를 완성하세요. is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드입니다. 날짜에서 월은 12월까지 일은 31일까지 있어야 합니다.

@staticmethod
def is_date_valid(date_string):
    year, month, day = map(int, date_string.split('-'))
    return month <= 12 and day <= 31

## ============================================================================================
#                                       심사문제
## ============================================================================================

# 표준 입력으로 시:분:초 형식의 시간이 입력됩니다. 
# 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요. 
# from_string은 문자열로 인스턴스를 만드는 메서드이며 
# is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다. 
# 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다. 
# 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')







#
#
#
#
#
#
#
#
#
#
#
#
#
















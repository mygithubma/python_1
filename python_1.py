# print("hello world")
# m=("mzc 2001019")
# print(m)

# n=("jsbvjs")
# print(n)
# n=("dddd")
# print(n)

# b=("nnnnn")
# print(b.title())

# b=("Nmsdf Idw sjcf")
# print(b.title())
# print(b.upper())
# print(b.lower())

# first_name=("m")
# last_name=("zc")
# full_name=f"{first_name}{last_name}"
# print(full_name)
# print(f"hello {full_name.upper()}")
# m=full_name.title()
# print(m)

# print("\npython")
# b=("  python  ")
# print(b.lstrip())

# n=("mzc")
# m=f"hello {n} sdvcnjdsv"
# print(m)

# f_n=("m")
# l_n=("zc")
# full_n=f"{f_n}{l_n}"
# print(full_n.upper())

# t=120_000_000
# print(t)

# import this

# b=['a','b','d']
# # b.insert(2,'c')
# # del b[2]
# # print(b.pop(2))
# # print(b)
# b.remove('b')
# print(b)

# n=['a','v','g','y']
# n.sort(reverse=True)
# print(n)
# print(sorted(n))
# n.reverse()
# print(n)
# t=len(n)
# print(t)
# print(n[-1])

# b=['a','b','v','f']
# for a in b:
#     print(f"{a.title()} egf gsf")

# for a in range(1,6):
#     print(a)

# n=list(range(1,5,2))
# print(n)

# ss=[]
# for v in range(1,11):
#     s=v**2
#     ss.append(s)
# print(ss)

# s=[1,2,3,4,5,6,7]
# print(min(s))

# s=[v**2 for v in range(1,4)]
# print(s)

# b=[a for a in range(1,100)]
# for a in b:
#     print(a)
# print(min(b))
# print(max(b))
# print(sum(b))

# b=[1,2,3]
# print(b[0:1])

# a=[1,2,3,4,5,6,7,8,9,0]
# print(a[:2])
# for b in a[:2]:
#     print(b)

# my_n=['p','i','j']
# f_n=my_n[:]
# my_n.append('fgh')
# f_n.append('dsg')
# print(my_n)
# print(f_n)

# s=(1,2,3,4)
# print(s)

# a=['af','bd','cf','dd']
# for b in a:
#     if b=='cf':
#         print(b.upper())
#     else:
#         print(b.title())

# a=['a','b','c']
# for aa in a:
#     if aa=='a':
#         print("fhguskgh")
#     else:
#         print(f"add {aa}")
# print('finish')

# a=[]
# if a:
#     for b in a:
#         print(f"{b}")
#     print('dfgdfg')
# else:
#     print("kog")

# have=['abc','def','ghi']
# re=['abc','fsg']
# for d in re:
#     if d in have:
#         print(f"add {d}")
#     else:
#         print(f"donnot have{d}")

# print("fsdgsrgs")

# alien_1={'color':'blue',
#          'points':34  }
# alien_1['x']=2
# alien_1['y']=8
# alien_1['color']='green'
# print(alien_1)

# alien_1={'x':5,'y':78,'speed':'medium'}
# print(f"{alien_1['x']}")
# if alien_1['speed']=='slow':
#         xx=1
# elif alien_1['speed']=='medium':
#         xx=2
# else:
#         xx=4
# alien_1['x']=alien_1['x']+xx
# print(alien_1['x'])
# del alien_1['x']
# print(alien_1)

# alien={'color':'blue','points':5,'x':564}
# p=alien.get('x','nbo')
# print(p)
# for a,b in alien.items():
#     print(f"\na{a}")
#     print(f"b{b}")
# for a in alien.keys():
#     print(a.title())

# f_n={
#     'color':'blue',
#     "points":8,
#     'fg':'sfg',
#     'as':'sfg'
#     }
# for n in set(f_n.values()):
#     print(n)

# alien=[]
# for alien_n in range(30):
#     new={'c':5,'f':95}
#     alien.append(new)
# for alien in alien[:5]:
#     print(alien)

# users={
#     'n':{
#         "name":'mzc',
#         'num':123,
#         "sex":'m',
#         },
#     'b':{
#         'name':'mhc',
#         'num':456,
#         'sex':'m',
#         }
#     }
# for na,us in users.items():
#     print(f"\n user:{na}")
#     f_n=f"{us['name']} {us['num']} {us['sex']}"
#     print(f"{f_n}") 

# m=input("djbsjdv iwill  jnsgj")
# print(m)

# n=input("input yours name:")
# print(f"hello {n}")

# p="p n b v h"
# p+="\n what is your name"
# name=input(p)
# print(name)

# age=input("how old are you")
# print(age)

# c=10
# while c<=55:
#     print(c)
#     c=c-1

# p="input something"
# p+="this is"
# m=""
# while m !='quit':
#     m=input(p)
#     if m !='quit':
#         print(m)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# a='fjhngjrw'
# b=True
# while b:
#     m=input(a)
#     if m=='quit':
#         # b=False
#         break
#     else:
#         print(m)

# p=['a','b','c','t']
# print(p)
# while 'a' in p:
#     p.remove('a')
# print(p)

# def greet():
#     print("hello")
# greet()

# def greet(username):
#     print(f"hello {username}")
# greet('jesso')

# def d(type,name):
#     print(f"\ni have a {type}")
#     print(f"my {type} name is {name}")
# d('cat','mm')

# def a(f_n,l_n,age):
#     p={'f':f_n,'l':l_n}
#     if age:
#         p['age']=age
#     return p
# m=a('m','zc',age=0)
# print(m)

# def greet_user(names):
#     for name in names:
#         msg=f"hello,{name.title()}"
#         print(msg)
# usernames=['a','b','c']
# greet_user(usernames)


# def print_models(unprinted_designs,completed_models):
#     while  unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print(f"printing model:{current_design}")
#         completed_models.append(current_design)
    
# def show_completed_models(completed_models):
#     print(f"the following models have been printed")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs=['a','b','c']
# completed_models=[]

# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)


# m=['a','z','v']
# n=[]
# def show(n):
#     for a in n:
#         print(a)
# def send(m,n):
#     while(m):
#         b=m.pop()
#         n.append(b)

# send(m[:],n)
# show(n)       
# print(m)


# def build_profile(first,last,**user_info):
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info

# user_profile=build_profile('a','b',l='add',jhh='efduewh')
# print(user_profile)


# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sit(self):
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         print(f"{self.name} rolled over")

# my_dog=Dog('Willie',6)
# your_dog=Dog('sdjf',52)
# print(f"my dog is name {my_dog.name}")
# print(f"my dog is {my_dog.age}")
# my_dog.sit()
# my_dog.roll_over()
# your_dog.sit()


# class Restaurant:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type

#     def describe_restaurant(self):
#         print(f"the restaurant' s name is {self.name}")
#         print(f"the restaurant's type is {self.type}")

#     def open_restaurant(self):
#         print(f"the {self.name} is 营业中")

# my_restaurant=Restaurant('mzc','mjg')
# your_restaurant=Restaurant('mhz','fjdgh')
# my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# your_restaurant.open_restaurant()


# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0
    
#     def get_descriptive_name(self):
#         long_name=f"{self.year}  {self.make}  {self.model}"
#         return long_name.title()
    
#     def reading(self):
#         print(f"this car has {self.odometer_reading} miles on it")

#     def update_odometer(self,mileage):
#         self.odometer_reading=mileage
#         if mileage>=self.odometer_reading:
#             self.odometer_reading=mileage
#         else:
#             print("you cannot roll back")

#     def increment_odometer(self,miles):
#         self.odometer_reading+=miles
        

# # my_car=Car('aud','a5',456)
# # print(my_car.get_descriptive_name())
# # # my_car.odometer_reading=25
# # my_car.update_odometer(25)
# # my_car.reading()
# # my_car.increment_odometer(23000)
# # my_car.reading()

# class Battery:
#     def __init__(self,battery_size=75):
#         self.battery_size=battery_size

#     def describe_battery(self):
#         print(f"hgfsgv{self.battery_size}")

#     def get_range(self):
#         if self.battery_size==75:
#             range=260
#         elif self.battery_size==100:
#             range=315
#         print(f"iewfwv {range}")

# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         # self.battery_size=75
#         self.battery=Battery()

#     # def describe_battery(self):
#     #     print(f"hjjssdfj {self.battery_size}")

# my_tesla=ElectricCar('tesla','model',2018)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# with open('E:/xuexibiji/VSCODE/lianxi_py/pi.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# filename='E:/xuexibiji/VSCODE/lianxi_py/pi.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename='E:/xuexibiji/VSCODE/lianxi_py/pi.txt'
# with open(filename) as file_object:
#     lines=file_object.readlines()

# pi_string=''
# for line in lines:
#     pi_string+=line.strip()

# birthday=input("input your's birthday")
# if birthday in pi_string:
#     print("your birthday in pijdsgb")
# else:
#     print("gsrgsrg")
# print(f"{pi_string[:10]}...")
# print(len(pi_string))


# filename='E:/xuexibiji/VSCODE/lianxi_py/pi.txt'
# with open(filename,'a') as file_object:
#     file_object.write("i love you")


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("fdshjgsvsfsrgs")


# title="ajsjhc sajcfhdsku dsvnjfksbv"
# t=title.split()
# print(t)

# import json
# numbers=[2,3,4,5,6]
# filename='number.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)

# import json
# filename='number.json'
# with open(filename) as f:
#     numbers=json.load(f)
# print(numbers)

# import json
# filename='username.json'
# try:
#     with open(filename) as f:
#         username=json.load(f)
# except FileNotFoundError:
#     username=input("what ia your name")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print(f"we will remember you when you come back,{username}")
# else:
#     print(f"welcome back,{username}")



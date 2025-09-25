# import sys
# print(sys.version)

#simple print statement
# print("Hello World!")

#printing two variables in a single line
# a = 789
# b = 123
# print(a, b)
# print("a :{},b : {}".format(a,b))

#two variable one line
# a = b = 10
# print(a,b)
# print(a *2)


#unknow two variables assign
# a, b = 10, 20
# c, d = a, b
# print(c,d,a,b)


#assign 3 variables with name of x,y,z = 56,90,34
# x, y, z = 56, 90, 34
# print(x, y, z)
# print(x*y, y*z, z*x) 

#types of variables
# name = "Rahul"
# age = 25
# phone = "91XXX53961"
# student = True
# print(type(name), type(age), type(phone), type(student))

#hours in a week
# days = 7
# one_day = 24
# hours = days * one_day
# minutes = hours * 60
# seconds = minutes * 60
# print("hours:", hours)
# print("minutes:", minutes)
# #print("seconds:", seconds, end ="\n" , seconds)


#input from user and convert into minutes
# count = input("Enter a number: ")
# min = 60
# print("Your minutes is :", int(count) * min)



# #age into days, hours, minutes, seconds
# countt = input("Enter a age: ")
# days = int(countt) * 365
# hour = days * 24
# minutes = hour * 60
# seconds = minutes * 60
# print("Your days is :", days)
# print("Your hour is :", hour)
# print("Your minutes is :", minutes) 
# print("Your seconds is :", seconds)



# #tuple
# tuple = (1, 2, 3, 4, 5)
# print(type(tuple))

# set = {1, 2, 3, 4, 5}
# print(type(set))

# dict = {"name": "Rahul", "age": 25, "phone": "91XXX53961"}
# print(type(dict))

# list = [1, 2, 3, 4, 5]
# print(type(list))



# a = [1, "rahul", 2.5, True]
# b = {80,90}
# c = (1,2,3,4)
# d = {"name": "Rahul", "age": 25, "phone": "91XXX53961"}

# print(a[2])
# print(list(b)[0])  # Convert set to list to access by index
# print(c[3])
# print(d["name"])



#if-else
# number = int(input("Enter your number: "))
# # if number % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")

# print("even" if number %  2 == 0 else "odd")
    
    
# percentage = int(input("Enter your percentage: "))
# # if percentage > 75:
# #     print("You cant enter the Program", percentage)
# # else:
# #     print("You can enter the Program", percentage)


# print("you can enter the program" if percentage > 75 else "you cant enter the program")


# username = "rahulrangu"
# password = "Rahul@123"

# a = input("Enter your username: ")
# b = input("Enter your password: ")

# # print("Login Successfull" if a == username and b == password else "Login Failed")

# if(a == username and b == password):
#     print("Login Successfull")
# else:
#     print("Login Failed")




#range
# a = range(10)
# print(a)
# print(list(a))
# print(tuple(a))
# print(set(a))





#for loop
# a = [13, 29, 33, 44, 55]
# for i in a:
    # if(i % 2 == 0):
    #     print("Even:", i)
    # else:
    #     print("Odd:", i)
    
    
# to get duplicate values in one list 
# a = [1,2,3,1,4,5]
# b = len(a)
# for i in range(0,b):
#     for j in range(i+1,b):
#         if(a[i] == a[j]):
#             print("Duplicate found:", a[i], "at indices", i, "and", j)
            
            
# # a = [1,2,3,4,5,]
# # print(len(a))



# #while
# a = int(input("Enter the number:"))
# while(a < 20):
#     print(a)
#     a+=2



#functions
def add(a,b):
    return a + b

print(add(1,3))
print(add(5,6))
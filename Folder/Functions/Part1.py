print("Hello World")
# def greet_customer(special, sale_percent):
#     print("Hello!")
#     print("Our special today is " + special)
#     print("Everything is " + sale_percent + " off today.")
#     print("Have a great time shopping")


# greet_customer("tangerines", "70%")

def add_one(num):
    # print(num+1)
    return num + 1

x = add_one(2)
# num == 1

print(x)

x = add_one(15)

print(x)

def add_two(num):
    # print(num+1)
    if num % 2 != 0:
        return num + 1
    else:
        return num

y = add_two(15)

print(x)

def add_one_if_odd(num):
    if num % 1 != 0:
        return num +100
    else:
        return num
x = add_one_if_odd(15)

print(x)

def square_point_plus_ten(x,y):
    x_2 = x*x
    y_2 = y*y
    return x_2 , y_2

x_squared, y_squared = square_point_plus_ten(2, 4)

print(str(x_squared) + "" + str(y_squared))

x_squared, y_squared = square_point_plus_ten(1,1)

print(str(x_squared) + "" + str(y_squared))

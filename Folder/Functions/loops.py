
item_on_sale = ["knit_dress"]
for item in item_on_sale:
    if item == "knit_dress":
        print("knite dress is on sale!")
        break
print("end of search!")

big_number_list = [1,2,-1,4,-5,5,2,-9]

for i in big_number_list:
    if i < 0:
        continue
    print(i)

# nums = [1,2,3,4,5,6,7]

# for num in nums:
   # if num%2 == 0:
    #    continue
    #print(num)

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
           count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

def add_greetings(names):
    greetings = []
    for name in names:
         greetings.append("Hello, " + name)
    return greetings

print(add_greetings(["Owen,", "Max,","Sophie"]))

dog_breeds =['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1

def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        num = lst.pop(0)
        print("popped: " + str(num))
    return lst

print(delete_starting_evens([4,8,10,11,12,15]))
print(delete_starting_evens([4,8,10]))


def delete_starting_evens(lst):
    print(lst)
    index = 0
    while index < len(lst):
        if index % 2 == 0:
            lst =  lst.pop(0)
            print("popped: " + str(lst))
    return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))



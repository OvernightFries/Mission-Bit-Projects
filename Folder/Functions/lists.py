last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = [("physics"),("calculus"),("poetry"),("history")]

grades = [(98), (97), (85), (88)]


[print(values) for values in zip(subjects, grades)]

subjects.append(("Computer Science"))
grades.append((100))

gradebook = list(zip(subjects, grades))

[print(values) for values in zip(subjects, grades)]

gradebook.append(("visual arts", 93))

print(list(zip(gradebook)))

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)

print(gradebook)

names = ["jenny", "alexus"]

name1 = names[0]
print(names)
print(names[0])

# # 0, 1, 2, 3, 4 ...

# names_and_heights = [["jenny", 67, 100], ["alexus", 70, 100]]
# print("name: " + names_and_heights[1][0] + "height: " + str(names_and_heights[1][1]) + "weight: " + str(names_and_heights[1][2])) #["jenny", 67]
# print(names_and_heights[0][0] + " is " + str(names_and_heights[0][1]) + " inches tall")

# names = ["jenny", "alexus", "sam"]
# #zip() does not include extra items from the longer list if list lengths are not the same
# heights = [67, 70]

# names_and_heights = list(zip(names, heights))
# #names_and_heights == [('jenny', 67), ('alexus', 70)]

# # tuples: (x, y) and cannot be changed
# # list: [x, y]

# print(list(names_and_heights))

# print(names_and_heights[0][0])

names = ["jenny", "alexus"]
# print("Before adding \"sam\": " + str(names))
# names.append("sam")
# print("After adding \"sam\": " + str(names))
# print("hello world")
# "hello world"

# names.insert(1, "alex")
#names[1] == "alex" -> True

names[1] = "alex"

print(names)
#["jenny", "alex"]

#range(x)
#start: 0
#stop: x-1
#step: 1
# new_range = list(range(10))
# print(new_range)

# #range(x, y, z)
# #start: x
# #stop: y-1
# #step: z
# even_range = list(range(0, 21, 2))
# print(even_range)

# #range(x, y)
# #start: x
# #stop: y-1
# #step: 1

# zero_to_five = list(range(0, 6))
# print(zero_to_five)

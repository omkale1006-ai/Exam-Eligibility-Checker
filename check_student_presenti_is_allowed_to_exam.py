#  A student will not be allowed to sit in exam if his/her attendence is less than 75%
# Take following input form user
# number of classes held
# number of classes  attended.
# and print
# percentage of class attendence
# is student is allowed to sit in exam or not

numofclassattend= int(input("Enter your class attends:"))
numofclassheld= int(input("Enter your total class:"))
perofclassattend = numofclassattend/numofclassheld * 100
print(f"percentage of clases attends {perofclassattend}%")

if perofclassattend < 75:
    print("Not allowed")
else:
    print("Allowed")

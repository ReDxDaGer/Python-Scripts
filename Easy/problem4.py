name = input("please tell your name")
age = int(input("please tell your age"))

if age >= 18:
    print(f"hello {name} you are a valid voter")
elif age <18 and age >0:
    print(f"hello {name} you are not a valid voter")
else:
    print("give a valid age")

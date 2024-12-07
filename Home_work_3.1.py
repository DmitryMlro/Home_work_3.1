first_num = int(input("Введіть перше число: "))
math_operation = input("Вкажіть операцію (+,-,*,/): " )
second_num = int(input("Введіть друге число: "))
if math_operation == "+":
    print("Відповідь:", first_num + second_num)
elif math_operation == "-":
    print("Відповідь:", first_num - second_num)
elif math_operation == "*":
    print("Відповідь:", first_num * second_num)
elif (first_num and second_num != 0) and math_operation == "/":
    print("Відповідь:", first_num / second_num)
else:
    print("Дані введено некоректно, або дільник дорівнює 0")
# write your code here
memory = 0

msg = {10: "Are you sure? It is only one digit! (y / n)",
       11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
       12: "Last chance! Do you really want to embarrass yourself? (y / n)"}


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
    print(msg)


while True:
    calc = input("Enter an equation")
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    else:
        if oper == "+" or oper == "-" or oper == "*" or oper == "/":
            check(x, y, oper)
            result = 0
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                try:
                    result = x / y
                except ZeroDivisionError:
                    print("Yeah... division by zero. Smart move...")
                    continue
            print(result)
            while True:
                store_result = input("Do you want to store the result? (y / n):")
                if store_result == 'y':
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            answer = input(msg[msg_index])
                            if answer == 'y':
                                if msg_index < 12:
                                    msg_index += 1
                                    continue
                                else:
                                    memory = result
                                    break
                            elif answer == 'n':
                                break
                            elif answer != 'n':
                                continue
                    else:
                        memory = result
                        break
                elif store_result == 'n':
                    break
                else:
                    continue
                break
            while True:
                continue_calc = input("Do you want to continue calculations? (y / n):")
                if continue_calc == 'y':
                    break
                elif continue_calc != 'n':
                    continue
                elif continue_calc == 'n':
                    exit()
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
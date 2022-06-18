# write your code here
memory = float(0)
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, msg_10, msg_11, msg_12]
mod = ["+", "-", "*", "/"]


def is_one_digit(v):
    output = False
    if -10 < v < 10 and v.is_integer():
        output = True
    return output


while True:

    print(msg_0)
    x, operator, y = input().split()
    if x == "M":
        x = str(memory)
    if y == "M":
        y = str(memory)
    if x.isalpha() or y.isalpha():
        print(msg_1)
    elif operator not in mod:
        print(msg_2)
    else:
        msg = ""
        if is_one_digit(float(x)) and is_one_digit(float(y)):
            msg = msg + msg_6
        if float(x) == float(y) and operator == "/":
            msg = msg + msg_6
        if float(x) == 1 or float(y) == 1 and operator == "*":
            msg = msg + msg_7
        if (float(x) == 0 or float(y) == 0) and (operator == "*" or operator == "+" or operator == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
            print(msg)
        result = float(0)
        if operator == "+":
            result += float(x) + float(y)
            print(result)
        elif operator == "-":
            result += float(x) - float(y)
            print(result)
        elif operator == "*":
            result += float(x) * float(y)
            print(result)
        elif operator == "/":
            if float(y) != 0:
                result += float(x) / float(y)
                print(result)
            else:
                print(msg_3)
                continue
        print(msg_4)
        store_result = input()
        if store_result == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    one_digit = input()
                    if one_digit == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                            continue
                        else:
                            memory += result
                            break
                    else:
                        break
            else:
                memory += result
        print(msg_5)
        continue_calc = input()
        if continue_calc == "y":
            continue
        else:
            break

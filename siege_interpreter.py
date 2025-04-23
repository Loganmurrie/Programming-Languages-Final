def pop_char(stack):
    return chr(stack.pop()) if stack else ''

def msg_mode(stack):
    return pop_char(stack)

def cat_mode(stack):
    return pop_char(stack)

def reverse_mode(stack):
    return pop_char(stack)

def multiply_mode(stack):
    a = int(input("Enter the first number to multiply: "))
    b = int(input("Enter the second number to multiply: "))
    return str(a * b)

def repeat_mode(stack):
    word = input("Enter the string to repeat: ")
    times = int(input("Enter how many times to repeat it: "))
    return (word + '\n') * times

def run(file_path):
    stack = []
    output = ""
    mode = ""
    cat_input_loaded = False

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split()

        if parts[0] == "Tachanka":
            if parts[1] == "Bandit":
                mode = "msg"
            elif parts[1] == "Castle":
                mode = "cat"
                cat_input_loaded = False
            elif parts[1] == "Doc":
                mode = "reverse"
                cat_input_loaded = False
            elif parts[1] == "Glaz":
                mode = "multiply"
            elif parts[1] == "Frost":
                mode = "repeat"
            output = ""
        elif parts[0] == "Thermite":
            if mode in ("cat", "reverse") and not cat_input_loaded:
                user_input = input("Enter a message to echo: ")
                for ch in reversed(user_input):
                    stack.append(ord(ch))
                cat_input_loaded = True
            else:
                num = int(parts[1])
                if 0 <= num <= 127:
                    stack.append(num)
                else:
                    print("Invalid ASCII value:", num)
                    return
        elif parts[0] == "Azami":
            if mode == "msg":
                output += msg_mode(stack)
            elif mode == "cat":
                while stack:
                    output += cat_mode(stack)
            elif mode == "reverse":
                while stack:
                    output += reverse_mode(stack)
            elif mode == "multiply":
                output = multiply_mode(stack)
                break
            elif mode == "repeat":
                output = repeat_mode(stack)
                break
        else:
            print("Unknown command:", parts[0])
            return

    if mode == "reverse":
        output = output[::-1]

    print("Output:", output)

if __name__ == "__main__":
    name = input("Enter the name of the program you want to run: ").strip()
    run(name)

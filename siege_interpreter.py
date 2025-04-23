def msg_mode(stack):
    return chr(stack.pop()) if stack else ''

def cat_mode(stack):
    return chr(stack.pop()) if stack else ''

def reverse_mode(stack):
    return chr(stack.pop()) if stack else ''

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
            elif parts[1] == "Doc":
                mode = "reverse"
            elif parts[1] == "Glaz":
                mode = "multiply"
            elif parts[1] == "Frost":
                mode = "repeat"
            output = ""
        elif parts[0] == "Thermite":
            num = int(parts[1])
            stack.append(num)
        elif parts[0] == "Azami":
            if mode == "msg":
                output += msg_mode(stack)
            elif mode == "cat":
                output += cat_mode(stack)
            elif mode == "reverse":
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

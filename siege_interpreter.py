import sys
import os

def generate_reverse_program_file(user_input, output_file="reversestring.txt"):
    with open(output_file, 'w') as f:
        f.write("Tachanka Doc\n")  # Doc = reverse mode
        for char in user_input:
            f.write(f"Thermite {ord(char)}\n")
            f.write("Azami\n")

def run_siege_program(file_path, args):
    mode = None
    stack = []
    message = ""

    mode_map = {
        "Bandit": "msg",
        "Castle": "cat",
        "Doc": "reverse",
        "Glaz": "multiply",
        "Frost": "repeat"
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        tokens = line.split()

        if tokens[0] == "Tachanka":
            raw_mode = tokens[1]
            if raw_mode not in mode_map:
                raise RuntimeError(f"Unknown mode: {raw_mode}")
            mode = mode_map[raw_mode]
            message = ""
            continue

        if tokens[0] == "Thermite":
            try:
                val = int(tokens[1])
                stack.append(val)
            except ValueError:
                raise RuntimeError(f"Invalid Thermite value: {tokens[1]}")

        elif tokens[0] == "Azami":
            if not stack and mode not in ["multiply", "repeat"]:
                raise RuntimeError("Azami called but stack is empty.")
            
            if mode in ["msg", "cat", "reverse"]:
                val = stack.pop()
                message += chr(val)

            elif mode == "multiply":
                try:
                    a = int(input("Enter the first number to multiply: "))
                    b = int(input("Enter the second number to multiply: "))
                    message = str(a * b)
                    break
                except ValueError:
                    raise RuntimeError("Invalid input. Expected two integers.")

            elif mode == "repeat":
                try:
                    text = input("Enter the string to repeat: ")
                    count = int(input("Enter how many times to repeat it: "))
                    message = text * count
                    break
                except ValueError:
                    raise RuntimeError("Invalid input. Expected a string and a number.")

        else:
            raise RuntimeError(f"Unknown command: {tokens[0]}")

    print("Output:", message[::-1] if mode == "reverse" else message)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        extra_args = sys.argv[2:]

        if file == "reversestring.txt":
            text = input("What string would you like to reverse? ")
            generate_reverse_program_file(text, file)

        run_siege_program(file, extra_args)

    else:
        file = input("Enter the name of the program file you want to run (e.g., helloworld.txt): ").strip()

        if file == "reversestring.txt":
            text = input("What string would you like to reverse? ")
            generate_reverse_program_file(text, file)

        run_siege_program(file, [])

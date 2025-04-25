def pop_char(stack):
    return chr(stack.pop()) if stack else ''

def msg_mode(stack):
    return pop_char(stack)

def cat_mode(stack):
    return pop_char(stack)

def reverse_mode(stack):
    return pop_char(stack)

def run(file_path):
    stack = []
    output = ""
    mode = ""
    cat_input_loaded = False
    mult_inputs = []
    mult_result = None
    repeat_string = ""
    repeat_count = 0
    inside_repeat_loop = False
    repeat_loop_commands = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().replace('\r', '')
        if not line:
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
                mult_inputs = []
                mult_result = None
            elif parts[1] == "Frost":
                mode = "repeat"
                repeat_string = ""
                repeat_count = 0
                inside_repeat_loop = False
                repeat_loop_commands = []
            output = ""

        elif parts[0] == "Fenrir":
            if mode == "multiply":
                if len(mult_inputs) < 2:
                    if len(parts) == 2:
                        mult_inputs.append(int(parts[1]))
                    else:
                        mult_inputs.append(int(input(f"Enter number {len(mult_inputs)+1} to multiply: ")))
                else:
                    return
            elif mode == "repeat":
                if len(parts) == 2:
                    repeat_count = int(parts[1])
                else:
                    repeat_count = int(input("Enter how many times to repeat it: "))

        elif mode == "repeat":
            if parts[0] == "Iana":
                repeat_string = input("Enter the string to repeat: ")
            elif parts[0] == "Oryx":
                inside_repeat_loop = True
            elif inside_repeat_loop:
                repeat_loop_commands.append(parts[0])

        elif parts[0] == "Deimos" and mode == "multiply":
            if len(mult_inputs) == 2:
                print(f"Multiplying {mult_inputs[0]} * {mult_inputs[1]}")
                mult_result = str(mult_inputs[0] * mult_inputs[1])
            else:
                return

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
                output = output[::-1]
            elif mode == "multiply":
                if mult_result is not None:
                    output = mult_result
                else:
                    return
            elif mode == "repeat":
                if inside_repeat_loop:
                    repeat_loop_commands.append("Azami")
                    inside_repeat_loop = False
                else:
                    print(f'Printing "{repeat_string}" {repeat_count} times:')
                    if repeat_loop_commands:
                        for _ in range(repeat_count):
                            for command in repeat_loop_commands:
                                if command == "Azami":
                                    output += repeat_string + '\n'
                    else:
                        for _ in range(repeat_count):
                            output += repeat_string + '\n'
                    repeat_loop_commands = []

        else:
            return

    if mode == "repeat" and repeat_loop_commands:
        print(f'Printing "{repeat_string}" {repeat_count} times:')
        for _ in range(repeat_count):
            for command in repeat_loop_commands:
                if command == "Azami":
                    output += repeat_string + '\n'

    print("\nFinal Output:\n", output)

if __name__ == "__main__":
    name = input("Enter the name of the program you want to run: ").strip()
    run(name)

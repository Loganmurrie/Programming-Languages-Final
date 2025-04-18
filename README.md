#WELCOME TO 
#TOM CLANCY'S SEIGE CODE

**Siege Code** is a custom stack-based interpreted language built using the names of operators from *Tom Clancy's Rainbow Six Siege*. It reads `.txt` files that contain only operator names and interprets them as commands, modes, and data instructions.

This project includes an interpreter (`siege_interpreter.py`) and several example Siege programs like printing "Hello World", reversing a string, multiplying numbers, repeating words, and forming sentences.

---

## Siege Code

| Operator     | Role                          | Description                                      |
|--------------|-------------------------------|--------------------------------------------------|
| **Tachanka** | Program starter                | Must be the first word in the file. Used as `Tachanka <mode>` |
| **Bandit**   | `msg` mode                     | Print characters from pushed ASCII values        |
| **Castle**   | `cat` mode                     | Build a sentence from pushed ASCII values        |
| **Doc**      | `reverse` mode                 | Prompts user for input string and prints reversed version |
| **Glaz**     | `multiply` mode                | Prompts user for two numbers and prints their product |
| **Frost**    | `repeat` mode                  | Prompts user for a string and count; repeats it  |
| **Thermite** | Push data                      | Followed by an ASCII number to push |
| **Azami**    | Execute / pop & print          | In `msg`, `cat`, and `reverse` modes, pops value from stack and builds output; in `multiply`, `repeat`, and `reverse`, it triggers user input prompt and prints result |

---

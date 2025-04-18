#  Welcome to Tom Clancy's Seige Interpreter 

**Siege Code** is a custom stack-based interpreted language using operator names from the famous game "Tom Clancy's Rainbow Six Seige". 

---

## Siege Code

| Operator     | Description                                      |
|--------------|--------------------------------------------------|
| **Tachanka** | Must be the first word in the file. Used as `Tachanka <mode>` |
| **Bandit**   | Print characters from pushed ASCII values        |
| **Castle**   | Build a sentence from pushed ASCII values        |
| **Doc**      | Prompts user for input string and prints reversed version |
| **Glaz**     | Prompts user for two numbers and prints their product |
| **Frost**    | Prompts user for a string and count; repeats it  |
| **Thermite** | Followed by an ASCII number to push |
| **Azami**    | In `msg`, `cat`, and `reverse` modes, pops value from stack and builds output; in `multiply`, `repeat`, and `reverse`, it triggers user input prompt and prints result |

---

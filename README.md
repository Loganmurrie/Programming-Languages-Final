#  Welcome, Operator, to the **Tom Clancy's Siege Interpreter** 

<p align="center">
  <img src="assets/Rainbow.gif" alt="Siege Code Animation" />
</p>

>  *"Breach the stack. Secure the logic. Execute the mission."*  
> This isn't your ordinary language. This is **Siege Code** — a custom **stack-based** language written in **Python**, where your commands are led by Operators from *Rainbow Six Siege*. 

Whether breaching a door or pushing ASCII, you're in for an elite coding op.

---

## What is Siege Code?

Siege Code is a **fun and simple programming language** designed for beginners.

It’s based on a concept called a **stack** — think of it like a pile of plates:
- You can **push** things on top (like letters or numbers).
- You can **pop** the top item off to use it.

Siege Code uses this stack to build up letters, sentences, math results, and more — all by writing commands using Siege Operators.

---

##  Siege Protocol: **Operator Commands**

Here are all the Operators you’ll use in Siege Code:

| **Operator** | **What It Does** | **Type** |
|--------------|------------------|----------|
| **Tachanka** | Mission Briefing. Always **start** your script with `Tachanka <mode>`. This tells Siege Code which mode you're using. | Setup |
| **Bandit**   | Comms Mode. Lets you push letters with `Thermite`, then print them using `Azami`. | **Mode** |
| **Castle**   | Sentence Constructor. You type a sentence, and it prints it back. | **Mode** |
| **Doc**      | Reversal Expert. Type something, and it prints it backwards. | **Mode** |
| **Glaz**     | Sniper Math. Multiplies two numbers you enter. | **Mode** |
| **Frost**    | Echo Trap. Repeats a word N times. | **Mode** |
| **Thermite** | ASCII Charge. `Thermite 65` pushes the letter **A** to the stack (since 65 is the ASCII code for A). | Command |
| **Azami**    | Print & Prompt. Pops the top value and prints it. Use this after `Thermite`. | Command |

> 💡 **Reminder:** You must start every program with `Tachanka <mode>`, or Siege Code won't know what to do!

---

## ✅ Example Deployment

Let’s say you want to print the word `Hello`.

Your program (save this in a file like `hello.txt`) would look like:

```text
Tachanka Bandit
Thermite 72
Azami
Thermite 101
Azami
Thermite 108
Azami
Thermite 108
Azami
Thermite 111
Azami

 ```

## Expected Output 

```
Hello
```

##  Final Briefing

You’re not just writing code — you're launching missions.  
From `Glaz`'s math shots to `Doc`'s reverse tactics, every line is tactical.  
Deploy your `.siege` files, command your operators, and **let Siege Code breach the system**. 

>  *“Complete the Mission and Execute the Defuse, Operator.”*

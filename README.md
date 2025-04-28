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

<p align="center">
  <img src="assets/Azami.gif" alt="Siege Code Animation" />
</p>

Here are all the Operators you’ll use in Siege Code:

| **Operator** | **What It Does** | **Type** |
|--------------|------------------|----------|
| **Tachanka** | Mission Briefing. Always **start** your script with `Tachanka <mode>`. This tells Siege Code which mode you're using. | Setup |
| **Bandit**   | Quick Comms: Let's you push letters with `Thermite`, then print them using `Azami`. | **Mode** |
| **Castle**   | Sentence Constructor:  You type a sentence, and it prints it back. | **Mode** |
| **Doc**      | Reversal Expert: Type something, and it prints it backwards. | **Mode** |
| **Glaz**     | Sniper Math: Let the interpreter know that you are wanting to multiply. | **Mode** |
| **Frost**    | Echo Trap: Let the interpreter know that you are wanting to repeat. | **Mode** |
| **Fenir**    | F-NATT Mine:  It takes in integer input (whether inputted or inside the file). | Input | 
| **Iana**     | Gemini Replicator:  Takes in any word/sentence | Input | 
| **Deimos**   | DeathMark Tracker:  When Deimos is called with Glaz, this will activate our multiplying function of two `Fenrir` Integers | Command | 
| **Oryx**     | Remah Dash: When called with Frost, this will activate our repeating process of the string a `Fenrir` amount| Command | 
| **Thermite** | ASCII Charge: `Thermite 65` pushes the letter **A** to the stack (since 65 is the ASCII code for A). | Command |
| **Azami**    | Print & Prompt: Pops the top value and prints it. | Command |

> 💡 **Reminder:** You must start every program with `Tachanka <mode>`, or Siege Code won't know what to do!

---

## ✅ Example Deployments

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

## How to use Fenrir : 

Fenrir can be used in two ways : 

1.) You can say `Fenrir 12` and it wil act like you have inputted `12` as your integer.

```Text
Tachanka Glaz
Fenrir 12
Fenrir 12
Deimos
Azami

```
## Expected Output :

```
Final Output: 144
```

OR

2.) You can enter it inside the program
```Text
Tachanka Glaz
Fenrir 
Fenrir 
Deimos
Azami
```

## Expected Output : 

```
Enter number 1 to multiply: 12
Enter number 2 to multiply: 12

Final Output : 144

```


##  Final Briefing

<p align="center">
  <img src="assets/Mozzie.gif" alt="Siege Code Animation" />
</p>

You’re not just writing code — you're launching missions.  
From `Glaz`'s math shots to `Doc`'s reverse tactics, every line is tactical.  
Deploy your `.siege` files, command your operators, and **let Siege Code breach the system**. 

>  *“Complete the Mission and Execute the Defuse, Operator.”*

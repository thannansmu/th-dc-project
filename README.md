# Taylor Hannan's Final Project for CS 2353   Fall 2021
## How to run:
#### Option 1: Running on local machine
1. Make sure you have Python3 installed
2. Make sure you have the Flask library installed. 
   To do this, enter the following into the terminal:
   ```pip3 install flask```

3. Enter the following terminal command: ```python3 main.py```
4. Text should pop up in the terminal and it should give you a link
5. Paste the link in a web browser (Chrome, Firefox, Safari, etc)


#### Option 2: Running on Website
You can also run the program using the following link: https://thannansmu.pythonanywhere.com/truth_table_home


## Steps for using the program
1. Enter formula into the text box
2. Press enter

## Syntax
- Characters you can use for the symbols are on the main page
- Conclusion is optional, but needed if more than one premise
- Conclusion can not have new variable not seen in premises
- Must have at least one premise (no conclusion only formulas)
- Simplify negations before typing them in. Example: ~~P must be typed in as P
- IMPORTANT: Program does not assume parentheses, so you must type them out
Example: P /\ Q -> R must be typed in as (P /\ Q) -> R
- HOWEVER, you don't need outermost parentheses. Example: If P /\ Q is by itself, type it in as is


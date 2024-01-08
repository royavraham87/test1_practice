<h1>
This is my Readme file for the first test practice

<p>
This progrem is calling for functions that are located on different libreries and link them together. the program does the following things:
<br>
<br>
1. the modul calc() is activated with a number. then it stores the number in a variable called "result" and print the result of the number multiplied by 2. "print(results)"
  <br><br>
2. following the activation of calc() another function that is called activate_calc is triggered. this function uses a global variable called calc_activated that it used as a flag to determine the program has been activated. the condition of the flag is then transfered to the function waga()
  <br><br>
3. the function waga() checks if the function calc() has been activated (calc_activated = True) if the answer is True it calls for the function calc() again and activate the function with another number {maybe a better approach is to use return to get the number from calc without activating it again} the function then returns the phrase "Baga" and the result of the new activation of the function calc (printed in the main)
  <br><br>
if the function calc wasn't activated (calc_activated = false) before waga() won't work and the massage "Error: calc wasn't activated"
4. the function check_array() receive a list [array of numbers] and checks if there are duplicate numbers in the array. it creates a new array called "duplicates" and put all the duplicate numbers there and then return these values to the main where they are printed.
  <br><br>
5. the function sort_array receive a list and return the list sorted and then it is printed in the main

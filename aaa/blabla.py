# blabla.py

from aaa.bbb.samp import calc

calc_activated = False  # Global flag variable to track calc activation

def waga():
    global calc_activated  # Use the global flag variable
    
    if calc_activated:
        result = calc(5)  # Assuming calc function is imported
        print("Function calc was activated successfully before")
        return "Baga " + str(result)
    else:
        print("Error: calc wasn't activated")
        return False

def check_array(ar):
    duplicates = set()
    for i in ar:
        counter = 0
        for j in ar:
            if i == j:
                counter += 1
        if counter > 1:
            duplicates.add(i)
    
    return duplicates

def sort_array(ar):
    return sorted(ar)

def activate_calc(result):
    global calc_activated
    calc_activated = True if result is not None else False

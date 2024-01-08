# app.py

from aaa.bbb.samp import calc
from aaa.blabla import check_array, sort_array, waga, activate_calc

def main():
    result = calc(3)  # Call calc first
    activate_calc(result)  # Update calc_activated flag based on the result
    
    print(result)
    print(check_array([2, 3, 4, 7, 4]))
    print(waga())
    print(sort_array([2, 3, 4, 7, 4]))

if __name__ == "__main__":
    main()

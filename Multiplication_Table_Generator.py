import pyinputplus as pyip
import sys

#Define Function
def create_table():

    #Define Variables
    base_number = pyip.inputNum("What is the base number you would like to generate a multiplication table for?")
    max_row_number = pyip.inputNum("What is the maximum amount of rows you would like to generate?", min=1)
    row_counter = 1

    #Loop and Print Results
    while row_counter <= max_row_number:
        result = base_number * row_counter
        print(f"{base_number} X {row_counter} = {result}")
        row_counter += 1
    
    #User Input to Determine Next Step
    next_step = pyip.inputYesNo("Would you like to create another multiplication table? (y/n)")
    
    # 'yes' response re-runs the function, 'no' answer ends the script
    if next_step == 'yes':
        create_table()
    else:
        sys.exit()

create_table()

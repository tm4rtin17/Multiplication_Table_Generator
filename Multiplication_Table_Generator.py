import pyinputplus as pyip

#Define Function
def create_table():

    #Define Variables
    base_number = pyip.inputNum("What is the base number you would like to generate a multiplication table for?")
    max_row_number = pyip.inputNum("How many rows would you like to generate?", min=1)
    row_counter = 1

    #Loop and Print Results
    while row_counter <= max_row_number:
        result = base_number * row_counter
        print(f"{base_number} X {row_counter} = {result}")
        row_counter += 1

#Run Initial Function  
create_table()

#Loop allows the user infinite table creations
while True:
    next_step = pyip.inputYesNo("Would you like to create another multiplication table? (y/n)") #(y/n) User Input to Determine Next Step
    if next_step == 'yes':
        create_table()
    else:
        print("Thank you for using the Multiplication Table Generator! Goodbye!")
        break




from employee import Employee

while(True):
    emp = Employee()
    print("----------- Welcome Employee -----------")
    print("1. Add a Record")
    print("2. Search for a record using id")
    print("3. Delete a record using id")
    print("4. Edit a record using id.")
    print("5. Display all records.")
    print("6. Exit")

    try:
        choice = int(input("Enter Your Choice = "))
    except ValueError:
        print("Enter a Valid Choice Format!")
        break
    
    if(choice == 1):
        emp.AddRecord()
    elif(choice == 2):
        emp.SearchRecord()
    elif(choice == 3):
        emp.DeleteRecord()
    elif(choice == 4):
        emp.EditRecord()
    elif(choice == 5):
        emp.Display()
    elif(choice == 6):
        print("Thanks For visiting us!")
        break
    else:
        print("Enter a Valid Number!")

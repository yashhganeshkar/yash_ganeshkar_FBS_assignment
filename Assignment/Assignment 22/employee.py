
from prettytable import PrettyTable

class Employee:

    dataPath = "/home/yashh_ganeshkar/DailyDev/FirstBit/Core Python/Assignments/Assignment 22/data.txt"

    def __init__(self):
        self.eid = 0
        self.ename = "NA"
        self.basicPay = 0
    
    def AddRecord(self):
        try:
            self.eid = int(input("Enter Your Employee ID = "))
            if(len(str(self.eid)) > 4):
                raise ValueError
            
            self.ename = input("Enter Employee Name = ").strip()
            self.basicPay = int(input("Enter Employee Basic Pay = "))

            with open(Employee.dataPath,"a") as data:
                row = f"{str(self.eid).strip()},{self.ename},{str(self.basicPay).strip()}\n"
                data.write(row)
            
            print("Record Add Successfully!")

        except ValueError:
            print("Employee ID should not have Digits more than 4!")
            Employee.AddRecord(self)
    
    def SearchRecord(self):
        try:
            eid = int(input("Enter ID = "))
            if(len(str(self.eid)) > 4):
                    raise ValueError
        except ValueError:
            print("Employee ID should not have Digits more than 4!")
            Employee.SearchRecord(self)

        table = PrettyTable()

        with open(Employee.dataPath,'r') as data:
            for line in data:
                if(line.strip()):
                    parts = line.split(',')
                    if(str(eid) == parts[0]):
                        table.field_names = ["EmpID","Emp Name","Basic Pay"]
                        table.add_row([parts[0],parts[1],parts[2]])
                        print(table)
                        break
                
            else:
                print("ID Not Found!")

    def DeleteRecord(self):
        try:
            eid = int(input("Enter ID = "))
            if(len(str(self.eid)) > 4):
                    raise ValueError
        except ValueError:
            print("Employee ID should not have Digits more than 4!")
            Employee.SearchRecord(self)
        
        lines_to_keep = []

        with open(Employee.dataPath, 'r') as data:
            for line in data:
                if(line.strip()):
                    parts = line.split(',')
                    if(str(eid) != parts[0].strip()):
                        lines_to_keep.append(line.strip())
        print(lines_to_keep)

        with open(Employee.dataPath,'w') as data:
            for line in lines_to_keep:
                row = f"{line}\n"
                data.write(row)
        print(f"{eid} Record is removed!")
    
    def EditRecord(self):
        try:
            eid = int(input("Enter ID = "))
            if(len(str(self.eid)) > 4):
                    raise ValueError
        except ValueError:
            print("Employee ID should not have Digits more than 4!")
            Employee.SearchRecord(self)

        updated_data = []

        with open(Employee.dataPath,'r') as data:
            for line in data:
                if(line.strip()):
                    parts = line.split(',')
                    if(str(eid) == parts[0].strip()):
                        ename = input("Enter Employee Name = ").strip()
                        try:
                            basicPay = float(input("Enter Your Basic Pay = "))
                        except ValueError:
                            basicPay = ''.join(parts[2])
                        
                        if(not ename):
                            ename = parts[1].strip()

                        updatedRecord = f"{parts[0].strip()},{ename},{str(basicPay).strip()}"
                        updated_data.append(updatedRecord)
                    else:
                        updated_data.append(line.strip())

        with open(Employee.dataPath, 'w') as data:
            for line in updated_data:
                row = f"{line.strip()}\n"
                data.write(row)
        
        print(f"{eid} Record Updated Successfully!")
    
    def Display(self):
        table = PrettyTable()

        with open(Employee.dataPath, 'r') as data:
            for line in data:
                if(line.strip()):
                    parts = line.split(',')
                    table.field_names = ["EmpID","Emp Name","Basic Pay"]
                    table.add_row([parts[0],parts[1],parts[2]])
        print(table)
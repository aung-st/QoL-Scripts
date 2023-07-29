import datetime 
import pandas as pd 
import os.path as path

class expiry():
    def __init__(self) -> None:
        if path.exists("data.csv"):
            self.data = pd.read_csv("data.csv")
        else:
            columns = ["Name","Expiry_Date"]
            self.data = pd.DataFrame(columns=columns)

    def add(self):
        print("Enter details in the following order: Name, Expiry_Date")
        name = input("Enter item name: ")
        y = int(input("Enter year of expiry: "))
        m = int(input("Enter month of expiry: "))
        d = int(input("Enter day of expiry: "))


        self.data = self.data.append({"Name":name, "Expiry_Date":datetime.datetime(y,m,d)},ignore_index = True)
        self.data.to_csv("data.csv",index=False)
        self.display()

    def delete(self):
        self.display()


    
    def display(self):
        print("Here are the following items that need to be used, in order.")
        print(self.data)
        print("""
        1: Add item
        2: Delete item
        3: Exit       
        """)
        option = int(input("Enter Option: ")) 

        if option == 1:
            self.add()
        elif option == 2:
            self.delete()
        elif option == 3:
            exit
        

if __name__ == "__main__":
    #date = datetime.datetime(2021, 3, 28) 
    #print(date)
    expiry().display()
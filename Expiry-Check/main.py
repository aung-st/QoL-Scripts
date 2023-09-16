from database import database 
from datetime import date
from datetime import datetime
class main():
    def __init__(self) -> None:
        self.database = database()
        self.connection = self.database.connect()
        self.database.create_table()
        self.menu()

    def expiry_date_check(self,items):
        today = date.today()
        print("\n")
        print("The current date is: ",today,)

        expiring_within_a_week = []
        expired = []
        for item in items:
            year,month,day = item[2].split('-')
            item_date = datetime(int(year),int(month),int(day)).date()

            if (item_date - today).days < 0:
                expired.append(item[1])

            elif (item_date - today).days <= 7:
                expiring_within_a_week.append(item[1])      

        if expired:  
            print("The following has expired and will be deleted from the table: ")
            print([item for item in expired])
            for item in expired:
                self.database.delete(item)
            print("------------------------------------------")     
        if expiring_within_a_week:
            print("The following will expire within the next 7 days, please use them soon: ")
            print([item for item in expiring_within_a_week])
    
    def menu(self):
        MENU_PROMPT = """\n-- La Mesa De Café --

        Please choose one of these options:

        1) See all items
        2) Add a new item
        3) Delete item
        4) Exit
        Option: \n"""

        while(user_input := int(input(MENU_PROMPT))) != 4:
            if user_input == 1:
                items = self.database.display()
                print("\n")
                for item in items:
                    print(item)
                self.expiry_date_check(items)
            elif user_input == 2:
                name = input("Enter Name of item: ")
                year = input("Enter Year: ")
                month = input("Enter Month: ")
                day = input("Enter Day: ")
                date = "-".join((year,month,day))
                self.database.add(name,date)
                print("Item Added: "+ name)
            elif user_input == 3:
                name = input("Enter name of item: ")
                self.database.delete(name)
                print("Item deleted")

            
if __name__ == "__main__":
    main()
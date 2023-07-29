from database import database 

class main():
    def __init__(self) -> None:
        self.database = database()
        self.connection = self.database.connect()
        self.database.create_table()
        self.menu()
    
    def menu(self):
        MENU_PROMPT = """\n-- La Mesa De Café --

        Please choose one of these options:

        1) See all items
        2) Add a new item
        3) Delete item
        4) Exit
        Option: """

        while(user_input := int(input(MENU_PROMPT))) != 4:
            if user_input == 1:
                items = self.database.display()
                for item in items:
                    print(item)
            elif user_input == 2:
                name = input("Enter Name of item: ")
                year = input("Enter Year: ")
                month = input("Enter Month: ")
                day = input("Enter Day: ")
                date = "-".join((year,month,day))
                self.database.add(name,date)
                print("Item Added: "+ name)

            
if __name__ == "__main__":
    main()
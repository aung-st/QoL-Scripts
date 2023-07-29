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
                database.display(self.connection)
            elif user_input == 2:
                name = input("Enter Name of item: ")
                year = int(input("Enter Year: "))
                month = int(input("Enter Month: "))
                day = int(input("Enter Day: "))
                date = "-".join(year,month,date)
                print(date)
                #database.add(name,date)

            
if __name__ == "__main__":
    main()
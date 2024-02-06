class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        user_input = input(
            """
        Hi! How Can I Help You?
        1. Press 1 to create a Pin
        2. press 2 to change Pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. anything else to exit

        """
        )
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("enter your pin:- ")
        self.pin = user_pin

        user_balance = int(input("enter balance:- "))
        self.balance = user_balance

        print("pin created succesfully")
        self.menu()

    def change_pin(self):
        old_pin = input("enter old pin ")

        if old_pin == self.pin:
            new_pin = input("enter new pin ")
            self.pin = new_pin
            print("pin change successful..")
            self.menu()
        else:
            print("cannot change pin")
            self.menu()

    def check_balance(self):
        user_pin = input("enter your pin ")

        if user_pin == self.pin:
            print("*" * 50)
            print("your balance is Rs", self.balance)
            print("*" * 50)
            self.menu()
        else:
            print("You enter wrong pin!")
            self.menu()

    def withdraw(self):
        user_pin = input("enter the pin :- ")
        if user_pin == self.pin:
            amount = int(input("enter the amount :- "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("*" * 50)
                print("withdrawl successful, your balance is :- ", self.balance)
                print("*" * 50)
            else:
                print("sorry! no sufficient balance :- ")
        else:
            print("please enter correct pin :- ")
        self.menu()


obj = ATM()
obj.menu()

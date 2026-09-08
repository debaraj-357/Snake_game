class Menu:

    def select_speed(self):
        print()
        print("========SELECT SPEED ========")
        print()
        print("1. Speed = 2")
        print("2. Speed = 3")
        print("3. Speed = 4")
        print("4. Speed = 5")
        print("5. Speed = 6")
        print("6. Speed = 7")
        print("7. Speed = 8")

        while True:
            choice =input("Enter your choice:- ")

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                return int(choice)+1
            print("Invalid choice. Please enter 1-7")
        


    def show(self):
        print("===============================")
        print("           SNAKE GAME          ")
        print("===============================")
        print()
        print("[1]. Start Game")
        print("[2]. select Speed")
        print("[3]. High Score")
        print("[4]. How to Play")
        print("[5]. Exit")

        while True:

            choice =input("enter your choice :- ")

            if choice in ["1", "2", "3", "4", "5"]:
                return choice

            print("invalid choice. Please enter 1-5")

    
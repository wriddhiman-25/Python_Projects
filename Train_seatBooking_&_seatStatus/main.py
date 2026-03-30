class Train:
    print("🙏WELCOME TO INDIAN RAILWAYS🙏")
    seats={
        13150:12,
        13147:7,
        13142:17
    }

    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    def checkStatus(self):
        if self.trainNo in self.seats:
            print(f"Available seats on Train no. {self.trainNo} is {self.seats[self.trainNo]}")
        else:
            print("Invalid train Number.")
    
    def book(self,ticket):
        if self.trainNo in self.seats:
            if self.seats[self.trainNo]>=ticket:
                self.seats[self.trainNo]-=ticket
                print(f"Congratulations 🎉 your {ticket} ticket(s) has been booked for Train no. {self.trainNo} successfully. ")
                print("Happy Journey 😊")
            else:
                print(f"We are Extremly Sorry!😓 only {self.seats[self.trainNo]} seats are available on Train no. {self.trainNo}")

train=Train(int(input("Enter the Train Number :")))
train.checkStatus()

if train.trainNo in train.seats:
    want_to_book = input("Do you want to buy tickets? (yes/no): ")

    if want_to_book == "yes":
        train.book(int(input("How many tickets do you want to buy: ")))
    elif want_to_book == "no":
        print("Thank you for checking the seat status.")
    else:
        print("Invalid choice. Please enter yes or no.")

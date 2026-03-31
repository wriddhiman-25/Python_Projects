class Account:
    def __init__(self, bal, acc_no, pin):
        self.bal = bal
        self.acc_no = acc_no
        self.pin = pin

    def verify_pin(self):
        entered_pin = int(input("Enter the 4 digit PIN code: "))
        if entered_pin == self.pin:
            return True
        print("Incorrect PIN. Transaction cancelled.")
        return False

    def debit(self, amount):
        if not self.verify_pin():
            return
        self.bal -= amount
        print(f"Dear Customer Rs.{amount} has been debited from account no. {self.acc_no}")
        print(f"Remaining balance in your account: Rs.{self.bal}")

    def credit(self, amount):
        if not self.verify_pin():
            return
        self.bal += amount
        print(f"Dear Customer Rs.{amount} has been credited to account no. {self.acc_no}")
        print(f"Remaining balance in your account: Rs.{self.bal}")


acc1 = Account(125000, 389894125, 2004)
acc1.debit(int(input("Enter the amount you want to debit: ")))
acc1.credit(int(input("Enter the amount you want to credit: ")))

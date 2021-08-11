class Atm:
    def __init__(self,cardnumber,pin):
        self.carnumber = cardnumber
        self.pin = pin
    def checkbalance(self):
        print("balance = 50000")
    def withdrawel(self,amount):
        new_amount = 50000-amount
        print("u have withdrawn" + str(amount)+"your remaining balance is"+str(new_amount) )
def main():
    card_number = input("insert your card number")
    pin_number = input("insert your pin number")
    new_user = Atm (card_number,pin_number)
    print("choose your activity")
    print("1.balance enquiry, 2. cash withdrawel")
    activity = int(input("enter the activity numeber"))
    if (activity == 1):
        new_user.checkbalance()
    elif(activity == 2):
        amount = int(input("enter the amount"))
        new_user.withdrawel(amount)
    else:
        print("enter a valid number")
if __name__ =="__main__":
    main()
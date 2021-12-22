class atm:
    def __init__(self, user_card_number, pincode) :
        self.user_card_number = user_card_number
        self.pincode = pincode

    def cashWithdrawal(self):
        print("This is cash withdrawal point")
    
    def BalanceCheck(self):
        print("check your balance here")
    
ic = atm(200347, 2508)
ic.cashWithdrawal()
ic.BalanceCheck()


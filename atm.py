class atm(object):
    def __init__(self,atm_card_number,enquiry,account_balace):
        self.atm_card_number=atm_card_number
        self.enquiry=enquiry
        self.account_balace=account_balace
        
        
    def withdraw(self):
        print('Cash Withdrawn')
        
    def deposit(self):
        print('Cash Deposited')
    
    def enquire(self):
        print('Enquired') 
    
        
          


vihaan=atm(135792468,'Nothing',50000)

print(vihaan.withdraw())
print(vihaan.deposit())
print(vihaan.enquire())
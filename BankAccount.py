class BankAccount:
    def __init__(self, account_holder, balence):
        self.account_holder = account_holder
        self.balence = balence
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balence += amount
            print(f'Se ha depositado {amount}$:  Saldo actual :{self.balence}$')
        else:
            print('No se puede Depositar, Cuenta inactiva')
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balence:
                self.balence -= amount
                print(f'Se ha retirado {amount}$: Saldo actual :{self.balence}$') 

    def desactive_account(self):
        self.is_active = False
        print(f'La Cuenta ha sido Desactivada')

    def active_account(self):
        self.is_active = True
        print(f'La Cuenta ha sido Activada')

account1 = BankAccount('Melisa', 3000)
account2 = BankAccount('Mike', 1200)

account1.deposit(100)
account2.deposit(600)
account2.desactive_account()
account2.active_account()
account2.deposit(200)
account1.withdraw(100)
account2.withdraw(800)
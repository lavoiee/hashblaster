from accountController import AccountController

accControl = AccountController()
x = accControl.accountlist
for i in range(len(x)):
    print(x[i].__str__())



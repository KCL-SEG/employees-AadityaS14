"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission=""):
        super().__init__(name, commission)
        self.salary = salary
    
    def get_pay(self):
        if self.commission:
            return self.salary + self.commission.get_commission()
        else:
            return self.salary
    
    def __str__(self):
        print(f"{self.name} works on a monthly salary of {self.salary}{str(self.commission)}. Their total pay is {self.get_pay()}.")
        return f"{self.name} works on a monthly salary of {self.salary}{str(self.commission)}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hours, wage, commission=""):
        super().__init__(name, commission)
        self.hours = hours
        self.wage = wage
    
    def get_pay(self):
        if self.commission:
            return (self.hours * self.wage) + self.commission.get_commission()
        else:
            return self.hours * self.wage
    
    def __str__(self):
        print(f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour{str(self.commission)}. Their total pay is {self.get_pay()}.")
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour{str(self.commission)}. Their total pay is {self.get_pay()}."


class BonusCommission():
    def __init__(self, bonus):
        self.bonus = bonus
    
    def get_commission(self):
        return self.bonus
    
    def __str__(self):
        return f" and receives a bonus commission of {self.bonus}"

    
class ContractCommission():
    def __init__(self, contracts, per_contract):
        self.contracts = contracts
        self.per_contract = per_contract
    
    def get_commission(self):
        return self.contracts * self.per_contract
    
    def __str__(self):
        return f" and receives a commission for {self.contracts} contract(s) at {self.per_contract}/contract"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, BonusCommission(600))

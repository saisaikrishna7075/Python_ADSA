'''
Abstraction : It hides the internal Implementation , shows the essentiaal Functions to the


Ex :
External :

ATM
 |
Card
 |
Enter PIN
 |
Withdraw
 |
Cash Draw

Internal :
1. Bank Details
2. Communication between ATM and Bank Server
3. PIN Hides

#Implement Abstraction in Python:
1. Python provides amodule called -->
2. With abc moule --> Abstract Classes
Abstract Class : Abstract classes are the class



from abc import ABC, abstractmethod

# abc --> module
# ABC --> Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def sound(self):
        print("Vehicle gives sond")
class Car(Vehicle):
    def sound(self):
        print("Car make sound")
v = Vehicle()
v.sound()
c = Car()
c.sound()
'''
#Write apython code using Abstraction for a payment (UPI & Paytm)?
from abc import ABC as Kalyani, abstractmethod
class Payment(Kalyani):
    @abstractmethod
    def Trans(self,amount):
        pass
class UPI(Payment):
    def Trans(self,amount):
        print("Trans of Ruppes",amount ,"Throught UPI")
class Paytm(Payment):
    def Trans(self, amount):
        print("Trans of Ruppes",amount ,"Throught paytm")
u = UPI()
u.Trans(500)
p = Paytm()
p = Trans(1000)
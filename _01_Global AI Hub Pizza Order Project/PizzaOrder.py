import csv
import datetime
#Pizza main Class
class Pizza():
    def __init__(self,description,price):
        self.description=description
        self.price=price
    
    def get_description(self):
        return self.description

    def get_coast(self):
        return self.price

#Pizza subclasslar
class ClassicPizza(Pizza):
    def __init__(self):
        self.description="Icerik :PizzaSosu, Sucuk, Salam, Sosis, Misir, Zeytin, Mantar, Yesilbiber, Kirmizi tatli biber, ve Mozerella Peynir "
        self.price=132.95
 
     
class MargheritaPizza(Pizza):
    def __init__(self):
        self.description="Icerik : PizzaSosu ,Domates, Mozarella, Fesleğen ve Zeytinyağı"
        self.price=100

class TurkishPizza(Pizza):
    def __init__(self):
        self.description="Icerik : PizzaSosu , Sucuk, Pastirma, Biber, ve Mantar"
        self.price=140
 
class NapoliPizza(Pizza):
    def __init__(self):
        self.description="Icerik : PizzaSosu ,Domates, Feslegen, Dilimlenmis Mozarella ,Sizma zeytinyagi ve Parmesan"
        self.price=110.85




#Decorator Main class inheritance from Pizza Class
class Decorator(Pizza):
    def __init__(self,description,price):
        super().__init__(self,description,price)
           
    def get_description(self):
        return self.description
    def get_coast(self):
        return self.price


#Decorator subclass
class Olive(Decorator):
    def __init__(self):
       self.description="Ilave Zeytin"
       self.price=12
class Mushroom(Decorator):
    def __init__(self):
        self.description="Ilave Mantar"
        self.price=20

class GoatCheese(Decorator):
    def __init__(self):
        self.description="Ilave Keçi Peyniri"
        self.price=23
    
class Meat(Decorator):
    def __init__(self):
        self.description="Ilave Et"
        self.price=50
    
class Onion(Decorator):
    def __init__(self):
        self.description="Ilave Sogan"
        self.price=9.90
    
class SweetCorn(Decorator):
    def __init__(self):
        self.description="Ilave Misir"
        self.price=14.99

#Pizza Order Function
def orderPreference():
    pizzaChoise=int(input("Lütfen Pizzanızı Seçiniz : "))
    global order 

    if pizzaChoise>0 and pizzaChoise<=4:
    
        match pizzaChoise:
            case 1:
                order=ClassicPizza()

            case 2:
                order=MargheritaPizza()
                
            case 3:
                order=TurkishPizza()
                
            case 4:
                order=NapoliPizza()
    
    else:
        print("Menüye Uygun Bir Değer Giriniz !!! ")
        orderPreference()

    return order 

#Sauce Order Funtion
def saucePreference():
    sauceChoise=int(input("Lütfen Eksta Sos Tercihinizi Giriniz *** 1 Adet Sos Seçebilirsiniz *** : "))
    global sauce
    if sauceChoise>10 and sauceChoise<=16:
        match sauceChoise:
            case 11:
                sauce=Olive()
                
            case 12:
                sauce=Mushroom()
                
            case 13:
                sauce=GoatCheese()
                
            case 14:
                sauce=Meat()
                
            case 15:
                sauce=Onion()
                
            case 16:
                sauce=SweetCorn()
                
        
    else :
        print("Menüye Uygun bir Değer Giriniz !!!")
        saucePreference()
    return sauce

#Main Function
def main():
    
    #Menu 
    menu=open("Menu.txt","r")
    print(menu.read())

    
    order= orderPreference() 
    sauce=saucePreference()

    print(f"{Pizza}",order.get_description())
    print("Pizza Fiyat : ", order.get_coast())
    print(sauce.get_description())
    print("Sos Fiyat : ", sauce.get_coast())

   
    TotalPrice=order.get_coast()+sauce.get_coast()
    print("Ödenecek toplam Tutar : ",TotalPrice)

    idCard=str(input("TC kimlik numaranızı giriniz : "))
    print("Kimlik Numaranız : ", idCard)
    
    creditCardNo=str(input("Kredi Kartı Numaranızı Giriniz : "))
    creditCardPassword=str(input("Kredi Kartı Şifrenizi Giriniz : "))

    print(f"Kredi Kartı Numaranız : {creditCardNo}", f"Kredi Kartı Şİfreniz : {creditCardPassword}")

    orderTime=datetime.datetime.now()
    print("Sipariş Zamanı : ", orderTime.strftime("%d.%m.%Y / %X"))

    #Write CSV File
    orderInfo=[idCard,creditCardNo,creditCardPassword,order.get_description(),sauce.get_description(),TotalPrice,orderTime]
    with open("Orders_Database.csv","a") as Orders_Database:
        write_customers=csv.writer(Orders_Database)
        write_customers.writerow(orderInfo)
    print()

main()



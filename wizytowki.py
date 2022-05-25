from faker import Faker
fake = Faker()

class Card:
    def __init__(self,typ, name, phone):
        self.typ = typ
        self.name = name
        self.phone = phone
        
        
class BaseContact(Card):
    def __init__(self, type, name, phone, mail):
       super().__init__("Base", name, phone)
       self.type = type
       self.mail = mail
    
    def contact(self):
        print(f"I dial the number {self.phone} and call {self.name}")
    
    def label_length(self):
        length = f"The length of the first and last name: {len(self.name)}"
        return length
    
    def info(self):
        information = "Card type: " + self.type + "\n" + "Name:"+ " " + self.name + "\n" + "Phone number:" + " "+ self.phone + "\n" + "Mail:" + " "+ self.mail
        return information


class BusinessContact(Card):
    def __init__(self, type, name, state, company, phone):
        super().__init__("Business",name, phone)
        self.state = state
        self.company = company
        self.phone = phone
        self.type = type
        
    def label_length(self):
        length = f"The length of the first and last name: {len(self.name)}"
        return length    
       
    
    def contact(self):
        print(f"I dial the number {self.phone} and call {self.name}")

    def info(self):
        information = "Card type: " + self.type + "\n" + "Name: " + self.name + "\n" + "State: " + self.company + "\n" + "Company: " + self.state + "\n" + "Phone number: " + self.phone
        return information


class Contactbusiness():
    def __init__(self, type, name, phone, company, state):
        super().__init__("Business",phone,name)
        self.name = name
        self.phone = phone
        self.company = company
        self.state = state
        self.type = type
    
    def contact(self):
        contact = f"I dial the number {self.phone} and call {self.name}"
        return contact

class Contactbase():
    def __init__(self, name, phone):
        super().__init__("Base",phone, name)
        self.name = name
        self.phone = phone
        

    def contact(self):
        contact = f"I dial the number {self.phone} and call {self.name}"
        return contact


class Organizer:
    owner = ""
    cardsBase = []
    def __init__(self, owner):
        self.owner = owner
    
    def addCard(self):
        type = input("Pick a card type (Base/Business): ")
        if type == 'Base':
            name = fake.name()
            mail = fake.email()
            phone = fake.country_calling_code() + fake.msisdn()[4:]
            newCard = BaseContact(type, name, mail, phone)
            self.cardsBase.append(newCard)
            print("Successfully added new card")
            
        elif type == 'Business':
            name = fake.name()
            company = fake.company()
            state = fake.job()
            phone = fake.country_calling_code() + fake.msisdn()[4:]
            newCard = BusinessContact(type, name, company, state, phone)
            self.cardsBase.append(newCard)
            print("Successfully added new card")
    def showCards(self):
        print('Cards list: ')
        for i in self.cardsBase:
            if i.type == 'Base':
                print(i.info())
                print(i.label_length())
                print("\n")
            
            elif i.type == 'Business':
                print(i.info())
                print(i.label_length())
                print("\n")
            
                       
    def contactbase(self):
        print("Contact people on the BaseContact list: ")
        for i in self.cardsBase:
            if i.type == 'Base':
                print(f"I dial the number {i.mail} and call {i.name}")
                          
            
    def contactbusiness(self):      
        print("Contact people on the BusinessContact list: ")
        for i in self.cardsBase:
            if i.type == 'Business':
                print(f"I dial the number {i.phone} and call {i.name}")
        
def main():                
    organizer = Organizer("Owner")

    while True:
        print("""What would you like to do?:    
                1- Add card
                2- Show cards
                3- Contact people on the BaseContact list
                4- Contact people on the BusinessContact list
                5- Exit""")
        x = input("Selected number: ")
    
   
        if x == '1': organizer.addCard()
        if x == '2': organizer.showCards()
        if x == '3': organizer.contactbase()
        if x == '4': organizer.contactbusiness()
        if x == '5': 
            print("Exiting bye...")
            break


if __name__ == "__main__":
    main() 
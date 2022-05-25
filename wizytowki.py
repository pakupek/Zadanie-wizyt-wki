from faker import Faker
fake = Faker()

class Card:
    def __init__(self,typ,imie, telefon):
        self.typ = typ
        self.imie = imie
        self.telefon = telefon
        
        
class BaseContact(Card):
    def __init__(self,rodzaj,imie, telefon, mail):
       super().__init__("Base",imie,telefon)
       self.rodzaj = rodzaj
       self.mail = mail
    
    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonie do {self.imie}")
    
    def label_length(self):
        długość = f"Długość imienia i nazwiska: {len(self.imie)}"
        #print(f"Długość imienia i nazwiska wynosi: {długość}")
        return długość
    
    def info(self):
        information = "Typ wizytówki: " + self.rodzaj + "\n" + "Imię:"+ " " + self.imie + "\n" + "Nr telefonu:" + " "+ self.telefon + "\n" + "Mail:" + " "+ self.mail
        return information


class BusinessContact(Card):
    def __init__(self,rodzaj, imie,stanowisko, firma, telefonsł):
        super().__init__("Business",imie, telefonsł)
        self.pozycja = stanowisko
        self.firma = firma
        self.telefonsł = telefonsł
        self.rodzaj = rodzaj
        
    def label_length(self):
        długość = f"Długość imienia i nazwiska: {len(self.imie)}"
        #print(f"Długość imienia i nazwiska wynosi: {długość}")
        return długość    
       
    
    def contact(self):
        print(f"Wybieram numer {self.telefonsł} i dzwonie do {self.imie}")

    def info(self):
        information = "Typ wizytówki: " + self.rodzaj + "\n" + "Imię: " + self.imie + "\n" + "Stanowisko: " + self.firma + "\n" + "Firma: " + self.pozycja + "\n" + "Telefon służbowy: " + self.telefonsł
        return information


class Kontaktbusiness():
    def __init__(self, rodzaj, imię, telefonsł, firma, stanowisko):
        super().__init__("Business",telefonsł,imię)
        self.imię = imię
        self.telsł = telefonsł
        self.firma = firma
        self.stanowisko = stanowisko
        self.rodzaj = rodzaj
    
    def contact(self):
        contact = f"Wybieram numer {self.telsł} i dzwonie do {self.imię}"
        return contact

class Kontaktbase():
    def __init__(self, imie, telefon):
        super().__init__("Base",telefon, imie)
        self.imie = imie
        self.telefon = telefon
        

    def contact(self):
        contact = f"Wybieram numer {self.telefon} i dzwonie do {self.imie}"
        return contact


class Organizer:
    właściciel = ""
    bazaWizytowek = []
    def __init__(self, właściciel):
        self.właściciel = właściciel
    
    def dodajWizytówkę(self):
        rodzaj = input("Rodzaj wizytówki (Base/Business): ")
        if rodzaj == 'Base':
            imię = fake.name()
            mail = fake.email()
            telefon = fake.country_calling_code() + fake.msisdn()[4:]
            nowaWizytowka = BaseContact(rodzaj,imię, mail, telefon)
            self.bazaWizytowek.append(nowaWizytowka)
            print("Pomyślnie dodano wizytówkę")
            
        elif rodzaj == 'Business':
            imię = fake.name()
            firma = fake.company()
            stanowisko = fake.job()
            telefonsł = fake.country_calling_code() + fake.msisdn()[4:]
            nowaWizytowka = BusinessContact(rodzaj,imię, firma, stanowisko, telefonsł)
            self.bazaWizytowek.append(nowaWizytowka)
            print("Pomyślnie dodano wizytówkę")
    def wyświetlWizytówki(self):
        print('Lista wizytówek: ')
        for i in self.bazaWizytowek:
            if i.typ == 'Base':
                print(i.info())
                print(i.label_length())
                print("\n")
            
            elif i.typ == 'Business':
                print(i.info())
                print(i.label_length())
                print("\n")
            
                       
    def kontaktbase(self):
        print("Kontakt z osobami z listy BaseContact: ")
        for i in self.bazaWizytowek:
            if i.typ == 'Base':
                print(f"Wybieram numer {i.mail} i dzwonie do {i.imie}")
                          
            
    def kontaktbusiness(self):      
        print("Kontakt z osobami z listy BusinessContact: ")
        for i in self.bazaWizytowek:
            if i.typ == 'Business':
                print(f"Wybieram numer {i.telefonsł} i dzwonie do {i.imie}")
        
def main():                
    organizerAnalityka = Organizer("Adam")

    while True:
        print("""Co chcesz zrobić?:    
                1- Dodać wizytówkę
                2- Wyświetlić wizytówki
                3- Kontakt z osobami z wizytówki BaseContact
                4- Kontakt z osobami z wizytówki BusinessContact
                5- Wyjście z programu""")
        x = input("Wybrany numer: ")
    
   
        if x == '1': organizerAnalityka.dodajWizytówkę()
        if x == '2': organizerAnalityka.wyświetlWizytówki()
        if x == '3': organizerAnalityka.kontaktbase()
        if x == '4': organizerAnalityka.kontaktbusiness()
        if x == '5': 
            print("Exiting bye...")
            break


if __name__ == "__main__":
    main() 
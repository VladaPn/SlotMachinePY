class Account():
    stanje=0
    def deposit(self):
        uplata=input("How much you want to deposit?")
        try:
            uplata=int(uplata)
            print(f"Na racun je uplaceno {uplata} dinara")
            trans=f"Na racun je uplaceno {uplata} dinara \n"
            self.stanje+=uplata
            with open('transakcije.txt', 'a') as file:
                file.write(trans)
        except Exception as e:
            print(e)
    def withdrawal(self):
        isplata=input("How much you want to withdrawal?")
        try:
            isplata=int(isplata)
        except Exception as e:
            print(e)   
        if(self.stanje>=isplata):
            self.stanje-=isplata
            print(f"Sa racuna je isplaceno {isplata} dinara")
            trans=f"Sa racuna je isplaceno {isplata} dinara \n"
            with open('transakcije.txt', 'a') as file:
                file.write(trans)
        else:
            print("Nemate dovoljno sredstava na racunu")
korisnik = Account()
def main():
    while True:
        akcija=input("D or W ")
        if akcija=="D":
            korisnik.deposit()
        elif akcija=="W":
            korisnik.withdrawal()
        else:
            break;
        print(f"Trenutno stanje je {korisnik.stanje}")
main()
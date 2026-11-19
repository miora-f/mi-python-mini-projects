def get_user_input():
    #Get the input from the user
    rechnung = float(input("Rechnungsbetrag (€): "))
    trinkgeld_prozent = float(input("Trinkgeld (%): "))
    personen = int(input("Anzahl Personen: "))

    return rechnung, trinkgeld_prozent, personen

def calculate_bill(rechnung, trinkgeld_prozent, personen):
    #calculate the tip
    trinkgeld = rechnung*trinkgeld_prozent / 100

    #calculate the total amount
    gesamtbetrag = rechnung + trinkgeld

    #calculate the amount per person
    pro_person = gesamtbetrag / personen
    
    return trinkgeld, gesamtbetrag, pro_person

def display_results(rechnung, trinkgeld, gesamtbetrag, pro_person):
    #display the result
    print(" \n---------- ERGEBNIS ---------")
    print(f"Rechnung: {rechnung:.2f} €")
    print(f"Trinkgeld: {trinkgeld:.2f} €")
    print(f"Gesamtbetrag: {gesamtbetrag:.2f} €")
    print(f"Pro Personen: {pro_person:.2f} €")

def main():
    print("------------ RECHNUNG und TRINGELD ---------")

    try:
        rechnung, trinkgeld_prozent, personen = get_user_input()

        if rechnung < 0 or trinkgeld_prozent < 0 or personen <= 0 :
            print("Fehler : bitte überprüfe deine Eingaben")
            return

        trinkgeld, gesamtbetrag, pro_person = calculate_bill(rechnung, trinkgeld_prozent, personen)

        display_results(rechnung, trinkgeld, gesamtbetrag, pro_person)
    
    except ValueError:
        print("Fehler : bitte gib eine gültige Zahl ein!")

if __name__ == "__main__":
    main()








def berechne_netto(brutto):
    netto = brutto * 0.65
    return netto

brutto_gehalt = float(input("Wie viel Brutto verdienst du (in Euro)? "))


mein_netto = berechne_netto(brutto_gehalt)

# 4. Ergebnis zeigen (Ausgabe)
print(f"Dein geschätztes Netto-Gehalt ist: {mein_netto} Euro.")





def checksicherheit(passwort):
    
    if len(passwort) < 8:
        print("Passwort zu kurz")
    else:
        print("Passwort akzeptiert")
        
        return checksicherheit
    
passwort = input("Geben Sie Ihr Passwort ein: ")
checksicherheit(passwort)

print("dein Passwort ist", passwort)


Mitarbeiter = []

Namen = input("Ihre Namen: ")
Passwort = input("Ihr Passwort: ")

if len(Namen) < 5:
    print("Namen zu kurz")
else:
    print("Namen akzeptiert")

if len(Passwort) > 5:
    Mitarbeiter.append(Namen)

print("aktuelle Mitarbeiter:", Mitarbeiter)
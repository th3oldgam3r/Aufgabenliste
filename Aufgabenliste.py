# Eine leere Liste, um Aufgaben zu speichern
tasks = []

# Funktion, um eine neue Aufgabe hinzuzufügen
def add_task(task):
    tasks.append(task)
    print("Aufgabe hinzugefügt:", task)

# Funktion, um alle Aufgaben anzuzeigen
def show_tasks():
    print("\nAktuelle Aufgaben:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

# Hauptprogrammschleife
while True:
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Beenden")
    
    choice = input("Bitte wählen Sie eine Option (1/2/3): ")
    
    if choice == '1':
        task = input("Geben Sie die Aufgabe ein: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("Das Programm wird beendet.")
        break
    else:
        print("Ungültige Auswahl. Bitte wählen Sie 1, 2 oder 3.")

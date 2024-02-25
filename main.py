import os
import subprocess
import msvcrt


def lock_folder():
    if os.path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"):
        print("Der Ordner ist bereits gesperrt.")
        return

    if not os.path.exists("Exegs"):
        os.makedirs("Exegs")
        print("Ordner 'Exegs' erfolgreich erstellt.")

    print("Packe vor dem Sperren deine Datein in den Ordner Exegs")
    confirmation = input("willst du fr sperren? (J/N): ")
    if confirmation.upper() == "J":
        os.rename("Exegs", "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}")
        subprocess.run(["attrib", "+h", "+s", "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"])
        print("Ordner erfolgreich gesperrt.")
    else:
        print("Vorgang abgebrochen.")


def unlock_folder():
    if not os.path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"):
        print("Der Ordner ist nicht gesperrt.")
        return

    password = getpass("Geben Sie das Passwort ein, um den Ordner zu entsperren: ")
    if password == "YOUR_PASSWORD":  # pw
        os.rename("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}", "Exegs")
        subprocess.run(["attrib", "-h", "-s", "Exegs"])
        print("Ordner erfolgreich entsperrt.")
    else:
        print("Ungültiges Passwort.")


def getpass(prompt="Enter Password: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            print('')
            return password
        elif char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)


if __name__ == "__main__":
    choice = input("(Sperren: S / Entsperrung: E): ")

    if choice.upper() == "S":
        lock_folder()
    elif choice.upper() == "E":
        unlock_folder()
    else:
        print("Ungültige Eingabe.")

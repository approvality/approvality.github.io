import time
import requests
import webbrowser
import os.path

def passwordprompt():
    while True:
        print("Enter password. Type 'exit' to exit console.")
        print("Math Problem 1: ((20 * 2 + 30) / 2 + 50 - 2) * 100)")
        print("Math Problem 2: 25 * 2 + 50 - 20 - 5")
        print("Combine the answers to both math problems by ascending numerical order for the password.")
        user_input = input("Password: ")
        if user_input.lower() in ["8375"]:
            print("Please wait - do not close the application.")
            time.sleep(15)
            print("Surprise in 5 seconds!")
            time.sleep(5)
            webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')
            url = 'https://raw.githubusercontent.com/approvality/approvality.github.io/main/Zrzut%20ekranu%202024-06-24%20152607.png'
            r = requests.get(url, allow_redirects=True)
            open('other surprise.png', 'wb').write(r.content)
            break
        elif user_input.lower() in ["exit"]:
            print("Exiting in 5 seconds.")
            time.sleep(5)
            break
        else:
            print("Invalid password - try again.")
             

while True:
    user_input = input("Continue? (Y/N) ")
    if user_input.lower() in ["yes", "y"]:
        passwordprompt()
        break
    elif user_input.lower() in ["no", "n"]:
        print("Exiting in 5 seconds.")
        time.sleep(5)
        break
    else:
        print("Invalid input. Please enter yes/no.")

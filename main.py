from brain import ask
from voice import speak

print("Seven Online")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    answer = ask(user)

    print("Seven:", answer)

    speak(answer)
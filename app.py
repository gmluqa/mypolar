import json
import os
from datetime import datetime

def track_mood():
    mood = int(input("How are you feeling today? (Scale of 1-10): "))
    pills = []
    pill_types = ["Depakine Chrono 500mg", "Pristiq 50mg"]

    num_pills = int(input("How many pills are you going to take today? "))

    for _ in range(num_pills):
        print("Select a pill type:")
        for i, pill_type in enumerate(pill_types, start=1):
            print(f"{i}. {pill_type}")

        selected_pill = int(input("Enter the number for the pill type: "))
        quantity = int(input("How many pills of that type will you take? "))

        pills.append({
            "pill": pill_types[selected_pill - 1],
            "quantity": quantity
        })

    today = datetime.now().strftime("%d/%m/%Y")

    data = {}
    if os.path.isfile("local/data.json"):
        with open("local/data.json", "r") as file:
            data = json.load(file)

    if today in data:
        data[today].extend(pills)
    else:
        data[today] = pills

    with open("local/data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Mood tracking complete.")

def main():
    track_mood()

if __name__ == "__main__":
    main()
import json
import os
from datetime import date

DATA_FILE = "habits.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_habit(data, name):
    if name not in data:
        data[name] = {}
        save_data(data)
        print(f"Added habit: {name}")
    else:
        print(f"Habit '{name}' already exists.")

def mark_done(data, name):
    today = str(date.today())
    if name not in data:
        print(f"Habit '{name}' doesn't exist. Add it first.")
        return
    data[name][today] = True
    save_data(data)
    print(f"Marked '{name}' as done for {today}.")

def show_streak(data, name):
    if name not in data:
        print(f"Habit '{name}' doesn't exist.")
        return
    dates = sorted(data[name].keys())
    print(f"{name}: {len(dates)} total completions")
    for d in dates[-7:]:
        print(f"  {d}: done")

def list_habits(data):
    if not data:
        print("No habits yet.")
        return
    for name, entries in data.items():
        print(f"- {name} ({len(entries)} completions)")

def main():
    data = load_data()
    while True:
        print("\n1. Add habit\n2. Mark done today\n3. Show streak\n4. List habits\n5. Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Habit name: ").strip()
            add_habit(data, name)
        elif choice == "2":
            name = input("Habit name: ").strip()
            mark_done(data, name)
        elif choice == "3":
            name = input("Habit name: ").strip()
            show_streak(data, name)
        elif choice == "4":
            list_habits(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

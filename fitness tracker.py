import json
import datetime

# File to store fitness data
DATA_FILE = "fitness_tracker.json"

# Function to load data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"workouts": []}

# Function to save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to log a workout
def log_workout():
    workout_type = input("Enter workout type (e.g., Running, Cycling, Weightlifting): ").strip()

    while True:
        try:
            duration = float(input("Enter duration in minutes: "))
            if duration <= 0:
                print("Duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            calories = float(input("Enter calories burned: "))
            if calories < 0:
                print("Calories cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    workout = {
        "date": date,
        "type": workout_type,
        "duration": duration,
        "calories": calories
    }

    data = load_data()
    data["workouts"].append(workout)
    save_data(data)

    print("\n✅ Workout logged successfully!")

# Function to view workout history
def view_history():
    data = load_data()
    
    if not data["workouts"]:
        print("\n🚫 No workouts logged yet.")
        return
    
    print("\n📌 Workout History:")
    print("-" * 50)
    for i, workout in enumerate(data["workouts"], 1):
        print(f"{i}. [{workout['date']}] {workout['type']} - {workout['duration']} min - {workout['calories']} kcal")
    print("-" * 50)

# Function to show statistics
def show_statistics():
    data = load_data()
    
    if not data["workouts"]:
        print("\n🚫 No data available for statistics.")
        return
    
    total_workouts = len(data["workouts"])
    total_duration = sum(w["duration"] for w in data["workouts"])
    total_calories = sum(w["calories"] for w in data["workouts"])

    print("\n📊 Fitness Statistics:")
    print(f"🏋️ Total Workouts: {total_workouts}")
    print(f"⏳ Total Duration: {total_duration:.2f} minutes")
    print(f"🔥 Total Calories Burned: {total_calories:.2f} kcal")

# Main menu
def main():
    while True:
        print("\n🔹 Personal Fitness Tracker")
        print("1️⃣ Log a Workout")
        print("2️⃣ View Workout History")
        print("3️⃣ Show Statistics")
        print("4️⃣ Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            log_workout()
        elif choice == "2":
            view_history()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("\n👋 Goodbye! Stay Fit! 💪")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the fitness tracker
if __name__ == "__main__":
    main()

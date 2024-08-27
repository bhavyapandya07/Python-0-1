# Lecture 20: Fitness Tracker Object-Oriented Programming Example

class Workout:
    def __init__(self, start, end, calories):
        self.start = start
        self.end = end
        self.calories = calories
    
    def __str__(self):
        return f"Workout from {self.start} to {self.end} burning {self.calories} calories."
    
    def get_calories(self):
        return self.calories
    
    def __eq__(self, other):
        return (self.start == other.start and
                self.end == other.end and
                self.calories == other.calories)

class OutdoorWorkout(Workout):
    def __init__(self, start, end, calories, activity):
        super().__init__(start, end, calories)
        self.activity = activity
    
    def __str__(self):
        return f"Outdoor workout: {self.activity} from {self.start} to {self.end} burning {self.calories} calories."
    
    def get_calories(self):
        return self.calories

class IndoorWorkout(Workout):
    def __init__(self, start, end, calories, activity):
        super().__init__(start, end, calories)
        self.activity = activity
    
    def __str__(self):
        return f"Indoor workout: {self.activity} from {self.start} to {self.end} burning {self.calories} calories."
    
    def get_calories(self):
        return self.calories

def select_workout_type():
    print("Select Workout Type:")
    print("1. Outdoor")
    print("2. Indoor")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return OutdoorWorkout
    elif choice == '2':
        return IndoorWorkout
    else:
        print("Invalid choice.")
        return None

def select_activity(workout_type):
    if workout_type == OutdoorWorkout:
        print("Select Outdoor Activity:")
        print("1. Running")
        print("2. Swimming")
        activity = input("Enter 1 or 2: ")
        if activity == '1':
            return 'Running'
        elif activity == '2':
            return 'Swimming'
        else:
            print("Invalid activity.")
            return None
    elif workout_type == IndoorWorkout:
        print("Select Indoor Activity:")
        print("1. Skipping")
        print("2. Pushups")
        activity = input("Enter 1 or 2: ")
        if activity == '1':
            return 'Skipping'
        elif activity == '2':
            return 'Pushups'
        else:
            print("Invalid activity.")
            return None

def calculate_calories(activity, duration):
    # Dummy calorie calculations based on activity
    calories_per_hour = {
        'Running': 600,
        'Swimming': 500,
        'Skipping': 400,
        'Pushups': 300
    }
    return calories_per_hour.get(activity, 0) * duration

def main():
    workout_type = select_workout_type()
    if workout_type:
        activity = select_activity(workout_type)
        if activity:
            duration = int(input("Enter workout duration in hours (e.g., 1, 2): "))
            calories = calculate_calories(activity, duration)
            workout = workout_type('Start Time', 'End Time', calories, activity)
            print(workout)
        else:
            print("Failed to select a valid activity.")
    else:
        print("Failed to select a valid workout type.")

if __name__ == "__main__":
    main()
"""
Water Intake Quantity Counter
A beginner-friendly command-line program to track daily water intake.
"""

def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 36)
    print("   WATER INTAKE QUANTITY COUNTER")
    print("=" * 36)

    goal_ml = get_positive_number("Enter your daily water goal in ml (e.g. 2000): ")
    total_ml = 0

    while True:
        print("\n--- MENU ---")
        print("1. Add water intake")
        print("2. View today's progress")
        print("3. Change daily goal")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            amount_ml = get_positive_number("Enter the amount of water consumed (ml): ")
            total_ml += amount_ml
            print(f"Added {amount_ml} ml. Total intake: {total_ml} ml.")
            if total_ml >= goal_ml:
                print("Great! You have reached your daily goal.")
        elif choice == "2":
            remaining_ml = max(goal_ml - total_ml, 0)
            percentage = (total_ml / goal_ml) * 100
            print("\n--- TODAY'S WATER INTAKE ---")
            print(f"Total consumed : {total_ml} ml ({total_ml / 1000:.2f} litres)")
            print(f"Daily goal     : {goal_ml} ml ({goal_ml / 1000:.2f} litres)")
            print(f"Goal completed : {min(percentage, 100):.1f}%")
            if remaining_ml:
                print(f"Remaining      : {remaining_ml} ml")
            else:
                print("Remaining      : 0 ml — goal reached!")
        elif choice == "3":
            goal_ml = get_positive_number("Enter your new daily goal in ml: ")
            print(f"Daily goal updated to {goal_ml} ml.")
        elif choice == "4":
            print(f"\nFinal intake: {total_ml} ml ({total_ml / 1000:.2f} litres)")
            print("Stay hydrated. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()

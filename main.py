'''
DEVELOPER(S): Alex Takayama
COLLABORATORS: Myself, Internet
DATE: 04/17/2026
'''

"""
Track mood check-ins and save them to a file.

This program asks the user for a check-in label, name, mood level,
energy level, and stress level. It calculates a mood score, calculates
an average level, gives an encouragement message, and saves each
check-in to a text file.
"""

##########################################
# IMPORTS:
# No modules are needed for this program.
##########################################


##########################################
# FUNCTIONS:
##########################################
def calculate_mood_score(mood_level, energy_level, stress_level):
    """Calculate and return the user's mood score."""
    starting_mood = mood_level * 10
    energy_boost = energy_level * 2
    stress_drag = stress_level * 2
    final_score = starting_mood + energy_boost - stress_drag
    return final_score


def calculate_average_level(mood_level, energy_level, stress_level):
    """Calculate and return the average of the three levels."""
    average_level = (mood_level + energy_level + stress_level) / 3
    return average_level


def get_valid_rating(prompt):
    """Get a rating from the user between 1 and 10."""
    rating = int(input(prompt))

    while rating < 1 or rating > 10:
        print("Invalid input. Please enter a number from 1 to 10.")
        rating = int(input(prompt))

    return rating


def get_mood_message(mood_score):
    """Return an encouragement message based on the mood score."""
    if mood_score >= 80:
        message = "You have strong energy today, so keep going and make the most of it."
    elif mood_score >= 60:
        message = "You are doing better than you think, so keep moving forward one step at a time. Being in a steady place is something to be proud of."
    elif mood_score >= 40:
        message = "You may be feeling mixed today. Take things one step at a time, small progress still matters."
    elif mood_score >= 20:
        message = "You seem a little overwhelmed. Give yourself a little extra patience today and focus on one simple step, slow down and take care of yourself."
    else:
        message = "Take a break, rest and reset. Remember that your well-being matters and hard days do not last forever."

    return message


def create_entry_line(check_in_label, user_name, mood_level, energy_level, stress_level, mood_score, average_level):
    """Create and return one formatted line to save in the history file."""
    entry_line = check_in_label + " | " + user_name + " | mood=" + str(mood_level) + " | energy=" + str(energy_level) + " | stress=" + str(stress_level) + " | score=" + str(mood_score) + " | average=" + str(average_level)
    return entry_line


def save_check_in(file_name, entry_line):
    """Save one check-in entry to the history file."""
    out_file = open(file_name, "a")
    out_file.write(entry_line + "\n")
    out_file.close()


def show_session_history(session_list):
    """Show the check-ins completed during this run of the program."""
    print("- Check-Ins Saved This Session -")

    for entry in session_list:
        print(entry)

    print()


def main():
    """Run the mood check-in tracker program."""
    history_file_name = "mood_history.txt"

    print("Mood Check-In Tracker")
    print()

    run_again = "yes"

    # I used a list instead of a dictionary because I wanted to keep
    # each check-in in the order it was entered during this session.
    session_list = []

    while run_again == "yes":
        print("- New Mood Check-In -")
        check_in_label = input("Enter a label for this check-in (example: Monday or April 20): ")
        check_in_label = check_in_label.strip()

        user_name = input("Enter your name: ")
        user_name = user_name.strip()
        user_name = user_name.title()

        mood_level = get_valid_rating("Enter your mood level (1-10): ")
        energy_level = get_valid_rating("Enter your energy level (1-10): ")
        stress_level = get_valid_rating("Enter your stress level (1-10): ")

        mood_score = calculate_mood_score(mood_level, energy_level, stress_level)
        average_level = calculate_average_level(mood_level, energy_level, stress_level)
        encouragement_message = get_mood_message(mood_score)

        print()
        print("- Mood Check-In Results -")
        print("Check-in label:", check_in_label)
        print(f"Name: {user_name}")
        print(f"Mood level: {mood_level}")
        print(f"Energy level: {energy_level}")
        print(f"Stress level: {stress_level}")
        print(f"Mood score: {mood_score}")
        print(f"Average level: {average_level:.2f}")
        print(f"Message: {encouragement_message}")
        print()

        # Create one line of text for the file.
        entry_line = create_entry_line(check_in_label, user_name, mood_level, energy_level, stress_level, mood_score, average_level)

        # Save the check-in to a text file for future reference.
        save_check_in(history_file_name, entry_line)

        # Add the same check-in to the list for this program session.
        session_list.append(entry_line)

        print("Your check-in was saved to mood_history.txt.")
        print()

        run_again = input("Would you like to do another mood check? (yes/no): ")
        run_again = run_again.strip()
        run_again = run_again.lower()
        print()

    if session_list != []:
        show_session_history(session_list)

    print("Thanks for using this Mood Check-In Tracker!")


##########################################
# MAIN PROGRAM:
##########################################
if __name__ == "__main__":
    main()
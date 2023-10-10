import tkinter as tk
import configparser

# Function to calculate the average grade
def calculate_grade():
    try:
        total_subjects = int(num_subjects_entry.get())
        if total_subjects > 11:
            # Display an error message if more than 11 subjects are entered
            grade_label.config(text="Max number of subjects allowed is 11", fg="red")
            return

        total_score = sum(float(score_entries[i].get()) for i in range(total_subjects))
        average_score = total_score / total_subjects

        if 90 <= average_score <= 100:
            grade_label.config(text="Average Grade: A", fg="green")
        elif 80 <= average_score < 90:
            grade_label.config(text="Average Grade: B", fg="blue")
        elif 70 <= average_score < 80:
            grade_label.config(text="Average Grade: C", fg="purple")
        elif 60 <= average_score < 70:
            grade_label.config(text="Average Grade: D", fg="orange")
        elif 0 <= average_score < 60:
            grade_label.config(text="Average Grade: F", fg="red")
        else:
            grade_label.config(text="Invalid score", fg="red")
    except ValueError:
        grade_label.config(text="Invalid input", fg="red")

# Function to reset the calculator
def reset_calculator():
    num_subjects_entry.delete(0, tk.END)  # Clear the entry widget
    grade_label.config(text="")
    create_fields_button.config(state="normal")  # Re-enable the "Create Score Fields" button
    reload_button.config(state="disabled")  # Disable the "Reload" button

    # Destroy the frame containing score entry fields
    for widget in frame.winfo_children():
        widget.destroy()

    # Clear the saved value in the configuration file
    save_config(num_subjects=None)

# Function to create score entry fields based on the number of subjects
def create_score_entry_fields():
    num_subjects = num_subjects_entry.get()  # Save the user-entered value
    save_config(num_subjects=num_subjects)  # Save the value to the configuration file

    try:
        total_subjects = int(num_subjects)
    except ValueError:
        grade_label.config(text="Invalid input", fg="red")
        return

    if total_subjects > 11:
        # Display an error message if more than 11 subjects are entered
        grade_label.config(text="Max number of subjects allowed is 11", fg="red")
        return

    for i in range(total_subjects):
        score_label = tk.Label(frame, text=f"Enter score for Subject {i + 1}:", bg="#FFC0CB")  # Pink background color for label
        score_entry = tk.Entry(frame, bg="white")  # White background color for entry
        score_label.pack()
        score_entry.pack()
        score_entries.append(score_entry)

    # Add the "Calculate" button below the created score entry fields
    calculate_button.pack(side="bottom", pady=10)
    grade_label.pack()
    create_fields_button.config(state="disabled")  # Disable the "Create Score Fields" button
    reload_button.config(state="normal")  # Re-enable the "Reload" button

# Function to save and load configuration
def save_config(num_subjects):
    config = configparser.ConfigParser()
    config.read('config.ini')
    if num_subjects is not None:
        config['User'] = {'NumSubjects': num_subjects}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        if 'User' in config:
            return config['User'].get('NumSubjects', None)
        else:
            return None

# Create the main window
root = tk.Tk()
root.title("Grade Calculator")

# Set the background color of the main window
root.configure(bg="#FFC0CB")  # Pink background color

# Create a frame with a border and background color
frame = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", bg="#FFC0CB")  # Pink background color
frame.pack(padx=10, pady=10)

# Create and configure widgets
num_subjects_label = tk.Label(frame, text="Enter the total number of subjects:", bg="#FFC0CB")  # Pink background color for label
num_subjects_entry = tk.Entry(frame, bg="white")  # White background color for entry
grade_label = tk.Label(frame, text="", font=("Arial", 16), bg="#FFC0CB")  # Pink background color for label

# Create a list to store score entry fields
score_entries = []

# Create a "Reload" button to reset the calculator
reload_button = tk.Button(frame, text="Reload", command=reset_calculator, state="disabled",bg="#FF00FF")  # Pink background color for button

# Create a button to generate score entry fields
create_fields_button = tk.Button(frame, text="Create Score Fields", command=create_score_entry_fields, bg="#FFC0CB")  # Pink background color for button

# Load the saved value from the configuration file
saved_num_subjects = save_config(num_subjects=None)

if saved_num_subjects is not None:
    num_subjects_entry.insert(0, saved_num_subjects)

# Place widgets on the window
num_subjects_label.pack()
num_subjects_entry.pack()
create_fields_button.pack()
reload_button.pack()

# Calculate button initially not packed
calculate_button = tk.Button(frame, text="Calculate", command=calculate_grade, bg="#FF00FF")  # Pink background color for button

# Suppress the warning about secure coding and set background color
root.tk_setPalette(background='#FFC0CB')  # Set a pink background color
root.createcommand('::tk::mac::ShowPreferences', lambda: True)  # Suppress the warning

# Start the GUI main loop
root.mainloop()
























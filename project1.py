import tkinter as tk
from tkinter import messagebox

# Dictionary to store student details
students = {}

# Functions
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    
    if student_id in students:
        messagebox.showerror("Error", "Student ID already exists.")
    elif not student_id or not name or not age or not grade:
        messagebox.showerror("Error", "All fields are required.")
    else:
        students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
        messagebox.showinfo("Success", "Student added successfully.")
        clear_fields()

def view_students():
    if not students:
        messagebox.showinfo("No Records", "No student records found.")
    else:
        view_window = tk.Toplevel(root)
        view_window.title("Student Records")
        view_window.geometry("400x300")
        for i, (student_id, details) in enumerate(students.items(), start=1):
            tk.Label(view_window, text=f"{i}. ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}", anchor="w").pack(fill="x", pady=2)

def search_student():
    student_id = entry_id.get()
    if student_id in students:
        details = students[student_id]
        messagebox.showinfo("Student Found", f"ID: {student_id}\nName: {details['Name']}\nAge: {details['Age']}\nGrade: {details['Grade']}")
    else:
        messagebox.showerror("Error", "Student not found.")

def update_student():
    student_id = entry_id.get()
    if student_id in students:
        name = entry_name.get()
        age = entry_age.get()
        grade = entry_grade.get()
        if not name or not age or not grade:
            messagebox.showerror("Error", "All fields are required for update.")
        else:
            students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
            messagebox.showinfo("Success", "Student details updated successfully.")
            clear_fields()
    else:
        messagebox.showerror("Error", "Student not found.")

def delete_student():
    student_id = entry_id.get()
    if student_id in students:
        del students[student_id]
        messagebox.showinfo("Success", "Student deleted successfully.")
        clear_fields()
    else:
        messagebox.showerror("Error", "Student not found.")

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

# Labels and Entry Fields
tk.Label(root, text="Student ID:").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)

tk.Label(root, text="Student Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Student Age:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

tk.Label(root, text="Student Grade:").pack(pady=5)
entry_grade = tk.Entry(root)
entry_grade.pack(pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).pack(pady=5)

# Run the application
root.mainloop()
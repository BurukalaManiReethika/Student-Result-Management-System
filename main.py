
---

## 💻 main.py (FULL CODE)
```python
class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 50:
            return 'C'
        else:
            return 'D'

    def __str__(self):
        return f"{self.sid}, {self.name}, {self.marks}, {self.grade}"


class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        student = Student(sid, name, marks)

        with open(self.filename, "a") as f:
            f.write(str(student) + "\n")

        print("✅ Student added successfully!")

    def view_students(self):
        try:
            with open(self.filename, "r") as f:
                data = f.readlines()
                if not data:
                    print("No records found.")
                for line in data:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found.")

    def search_student(self):
        sid = input("Enter Student ID: ")
        found = False

        with open(self.filename, "r") as f:
            for line in f:
                if line.startswith(sid):
                    print("Found:", line.strip())
                    found = True
                    break

        if not found:
            print("Student not found.")


def menu():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()

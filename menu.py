#!/usr/bin/env python3

from create_state import create_state_structure, find_student_in_state

def main_menu():
    state_objects, subjects = create_state_structure()

    while True:
        print("\nSchool Marksheet System")
        print("1. Find Student by ID")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ").strip()
            if not student_id:
                print("Student ID cannot be empty. Please try again.")
                continue
            
            student, subjects = find_student_in_state(state_objects, subjects, student_id)
            if student:
                print("\nStudent Found:")
                print(student.__str__(subjects))
            else:
                print("\nStudent not found. Please check the ID and try again.")

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1 to find a student or 2 to exit.")


if __name__ == "__main__":
    main_menu()


#!/usr/bin/env python3

# create_state.py
from read_data import read_csv
from structures import State, County, School, Student

def create_state_structure():
    # Example CSV file paths
    students_csv_file_path = 'data/students.csv'
    schools_csv_file_path = 'data/schools.csv'
    counties_csv_file_path = 'data/counties.csv'
    states_csv_file_path = 'data/states.csv'
    subjects_csv_file_path = 'data/subjects.csv'
    marks_csv_file_path = 'data/marks.csv'

    # Reading data from CSV files
    students_data = read_csv(students_csv_file_path)
    schools_data = read_csv(schools_csv_file_path)
    counties_data = read_csv(counties_csv_file_path)
    states_data = read_csv(states_csv_file_path)
    subjects_data = read_csv(subjects_csv_file_path)
    marks_data = read_csv(marks_csv_file_path)

    # Organizing subjects data
    subjects = {row['subject_id']: row['subject_name'] for row in subjects_data}

    # Organizing data into states, counties, schools, and students
    states = {}
    for state in states_data:
        state_id = state['state_id']
        states[state_id] = State(state_id)

    # Create counties and add them to states
    counties_dict = {}
    for county in counties_data:
        county_id = county['county_id']
        state_id = county['state_id']
        new_county = County(county_id, state_id)
        counties_dict[county_id] = new_county
        if state_id in states:
            states[state_id].add_county(new_county)

    # Create schools and add them to counties
    for school in schools_data:
        school_id = school['school_id']
        county_id = school['county_id']
        if county_id in counties_dict:
            new_school = School(school_id, county_id)
            counties_dict[county_id].add_school(new_school)

    # Create students and add them to schools
    for student in students_data:
        student_id = student['student_id']
        school_id = student['school_id']
        class_id = student['class_id']
        # Assuming we need to find the corresponding county and state for the school
        found = False
        for state in states.values():
            for county in state.counties.values():
                if school_id in county.schools:
                    school = county.schools[school_id]
                    school.add_student(Student(student_id, school_id, class_id))
                    found = True
                    break
            if found:
                break

    # Add marks to students
    for mark in marks_data:
        student_id = mark['student_id']
        subject_id = mark['subject_id']
        marks = int(mark['marks'])
        for state in states.values():
            student = state.find_student(student_id)
            if student:
                student.add_subject_mark(subject_id, marks)

    return states, subjects

def find_student_in_state(state_objects, subjects, student_id):
    for state in state_objects.values():
        student = state.find_student(student_id)
        if student:
            return student, subjects
    return None, None


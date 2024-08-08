# structures.py
class Marksheet:
    def __init__(self, student_id):
        self.student_id = student_id
        self.marks = {}

    def add_subject_mark(self, subject_id, marks):
        self.marks[subject_id] = marks

    def get_marks(self, subjects):
        return [(subjects[subject_id], mark) for subject_id, mark in self.marks.items()]

    def __str__(self, subjects):
        marks_str = ", ".join([f"{subjects[sub_id]}: {mark}" for sub_id, mark in self.marks.items()])
        return f"Student ID: {self.student_id}, Marks: {marks_str}"


class Student:
    def __init__(self, student_id, school_id, class_id):
        self.student_id = student_id
        self.school_id = school_id
        self.class_id = class_id
        self.marksheet = Marksheet(student_id)

    def add_subject_mark(self, subject_id, marks):
        self.marksheet.add_subject_mark(subject_id, marks)

    def __str__(self, subjects):
        return self.marksheet.__str__(subjects)


class School:
    def __init__(self, school_id, county_id):
        self.school_id = school_id
        self.county_id = county_id
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def find_student(self, student_id):
        return self.students.get(student_id, None)


class County:
    def __init__(self, county_id, state_id):
        self.county_id = county_id
        self.state_id = state_id
        self.schools = {}

    def add_school(self, school):
        self.schools[school.school_id] = school

    def find_student(self, student_id):
        for school in self.schools.values():
            student = school.find_student(student_id)
            if student:
                return student
        return None


class State:
    def __init__(self, state_id):
        self.state_id = state_id
        self.counties = {}

    def add_county(self, county):
        self.counties[county.county_id] = county

    def find_student(self, student_id):
        for county in self.counties.values():
            student = county.find_student(student_id)
            if student:
                return student
        return None


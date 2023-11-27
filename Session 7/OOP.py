# Classroom management system
class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number


class Student(Person):
    def __init__(self, name, email, phone_number, student_id, courses_enrolled, grades):
        super().__init__(name, email, phone_number)
        self.student_id = student_id
        self.courses_enrolled = courses_enrolled
        self.grades = grades


class Teacher(Person):
    def __init__(self, name, email, phone_number, teacher_id, courses_taught):
        super().__init__(name, email, phone_number)
        self.teacher_id = teacher_id
        self.courses_taught = courses_taught

    def display_courses_taught(self):
        print(self.name + " is teaching the following courses: ")
        for course in self.courses_taught:
            print(course)

    def submit_grades(self, student, course, grade):
        if course in self.courses_taught and student in course.students:
            student.grades[course.course_id] = grade
            print(f"Grade submitted for {student.name} in {course.course_name}.")
        else:
            print(f"sorry, can't submit the grade. {self.name} is not teaching {course.course_name} or {student.name} isn't enrolled in that course")


class Course:
    def __init__(self, course_id, course_name, max_students, current_students):
        self.course_id = course_id
        self.course_name = course_name
        self.max_students = max_students
        self.current_students = current_students
        self.students = []

    def enroll_student(self, student):
        if(len(self.students) < self.max_students):
            self.students.append(student)
            self.current_students += 1
            student.courses_enrolled.append(self)
            print(student.name + " has been enrolled in " + self.course_name + " course.")
        else:
            print("sorry, " + self.course_name + " course is full and can't be enrolled.")

    def display_students(self):
        print("Students enrolled in " + self.course_name + " course: ")
        for student in self.students:
            print(student.name)


def create_person():
    name = input("Enter your name: ")
    email = input("Enter your Email: ")
    phone_number = input("Enter your phone number: ")
    return Person(name, email, phone_number)


def create_student():
    person = create_person()
    student_id = input("Enter your ID: ")
    return Student(person.name, person.email, person.phone_number, student_id, courses_enrolled=[], grades={})


def create_teacher():
    person = create_person()
    teacher_id = input("Enter teacher ID: ")
    return Teacher(person.name, person.email, person.phone_number, teacher_id, courses_taught=[])


def get_course_by_id(course_id):
    courses = [
        Course(course_id="MATH101", course_name="Mathematics 101", max_students=20, current_students=0),
        Course(course_id="PHY101", course_name="Physics 101", max_students=15, current_students=0),
        Course(course_id="ENG101", course_name="English 101", max_students=25, current_students=0),
    ]
    for course in courses:
        if course.course_id == course_id:
            return course

    return None


def main():
    print("Welcome to the classroom management system")

    role = input("Are you a student or a teacher? ")

    while role != "student" or role != "teacher":
        if role == "student":
            student = create_student()
            print(f"Welcome {student.name}, You are now a new student with us.")

            while input("Do you want to enroll in a course? (yes/no): ") == "yes":
                course_id = input("Enter the course ID you want to enroll in: ")
                course = get_course_by_id(course_id)

                if course:
                    course.enroll_student(student)
                else:
                    print("sorry, There is no course with this ID.")

            print("\nCourses you are enrolled in:")
            for course in student.courses_enrolled:
                print(course)

        elif role == "teacher":
            teacher = create_teacher()
            print(f"\nWelcome, {teacher.name}! You are now registered as a teacher.")

            while input("Do you want to teach a course? (yes/no): ").lower() == "yes":
                course_id = input("Enter the course ID you want to teach: ")
                course = get_course_by_id(course_id)
                if course:
                    teacher.courses_taught.append(course)
                    print(f"{teacher.name} is now teaching {course.course_name}.")
                else:
                    print("Invalid course ID. Please try again.")

            teacher.display_courses_taught()


if __name__ == "__main__":
    main()
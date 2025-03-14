
from fastapi import FastAPI, HTTPException
from student import Student

fastapi_app = FastAPI()

students = []
@fastapi_app.get("/")
def root():
    return {"message": "Hello World"}

@fastapi_app.get("/students", response_model=list[Student])
def get_students():
    return students

@fastapi_app.get("/students", response_model=list[Student])
def get_students_by_limit(limit: int = 3):
    return students[0:limit]

@fastapi_app.post("/student")
def create_student(student:Student):
    students.append(student)
    return student

@fastapi_app.get("/students/{student_id}", response_model=Student)
def get_student(student_id:int) -> Student:
    if student_id < len(students):
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@fastapi_app.put("/students/{student_id}")
def update_student(student_id:int, student:Student):
    if student_id < len(students):
      students[student_id] = student
      return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@fastapi_app.delete("/students/{student_id}")
def delete_student(student_id:int):
    if student_id < len(students):
      student = students[student_id]
      students.remove(student)
      return students
    else:
        raise HTTPException(status_code=404, detail="Student not found")
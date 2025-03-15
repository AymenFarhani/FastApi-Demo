
from fastapi import FastAPI, HTTPException
from student import Student

fastapi_app = FastAPI()

students = []
current_id = 1
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
    global current_id
    student.id = current_id
    students.append(student)
    current_id += 1
    return student

@fastapi_app.get("/students/{student_id}", response_model=Student)
def get_student(student_id:int) -> Student:
    student = next((s for s in students if s.id == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@fastapi_app.put("/students/{student_id}")
def update_student(student_id:int, new_student:Student):
    student = next((s for s in students if s.id == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = new_student.name
    student.email = new_student.email
    student.is_active = new_student.is_active
    return student

@fastapi_app.delete("/students/{student_id}")
def delete_student(student_id:int):
    student = next((s for s in students if s.id == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    students.remove(student)
    return students
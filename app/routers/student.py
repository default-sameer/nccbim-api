from bson.objectid import ObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from app.models import Student, User
from app.database import student_collection
from app.schemas import studentSerializer, studentsSerializer
from typing import Optional
from app.oauth2 import get_current_user

student = APIRouter(prefix='/student', tags=['Students'])


@student.get('/')
async def getAll(sort: Optional[str] = 'batch', limit: Optional[int] = 10, skip: Optional[int] = 0):
    student = student_collection.find().sort(sort).limit(limit).skip(skip)
    if student:
        return {"status" : "ok" , "data" : studentsSerializer(student)}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f"Student don't exist")
    
@student.get('/{id}')
async def getOne(id: str):
    if len(id) == 24:
        student = student_collection.find_one({'_id': ObjectId(id)})
        if student:
            return {"data" : studentSerializer(student)}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f"Student with id {id} dones't exist")
    else:
        return {'Message': 'Please Enter 24 Charater Long ID'}

@student.get('/get-by/{batch}')
async def getBatch(batch: int, sort: Optional[str] = 'name', skip: Optional[int] = 0, limit: Optional[int] = 10):
    students = []
    document = student_collection.find({'batch': batch}).sort(sort).skip(skip).limit(limit)
    for student in document:
        students.append(Student(**student))
    return {'data': students}


@student.post('/')
async def post(student: Student, current_user: User = Depends(get_current_user)):
    insert_student = student_collection.insert_one(dict(student))
    student = student_collection.find({'_id': insert_student.inserted_id})
    return studentsSerializer(student)

@student.put('/{id}')
async def put(id: str, student: Student, current_user: User = Depends(get_current_user)):
    student = student_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(student)})
    return studentSerializer(student_collection.find_one({'_id': ObjectId(id)}))

@student.delete('/{id}')
async def delete(id: str, current_user: User = Depends(get_current_user)):
    student_collection.find_one_and_delete({'_id': ObjectId(id)})
    return  {"status" : "ok" , "message" : 'Student Deleted'}




def studentSerializer(student) -> dict:
    return {
        "id" : str(student["_id"]),
        "batch": student["batch"],
        "name": student["name"],
        "tu_roll": student["tu_roll"],
        "tu_registration": student["tu_registration"],
    }
    
# def studentSerializer(student) -> dict:
#     return {
#         "id" : str(student["_id"]),
#         "batch": student["batch"],
#         "name": student["name"],
#         "email": student["email"],
#         "tu_roll": student["tu_roll"],
#         "tu_registration": student["tu_registration"],
#         "address": student["address"],
#     }
    



def studentsSerializer(students) -> list:
    return [studentSerializer(student) for student in students]


def user_helper(user) -> dict:
    return {
        "username": user['username'],
        "email": user['email'],
    }

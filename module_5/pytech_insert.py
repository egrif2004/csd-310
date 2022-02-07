from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.mclts.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

client = MongoClient(url)

db = client.pytech

thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
}
bilbo = {
     "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
}
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
}
students = db.students

print("\n  -- INSERT STATEMENTS --")
thorin_student_id = students.insert_one(thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")
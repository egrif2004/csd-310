MongoDB: insert_one()Example
fred = {
    "first_name":"Fred"
}
fred_student_id = students.insert_one(fred) .inserted_id

print (fred_student_id)

MongoDB: find ()Example
docs = db.collection_name.find ({})
for doc in docs:
    print(doc)
MongoDB: find_one () Example
doc = db.collection_name.find_one ({"student_id": "1007"})

print (doc["student_id"])

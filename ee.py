students= {
    "student1":{
        "name":"shahad",
        "age":19,
        "major":"cyber security",
        "skills":["python","Networking"]

    },
    "student2":{
         "name":"Sara",
         "age":23,
         "major":"Computer Science",
         "skills":["HTML","CSS"]

},

     "student3":{
        "name":"Leen",
        "age":17,
        "major":"Student",
        "skills":["Python","scratch"]
    }
}
print("Skills of student:")
for skill in students["student2"]["skills"]:

 print("-", skill)
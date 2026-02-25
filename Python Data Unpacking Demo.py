person = {
    "name": "Shahad",
    "age": 19,
    "city": "Jeddah",
    "job": "Programmer",
    "hobby": "Gaming"
}
def show_person(**info):
    name= info["name"]
    city= info["city"]
    other_info={k:v for k,v in info.items() if k not in ["name", "city"]}
    print(name)
    print(city)
    print(other_info)
show_person(**person)

# info={'key1':"value1",'key2':"value2",'key3':"value3","age":56,"isAdult":True,"marks":[81,76,99]}
# print(info)
# print(info["age"])
# print(info["marks"])
# info["key1"]="Apnaclg"
# info["isAdult"]=False
# print(info)
# nested dictionary
Student={
    "name":"Samridhi",
    "age":19,
    "marks":{
        "maths":99,
        "science":98,   
        "english":97
 }}
# print(Student)
# print(Student["marks"]["science"])
print(list(Student.keys()))
print(list(Student.values()))
print(list(Student.items()))
print(Student.update({"city":"delhi"}))
print(Student)
                      

nested_dic = {
    "Persona1":{
        "name": "david",
        "age": 23,
        "city":"guate"
    },
    "Persona1":{
        "name": "juan",
        "age": 23,
        "city":"guate"
        },
    "Persona1":{
        "name": "lopez",
        "age": 23,
        "city":"guate"
    }
}

for key, value in nested_dic.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")
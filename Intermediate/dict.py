dict1={"name":"max","age":28}
print(dict)
dict2=dict(name="mary",age=24)
print(dict2)
value=dict2["age"]
print(value)
del dict2["age"]
print(dict2)
dict1.pop("age")
print(dict1)
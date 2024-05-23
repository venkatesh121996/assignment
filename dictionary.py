dictionary={"name":"venkatesh","company":"Infinitude","course":"AIML","test":"python","key":"value"}

print(dictionary.keys())
print(dictionary.values())

x=dictionary.pop("key")
print(dictionary)

dictionary["car"]="Tesla"
print(dictionary)

a=list(dictionary)
b=list(dictionary.values())
print(a,b)
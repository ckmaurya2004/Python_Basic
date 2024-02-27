# d1 = list({"kiran":"dairy-milk","priya":"roti","shivani":"chawal", "m":"samosa"})
# print(d1)
# print(type(d1))
# d1["nakul"]="sweet"
# print(d1)
# del d1["nakul"]
# print(d1.get("kiran"))
# d1.update({"mamta":"chawmeen"})
# print(d1)
# d1.clear()
# print(d1)

# d2 = d1
# del d2["mamta"]
# print(d1)

# d2 = d1.copy()
# del d2["mamta"]
# print(d1)
# print(d2)

# x=d1.fromkeys("mamta")
# print(x)
# print(d1.pop("kiran"))
# print(d1.popitem())
# print(d1.values())
# print(d1.setdefault)

# print(type(d1))
# print(d1)


d1 = {"a":"apple","b":"boll","c":"cat","d":"dog"}
print("please ! enter your keys")
n = input()
print(d1[n])
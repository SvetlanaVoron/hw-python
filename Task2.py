f = open("Text2.txt", "r")
str = f.readlines()
print(str)
print(f"Количество строк: {len(str)}")

for i, str in enumerate(str, start=1):
    print(len(str.split()))
f.close()
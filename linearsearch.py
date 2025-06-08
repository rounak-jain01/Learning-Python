l = [56,89,345,256,23,77,3234,78,99,785,473,6753,785,64]
key = 99

for i in range(len(l)):
    if l[i] == key:
        print(f"{key} is at index {i}")
        break;
else:
    print(f"{key} is not found")


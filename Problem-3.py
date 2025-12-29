a = int(input("Enter a number: "))

if a % 2 == 0:
    limit = a - 1
else:
    limit = a

result = []
for i in range(limit // 2 + 1):
    result.append(2 * i + 1)

print(", ".join(map(str, result)))

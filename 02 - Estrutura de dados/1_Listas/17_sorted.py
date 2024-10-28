linguagens = ["python", "js", "c", "java", "csharp"]

array_sorted = sorted(linguagens)

print(array_sorted)

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
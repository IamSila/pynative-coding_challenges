def count_emma(statement):
    print("Given statement", statement)
    count = 0
    for i in range(len(statement) - 1 ):
        count += statement[i:i+4] == "Emma"
    return count


result = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", result, "times")
name = 0
print(name + True)

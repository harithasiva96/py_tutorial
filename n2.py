# Slicing

b="Hello world"
c="Helloworld"

print(b[2:5])
print(c[::-1])
# Get characters from the start
print(b[:5])
# Slice to the end
print(b[2:])
print(b[-5:-2])

x="Welcome Home"
print(x.upper())
print(x.lower())
print(x.replace("H","D"))
print(x.split())

word="python"
print(word[0:2])    # characters from position 0 (included) to 2 (excluded)
print(word[2:5])    # characters from position 2 (included) to 5 (excluded)
print(word[:2])     # character from the beginning to position 2 (excluded)
print(word[4:])     # characters from position 4 (included) to the end
print(word[-2:])    # characters from the second-last (included) to the end
print(word[:2] + word[2:])
print(word[:4] + word[4:])

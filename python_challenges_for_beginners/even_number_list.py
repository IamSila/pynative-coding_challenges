

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)

['P', 'Y', 'n', 'a', 't', 'i', 'v', 'e']


for i in x[0::2]:
    print(i)
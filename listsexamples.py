mylist = ["apple", "pear", "banana", "banana", "pear", "more poop", "banana", "durian"]

mylist.append("durian")

mylist[0] = "poo poo"

print(mylist)

# searching a list

index = -1
target = "banana"

for i in range(len(mylist)):
    if target == mylist[i]:
        index = i

print("I found %s at index: %d" % (target, index))

counter = 0
for i in range(len(mylist)):
    if target == mylist[i]:
        counter += 1

print("I found the %s %d many times" % (target, counter))


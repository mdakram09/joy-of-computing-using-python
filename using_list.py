shopping=["oil","turmeric","bread"]
for item in shopping:
    print(item,)


print("\n\n")
for i in range(len(shopping)):
    print(shopping[i])

ages=[12,34,65,87,23,5,4,5,6,7,8,23,56,32,54,34,12,12,12,22,5,4,7]
print(ages.count(5))
shopping.append("curd")
shopping.insert(2,"biryani")
print(shopping)

print(shopping[2:5])


ages.sort()
print(ages)

ages.reverse()
print(ages)
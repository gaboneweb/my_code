def even_numbers():
    num = 0
    while num < 101:
        if num % 2 == 0 and num != 0:
            yield num
        num += 1
def infinite_sevens():

  while True:

    yield 7

        

# for i in infinite_sevens():

#   print(i,end= "")

for i in even_numbers():
    print(i, end= " ")
print()


#Generators can be converted to lists

print(list(even_numbers()))


'''
Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list. 
'''
txt = input()

def words():
    #your code goes here
    for i in txt.split(" "):
        yield i

print(list(words()))
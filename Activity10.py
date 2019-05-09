from __future__ import division
import random
import string

#input student number and display
studentnumber = input("type studentnumber: ")
print("0. The studenent number is: ", studentnumber)


#calculate the length of the student number and count how many prime numbers are in it
lstunum = len(studentnumber)
x = 0

for i in studentnumber:
    p = int(i)
    #print(m)
    if p > 1:
        j = 2
        while(j <= (p/j)):
            if not(p%j): break
            j = j + 1
        if (j > p/j) : x = x + 1

print("1. The number of prime numbers in this student number is: ", x)

#calculate random number
p = x
if p == 0: p = 1

q = 0
q = random.randint(25, 51)
print("2. The random number is: ", q)

#divide the random number (q) with the amount of prime numbers (p)
r = q // p
print("3. The number of string generated is: ", r)

#generate list of strings and sort amount of vowels present in accending order

stringlist = [''] * r
vowellist = [0] * r
stringlength = 5
tempstring = ''

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

for w in range(0, r):
    #print(w)
    tempstring = randomString(stringlength)
    stringlist[w] = tempstring
    vowels=0
    for k in tempstring:
        if(k =='a' or k =='e' or k =='i' or k =='o' or k =='u' or k =='A' or k =='E' or k =='I' or k =='O' or k =='U'):
            vowels=vowels+1
    vowellist[w] = vowels
    #print(tempstring)
    tempstring = ''
    if stringlength == 5:
        stringlength = 7
    else:
        stringlength = 5

print("4. List of Strings: ")
print("******************")
for w in range(0, r):
    print(w, " - ", stringlist[w])

print("******************")
print("")
print("5. Sorted List: ")
print("******************")
for j in range(len(vowellist)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(vowellist)-1:
        #comparing the adjacent elements
        if vowellist[i]<vowellist[i+1]:
            #swapping
            vowellist[i],vowellist[i+1] = vowellist[i+1],vowellist[i]
            stringlist[i],stringlist[i+1] = stringlist[i+1],stringlist[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
for w in range(0, r):
    print(w, " - ", stringlist[w], " (Vowels: ", vowellist[w], ")")
print("******************")


input('Press ENTER to exit')

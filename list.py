a=[1,2,3,4,5]
a=['astha','bhardwaj']
print(a)
print(len(a))
print(a[1])
print(a[:-1])   #len(a)-1 = 4 , 4-1

#how to chage the value in a given list
a[0]='ravita'  # at the place of index 0 it will replace 1 with ravita
a[0:]='ravita' #it will split as it is a string
a[2:3]='ravita'
a[2:4]='ravita'
a[2:]='ravita'
a[0]=['ravita','astha']  # it will replace 1 with ravita astha
a[0:3]=['ravita','astha']
print(a)
b=["astha","ravita","mukul","radha","shreya","pandu","panda"]
print(len(b))
print(b[:2]) #2-1
b[2]='gautam'
b[2:3]='gautam'
b[2:3]='gautam'
b[2]=['gautam']
b[2:4]=['gautam']
print(b)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# how to add items to our list

a=[]
a.append("1,2,3,4,5")
a.append(1)
a.append(143)
a.append("ravita")
a.append("astha")
a.append("mukul")
a.append("3 friend")
print(a)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#some more method to add data in our list
#insert method
#how to join (concatenate) two list
#extend method
#difference between append and extend method

a=['astha','mukul','ravita']
a.insert(2,'radha')
a.insert(0,'shreya')
print(a)
b=[1,2,3,4,5,6,7,8,9,10]
c=a+b
print(c)
a.extend(b)
print(a)
a.append(b)
print(a)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# most common method used to delete a data in a list

#pop method

a=[1,2,3,4,5,"astha",'ravita','mukul']
a.pop()
a.pop(1)
# a.pop(10)
print(a)

#del method

del a[1]
print(a)

#remove method
b=[1,2,3,4,5,'astha','astha','ravita']
b.remove('astha')
print(b)

# in keyword in list
a=[1,2,3,4,5,6,7,8,9,10,'astha','ravita','mukul']
print(a)
if 'astha' in a:
    print("present")
else:
    print("not present")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#some more method
    
#count

a=[1,2,3,4,4,54,5,54,54,6,135]
b=['astha','ravita','mukul','radha','shreya']
print(a.count(4))

#sort
a.sort()
print(a)

b.sort()
print(b)    

# #sorted function

print(sorted(a))
print(a)

# #clear

a.clear()
print(a)

#copy

a_copy=a.copy()
print(a_copy)


'''string'''

a= 1,2,3,4,5
print(a)
print(a[:2])


''''''''''''''''''''''''''''''''''''''

"""compare list"""
# == , is


a=['apple','banana',6,4,'mukul','ravita','astha',7,9,6]
b=[2,3,"radha","shreya","orange","pear",'kiwi']
c=['apple','banana',6,4,'mukul','ravita','astha',7,9,6]
print(a==b) #== check value
print(a==c)
print(a is b) #is check either the two list are at same place in memory 


'''split method'''
# convert list to string

a='my name is astha bhardwaj and currently i am pursuing my gradution from b-tech'.split()
print(a) 
b='my name is astha bhardwaj and currently i am pursuing my gradution from b-tech'.split('i')
print(b)
name,age='astha, 19'.split(',')
print(name)
print(age)

'''join method'''
# convert a list to string
a=['apple','banana','6','4','mukul','ravita','astha','7','9','6']
print(','.join(a))

'''looping in list'''
#for loop
a=['apple','banana',6,4,'mukul','ravita','astha',7,9,6]
for i in a:
    print(i)
 
#while loop
b=['mukul','ravita','astha','radha','shreya',1,4,3]
i=0
while i<len(b):
    print(b[i])
    i+=1
a=[['apple','banana',6,4],['mukul','ravita','astha'],[7,9,6]]
print(a[0])
print(a[1])
print(a[2])
for i in a:
    print(a)
for sublist in a:
    for i in sublist:
        print(i)
print(a[2][0])
b=[[1,2,3],[4,5,6],[7,8,9]]
for i in b:
    print(i)

'''more about list'''
#generate list with range function
#something more about pop method
#index method
#pass list to a function

number=list(range(1,21))
print(number)
number.pop()
print(number.pop())
# print(number.index(20))
b=1,2,3,4,5,6,7,9,8,1,2
print(b.index(1,4)) #1 dekho kaha hai 4 k baad se
print(b.index(2,4,11)) #4 se 11 tak k bich me 2 kaha h



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Questions on list 

''' 1. define a function which will take list containing number as input
and return list contaning square of every elements
example
numbers=[1,2,3,4]
square_list(numbers)------->return-------->[1,4,9,16]'''

def sq_list(a):
    number_list=[]
    for i in a:
        number_list.append(i**2)
    return number_list

number=list(range(1,11))
print(sq_list(number))

def astha(a):
    number=[]
    for i in a:
        number.append(i**2)
    return number
b=list(range(1,20))
print(astha(b))


#ex 2
'''write a code in python to reverse a list'''
# case 1
def ravita(a):
    a.reverse()
    return a

number=[1,2,3,4]
print(ravita(number))
# case 2
def reverse_list(a):
    return a[::-1]
number=[1,2,3,4]
print(reverse_list(number))
# case 3
def ravita(l):
    b=[]
    for i in range(len(l)):
        popped_item=l.pop()
        b.append(popped_item)
    return b

# number=[1,2,3,4]
number=list(input("enter the list: "))
print(ravita(number))


# ex 3
'''define a function that take list of word as argument and return list with reverse of every element in that list'''
def reverse(l):
    a=[]
    for i in l:
        a.append(i[::-1])
    return a
c=['astha','ravita']
print(reverse(c))

#ex 4
'''write a code in python to filter even and odd from a list'''
def even_odd(l):
    b=[]
    c=[]
    for i in l:
        if(i%2==0):
            b.append(i)
        else:
            c.append(i)
    # output=[b,c]
    # return output
    # return b+c
    return b,c

a=[1,2,3,4,5,6,7,8,9,10]
print(even_odd(a))

#ex 5

'''write a code in python to check common value in list'''

def common_number(l1,l2):
    b=[]
    for i in l1:
        if i in l2:
            b.append(i) 
    return b
# print (common_number([1,2,3,4],[2,3,7,8]))
b=list(input("enter the list: "))
a=list(input("enter the list: "))
print(common_number(b,a))

# ex 6

'''to check how many list are their inside a list'''
      
def num(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
b=[1,2,3,[2,3],[]]
print(num(b))

'''max and min'''
a=[1,2,3,4,5,7]
print(max(a))
print(min(a))
def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(a))
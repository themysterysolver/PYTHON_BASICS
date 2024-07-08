#LISTS is mutable!
a=[1,'hello',3.14159,[2,4,6]]
print(a," is my list")
print("length of a:",len(a));
a[0:4]=[1,2,3,4]
a[3]='yo'
#changing varaiables!
print(a," is my list")
print(a.append(5),'appended string')#.append() one element @once
print(a," is my appended list")
print(a.extend([6,7,8,9,10]),'extended string')#.extendd([ ]) more than one element @once
print(a," is my extended list")
print(a.insert(9,'hello I am replaced at index 9'))#.insert(index,element)
print(a," is my list")
del a[0]
'''index know'''#del lname(index)/(range=>from to) 
print(a,'deleted oth index')
del a[0:6]#5th index
print(a,'deleted o to 6-1th index!! index')
print(a.remove(8),'elemnt 8 is removed')#index unknown!!! element known!!!
print(a," is my list")
b=a.pop(1) #index know!
print(b,'is the pooped up element')
a.clear()
print(a," is my list without elemnets!!.")#clear() everything juts keeps th EMPTY list!!
a=list(range(1,11,2)) #list from range()
print(a," is my list using range!")
c=a.copy()
print(a," is my list",c,"is the copy")
''' .count(substr,start,end).......counts the string'''# .count(value) in list counts the number of similar values! 
''' similar to str.find() returns the index of the first elemennt! '''#.index(element)
a.extend([3,3,3,3,3,3])
print(a," is my list after extend!!")
count=a.count(3)
print(count,'  is the count of no of  3 in the list!')
i=a.index(3)
print(i," is the index of 1st no 3 in list after appending!!")
del a[6:12]
print("the list after deltion from index 6 to 11(12-1) is",a)
a.reverse()
print(a,'is the reversed string!')
#.sort() ......default ascending,reverse is SET as true then descending!
maxy=max(a) #max(list)
miny=min(a) #min(list)
sumy=sum(a)#sum(list)
print("the max is {} and the minimum is {} and sum of the list is {}".format(maxy,miny,sumy))


#TUPULES is immutable! [ ]----->() unordered hence no indices
'''  list and tupules can be createed in empty a=[] , a=()'''
a=tuple(a)#tuple from list!
print(a,"a is a tuple!")
#list and tuples are classes in python!
del a
t=tuple(list(range(0,30,2)))
'''tuple assignement (a,b)=(1,2)'''
def max_min(t):
    max_=max(t)
    min_=min(t)
    return (max_,min_)
(mx_val,mn_val)=max_min(t)
print("the max is {} and min is {} of the tuple {}".format(mx_val,mn_val,t))

#SETS are mutable an unique! and sets can have diff data type!
t=set(t)
print(t,"is a set")
#.add()
#A.union(B) |
#A.intersection(B) &
#A.symmetric_difference(B) ^ (A&B)-(A|B)
#A.difference(B) A-B
#is_prime

''' THEY ARE
    DATA STRUCTURE!!!'''
#DICTIONARIES!!
#var={key:value,}
# create var{}
#so, while the syntax for creating an empty set using {} appears similar to creating an empty dictionary,
#Python interprets it as an empty dictionary. If you want to create an empty set, it's safer to use set() or {} with a space inside (i.e., { }).
''' list=[z**2 for z in range(1,11)]
    dict={x:x*2 for x in range(1,11}'''
#acess using dict[key]
#adding extra element dict[new key]=new val/element!













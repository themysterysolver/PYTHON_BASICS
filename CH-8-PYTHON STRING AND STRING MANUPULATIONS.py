#strings are immutable!
#-ve index from last!
'''' int(x,2/10/8/16)''' #to decimal
''' format(x,b/x/o/f)''' #decimal to others!!
#str[ ]
a=input("enter a sentance:")
print("str length:",len(a)) #len()
b,c=input("enter the word to be replaced:"),input("enter the NEW word:")
print(a.replace(b,c)) #replace(old,new)
#del a
print(a *4) #repeats <str*num>
#splice operator<[start,end,stride]> #end=end-1!!!!!!
#formating strings %d,%s,%c (str%())
# .format() { } -placeholders.....str.format()
print(a.capitalize()) #.capitalixe()
print(a.lower()) #small
print(a.islower()) #if small
print(a.isupper()) #if upper
print(a.center(20,'$')) #.center(width,'symbol')
print(a.find("abi",0,10)) #.find(substr,start,end)
print(a.isalnum())#if alphanumerical
print(a.isalpha())# if alphabets
print(a.isdigit())#if nums
print(a.title()) #1st leteer CAPS
print(a.swapcase()) #swaps!
print(a.islower()) #small
print(a.islower())
''' .count and .find '''
#.counts substr .count(substr,start,end) 
'''in and not in''' #are call MEMBERSHIP OPERATORS!!


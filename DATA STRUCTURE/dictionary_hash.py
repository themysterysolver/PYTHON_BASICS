#ABOUT dictionary!
d={}
di=dict()
print(d,di)
d[1]='a'
print(d,di)
val=d[1]
print(val)
a=[i*13 for i in range(2,10)]
for index,key in enumerate(a): '''enumerate'''
    di[index]=key
print(di)
for key,val in di.items(): '''return list of tupes( key ,value pairs)'''
    print(key,val)
print(d.get(100,0)) '''to get default'''
print(di.items())'''list of items(key,val)'''
print(di.keys()) '''list of keys'''
print(di.values()) '''list of values'''

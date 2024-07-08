x=int(input("enter x:"))
if x>=90 and x<100: #and 
        print("O grade")
elif  x>=80 and x<90: #rem :
        print("A+ grade")
else:
        print("failed")
if "hello" in "My name is prabha! hello":
        print("found")
else:
        print("not found")
n=int(input("enter n:")) #sum
sum=float((n*(n+1))/2)
print("sum of n natural numbers:",sum)
sum=0
i=0
while(i<=n): #while loop #whille loop can have a else part too!!
        sum=sum+i
        i=i+1
print("sum of n natural numbers:",sum)
for ch in "hello":  #ch was never declared!!
    print(ch,end='') #in this case output will come in the same line adjacent to each other!!!!!
print("\n")
for i in range(-10,11,1): #start,end,step     #also end=end-step!!! #range(20),0-19 inc by step 1!!
    print(i,sep='\n')
# make use of pass,continue,break!!

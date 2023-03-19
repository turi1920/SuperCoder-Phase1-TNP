#Positional Function

def function (n1,n2,n3,n4):
    print(n1,n2,n3,n4)

function(10,20,30,40)

#KeyWord Arguments


def function (n1,n2,n3,n4):
    print(n1,n2,n3,n4)

function(n2=10,n1=20,n4=30,n3=40)

#default Function

def function3(name , roll, branch , Collegename="Giet"):
    print(name ,roll,branch,Collegename)

function3("Pawan","20cse323","Cse","GIET")

#OverLoading Function

def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()

def add(*var):
    sum=0
    for i in var:
        sum+=i
    return sum
print(add(10,20))






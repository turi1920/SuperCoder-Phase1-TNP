
#Challange1 Number of Digit and Alphabet
'''
a = input()
l = []
d=0
alpha=0
for i in a:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        alpha=alpha+1
l.append(alpha)
l.append(d)
print(l)

#Challange2 Joing the First And Last from a list

b=[]
c=0
a = int(input())
l = list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==a:
            b.append((l[i],l[j]))
            c+=1
print(b)
print(c)


#Challange 3  join 2 digit from last and first

def returnstring(s):
    k=""
    d = len(s)
    if d <= 2:
        return -1
    else:
        k += (s[:2]+s[-2]+s[-1])
        return (k)
s = input()
print(returnstring(s))


#Challange 4  Playing with Ing and Ly

def unchange(s):
    if(len(s)<3 and):
        return s
    elif(s[-3:]=="ing"):
        s+="ly"
        return s
    elif(s[-3:]!="ing"):
        s+="ing"
        return s
s = input()
print(unchange(s))



#Challange 5  number of digit is equal and Should have each different number

def check_double(a):
    n = a*a
    one = str(a)
    two = str(n)
    if(len(one)==len(two)):
        s=[]
        d=[]
        for i in one:
            s.append(i)
        for i in two:
            d.append(i)

        for i in s:
            if s[i] == d[i]:
                return True
    else:
        return False
a = int(input())
print(check_double(a))


# Challange 6 Student frequency


def f_m_t_a(a):
    avg=0
    sum=0
    c=0
    for i in a:
        sum+=i
        avg=sum/10
    for i in a:
        if i > avg:
            c+=1

    return (c/10)*100

def g_f(a):
    l=[]
    z=0
    m = max(a)
    for i in range(0,m):
        for j in a:
            if(i==j):
                z+=1
        l.append(z)
        z=0
    return(l)


def shorts(l):
    return sorted(l)




l = tuple(map(int,input().split()))
print(f_m_t_a(l))
print(g_f(l))
print(shorts(l))



# Challange 7 Language Learning

def sub(d,l):
    l2=[]
    for i in l:
        l2.append(d[i])
    return l2

l ={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(sub(l,list1))


#Challange 8
n1 = int(input())
n2 = int(input())
result=[]
array = [for i in range (n1,n2+1)]
for i in range (len(array)):
    for j in range(i,len(array)):
        result.append()
'''




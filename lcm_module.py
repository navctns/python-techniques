#93.Program to create modules for LCM, GCD and HCF for n numbers

"""
def lcm(a,b):
    set1=set([i for i in range(2,a//2+1) if a%i==0])
    set2=set([i for i in range(2,b//2+1) if b%i==0])
    return min(set1.intersection(set2))
"""
"""
def lcm(*a):
    set1={}
    #set1=set([i for i in range(2,a//2+1) if a%i==0])
    set1.update([i for i in range(2,a//2+1) if a%i==0])
    #set2=set([i for i in range(2,b//2+1) if b%i==0])
    #return min(set1.intersection(set2))
    return min(set1)
"""
"""
def lcm(*a):
    list1=list(a)
    list_all=[]
    set1=set()
    set2=set()
    for i in list1:
        for j in range(2,i//2):
            if i%j==0:
                if j not in set1:
                    set1.add(j)
                    
                
            
        list_all.append(set1)#all sets combinded to a list
        set1.clear()
        #lcm_val=list_all[0].intersection(list_all[1:])
    return lcm_val
        #set1.update([j for j in range(2,i//2) if i%j==0])
    return min(set1)
"""
"""
def lcm(*a):
    '''
    input: sequence of numbers
    output: lcm
    logic:
    input is converted to a list
    all multiplicants of all numbers are stored to a list by cheking
    num%i==0
    then found the common multiplicants by comparing its count with the
    length of input(since it should be common to every input)
    then took the minimum from it
    '''
    list1=list(a)
    len_in=len(list1)#length of input
    list_all=[]#all multiplicants
    list_fin=[]#common multiplicants
    #set1=set()#not used here
    #set2=set()#not used here
    for i in list1:
        for j in range(2,i//2+1):
            if i%j==0:
                list_all.append(j)
    print("listall:",list_all)#for debugging
    
    for i in list_all:
        if list_all.count(i)==len_in:
            list_fin.append(i)
    #print(list_fin)#for debugging
    #print("len_in:",len_in)#debugging
    if len(list_fin)==0:
        print("No lcm")
        return None
    else:
        return min(list_fin)
 """

def lcm(*a):
    """
    input: sequence of numbers
    output:LCM
    """
    list1=list(a)
    listm=max(list1)
    list_all=[]#all products
    list_fin=[]#common products to all nums
    for i in list1:
        for j in range(1,listm+1):
            list_all.append(i*j)
    for k in list_all:
        if list_all.count(k)==len(list1):
            list_fin.append(k)
    return min(list_fin)

def gcd(*a):
    """
    input: sequence of numbers
    output: GCD of numbers
    logic:
    input is converted to a list
    all multiplicants of all numbers are stored to a list by cheking
    num%i==0
    then found the common multiplicants by comparing its count with the
    length of input(since it should be common to every input)
    then took the maximum from it
    """
    list1=list(a)
    len_in=len(list1)#length of input
    list_all=[]#all multiplicants
    list_fin=[]#common multiplicants
    #set1=set()#not used here
    #set2=set()#not used here
    for i in list1:
        for j in range(2,i//2+1):
            if i%j==0:
                list_all.append(j)
    print("listall:",list_all)#for debugging
    
    for i in list_all:
        if list_all.count(i)==len_in:
            list_fin.append(i)
    #print(list_fin)#for debugging
    #print("len_in:",len_in)#debugging
    if len(list_fin)==0:
        print("No lcm")
        return None
    else:
        return max(list_fin)   

    
#print(lcm(15,6,18,27))
""""
def gcd(a,b):
    set1=set([i for i in range(2,a//2+1) if a%i==0])
    set2=set([i for i in range(2,b//2+1) if b%i==0])
    return max(set1.intersection(set2))
    """
"""def gcd(a,b):
    if a>b:
        a=a-b
    else:
        b=b-a
    return a
"""

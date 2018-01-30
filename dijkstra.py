## I'll use math.inf to represnt infinite number
import math

################# (Graph info) ##################
######## ( {adj list} , {vertices} ) ############

def graphinfo(fname):
    file = open(fname, 'r')
    content = file.readlines()
    file.close()
    for i in range(len(content)):
        content[i]=content[i].replace('\n','')
        content[i]=content[i].split()

    adj={}
    vertx={}
    for i in range(1,len(content)):
        infinity=math.inf
        vertx[content[i][0]]=infinity
        vertx[content[i][1]]=infinity
        if(content[i][0] in adj.keys()):
            adj[content[i][0]].append((content[i][1],content[i][2]))
        else:
            adj[content[i][0]]=[(content[i][1],content[i][2])]
    for i in vertx:
        if(i not in adj):
            adj[i]=[]
    for i in adj:
        adj[i].sort()
    

    return(adj,vertx)



############### HEAP implementaion ###############

def swap(l,s,d):
    tmp=l[s]
    l[s]=l[d]
    l[d]=tmp
    
def heapadd(l,item):
    l.append(item)
    ## Top/min : k --> [ L: 2k+1 -----  R: 2k+2  ]
    c=len(l)-1
    p=int((c-1)/2)
    while(c>0 and l[p][1]>l[c][1]):
        swap(l,c,p)
        c=p
        p=int((c-1)/2)

def heapdecrease(l,key,value):
    c=0
    flag=True
    while(flag and len(l)>0):
        if(l[c][0]!=key):
            c+=1
        else:
            flag=False
    l[c]=(key,value)
    p=int((c-1)/2)
    while(c>0 and l[p][1]>l[c][1]):
        swap(l,c,p)
        c=p
        p=int((c-1)/2)

def heapmin(l):
    llast=len(l)-1
    swap(l,0,llast)
    pop=l.pop()
    llast=len(l)-1
    ###### To fix the heap stracture #######
    parent=0
    flag=True
    while(flag):
        ## left child and Righ child
        ## Top/min : k --> [ L: 2k+1 -----  R: 2k+2  ]
        lc=(2*parent)+1
        rc=(2*parent)+2
    
        if(lc>llast): ## no children
            flag=False
            
        elif(lc==llast): ## only left child
            flag=False
            if(l[lc][1]<l[parent][1]):
                    swap(l,parent,lc)
                    
            ##if parent > child --> swap(l,parent,childL)
                    
        elif(lc<llast): ## both children exist
            #pick the minimum
            if(l[lc][1]>l[rc][1]): #if the left child larger than the right --> swap parent/right if parent greater
                if(l[rc][1]<l[parent][1]):
                    swap(l,parent,rc)
                    parent=rc
                else:
                    flag=False
            else: #if the right child larger than or equal to the left --> swap parent/left if parent greater
                if(l[lc][1]<l[parent][1]):
                    swap(l,parent,lc)
                    parent=lc
                else:
                    flag=False
    return(pop)


############### Dijkstra’s algorithm implementaion ###############

def dj(fname,s='A'):
    graph=graphinfo(fname)
    graph[1][s]=0
    H=[]
    keys={}
    pre={}
    adj=graph[0]
    for i in graph[1]:
        heapadd(H,(i,graph[1][i]))
        keys[i]=graph[1][i]
        pre[i]=None
    while(len(H)>0):
        u = heapmin(H)
        for i in adj[u[0]]:
        # i is tuple(neighbot, weight)
            if(float(keys[i[0]])>(float(keys[u[0]])+float(i[1]))):
                keys[i[0]]=(float(keys[u[0]])+float(i[1]))                   
                heapdecrease(H,i[0],keys[i[0]])
                pre[i[0]]=u[0]
    return(keys,pre)


## This function Dijkstra(file_name, start, end) outputs the followings :
##    1- The weight of a shortest path from vertex A to vertex B in the graph.
##    2- The sequence of vertices on a shortest path from A to B.
   
def dijkstra(fname,s='A',e='B'):
    result=dj(fname,s)
    weight=(int(result[0][e]))
    sequence=''
    l=[]
    l.append(e)
    pre=result[1][e]
    while(pre!=None):
        l.append(pre)
        pre=result[1][pre]
    last=len(l)-1
    while(last>=0):
        sequence+=(l[last]+' ')
        last-=1

    print(weight)
    print(sequence)

while True:
    fname=input('\nPlease enter the file\'s name ( i.e. Case1.txt ) / or q for Quit : ')
    print('')
    if(fname.upper()=='Q' or fname.upper()=='QUIT'):
        break
    else:
        try:
            dijkstra(fname)
        except:
            print('Sorry :(\nThe file\'s name is invalid\n')
print('\nThank you')

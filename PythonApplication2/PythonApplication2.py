class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return self.data


class LinkList:

    def __init__(self,n=None):
        self.head = n
    
    def __str__(self):
        s = ',data = '
        t = self.head
        i=0
        while t != None :
            i+=1
            s += t.data
            if t.next != None :
                s+='->'
            t = t.next
        return 'size= ' +str(i)+' '+s
    
    def tail(self):
        t = self.head
        while t.next != None :
            t = t.next
        return t

    def size(self):
        t =self.head
        cnt = 0
        while t != None :
            cnt += 1
            t = t.next
        return cnt

    def append(self,data):
        t = self.head
        while t.next!=None:
            t = t.next
        t.next = node(data)

    def add(self,data,address):
        if address == 0 :
            n = node(data,self.head)
            self.head = n
        elif  address > self.size() :
            print('error your address is not in bound')
            return None        
        else :
            t = self.head
            cnt = 0
            while cnt < address-1 : # (0)_n1_--(1)-->_n2_--(2)-->_n3_
                t = t.next
                cnt+=1
            #print(t)
            temp_node = node(data,t.next)
            t.next = temp_node

    def remove(self,n):
        # _n1_-->_n2_-->_n3_
        t = self.head
        p = self.head
        if n == 1 :
            self.head  = t.next
            return t
        elif n > self.size():
            print('ERROR ont of bound of this LL')
            return None
        else:
            preT = t
            t = t.next
            cnt = 2
            while cnt != n :
                cnt += 1
                preT = t
                t = t.next
            preT.next = t.next
            return p




    def BottomUp(self,n):
        N = (self.size()*n)//100
        cnt = 0  #(self.size()*n)//100
        oldH = self.head
        oldT = oldH
        index = None
        while oldT.next!=None:
            if cnt<N:
                cnt+=1
                index = oldT
            oldT = oldT.next
        #print(N,index)
        self.head = index.next
        oldT.next = oldH
        index.next = None
        return self

    def deBottomUp(self,n):
        N = self.size()-(self.size()*n)//100
        cnt = 0
        oldH = self.head
        oldT = oldH
        index = None
        while oldT.next != None :
            if cnt < N :
                index = oldT
                cnt+=1
            oldT = oldT.next
        #print(index,oldT)
        self.head = index.next
        oldT.next = oldH
        index.next = None
        return self

    def riffleShuffle(self,n):
        N = (self.size()*n)//100
        t = self.head
        cnt = 0 
        while cnt < N-1 :
            t = t.next
            cnt+=1
        #print(t)
        Lhead = self.head
        Rhead = t.next
        Rtail = Rhead
        Ltail = Lhead
        numAdd = 0
        dataAdd = []
        while Rtail != None :
            dataAdd.append(Rtail.data)
            numAdd+=1
            Rtail = Rtail.next
        #print(dataAdd)

        while Ltail.next != Rhead:
            Ltail = Ltail.next
        Ltail.next = None
        #print(Lhead,Ltail,Rhead,Rtail)
        for i in range(numAdd,0,-1):
            #print(i)
            self.add(dataAdd[i-1],i)
    
    def deRiffleShuffle(self,n):
        N = self.size()-(self.size()*n)//100
        for i in range(2,2+N):
            self.append(self.remove(i).data)

n = node('1')
l = LinkList(n)
l.append('2')
l.append('3')
l.append('4')
l.append('5')
l.append('6')
l.append('7')
l.append('8')
l.append('9')
l.append('0')
print(l)

print(l.BottomUp(30))
l.riffleShuffle(60)
print(l)    
#print(l.remove(9))
l.deRiffleShuffle(60) 
print(l)
print(l.deBottomUp(30))

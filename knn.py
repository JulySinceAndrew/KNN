import numpy as np
Inf=999999999
import matplotlib.pyplot as plt

class sort_list(object):
    def __init__(self,k):
        self.list=[]
        self.maxarg=0
        self.k=k
        for i in range(k):
            self.list.append((-1,Inf))

    def sort(self):
        max=-1
        arg=-1
        for i in range(self.k):
            if max<self.list[i][1]: #0为index 1为value
                arg=i
                max=self.list[i][1]
        self.maxarg=arg

class KNN(object):
    def __init__(self,p,k,X_set,Y_set): #p对应选取的Lp距离
        self.p=p
        self.k=k
        self.X=X_set
        self.Y=Y_set
    def predict(self,vector):
        min_dis=sort_list(self.k)
        for i in range(self.X.shape[0]):
            dis=0
            for l in range(self.X.shape[1]):
                dis+=abs(self.X[i][l]-vector[l])**(self.p)
            dis=dis**(1/self.p)
            if dis<min_dis.list[min_dis.maxarg][1]:
                min_dis.list[min_dis.maxarg]=(i,dis)
                min_dis.sort()
        y=set(self.Y)
        count=dict()
        for value in y:
            count[value]=0
        for v in min_dis.list:
            count[self.Y[v[0]]]+=1
        print(count)
        print(min_dis.list)
        max=0
        maxy=-1
        for v in count.items():
            if max<v[1]:
                max=v[1]
                maxy=v[0]
        return  maxy

X_set=np.array([[9,9],[0,0],[2,4],[3,3],[3,4],[4,2],[4,4],[4,3],[5,3],[6,2],[7,1],[2,9],[3,8],[4,6],[4,7],[5,6],[5,8],[6,6],[7,4],[8,4],[10,10],[1,1]])  #0-1内
Y_set=np.array([1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2])
plt.savefig("./result.jpg")
X1_predict=np.linspace(0,10,60)
X2_predict=np.linspace(0,10,60)
nn=KNN(2,3,X_set,Y_set)
i=0
for x1 in X1_predict:
    for x2 in X2_predict:
        v=(x1,x2)
        y=nn.predict(v)
        i=i+1
        if y ==1:
            plt.plot(v[0],v[1],'o',color='orangered')
        else :
            plt.plot(v[0],v[1],'o',color='skyblue')
for i in range(X_set.shape[0]):
    if Y_set[i] == 1:
        plt.plot(X_set[i][0],X_set[i][1],'ro',color='darkred')
    else:
        plt.plot(X_set[i][0], X_set[i][1],'ro',color='blue')
plt.show()

# https://github.com/sipocz/perceptron.git

class perceptron:
    
    def __init__(self) -> None:
        self.fitted=False
    
    def permutation(self,size):
        f=[]
        for i in range(len(f)):
            f.append(i)
        pass

    def vek_add(self,v1,v2):
        o=v1
        for i in range(len(v2)):
            o[i]+=v2[i]
        print("vek_ADD",o)
        return(o)        


    def vek_skalar_mul(self,v,s):
        print("MUL:",v, "skalar:",s)
        o=[]
        for i in range(len(v)):
            o.append(v[i]*s)
        print("MUL out:",o)
        
        return(o)

    def vek_mul(self,v1,v2):
        su=0
        for i in range(len(v1)):
            su+=v1[i]*v2[i]
        return(su)
    
    def mat_mul(self,M,v):
        o=[]
        for i in len(M):
            o.append(M[i],v)
        return(o)
    
    

    def convert_to_01(self,v):
        o=[]
        for i in v:
            if i<=0:
                o.append(0)
            else:
                o.append(1)
        return(o)


    def fit(self, X,y,n_epochs=10, lr=0.01):
        self.n_samples=len(X)
        self.n_features = len(X[0])
        self.y=y
        self.X=X
        self.n_epochs=n_epochs
        self.lr=lr
        self.akt=0
        self.weights=[]
        for i in range(self.n_features):
            self.weights.append(0)
        self.bias=0

        for self.akt in range(self.n_epochs):
            #Xakt=self.X[self.akt]
            print("Starting epoch:", self.akt)
            print("Weights:",self.weights)
            for x,label in zip(X,y):
                y_=label
                # perceptron esetén [-1, 1] a tartomány
                if y_==0:
                    y_=-1
                
                
                if (self.vek_mul(self.weights,x)+self.bias)*y_<=0:
                    print("Weigths korrection")
                    self.weights=self.vek_add(self.weights,self.vek_skalar_mul(x,y_*self.lr))
                    self.bias=self.bias+y_*self.lr
        self.fitted=True
        print("Finished training.")
    
    def predict(self,X):
        if not self.fitted:
            raise ValueError("Perceptron model is not fitted")
        elif len(X[0]) != self.n_features:
            raise ValueError(f"Incorrect number of input features (expected {self.n_features})")
        else:
            
            # Please think through and explain the trainer, WHY this is a matmul!?
            #You can remove the line, just here to make you think.
            activations=[]
            for i in range(len(X)):
                activations.append(self.vek_mul(X[i],self.weights)+self.bias)

            
            
            
            o = self.convert_to_01(activations) 
            # Tricky conversion of signs to 0/1 labels
            return o        

X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1]
pcn=perceptron()
pcn.fit(X,y,n_epochs=1000)
print(pcn.predict(X))


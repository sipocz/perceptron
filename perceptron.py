# https://github.com/sipocz/perceptron.git

class perceptron:
    
    def __init__(self) -> None:
        self.fitted=False
    
    def permutation(self,size):
        f=[]
        for i in range(len(f)):
            f.append(i)
        pass

    def vek_skalar_mul(self,v,s):
        print("MUL:",v)
        su=0
        for i in range(len(v)):
            su+=v[i]*s
        return(su)

    def vek_mul(self,v1,v2):
        sum=0
        for i in range(len(v1)):
            sum+=v1[i]*v2[i]
        return(sum)
    
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
            Xakt=self.X[self.akt]
            print("Starting epoch:", self.akt)
            for x,label in zip(X,y):
                y_=label
                # perceptron esetén [-1, 1] a tartomány
                if y_==0:
                    y_=-1
                
                
                if (self.vek_mul(self.weights,x)+self.bias)*y_<=0:
                    self.weights+=self.vek_skalar_mul(x,y_*self.lr)
        self.fitted=True
        print("Finished training.")
    
    def predict(self,X):
        if not self.fitted:
            raise ValueError("Perceptron model is not fitted")
        elif X.shape[1] != self.n_features:
            raise ValueError(f"Incorrect number of input features (expected {self.n_features})")
        else:
            
            # Please think through and explain the trainer, WHY this is a matmul!?
            #You can remove the line, just here to make you think.
            activations = self.mat_mul(X, self.weights) + self.bias
            o = self.convert_to_01(activations) 
            # Tricky conversion of signs to 0/1 labels
            return o        

X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1]
pcn=perceptron()
pcn.fit(X,y,n_epochs=100)


import random
class matrix:
    #Matrix Representation

    def randmat(self,n,m):
        mat = []
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(random.randint(0,10))
            mat.append(row)
        return mat
            
    def constant(self,n,m,c):
        mat =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(c)
            mat.append(row)
        return mat
    
    def zeros(self,n,m):
        x = self.constant(n,m,0)
        return x
    
    def ones(self,n,m):
        return constant(n,m,1) 
    
    def eye(self,n):
        mat =[]
        for i in range(n):
            row =[]
            for j in range(n):
                if j==i:
                    row.append(1)
                else:
                    row.append(0)
            mat.append(row)        
        return mat  
    #Slicing
    def shape(self,M):
        return tuple(M)
    
    def row(self,M,n):
        if(n>len(M)):
            return "Matrix's row exceeded"
        for i in range(len(M)):
            if i == n-1:
                return M[i]

    def col(self,M,n):
        col_mat = []
        if(n>len(M[1])):
            return "Matrix's column excedeed"
        for i in range(len(M)):
             col_mat.append(M[i][n-1])
        return col_mat
    
    def block(self,M,n_0,n_1,m_0,m_1):
        try:
            small_mat=[]
            for i in range(m_0,m_1+1):     #Traversing the matrix
                row =[]
                for j in range(n_0,n_1+1):
                    row.append(M[j-1][i-1])
                small_mat.append(row)
        except IndexError as ie:
            return ie                     #catching index out of range error     
        return small_mat
    
    def transpose(self,M):
        trans_mat = []
        for i in range(len(M[0])):
            row=[]
            for j in range(len(M)):
                row.append(M[j][i])  
            trans_mat.append(row)
        return trans_mat
    def scalarmul(self,M,c):
        for i in range(len(M)):
            for j in range(len(M[0])):
                M[i][j]=M[i][j]*c
        return M
    
    def add(self,M,N):
        if(len(M)!=len(N) or len(M[0])!=len(N[0])):
            return "Invalid Size of Matrices"
        sum_mat=[]
        for i in range(len(M)):
            row=[]
            for j in range(len(M[0])):
                row.append(M[i][j] + N[i][j])
            sum_mat.append(row)
        return sum_mat
    
    def sub(self,M,N):
        if(len(M)!=len(N) or len(M[0])!=len(N[0])):
            return "Invalid Size of Matrices"
        sub_mat=[]
        for i in range(len(M)):
            row=[]
            for j in range(len(M[0])):
                row.append(M[i][j] - N[i][j])
            sub_mat.append(row)
        return sub_mat
    def elementmult(self,M,N):
        if(len(M)!=len(N) or len(M[0])!=len(N[0])):
            return "Invalid Size of Matrices"
        ele_mat=[]
        for i in range(len(M)):
            row=[]
            for j in range(len(M[0])):
                row.append(M[i][j] * N[i][j])
            ele_mat.append(row)
        return ele_mat
    def matmult(self,M,N):
        if(len(M[0])!= len(N)):
            return "Invalid Size of Matrices"
        mul_mat=[]
        for r in range(len(M)):
            row=[]
            for c in range(len(N[0])):
                total =0
                for k in range(len(M[0])):
                    total+= M[r][k]*N[k][c]
                row.append(total)
            mul_mat.append(row)
        return mul_mat
    
    def dot(self,A,B):
        if(len(A)!=len(B)):
            return "Invalid Vector Size"
        sum=0
        for i in range(len(A)):
            mul = A[i]*B[i]
            sum+=mul
        return sum
    def outer(self,A,B):
        if(len(A)!=len(B)):
            return "Invalid Vector Size"
        out_mat=[]
        for i in range(len(A)):
            row = []
            for j in range (len(B)):
                row.append(A[i]*B[j])
            out_mat.append(row)
        return out_mat
    
    def norm(self,M,i):
        if(i==1):
            norm_list=[]
            sum = 0
            for i in range(len(M)):
                sum+= M[i]     
            return sum
        elif(i==2):
            sum = 0
            for i in range(len(M)):
                sum+= M[i]**2
            norm2 = sum**(0.5)
            return norm2
        elif(i==0):
            return max(M)
        else:
            sum = 0
            for e in range(len(M)):
                sum += M[e]**i
            norm_p= sum ** (1. /i)
            return norm_p
    if __name__ == '__main__':
        main()
 
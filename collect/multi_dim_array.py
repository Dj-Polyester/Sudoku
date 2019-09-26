class MultiDimArray:
    def __init__(self,*args):
        self.dims=args[:-1]
        self.dim=len(self.dims)
        self.letter=args[-1]
        self.array=[]
        self.ndarray(self.dim,self.dims,self.letter,self.array)
        self.array=self.array[0]
    
    def getElem(self,dims):
        return self.iterElem_return(self.dim,dims,self.array)
        
    def changeElem(self,val,coo):
        count=len(coo)
        self.iterElem_chng(val,count,coo,self.array)
    
    @classmethod
    def ndarray(cls,count,iter_list,letter,tmp1):
        iter=len(iter_list)-count
        num=iter_list[iter]
        
        if count==1:
            tmp2=[]
            for _ in range(num):
                tmp2.append(letter)
            tmp1.append(tmp2)
            
        else:
            count-=1
            tmp2=[]
            for _ in range(num):
                cls.ndarray(count,iter_list,letter,tmp2)
            tmp1.append(tmp2)
    
    @classmethod        
    def iterElem_return(cls,count,iter_list,tmp):
            iter=len(iter_list)-count
            num=iter_list[iter]
            print(tmp)
            if count==1:
                return tmp[num]
            else:
                count-=1
                return cls.iterElem_return(count,iter_list,tmp[num])
    @classmethod        
    def iterElem_chng(cls,val,count,iter_list,tmp):
            iter=len(iter_list)-count
            num=iter_list[iter]
            
            if count==1:
                tmp[num]=val
            else:
                count-=1
                cls.iterElem_chng(val,count,iter_list,tmp[num])



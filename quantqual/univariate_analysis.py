class Univariate():
    
    
    def quanqual(dataset):
        quan=[]# we r creating 2 empty lists to append the columnnames wen the condition is true.
        qual=[]
        for columnname in dataset.columns: #only if the for condition is true then only the if else loop should run
    
         if dataset[columnname].dtypes==object:
            quan.append(columnname)
  
         else:
            qual.append(columnname)
        print("quan=",quan)# instead of running each column name we print both the lists at the end of loop.
        print("qual=",qual)
        return quan,qual# we have to always return wat we want

    
    
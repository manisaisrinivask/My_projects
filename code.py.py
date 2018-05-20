
# coding: utf-8

# In[70]:


from itertools import combinations
import csv
with open('sample.csv.txt') as csvf:
    readcsv = csv.reader(csvf,delimiter=',') 
    
    for row in readcsv:
        target_price=float(row[1])
        break
    lst=[]
    items=[]
    prices=[]
    for row in readcsv:
        item=row[0]
        price=float(row[1])
        if price != target_price:
            items.append(item)
            prices.append(price)
    sum=0
    help_lst=[]
    for i in range(len(items)):
        comb=list(combinations(prices,i))
        for val in comb:
            for i_val in val:
                sum=sum+i_val
                help_lst.append(items[prices.index(i_val)])    
            if sum==target_price:
                print(help_lst)
            sum=0
            help_lst=[]
            
                
                
            
            
    
        
        
        
        
            
        
    
        
    


# # 

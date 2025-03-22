import pdb
import pandas as pd
import re 

df = pd.read_excel(r"C:\Users\aa103\OneDrive\Desktop\Book1.xlsx")
df_cols = df.columns
test=[]
for x in range(len(df_cols)-1):

        if re.search('unnamed',df_cols[x],re.IGNORECASE)==None and  re.search('unnamed',df_cols[x+1],re.IGNORECASE)!=None:
            test.append((df_cols[x],df[df_cols[x]][0]))
            for y in range(x+1,len(df_cols)):
                if re.search('unnamed',df_cols[y],re.IGNORECASE)!=None:
                     test.append((df_cols[x],df[df_cols[y]][0]))
                else:
                    break

        
        elif re.search('unnamed',df_cols[x],re.IGNORECASE)==None and   re.search('propsed',df_cols[x],re.IGNORECASE)!=None :
                test.append((df_cols[x],df[df_cols[x]][0]))
        elif   re.search('unnamed',df_cols[x],re.IGNORECASE)==None:
                test.append((df_cols[x],''))

columns = pd.MultiIndex.from_tuples(test)
df.columns = columns
 set_proposed = {x[0] for x in df.columns if re.search('proposed' , x[0] ,re.IGNORECASE)} 

pdb.set_trace()

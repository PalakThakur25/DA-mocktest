import pandas as pd 
df=pd.DataFrame({ 
"Name":["Palak","Varad","Bhumika","Durva"], 
"Dept":["CS","AIML","ML","IT"], 
"Marks":[90,87,92,83] 
}) 
print("Orignal Data:\n",df) 
print("\n Subset (marks>90):\n",df[df["Marks"]>90]) 
print("\nSorted by Marks (Ascending):\n", 
df.sort_values("Marks")) 
print("\nSorted by Marks (Descending):\n",  
df.sort_values("Marks", ascending=False))  
print("\nGrouped (Average Marks by Department):\n", 
df.groupby("Dept")["Marks"].mean())  
print("\nMean =", df["Marks"].mean())  
print("Median =", df["Marks"].median())  
print("Mode =")  
print(df["Marks"].mode())
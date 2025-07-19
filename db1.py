import pandas as pd
data={'Name':['Divya','Raju','Sujitha','Sushma'],
      'Age':[25,30,32,28],
      'City':['Hubli','Pune','Goa','Madras']}
df=pd.DataFrame(data)
df.to_csv('Sample_dataset.csv',index=False)
print("csv file saved as 'sample_dataset.csv")
df.to_excel('case_excel_dataset.xlsx',index=False)
print("Excel file saved as case_excel_dataset.xlsx")

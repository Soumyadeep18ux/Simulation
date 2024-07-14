#SIMULATION OF OPTICAL PROPERTY OF CLASS AS PER BRITISH STANDARD BS-EN-410-1998 USING PYTHON
import pandas as pd

dataframe1=pd.read_csv(r"C:\Users\SOUMYADEEP PAL\Documents\NEW.csv")
data=pd.read_csv(r"C:\Users\SOUMYADEEP PAL\Documents\tau.csv")
dataframe3=pd.read_csv(r"C:\Users\SOUMYADEEP PAL\Documents\R.csv")
df=pd.DataFrame(data)

df1 = df.sort_values(by='Wavelength', ascending=True)

dataframe2=df1[(df1['Wavelength']%10==0)&(df1['Wavelength']>=380)&(df1['Wavelength']<=780)]

df3=dataframe3.sort_values(by='Wavelength', ascending=True)
final_df3=df3[(df3['Wavelength']%10==0)&(df3['Wavelength']>=380)&(df3['Wavelength']<=780)]


c=dataframe1.groupby('lambda').__len__()
b=dataframe2.groupby('tau').__len__()
#print(c,b)

sum=0
sum1=0
sum2=0
for i in range(c):
    sum=sum + (dataframe1.D.values[i]*dataframe2.tau.values[i])
    sum2= sum2 + (dataframe1.D.values[i]*final_df3.R.values[i])
    sum1=sum1 + dataframe1.D.values[i]

result1= sum/sum1
print("Transmittence of sample under test is :",result1)

result2=sum2/sum1
print("Reflectence of sample under test is :",result2)

result3=100-result1-result2
print("Absorbtence of sample under test is:", result3)
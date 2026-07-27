import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
#data = np.random.uniform(1 , 7 , 10000)
#print(data)
#plt.hist(data , bins=30)
#plt.show()
colors = ["Red" , "Blue" , "Green" , "Black"]
#print(np.random.choice(colors , 20))
np.random.seed(40)
num = np.arange(1 , 11)
#print(num)
new_num = np.random.permutation(num)
#print(new_num)
#print(np.random.randint(1 , 7 , 20))
#print(np.unique(np.random.randint(1 , 7 , 20) , return_counts=True))
#print(np.random.rand())
#print(np.random.rand())
np.random.seed(40)  
record1 = np.random.choice(['H','T'],10000)
record2 = np.random.choice(['H' , 'T'] , 10000)
print(record1[:20])
head = np.sum(record1 == 'H')
tail = np.sum(record1 == 'T')
print(head/len(record1))
print(tail/len(record1))
dice = np.random.randint(1 , 7 , 10000)
p4 = np.sum(dice == 4)/len(dice)
print(f"manuly = {p4}")
print("theoretical = " , 1/6)
not_p4 = np.sum(dice != 4)/len(dice)
print(not_p4)
print(not_p4 + p4)
A = dice % 2 == 0
B = dice > 4
pA = np.mean(A)
pB = np.mean(B)
pAB = np.mean(A & B)
P_Union = pA + pB - pAB
print(P_Union) 
print(np.mean(A | B))
print(np.mean((record1 == 'H') & (record2 == 'H')))
print(0.5 * 0.5)
data_frame = pd.DataFrame({
    "Gender" : ['F' , 'M' , 'M' , 'F' , 'F' , 'M' , 'M' , 'M' , 'F'],
    "Passed" : [ 1 ,   0 ,   1  , 0 ,   1 ,   1 ,   0 ,   1 ,   1]
})
print((data_frame[data_frame["Gender"] == 'M']["Passed"] == 1).mean())
print((data_frame[data_frame["Passed"] == 1]["Gender"] == 'M').mean() *  (data_frame["Passed"] == 1).mean() / (data_frame["Gender"] == 'M').mean())
normal = np.random.normal(170 , 10 , 100000)
plt.hist(normal , bins=30)
plt.title("Normal Distribution")
plt.show()

uniform = np.random.uniform(0 , 10 , 100000)
plt.hist(uniform,bins=20)
plt.title("Uniform Distribution")
plt.show()
binomial = np.random.binomial(10 , 0.5 , 100000)
plt.hist(binomial , bins=11)
plt.title("Binomial Distribution")
plt.show()
#df = sns.load_dataset('titanic')
#print(df.head())
#print(df.sibsp.unique())
#seed ملاحظة  عند تشغيل الخلية في النوت بوك يكون المولد العشوائي في الكيرنال مضبوط على آخر 
#تم تنفيذه بالتالي لضمان العشوائية التامة في كل مرة يتم تشغيل الكود فيها يفضل اضافة سطر في نهاية الكود  
# np.random.seed(None)
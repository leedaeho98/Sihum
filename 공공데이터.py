import csv
import matplotlib.pyplot as plt

#-------------------성별별 노트북 검색량----------------------------------------------------------
f=open(r'C:C:\Users\a10\Desktop\이대호\notebook.csv',encoding="utf-8")
data=csv.reader(f)
next(data)
mandata=[]
womandata=[]
date=[]
for row in data:
    if row[1] !="":
        mandata.append(float(row[1]))
    if row[2] !="":
        womandata.append(float(row[2]))
    if row[0] !="":
        date.append(row[0])


plt.subplot(221)
plt.title("How many search 'Notebook'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date,mandata,label="Man, search 'Notebook'")
plt.plot(date,womandata,label="Woman, search 'Notebook'")
plt.legend()
#------------------인치별 노트북 가방 검색량------------------------------------------------------
f2=open(r'C:\Users\a10\Desktop\이대호\note.csv',encoding="utf-8")
data2=csv.reader(f2)
next(data2)
data17inch=[]
data15inch=[]
data13inch=[]
date2=[]

for row in data2:
    if row[1] !="":
        data17inch.append(float(row[1]))
    if row[2] !="":
        data15inch.append(float(row[2]))
    if row[3] !="":
        data13inch.append(float(row[3]))
    if row[0] !="":
        date2.append(row[0])

plt.subplot(222)
plt.title("How many search 'Notebookcase'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date2,data17inch,label='17inch case')
plt.plot(date2,data15inch,label='15inch case')
plt.plot(date2,data13inch,label='13inch case')
plt.legend()
#---------------------성별별 17인치 가방 검색량-------------------------------------------------
f3=open(r'C:\Users\a10\Desktop\이대호\17in.csv',encoding="utf-8")
data3=csv.reader(f3)
next(data3)
mandata2=[]
womandata2=[]
date3=[]
for row in data3:
    if row[1] !="":
        mandata2.append(float(row[1]))
    if row[2] !="":
        womandata2.append(float(row[2]))
    if row[0] !="":
        date3.append(row[0])

plt.subplot(223)
plt.title("How many search '17inch case'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date3,mandata2,label="Man, search '17inch case'")
plt.plot(date3,womandata2,label="Woman, search '17inch case'")
plt.legend()
plt.show()
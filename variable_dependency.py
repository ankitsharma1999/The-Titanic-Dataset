import pandas as pd
import matplotlib.pyplot as plt
import time

#reading the csv file
df = pd.read_csv("train.csv")
#checking if gender is a factor
gender=df.loc[:,'Sex']
sur=df.loc[:,'Survived']
c=0
female=0
male=0
while(c<=890):
    if gender[c]=='female':
        female=female+1
    else:
        male=male+1
    c=c+1
print("GENDER WISE SURVIVAL RATE")

f=0
m=0
c2=0
while(c2<=890):
    if gender[c2]=='female':
    	if sur[c2]==1:
    		f=f+1
    else:
    	if sur[c2]==1:
    		m=m+1
    c2=c2+1
fp=(f/female)*100
mp=(m/male)*100
print(fp,"% is the female survival rate")
print(mp,"% is the male survival rate")
#74.20382165605095 18.890814558058924
#seeing the above results it is proved that women are more likely to survive
#thus gender is a feature of interest

#checking if Pclass was a factor

print("*********************************************************************************************************************************************")
print("CLASS WISE SURVIVAL RATE")

pclass=df.loc[:,'Pclass']
c3=0
p1=0
p2=0
p3=0
pp1=0
pp2=0
pp3=0
p1p=0
p2p=0
p3p=0
while(c3<=890):
    if pclass[c3]==1:
    	pp1=pp1+1
    	if sur[c3]==1:
    		p1=p1+1
    elif pclass[c3]==2:
    	pp2=pp2+1
    	if sur[c3]==1:
    		p2=p2+1
    else:
    	pp3=pp3+1
    	if sur[c3]==1:
    		p3=p3+1
    c3=c3+1
p1p = (p1/pp1)*100
p2p = (p2/pp2)*100
p3p = (p3/pp3)*100
print(p1p,"% is the first class survival rate")
print(p2p,"% is the second class survival rate")
print(p3p,"% is the third class survival rate")

#thus class is also a feature
#checking for age
#0-17  Children
#18-49 Adults
#50-80 Old

print("*********************************************************************************************************************************************")
print("AGE WISE SURVIVAL RATE")

y=df.loc[:,'Age']
x=df.loc[:,'Survived']
c4=0
age=[]
s=[]
while c4<=890:
	if y[c4]==y[c4]:
		age.append(y[c4])
		s.append(x[c4])
		pass
	pass
	c4=c4+1
c5=0
ch=0
ct=0
ad=0
at=0
ol=0
ot=0
while c5<=713:
	if age[c5]>=0 and age[c5]<=17:
		ct=ct+1
		if s[c5]==1:
			ch=ch+1
	elif age[c5]>=18 and age[c5]<=49:
		at=at+1
		if s[c5]==1:
			ad=ad+1
	else:
		ot=ot+1
		if s[c5]==1:
			ol=ol+1
	c5=c5+1
	pass
print(((ch/ct)*100),"% is the child survival rate.")
print(((ad/at)*100),"% is the adult survival rate.")
print(((ol/ot)*100),"% is the old survival rate.")

time.sleep(10)

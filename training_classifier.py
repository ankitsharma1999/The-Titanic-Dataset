from sklearn.svm import SVC
import numpy as np
import pandas as pd

#reading the training data
df = pd.read_csv("train.csv")

#reading testing data
test=pd.read_csv("test.csv")

#next we need to extract the features namely gender,travelling class and age

age=df.loc[:,'Age']
#imported the age

p_class=df.loc[:,'Pclass']
#imported the travelling class

sex=df.loc[:,'Sex']
#imported the gender

sur=df.loc[:,'Survived']
#imported the data whether the individual survived or not

#Next we need to remove the Nan data from age and the corresponding data from p_class and sex

c=0
t=0
new_age=[]
new_sex=[]
new_pclass=[]
new_sur=[]
while c<=890:#since there are total 891 entries 
	if age[c]==age[c]:
		t=t+1
		new_age.append(age[c])
		new_sex.append(sex[c])
		new_pclass.append(p_class[c])
		new_sur.append(sur[c])
		pass
	c=c+1
	pass

#removed all the NaN data from age and the corresponding data from the p_class,sur and sex array
#new no of entries is 714

#convert sex data to 0 and 1
#0->male and 1->female
sex2=[]
c2=0
while c2<=713:
	if new_sex[c2]=='male':
		sex2.append(0)
		pass
	else:
		sex2.append(1)
	c2=c2+1
	pass
#converted male and female to 0 and 1 respectively
c3=0
tX=[]
X=[]
while c3<=713:
	tX=np.array([new_age[c3],new_pclass[c3],sex2[c3]])
	X.append(tX)
	c3=c3+1
	pass
#now X has the training features

y=new_sur
#now y has the training labels

#creating and training the classifier
clf=SVC(gamma='auto')#classifier created
clf.fit(X,y)#classifier trained

#extracting testing data ie age, sex and travelling class

p=test.loc[:,'Age']
q=test.loc[:,'Sex']
r=test.loc[:,'Pclass']

#age has NaN values that needs to be removed

count=0
test_age=[]
test_sex=[]
test_class=[]
while count<=417:
	if p[count]==p[count]:
		test_age.append(p[count])
		test_class.append(r[count])
		test_sex.append(q[count])
		pass
	count=count+1
	pass
#now we need to change male to 0  and female to 1

count1=0
t_sex=[]
while count1<=331:
	if test_sex[count1]=='male':
		t_sex.append(0)
	else:
		t_sex.append(1)
	count1=count1+1
	pass
test_X=[]
t_x=[]
count2=0
while count2<=331:
	t_X=np.array([test_age[count2],test_class[count2],t_sex[count2]])
	test_X.append(t_X)
	count2=count2+1
	pass
results=clf.predict(test_X)
print(results)
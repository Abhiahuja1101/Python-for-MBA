#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Old Tax Regime
x=int(input("enter the salary: "))
if x<=250000:
    print("you are tax free bro ")
if x>=250000 and x<500000:
    print("you have to pay tax bro ")
    tax =(x-250000)*.05 #tax rate is 5%
    print("tax is ",tax)
if x>=500000 and x<1000000:
    print("you have to pay tax bro ")
    tax =(x-500000)*.2 + 250000*.05 #tax rate is 20%
    print("tax is ",tax)
if x>=1000000:
    print("you have to pay tax bro ")
    tax =500000*.2 + 250000*.05 +(x-1000000)*.3 #tax rate is 30%
    print("tax is ",tax)


# In[ ]:


#New Tax Regime
x=int(input("enter the salary: "))
if x<300000:
    print("you are tax free bro ")
if x>300000 and x<600000:
    print("you have to pay tax bro ")
    tax =(x-300000)*.05 #tax rate is 5%
    print("tax is ",tax)
if x>=600000 and x<900000:
    print("you have to pay tax bro ")
    tax =(x-600000)*.1 + 300000*.05  #tax rate is 10%
    print("tax is ",tax)
if x>=900000 and x<1200000:
    print("you have to pay tax bro ")
    tax =(x-900000)*.15 + 300000*.1 + 300000*.05 #tax rate is 15%
    print("tax is ",tax)
if x>=1200000 and x<1500000:
    print("you have to pay tax bro ")
    tax =(x-1200000)*.20 + 300000*.1 + 300000*.05 + 300000*.15 #tax rate is 20%
    print("tax is ",tax)
if x>=1500000:
    print("you have to pay bhot jyada  tax bro ")
    tax =(x-1500000)*.20 + 300000*.1 + 300000*.05 + 300000*.15 +300000*.2 #tax rate is 20%
    print("tax is ",tax)


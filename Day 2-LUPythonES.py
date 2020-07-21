#!/usr/bin/env python
# coding: utf-8

# # Day-2 Assignment-1

# In[2]:


print("Hello guys this is the day-2 learning")


# Pyhton Syntax usage for print stmt

# In[3]:


print("This is a back slash \ character ")


# The above is the \ means continuation usage of print stmt by removing the syntax errors like new line....

# In[4]:


print("Welcome python")


# In[5]:


print("This is my the use of \"backslash\" character")


# Balancing the quotes of print stmt

# In[6]:


print("""This is an instance of a triple quotes 
Hey here is the difference
""")


# In[7]:


"""
this notebook was created by me
"""


# In[8]:


print('usage of single quotes')


# In[9]:


print("usage \t of escape \n sequence")


# Assignment  operator variables usaging in print stmt..........

# In[12]:


name = 'mickey mouse'
age = 20
salary = 20000

print("Disney famous cartoon character is", name,"age is", age, "salary is", salary)


# In[13]:


print("Disney famous cartoon character is %s age is %d salary is %d" %(name, age, salary))


#  Variable assignment

# In[14]:


a = 20
b = 12
print(a)
print(b)


# Id keyword is used represent the address of the variable in memory...\n
# ***In each Id of integer in between -5 to 256 are represent the same address***

# In[15]:


print(id(a))
print(id(b))


# In[16]:


x = y = z = 50
print(x)
print(y)
print(id(y))


# Deleting the variable name not the data

# In[17]:


del(x)
print(x)
print(y)


# In[18]:


print(y)


# Operators

# In[19]:


a = 50
b = 10
c= 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**c)
print(a^c)


# In[22]:


x = 20
y = 10
print(x == y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)
print(x!= y)


# In[23]:


print(x = !y)


# In[24]:


x = 20
y = 10
print(x & y)
print(x | y)
print(~x)
print(~y)


# In[25]:


print(bin(a))


# In[26]:


x = 30
y = 15
print(x and y)
print(x or y)


# In[27]:


p = 10

print(10 > 9 and p >= 10)
print(10 < 9 and p >= 11)


# In[28]:


n = 20

print(10 < 9 or n > 10)
print(10 > 9 or n <= 10)


# precedence rule

# In[29]:


print(15+3/2-1*15/11//20)


# In[30]:


a = -2
b = 266
c = 266
print(a is b)
print(a is not c)
print(b is c)


# In[31]:


str = "manasa is  a good friend"
str1 = "friend"
# str1 in str
print(str not in str1)


# In[32]:


s = t = 266

print(id(s))
print(id(t))


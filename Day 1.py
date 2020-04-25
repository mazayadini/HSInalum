#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hacktive8')


# ## Integer
# 
# Integer adalah tipe data yang berupa angka

# In[2]:


print(123123123)


# In[3]:


type(10)


# ## Floating Point
# 
# Tipe data berupa desimal

# In[4]:


4.2


# In[5]:


type(3.2)


# In[6]:


.2


# In[7]:


.4e7


# In[8]:


4.2e-2


# ## String
# 
# Tipe data berupa sequence of character data
# 

# In[9]:


print('Ini adalah string')


# In[10]:


type('ini adalah string')


# In[11]:


print("I'm")


# ## Boolean
# 
# Tipe data berupa true atau false

# In[12]:


True


# In[13]:


False


# In[15]:


Type('True')


# In[16]:


Type('True')


# In[17]:


type('True')


# ## Variable

# In[18]:


n = 300


# In[19]:


n


# In[20]:


n = k =300
print(n,k)


# In[21]:


print(n)


# In[22]:


print(k)


# ### Variable Name

# In[28]:


name = 'Mazaya'
Age = 26
has_laptop = True
print(name, Age, has_laptop)


# In[26]:


bola_naga_9 = True


# In[27]:


age = 1
print(age)


# ## Operator & Expression in Phyton
# 
# Special symbol untuk melakukan komputasi

# In[29]:


a = 10


# In[30]:


b=20


# In[31]:


a+b


# In[32]:


a-5+b


# ## Aritmatic Operator

# In[34]:


a=10
b=20

print(a==b) #sama dengan
print(a!=b) #tidak sama dengan
print(a<=b)  #kurang dari sama dengan
print(a>=b) #lebih dari sama dengan


# ## String Manipulator

# In[35]:


# + Operator

s = 'foo'
t = 'bar'
u = 'bas'

print(s+t)


# In[36]:


s+t+u


# In[38]:


print ('Hacktive8' + ' Inalum')


# In[39]:


# * Operator

s*4


# In[41]:


# in Operator

s = 'foo'
s in 'food is ready'


# In[42]:


s in 'good for us'


# # Case Convertion

# In[46]:


s='hacTIve8 inalum'


# In[47]:


# Capitalize

s.capitalize()


# In[48]:


# Title

s.title()


# In[49]:


#lower

print(s.lower())

#uppercase
print(s.upper())


# In[50]:


#swapcase
s.swapcase()


# ## List
# 
# Ditandai dengan '[ ]'

# In[51]:


a = ['foo','bar','bas']


# In[52]:


a


# In[53]:


a = ['inalum', 2,3,True,2.34,False,'hacktive']


# In[54]:


a


# In[55]:


b = ['foo','bar','baz','dor','qux','den']


# In[56]:


b


# In[58]:


b[0]


# In[59]:


b[5]


# In[61]:


b[3]


# In[62]:


b[-1]


# In[63]:


# Slicing

b[1:4]


# In[64]:


b[0:5]


# In[65]:


b[:5]


# In[66]:


b[2:]


# In[67]:


print(b)


# In[68]:


b+['value1','value2']


# In[69]:


print(b[1:4])


# In[70]:


b*2


# In[72]:


print(b)

len(b)


# In[75]:


# ambil urutan abjad/angka terkecil

min(b)


# In[76]:


# ambil urutan abjad/angka terbesar

max(b)


# In[77]:


c = [1,2,3,4,5]
print(min(c))
print(max(c))


# # Modifiying Single List Value
# 
# b

# In[78]:


b


# In[80]:


b[2]=10


# In[81]:


b


# In[84]:


b[-1]=20


# In[85]:


b


# In[86]:


del b[3]


# In[87]:


b


# # Modifiying Multiple List Value

# In[89]:


b


# In[90]:


b[1:4]


# In[91]:


b[1:4]=[1.1,1.2,1.3]


# In[92]:


b


# # Tuples

# In[93]:


t = ('foo','bar','bas','qux','quux','corge')


# In[94]:


t


# In[95]:


t[0]


# In[96]:


t[-1]


# In[97]:


t[0]='new value'


# # Dictionary

# In[99]:


identitas = {
    key: value
}


# In[100]:


identitas ={
    'nama':'Mazaya',
    'Lname':'Dini',
    'Age':26
}


# In[101]:


identitas


# In[102]:


identitas['Age']


# In[103]:


identitas['Alamat']


# In[105]:


identitas['Pekerjaan']='Hantu'


# In[106]:


identitas


# In[107]:


identitas ['Pekerjaan']='Buruh'


# In[108]:


identitas


# In[109]:


del identitas['Pekerjaan']


# In[110]:


identitas


# In[111]:


person = {}


# In[115]:


type(person)


# In[121]:


person['nama']= 'Nama Depan'
person['Lname']= 'Nama Tengah'
person['children']=['anak1','anak2']


# In[117]:


person


# In[118]:


person['nama']


# In[119]:


person['children']


# In[122]:


person['children'][1]


# In[123]:


d = [1,2,3,[4,5,6],7,8]


# In[124]:


d[3]


# In[125]:


d[3][0]


# In[126]:


d={'a':10,'b':20,'c':30}


# In[127]:


d


# In[129]:


# keys

d.keys()


# In[132]:


# value
d.values()


# In[133]:


# Phyton Statement

print('Hello World!')

x = [1,2,3]


# In[139]:


# Line Continuation

person1_age = 42
person2_age = 43
person3_age = 44

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age


# In[140]:


someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65) or 
    (person2_age >= 18 and person2_age <= 65) or 
    (person3_age >= 18 and person3_age <= 65)
)
someone_is_of_working_age


# In[141]:


a=[[1,2,3],[4,5,6],[7,8,9]]


# In[142]:


a


# In[143]:


a=[[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]


# In[144]:


print(a)


# In[145]:


a


# In[146]:


a=[
    [1,2,3],[4,5,6],[7,8,9],[1,2,3],
    [4,5,6],[7,8,9],[1,2,3],[4,5,6],
    [7,8,9],[1,2,3],[4,5,6],[7,8,9],
    [1,2,3],[4,5,6],[7,8,9],[1,2,3],
    [4,5,6],[7,8,9]
]


# In[147]:


a


# In[148]:


s=
'Hello World!'


# In[151]:


s='Hello World'


# In[152]:


s


# In[155]:


# Multiple Statement Per Line

x=1;y=2;z=3
print(1);print(2);print(3)


# In[158]:


# comments

a = ['foo','bar'] # i am comment
a


# In[160]:


"""
Mazaya Dini Ramadhani
LALALALALAL

"""
pi = 3.14
r = 12

area = pi*(r**2)
print ('the area of circle is', area)


# # Conditional

# In[162]:


# If Statement

x = 0
y = 5

if x < y:
    print('yes')
if y < x:
    print('yes')
if 'aul' in 'grault':
    print('yes')


# In[163]:


if 'foo' in ['bar','baz','qux']:
    print('Expresstion was true')
    print('Execution Statement')
    print('...')
    print('done')
print('after conditional')


# In[164]:


if 'foo' in ['bar','baz','qux','foo']:
    print('Expresstion was true')
    print('Execution Statement')
    print('...')
    print('done')
print('after conditional')


# In[165]:


if 'foo' in ['foo','bar','baz']:
    print('Outer condition is true')
    
    if 10 > 20:
        print ('Inner Condition')
        
    print('between inner condition')
    
    if 10 < 20:
        print ('inner condition 2')
        
    print('end condition')


# In[166]:


# else and elif

if x < 50:
    print('x is small')
else:
    print('x is large')


# In[167]:


# else and elif

if x > 50:
    print('x is small')
else:
    print('x is large')


# In[168]:


name = 'hacktive8'

if name == 'fred':
    print('Hi Fred')
elif name == 'xander':
    print('Hi Xander')
elif name == 'hacktive8':
    print('Hi hacktive8')
    
else:
    print('I dont know')


# In[170]:


name = 'mazaya'

if name == 'fred':
    print('Hi Fred')
elif name == 'xander':
    print('Hi Xander')
elif name == 'hacktive8':
    print('Hi hacktive8')
    
else:
    print('I dont know')


# In[171]:


if 'a' in 'bar':
    print('right')
elif 1/0:
    print('wrong')
elif var:
    print('wrong also')


# In[175]:


if 'r' in 'bar':
    print('right')
elif 1/0:
    print('wrong')
elif var:
    print('wrong also')


# In[176]:


#one line if statement

x=2
if x == 1: 
    print ('foo')
    print ('baz')
elif x == 2:
    print ('do')
    print ('re')
else:
    print ('no')
    print ('dont')


# In[177]:


# ternary operator (conditional expresssion)

age = 12

'teen' if age < 21 else 'adult'


# In[178]:


age = 26

'teen' if age < 21 else 'adult'


# In[180]:


if a > b:
    m = a
else:
    m = b

m = a if a > b else b


# In[181]:


## pass statement

if True:
    pass

print('foo')


# In[182]:


## while

n = 5
while n > 0:
    n -= 1
    print(n)


# In[184]:


# break & continue statement

n = 5
while n > 0:
    n -= 1 # didapatkan 4
    if n == 2: # dilewati karena 4!=2
        break #pass
    print(n) # 4 3
print('loop end')


# In[185]:


n = 5
while n > 0:
    n -= 1 # didapatkan 4
    if n == 2: # dilewati karena 4!=2
        continue #pass
    print(n) # 4 3
print('loop end')


# In[186]:


#else clause

n = 5
while n > 0:
    n -= 1 
    if n == 2: 
        break 
    print(n) 
else:
    print('loop end')


# In[187]:


# one - line while loops

n = 5

while n > 0: n-=1; print(n)


# In[188]:


# for loops

a = ['foo','bar','baz']

for i in a:
    print(i)


# In[191]:


d = {'foo': 1,'bar': 2,'baz': 3}

for k in d:
    print(k)


# In[192]:


for k in d:
    print(d[k])


# In[193]:


d['foo']


# In[195]:


for v in d.values():
    print(v)


# In[199]:


# range function

x = range (10)


# In[200]:


x


# In[201]:


for n in x:
    print(n)


# In[202]:


# break and continue

for i in ['foo','bar','baz','quz']:
    if 'z' in i:
        break
    print(i)


# In[204]:


for i in ['foo','bar','baz','qux']:
    if 'z' in i:
        continue
    print(i)


# In[205]:


# else clause

for i in ['foo','bar','baz','qux']:
    print(i)
else:
    print('done')


# In[207]:


for i in ['foo','bar','baz','qux']:
    if 'z' in i:
        break
    print(i)
else:
    print('done')


# In[2]:


temp = input("Ketikan termperatur yang ingin dikonversi, eg 45F, 28C : ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == "F":
    result = int(round((degree - 32) * 5 / 9))
else:
    print("masukkan input yang benar")
    
print("Temperaturnya adalah", result)


# In[214]:


temp


# In[215]:


result


# In[1]:


while True:
    msg = input("Ketikkan karakter: ").lower()
    print(msg)
    if msg == 'stop':
        break


# In[ ]:





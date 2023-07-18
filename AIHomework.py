#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Resourse:
    def __init__(self, name, manufacturer, total = 0, allocated = 0):
        self.name = name
        self.manufacturer = manufacturer
        self.total = total
        self.allocated = allocated
    def __str__(self):
        return self.name
    def __repr__(self):
        return str((self.__class__.__name__, self.name, self.manufacturer, self.total,
                self.allocated))
    def claim(self,n):
        if self.total - self.allocated >= n:
            self.allocated += n
            print("Using ", n , self.name)
        else:
            print("we have not enough materials")
    def freeup(self, free):
        if self.allocated >= free:
            self.allocated -= free
            print(" Freeup", free , "materials")
        else:
            print("We have not Freeup materials")
    def died(self,d):
        if self.total >= d:
            self.total -= d
            if self.allocated > self.total:
                self.allocated = self.total
        else:
            print("invalid materials")
    def purchased(self,p):
        if p >= 0:
            self.total += p
            print("vsyo xorosho")
        else:
            print("vsyo vapshe ne xorosho")


# In[2]:


class Storage:
    def __init__(self,copacity):
        self.copacity = copacity
    
    


# In[3]:


class Cpu:
    def __init__(self,socket, power_watts):
        self.socket = socket
        self.power_watts = power_watts
    def buy(self,socket,power_watts,quantity,resourse:Resourse):
        resourse.allocated += quantity
    def __repr__(self):
        return f'Congratulation you already reserved CPU by this parameters {self.socket},\
                {self.power_watts}'


# In[10]:


class Ssd(Storage):
    def __init__(self,copacity, interface):
        super().__init__(copacity.copacity)
        self.interface = interface
    def buy(self,resourse:Resourse,quantity):
        resourse.allocated += quantity
    def __repr__(self):
        return f'Congratulation you already reserved SSD by this parameters {self.copacity},{self.interface}'


# In[11]:


class Hdd(Storage):
    def __init__(self,copacity, size, rpm):
        super().__init__(copacity.copacity)
        self.size = size
        self.rpm = rpm
    def buy(self,quantity,resourse:Resourse):
        resourse.allocated += quantity
    def __repr__(self):
        return f'Congratulation you already reserved HDD by this parameters {self.copacity},{self.size},\
        {self.rpm}'


# In[12]:


resourse = Resourse("Gago","Hamik")
storage = Storage("64GB")
cpu = Cpu("socket","jocket")
ssd = Ssd(storage,"interface")
hdd = Hdd(storage,"64x64","shat hzor")

hdd.buy(6,resourse)
print(hdd)

ssd.buy(resourse,5)
print(ssd)


# In[113]:


print(resourse.allocated)


# In[27]:


class Check(type):
    
    def __new__(cls, name, bases, dct):
        new = super().__new__(cls, name, bases, dct)
        print(new)
        if new.__annotations__['y'] != str:
            raise TypeError
        return new

class B(metaclass=Check):
    
    x:int = 3
    y:str = "d"

        


# In[28]:


# Implement a hierarchy of classes representing different types of vehicles, such 
# as cars, motorcycles, and bicycles. Demonstrate inheritance, method overriding, 
# and polymorphism by implementing common methods 
# and attributes specific to each vehicle type.


# In[56]:


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,make,model):
        self.make = make
        self.model = model
    @abstractmethod
    def move(self):
        pass
    


# In[57]:


class Car(Vehicle):
    def __init__(self,make,model,doors:int):
        super().__init__(make,model)
        self.doors = doors
    def move(self):
        print(f'you are moving by car which is {self.make},{self.model} and have {self.doors} doors.')
    
    
        


# In[58]:


class Motorcycle(Vehicle):
    def __init__(self,make,model,airodinamics):
        super().__init__()
        self.airodinamics = airodinamics
    def move(self):
        print(f'you are moving by car which is {self.make},{self.model} and have {self.airodinamics} airodinamics.')


# In[46]:


class Bicycle(Vehicle):
    def __init__(self,make,model):
        super().__init__()
    def move(self):
        print(f'you are moving by car which is {self.make},{self.model}.')


# In[60]:


car = Car("BMW","5 SERIES",5)
car.move()


# In[61]:


# Define an abstract base class for a data storage system, with methods like save(), load(), 
# and delete(). Implement concrete subclasses representing different storage systems, such as 
# file-based storage and database storage, ensuring they adhere to the abstract 
# interface.


# In[70]:


from abc import ABC,abstractmethod
class DataStorage(ABC):
    @abstractmethod
    def save(self, data):
        pass
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def delete(self):
        pass


# In[71]:


class FileBased(DataStorage):
    def save(self, file_name, data):
        with open(file_name,"a") as file:
            file.write(data)
        return f'your {data} already in {file_name}'
    def load(self,file_name):
        with open(file_name,'r') as file:
            return file.read()
    def delete(self,file_name):
        remove(file_name)
        return f'Your {file_name} already removed'


# In[72]:


class DataBaseStorage(DataStorage):
    def __init__(self):
        self.database = {}
    def save(self,data,value):
        database.get(data, value)
        return "data already in database if it wasn't"
    def load(self):
        for key, value in self.database.items:
            print((key,value))
        return "this is your data"

    def delete(self,database):
        del(database)
        return f'Your database removed'
        


# In[65]:





# In[68]:





# In[ ]:





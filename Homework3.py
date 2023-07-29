#!/usr/bin/env python
# coding: utf-8

# In[1]:


classdict = {}
exec('''
def __init__(self,*args):
     pass
def __eq__(self,other):
    pass
def __hash__(self):
    pass''',
globals(), classdict)


# In[2]:


classdict


# In[3]:


metaclass = type('MyMetaclass',(object,),classdict)


# In[4]:


metaclass.__dict__


# In[28]:


class MyNewMeta(type):
    
    def __new__(mcls, name, base, class_dict):

#         exec('''
# def __init__(self,*args):
#      pass
# def __eq__(self,other):
#     pass
# def __hash__(self):
#     pass''',
# globals(), class_dict)
        
        print(f'mcls is {mcls}, name is {name}, base is {base} and finally is class_dict is {class_dict}')
        
        if "__slots__" in class_dict:
            cords = class_dict['__slots__']
            dimensions  = len(cords)
            
            
            
        
            def __init__(self, *args):

                for arg in args:
                    if not isinstance(arg,int):
                        raise ValueError("cordinates is not integers please take integer cordinates")

                if dimensions != len(args):
                    raise ValueError( "You have dimensional problem" )

                for i, cord in enumurate(cords):
                    setattr(self, cords, args[i])

            def __eq__(self,other):

                if not isinstance(other,self.__class__):

                    raise TypeError("Different types")

                return all(getattr(self, cord) == getattr(other, cord) for cord in cords)

            def __hash__(self):
                return hash((getattr(self,cord) for cord in cords))
            class_dict["__init__"] = __init__
            class_dict["__eq__"] = __eq__
            class_dict["__hash__"] = __hash__
        class_obj = super().__new__(mcls, name, base, class_dict)
        
        return class_obj
    


# In[13]:


# newmeta = MyNewMeta("Generics",(object,),classdict)


# In[14]:


# type(newmeta)


# In[15]:


class Point2D(metaclass = MyNewMeta):
    __slots__ = ("_x","_y")


# In[16]:


class Point3D(metaclass = MyNewMeta):
    __slots__ = ("_x","_y","_z")


# In[17]:


class Point4D(metaclass = MyNewMeta):
    __slots__ = ("_x","_y","_z","_d")


# In[19]:


point = Point2D(0,0,0)


# In[ ]:


point.__dict__


# In[20]:


# PROJECT 2


# In[87]:


class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


# In[88]:


class Hundred(metaclass=SingletonMeta):
    def __init__(self):
        setattr(self, 'name', 'hundred')
        setattr(self, 'value', 100)


# In[94]:


h = Hundred()
h1 = Hundred()
print(h1 is h2)


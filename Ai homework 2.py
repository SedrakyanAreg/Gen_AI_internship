#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ValidType:
    def __init__(self,gtype):
        self.gtype = gtype

        
    def __set_name__(self,insatnce,property):
        self.property = property
        
    def __set__(self,instance,value):
        
        if not isinstance(value, self.gtype):
    
            raise ValueError ("Entered wrong type")
            
        instance.__dict__[self.property] = value
        
    def __get__(self,instance,owner):
        return instance.__dict__.get(self.property,None)


# In[2]:


class RealInteger(ValidType):
    def __init__(self):
        super().__init__(int)


# In[3]:


class RealFloat(ValidType):
    def __init__(self):
        super().__init__(float)


# In[4]:


class RealList(ValidType):
    def __init__(self):
        super().__init__(list)


# In[5]:


class RealString(ValidType):
    def __init__(self):
        super().__init__(str)


# In[6]:


class Person:
    age = RealInteger()
    height = RealFloat()
    tags = RealList()
    favorite_foods = RealList()
    name = RealString()
    

    


# In[7]:


class Int:
    def __init__(self, value, min_target=None, max_target=None):
        self.min_target = min_target
        self.max_value = max_target
        self.value = value

    def __set_name__(self, owner, name):
        self.name = name

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer.")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be greater than or equal to {self.min_value}.")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be less than or equal to {self.max_value}.")
        return value

    def __set__(self, instance, value):
        validated_value = self.validate(value)
        instance.__dict__[self.name] = validated_value


class Point2D:
    def __init__(self, x, y):
        self.x = Int(x)
        self.y = Int(y)

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer.")
        if value < 0:
            raise ValueError(f"{self.name} must be a non-negative integer.")
        instance.__dict__[self.name] = value


class Point2DSequence:
    def __init__(self, min_count=None, max_count=None):
        self.min_count = min_count
        self.max_count = max_count

    def __set_name__(self, owner, name):
        self.name = name

    def validate(self, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError
        if self.min_count is not None and len(value) < self.min_count:
            raise ValueError
        if self.max_count is not None and len(value) > self.max_count:
            raise ValueError
        for point in value:
            if not isinstance(point, Point2D):
                raise ValueError
        return value

    def __set__(self, instance, value):
        validated_value = self.validate(value)
        instance.__dict__[self.name] = validated_value


class Polygon:
    def __init__(self, *vertices):
        self.vertices = Point2DSequence(min_count=3, max_count=10)
        if vertices:
            self.vertices = list(vertices)

    def append(self, point):
        if len(self.vertices) >= self.vertices.max_count:
            raise ValueError("There are maximum vertics")
        self.vertices.append(point)


# In[ ]:





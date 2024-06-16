import matplotlib as mp

#return package name
print(mp.__package__)
print(mp.__name__)

#return current path
print(mp.__path__)
print(mp.__file__)

#return version of module
print(mp.__version__) 

#return user OS type
print(mp.get_backend())

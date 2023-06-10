d1={'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}

#to extract any values from dictionary we need to use the below functions

print(d1['k3'])

#lets explore about the config box.



from box import ConfigBox


d2=ConfigBox(d1={'k1':'v1','k2':'v2','k3':'v3','k4':'v4'})

print(d2.k3)



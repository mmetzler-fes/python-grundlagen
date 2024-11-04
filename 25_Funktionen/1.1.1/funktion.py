def umkehr(x):
    umkehr=""
    for i in range(len(x)-1,-1,-1):
        umkehr+=x[i]
    return umkehr

#Hinweis: Es gibt auch noch eine Kurzlösung
def my_umkehr(x):
  return x[::-1]

name="Martin"
print (umkehr(name))
print (my_umkehr(name))


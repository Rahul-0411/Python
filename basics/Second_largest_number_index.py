lista=[2,13,14,15,6]
h=s=-1
index_s=-1

for i in range(0,len(lista)):
        if lista[i]>h:
                s=h
                h=lista[i]
                index_s=i-1

        elif lista[i]!=h and lista[i]>s:
                s=lista[i]
                index_s=i

print(index_s)

                
a={1:0,2:1,3:2,4:4,5:5,6:6,7:7,8:8,9:9,10:10}

for i in a:
    z=a.get(i)
    z=i*i
    a.update({i:z})
print a
input()

import csv
from pprint import pformat


def read_csv():
    f = open("data2.csv", 'r')
    lt = list(list(row) for row in csv.reader(f, delimiter=','))
    for row in lt:
        for i in range(0, len(row)):
            if '.' not in lt:
                int(i)
            elif 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,v,z' in lt:
                str(i)
            else:
                float(i)
    print(pformat(lt))


read_csv()

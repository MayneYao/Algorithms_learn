'''
希尔排序是插入排序的高效改进版
非稳定排序，不稳定因素在于步长的选择
已知的最好步长序列是由Sedgewick提出的(1, 5, 19, 41, 109,...)
参见:https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F
'''
import math

#插入排序
def insertion_sort(a):
    if len(a)==1:
        return a
    for i in range(1,len(a)):
        tmp=a[i]
        while i!=0:
            if tmp<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
            else:
                break
            i-=1
    return a

#得到步长序列
def getStepnum(num):
    list=[]
    for i in range(num):
        list.append(9*4**i-9*2**i+1)
        list.append(2**(i+2)*(2**(i+2)-3)+1)
    list.sort()
    list.reverse()
    return list

#希尔排序
def shell_sort(a):
    m = len(a)
    b=[]
    i=1
    while m>getStepnum(i)[0]:
        i+=1
    step = getStepnum(i-1)
    print(step)
    for i in step:
        if i>1:
            for j in range(i):
                for k in range(math.ceil(m/i)):
                    if (j+k*i)<m:
                        b.append(a[j+k*i])
                print(insertion_sort(b[j*i:(j+1)*i]))
        else:
            insertion_sort(b)
    return b
print(shell_sort([1,2,3,123,12,41,24,12,21,4,12,412,53,25,3,53,25,252,3,5,23,5,23,5,235,4,6,5,9,7,8,0]))


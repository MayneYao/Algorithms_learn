'''
希尔排序是插入排序的高效改进版
非稳定排序，不稳定因素在于步长的选择
已知的最好步长序列是由Sedgewick提出的(1, 5, 19, 41, 109,...)
参见:https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F
'''
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

def shell_sort(a):

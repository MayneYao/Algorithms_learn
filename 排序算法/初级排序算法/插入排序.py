'''
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
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


print(insertion_sort([3,2,1,5,3,5,2,7,9]))
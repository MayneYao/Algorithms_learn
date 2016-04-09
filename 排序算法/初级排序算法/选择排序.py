'''
1.在数组中寻找最小的元素，将它和数组的第一个元素交换位置。
2.再剩下的元素中继续寻找最小的元素，再与数组第二个元素交换位置。
3.以此类推。
'''
def selection_sort(a):
    for i in range(len(a)):
        minn =i
        for j in range(i+1,len(a)):
            #如果后一项比最小项小，那么2者交换
            if min(a[j],a[minn])==a[j]:
                a[j],a[minn]=a[minn],a[j]
    return a


print(selection_sort(["a","v","c"]))
print(selection_sort([1,2,4,7,3,4,5]))



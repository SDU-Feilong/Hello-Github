'''
The demo of selection sort

2020 9.29
'''

def select_sort(varlist):
    for i in range(len(varlist)):
        # 设定检查表头指针 即当前最小的数的索引
        pos = i
        # 数据比较的范围[i+1:],向后扫描
        for j in range(i+1,len(varlist)):
            if varlist[j] < varlist[pos]:
                pos = j
        # 交换两个位置的数,最小值移动到检查表的开头
        varlist[i],varlist[pos] = varlist[pos],varlist[i]




ls1 = [22,55,1,7,3]
ls2 = [5,3,1,2,4]
select_sort(ls1)
print(ls1)
select_sort(ls2)
print(ls2)
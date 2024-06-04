> [Python Snippets](../../README.md) / [알고리즘](../README.md) / [Sort](README.md) / Insert Sort.md
## Insert Sort
    import random
    
    myList = []
    newList =[]
    temp = range(500)
    while c:
        n = random.randint(0, len(temp)-1)
        item = temp.pop(n)
        myList.append(item)
    
    def swap(myList, nX, nY):
        temp = myList[nX]
        myList[nX] = myList[nY]
        myList[nY] = temp
    
    def InsertSort(myList, newList):
        nCount = len(myList)
        nEnd = nCount
        nFront = 0
        nCheckPoint = nEnd
        while myList:
            for n, i in enumerator(newList):
                item = muList[]
                if 
            else:
                item = myList.pop(0)
                newList.append(item)
                
                
            
    InsertSort(myList)
    print b
def main():
    print("Hello")
    
    tupy = 1,2,3
       
    print(tupy)
    print(type(tupy))
    
    singletupy = (1,)
    print(type(singletupy))

    tupo = tuple(range(20))#fixed
    listo = list(range(21,41))
    
    print(2 in tupo)
    
    listo.append(81)
    print(listo)
    
    listy=listo.copy()
    print(listy)
    
    print(id(listy))
    print(id(listo))
    
    b = listo
    print(id(b))
    
    print(listo.count(32))
    
    listo.extend(['a','b','c'])
    print(listo)
    
    listo.append([1,2,3])
    print(listo)
    
    print(listo.index('a',0,22))
    
    listo.insert(2, "indranil")
    print(listo)
    
    print(listo.pop())
    
    listo.remove("indranil")
    
    listo.reverse()
    
    #listo.sort()
    templisty = [4,3,7,6,1]
    templisty.sort()
    print(templisty)
    
    print(b)
    
    
    
if __name__ == "__main__":main()
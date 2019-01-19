#!/usr/bin/python3

def main():
    print("Hello World")
    
    no1 = 4
    no2 = 5
    
    print('Value one is {} and value two is {}'.format(no2,no1))
    
    str1 = "top ten programming languages in 2019" 
    u = str1.split()

    for i in u:
        print(i, end='-')
    
    print('\n')
    url ='$'.join(u)
    print(url)
    
    str1 = "Indranil"
    print(str1,"Phukan")
    print(url,".html",sep='')
    
    
    
    
if __name__ == "__main__":
    main()
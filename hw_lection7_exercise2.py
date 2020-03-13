def make_country():
    name = str(input("Input name of country: "))
    capital = str(input("Input capital of country: "))  
    dict1 = dict.fromkeys(name,capital) 
    print(dict1)
    
make_country()

#не полностью,не понял почему оно каждую букву как разный ключ закидывает
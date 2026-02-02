def acronym():
    while True:
        a= input("Enter a string: ")
        b= a.split()
        c= ""
        for i in b:
            c += i[0].upper()
        print("The acronym is:", c)
        if a == "":
            print("Exiting")
            break   

acronym()
    
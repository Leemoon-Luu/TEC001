a = float(input("Enter inches = "))

def converts_inches_to_centimeters(a):
    while True:
        if a < 0:
            print("The program end")
            break
        else:
            b = a * 2.54
            print("Centimeter = ", b)
            i = input("New data ? (0: no, 1: yes): ")
            if i == "1":    
                a = float(input("Enter inches = "))
            elif i == "0":
                print("The program end")
                break

b = converts_inches_to_centimeters (a)
def middle_character():
 
    while True:
        s= input("Enter your word: ")
        a= len(s)

        if s == "":
            print("exit")
            break
        elif a % 2 == 0:
            word= s[(a//2)-1:(a//2)+1]
            print("The middle characters are: ", word)
        else:
            word= s[a//2]
            print("The middle character is: ", word)
        
word = middle_character()
def num_check():
    num="1870"
    attempt = 10
    while attempt >0:
        guess=str(input("Guess the number: "))
        if guess== num:
            print("congrats you WIN!!!!")
            break
        else:
            attempt-=1
            print("you have "+attempt+" attempts\n")
            for char, word in zip(num, guess):
                print
            
            
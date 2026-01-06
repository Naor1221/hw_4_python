def manu_A_B():
    A = 0
    B = 0
    while 1:
        option = input("Enter your option:"
                       "\nA for update A value"
                       "\nB for update B value"
                       "\nS for saving changes to a file"
                       "\nL for loading data of A & B"
                       "\nQ for quit\n")
        if option == 'A' or option == 'a':
            A = int(input("Enter new value for A:"))
        elif option == 'B' or option == 'b':
            B = int(input("Enter new value for B:"))
        elif option == 'S' or option == 's':
            # w is overwriting the file, and this is ok for this mission.
            f = open("file.txt", mode='w', encoding="utf8")
            f.write(f"A:{A}\n")
            f.write(f"B:{B}\n")
            f.close()
        elif option == 'L' or option == 'l':
            #f enables running on lines
            f = open("file.txt", mode='r', encoding="utf8")
            #thus:
            for line in f:
                print(line, end='')
            f.close()
        elif option == 'Q' or option == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong choise\nTry again.")

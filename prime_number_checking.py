def prime_number():

    check_number = int(input("Nhap so : "))

    if check_number < 2 :
        print ("Day khong phai la so nguyen to ")
    else : 
        for i in range (2 , int(check_number**0.5 + 1 )):
            if check_number % i == 0 :
                print ("Day khong phai la so nguyen to")
                break 
        else: 
            print ("Day la so nguyen to")

while True : 
    prime_number()
    choice = input("Ban co muon kiem tra tiep khong Y/N : ").upper()
    if choice == "N":
        print("Tam biet!")
        break 
    elif choice != "Y":
        print("Invalid input , auto exit.")
        break
        



def starter():
    #importing random in
    import random
   
    #decides + or -
    numeral_list = [1, 2]
    mathh = random.choice(numeral_list)
   
    #list of numbers it pulls from
    def globalMa():
        global numeral_list_two
        global numeral_list_three
        numeral_list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numeral_list_three = [1.4, 2.6, 3.1, 4.5, 5.2, 6.6, 7.3, 8.7, 9.2, 10.6, 11.5, 12.4, 13.6]
    globalMa()
   
    #dif setter
    print("What difficulty do you want 1 for easy, or 2 for hard?")
    P_dif = input(": ")
   
    #number 1 and 2 = the random number here
    if P_dif == "1":
        number_one = random.choice(numeral_list_two)
        number_two = random.choice(numeral_list_two)
        dif_check = 1
    else:
        number_one = random.choice(numeral_list_three)
        number_two = random.choice(numeral_list_three)
        dif_check = 2
   
   
   
    #int to string
    number_one_str = str(number_one)
    number_two_str = str(number_two)
   
    #asks what the problem is
    if mathh == 1:
        print("What is " + number_one_str + " + " + number_two_str)
        P_ans = input(": ")
        checker = 1
    else:
        print("What is " + number_one_str + " - " + number_two_str)
        P_ans = input(": ")
        checker = 2
   
    #str to int
    if dif_check == 1:
        P_anss = int(P_ans)
        number_one = int(number_one)
        number_two = int(number_two)
    else:
        P_anss = float(P_ans)
        number_one = float(number_one)
        number_two = float(number_two)
       
    #sets the right answer    
    if checker == 1:
        answer = number_one + number_two
    else:
        answer = number_one - number_two
   
    #final step
    if P_anss == answer:
        print("good job! you got it right!")
        starter()
    else:
        print("ooh try again")
        starter()
   
#intro
print("=----------------------=")
print("=---Ethans Math Game---=")
print("=----------------------=")
starter()
   

Ques = ['Meenakshi temple is in \n 1) Madurai 2) Chennai 3) Trivandram 4) Puri',
        'Bahubali festival is related to \n 1)Islam 2) Hinduism 3) Buddism 4) Jainism',
        'Who is the author of the Epic "Meghdoot"? \n 1) Vishakadatta 2) Valmiki 3) Banabhatta 4) Kalidas',
        "Good Friday is observed to commemorate the event of \n 1) birth of Jesus Christ, 2) birth of' St. Peter 3) crucification of Jesus Christ 4) rebirth of Jesus Christ" ]

Ans = [1,4,4,3]

Score=0
Amount=0

for i in range(len(Ques)) :
        print(Ques[i])
        UserInp = int(input("Enter the answer:"))
        if UserInp==Ans[i]:
                print(Ans[i])
                Score=Score+1
                Amount=Amount+5000
                print("Correct Answer!!! Moving to Next question now...")
        else:
                break

print("Your Score :", Score)
print("Your Winning Amount:", Amount)

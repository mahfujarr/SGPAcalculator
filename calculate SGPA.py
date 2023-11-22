def markToGrade(m):
    if (m<60):
        print("You've Failed\n")
        return 0.0
    elif(m >= 60 and m<=64):
        print("You've got 'D'\n")
        return 1.0
    elif(m >= 65 and m<=69):
        print("You've got 'D+'\n")
        return 1.5
    elif(m >= 70 and m<=73):
        print("You've got 'C-'\n")
        return 2.2
    elif(m >= 74 and m<=76):
        print("You've got 'C'\n")
        return 2.5
    elif(m >= 77 and m<=79):
        print("You've got 'C+'\n")
        return 2.8
    elif(m >= 80 and m<=83):
        print("You've got 'B-'\n")
        return 3.1
    elif(m >= 84 and m<=86):
        print("You've got 'B'\n")
        return 3.4
    elif(m >= 87 and m<=89):
        print("You've got 'B+'\n")
        return 3.7
    elif(m >= 90 and m<=100):
        print("You've got 'A'\n")
        return 4.0

def GradePoint(m,h):
    return(m*h)

ch_eng = 4
ch_csc = 3
ch_env = 2
ch_art = 1   
Sch = (ch_eng + ch_csc + ch_env + ch_art)


print("Welcome to IUBAT SGPA calculator for Fall'23.\nI really hope you get satisfied after seeing the result.\n")

en = float(input("Enter your ENG 101 marks: \n="))
en=markToGrade(en)
cs = float(input("Enter your CSC 103 marks: \n="))
cs=markToGrade(cs)
ev = float(input("Enter your ENV 103 marks: \n="))
ev=markToGrade(ev)
ar = float(input("Enter your ART 102 marks: \n="))
ar=markToGrade(ar)


GP_en = GradePoint(en,ch_eng)
GP_cs = GradePoint(cs,ch_csc)
GP_ev = GradePoint(ev,ch_env)
GP_ar = GradePoint(ar,ch_art)

SGP = (GP_en + GP_cs + GP_ev + GP_ar)

SGPA = (SGP/Sch)
print(f"Your SGPA for this semester is: {SGPA}\n")

input('Press ANY button to exit')
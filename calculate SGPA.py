def markToGrade(m):
    if (m<60):
        print("You've Failed")
        return 0.0
    elif(m >= 60 and m<=64):
        print("You've got 'D'")
        return 1.0
    elif(m >= 65 and m<=69):
        print("You've got 'D+'")
        return 1.5
    elif(m >= 70 and m<=73):
        print("You've got 'C-'")
        return 2.2
    elif(m >= 74 and m<=76):
        print("You've got 'C'")
        return 2.5
    elif(m >= 77 and m<=79):
        print("You've got 'C+'")
        return 2.8
    elif(m >= 80 and m<=83):
        print("You've got 'B-'")
        return 3.1
    elif(m >= 84 and m<=86):
        print("You've got 'B'")
        return 3.4
    elif(m >= 87 and m<=89):
        print("You've got 'B+'")
        return 3.7
    elif(m >= 90 and m<=100):
        print("You've got 'A'")
        return 4.0

def creditHours(h):
    if (h==eng):
        return 4
    elif(h==csc):
        return 3     
    elif(h==env):
        return 2     
    elif(h==art):
        return 1     

print("Welcome to IUBAT SGPA calculator for Fall'23.\nI really hope you get satisfied after seeing the result.")

eng = float(input("Enter your ENG 101 marks: \n="))
eng=markToGrade(eng)
csc = float(input("Enter your CSC 103 marks: \n="))
csc=markToGrade(csc)
env = float(input("Enter your ENV 103 marks: \n="))
env=markToGrade(env)
art = float(input("Enter your ART 102 marks: \n="))
art=markToGrade(art)

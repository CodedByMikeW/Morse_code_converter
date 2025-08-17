
Morse_Code={
    'Letters':{
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-..",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--..",
        "-":"Space"
},
    "Numbers":{
        '1':".----",
        '2':"..---",
        '3':"...--",
        '4':"....-",
        '5':".....",
        '6':"-....",
        '7':"--...",
        '8':"---..",
        '9':"----.",
        '0':"-----",


    }
}


# if isinstance(char,int):
def Comms():
    print("Welcome to the Morris code Converter. Input Numbers or Letters and ' - ' for a Space ")
    Translation_let= input("Convert Letters this into Morris Code: ").upper()
    Translation_Num=input("Convert Numbers this into Morris Code: ")
    for chars in Translation_let :#and Translation_Num:
        if isinstance(chars,str):
            print(f"This is Letter code {Morse_Code['Letters'][chars]}")
    for Nums in Translation_Num:#and Translation_Num:
            print(f"Number Code {Morse_Code['Numbers'][Nums]}")
#Comms()


def together():
    print("Welcome to the Morris code Converter. Input Numbers or Letters and use ' - ' for a Space. ")
    Trancript=[]
    Translation = input("Put the Numbers and Letters that you want to convert into Morris Code: ").upper()
    for chars in Translation :#and Translation_Num:
        if chars not in Morse_Code['Letters']:
            Trancript.append(Morse_Code['Numbers'][chars])
            print(f"This is Numbers code {Morse_Code['Numbers'][chars]}")
        elif chars not in Morse_Code['Numbers']:
            Trancript.append(Morse_Code['Letters'][chars])
            print(f"This is Letter code {Morse_Code['Letters'][chars]}")

    print(f"This is the Transcript : {Trancript}")

together()
#Example cool message that can be Converted : Hello-General-Bob-This-is-the-Nuclear-Codes-2691670679697267

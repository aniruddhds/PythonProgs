# mad libs
def libs1():
    adj1=input("An adjective: ")
    adj2=input("Another adjective: ")
    bird=input("A bird: ")
    room=input("Room in a house: ")
    verb=input("Verb (in past tense): ")
    verb2=input("A verb: ")
    sentence=f"It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. I {verb} down the stairs to see if I could help {verb2} the dinner."
    print("+++++++++++++++++++++++++++++++++++++")
    print("Your sentence is :--")
    print("+++++++++++++++++++++++++++++++++++++")
    print(sentence)
    return sentence

def libs2():
    noun1=input("A noun (person): ")
    noun2=input("A noun (a person): ")
    noun3=input("A noun (person, place or thing): ")
    noun4=input("A noun (person, place or thing): ")
    noun5=input("A noun (person, place or thing): ")
    sentence=f"{noun1} went to the beach with {noun2}. They saw {noun3} and {noun4}. Later, they built a sandcastle out of {noun5}."
    print("+++++++++++++++++++++++++++++++++++++")
    print("Your sentence is :--")
    print("+++++++++++++++++++++++++++++++++++++")
    print(sentence)
    return sentence

def endcard():
    print("=====================================")
    print("Thank you for playing.")
    print("Visit again for more funny sentences.")
    
def fileWriter(sen):
    file=open('MadLibs.txt','a')
    file.write(f"Your madlibs sentence: {sen} \n")
    file.close()
    print("Sentence written to file.")
    
print(f"=========Welcome to MAD LIBS!!==========")
print("Now for your first sentence:-- ")
sen1=libs1()
fileWriter(sen1)
dec=input("Do you want to try one more? (y/n) : ")
if dec.lower()=='y':
    sen2=libs2()
    fileWriter(sen2)

endcard()

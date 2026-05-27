#Jordan Potenza

#Init
import time
import random

#Functions
def main():
    print("Welcome to Hogwarts!!!!!")
    name=input("What is your name: ")
    print("..")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print(house(name))
    #This assigns the house based on nam
def house(name):
        if name=="Harry" or name=="Hermione" or name=="Ron":
            return "Gryffindor"
        elif name=="Newt" or name=="Nymphadora" or name=="Pomona":
            return "Hufflepuff"
        elif name=="Luna" or name=="Cho" or name=="Filius":
            return "Ravenclaw"
        elif name=="Voldemort" or name=="Draco" or name=="Severus":
            return "Slytherin"
        else:
             x=random.randint(1,4)
             if x==1:
                  return "gryffindor"
             if x==2:
                  return "Hufflepuff"
             if x==3:
                  return "Ravenclaw"
             if x==4:
                  return "Slytherin"




#Main
main()

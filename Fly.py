import Insect_Class as i

def main():
    
    mosquito = i.Insect(2,4)
    housefly = i.Insect(3,6)

    mosquito.flight()
    housefly.flight()

    print("The mosquito can fly up to", mosquito.get_flight(), "miles.")
    print("The housefly can fly up to", housefly.get_flight(), "miles.")
    
    #print("The insect travelled " + str(insect.get_flight()) + " miles.")

main()
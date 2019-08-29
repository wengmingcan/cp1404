
"""
Name: weng mingcan
Date:23/08/2019
Brief program details :
Github:
"""

from operator import itemgetter
import csv


def main():
        """this is main function """
        print("Travel Tracker 1.0 - by weng mingcan")
        print("3 places loaded from places.csv")
        #print("{} places loaded".format(len(places)))
        #"""list.seek(0)
        #list.truncate()
        #list.write(places)
        #list.close()"""
        places=[]
        sorted_places(places)
        global places_data

        menu()


def sorted_places(places):
    places_list =[]
    places = open("places.csv",'r')
    global places_file
    places_file = places.readlines()
    places.close()

    global places_data
    for each in places_file:
        each = each.strip().split(',')
        places_list.append(each)
    print(places_list)
    places_list.sort(key=itemgetter(3,2))
    places_data = places_list

def menu():
    """this function is used to list menu"""
    while True:
        print("Menu:")
        print("L - List places")
        print( "A - Add new place")
        print("M - Make a place as visited")
        print("Q - Quit")
        chose = raw_input(">>>").upper()
        print(chose)
        if chose == "L":
            l_places()
        elif chose == "A":
            a_places()
        elif chose == "M":
            m_place()
        elif chose == "Q":
            quit()
            break
        else:
            print("Invalid menu choice")

def l_places():
    visit = 0
    unvisit = 0
    counter = 0
    places_data.sort(key=itemgetter(3,2))
    for each in (places_data):
        if each[3] == 'n':
            counter += 1
            print("{:<2}* {:<10} {:<12} {:>5}".format(counter, each[0],each[1],each[2]))
            visit += 1
        if each[3] == 'v':
            counter += 1
            print("{:<2}  {:<10} {:<12} {:>5}".format(counter, each[0],each[1],each[2]))
            unvisit += 1
    print("{}  places, You still want to visit {} places ".format(counter, unvisit))

def a_places():

    while True:
        name = raw_input("Enter place: ")
        if name == "":
            print("must enter a place")
        else:
            break
    while True:
        country = raw_input("Enter the country: ")
        if country == "":
            print("must Enter an country")
        else:
            break
    while True:
        try:
            priority = int(raw_input("Enter Priority: "))
            if priority == "" or priority <= 0:
                print("enter a valid number")
            else:
                break
        except ValueError:
            print("priority must be number")
    print("{0}, {1}, {2} has be succeed to sort".format(name, country, priority))
    global places_data
    places_data.append([name, country, priority, "n"])
    places_data.sort(key=itemgetter(3,2))


def m_place():
    """This function is used to complete place"""
    l_places()
    while True:
        m_place = int(input("Make a place as visited:"))
        try:
            if places_data[m_place-1][3] == 'v':
                print("This place already be visited")
            if places_data[m_place-1][3] == 'n':
                places_data[m_place-1][3] = 'v'
                unvisited_counter = 0
                for place in places_data:
                    if place[3] == 'n':
                        unvisited_counter += 1
                print("{} places. You still want to visit {} places ".format(len(places_data), unvisited_counter))
                break
        except ValueError:
            print("only can enter number")


def quit():
    with open("places.csv", "w") as place_file:
        place_writer = csv.writer(place_file, delimiter=",")
        for place in places_data:
            place_writer.writerow([place[0], place[1], place[2], place[3]])
    print("Have a nice day :)")


main()


# def changetostr():
#     """This function is used to change the list to string for saving to the CVS"""
#     newstr = ""
#     for each in  :
#         for word in each:
#             newstr += str(word)+","
#         newstr = newstr[:-1]
#         newstr += '\n'
#     return newstr
# main()

cities = ["nagpur","betul","bhopal","indore"]

heroes = ["thor","iron-man","spdier-man"]
#len (cities)
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")


print_list(heroes) 
print_list(cities)
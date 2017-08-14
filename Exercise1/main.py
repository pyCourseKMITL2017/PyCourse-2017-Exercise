import json
import csv

result = {}


def isExist(animal):
    return animal in result


with open('animal.csv', 'rb') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        name, weight, animal = row
        ###################### Hint ####################
        # add x to list a: a.append(x)                 #
        # add key 'x' value 'y' to dict a: a[x] = y    #
        # check the key 'x' exist in result: isExist(x)#
        ################################################
        # Your Code Here!

        
        # print("{} -> {} -> {}".format(name, weight, animal))


print("Result")
print(json.dumps(result, indent=4, sort_keys=True))

##### The Correct Result Should be... #####
# {
#     "chipmunk": [
#         "mathias",
#         "ace"
#     ],
#     "coati": [
#         "mocha",
#         "bacon",
#         "chom",
#         "shelton",
#         "ruby",
#         "champ"
#     ],
#     "deer": [
#         "ray"
#     ],
#     "dugong": [
#         "michael",
#         "jeff",
#         "angela",
#         "roscoe",
#         "oliver",
#         "lulu",
#         "jasmin"
#     ],
#     "eland": [
#         "tony",
#         "agnis",
#         "dalton",
#         "jameson",
#         "lacey",
#         "diesel"
#     ],
#     "hog": [
#         "lott",
#         "adam",
#         "marcus",
#         "cleo",
#         "emma"
#     ],
#     "hyena": [
#         "toby",
#         "khan",
#         "soyu",
#         "chester",
#         "panda"
#     ],
#     "marten": [
#         "milo",
#         "milkshake",
#         "don",
#         "jonathon"
#     ],
#     "panda": [
#         "peter",
#         "latte",
#         "lexi",
#         "peanut",
#         "samantha",
#         "daniel"
#     ],
#     "pig": [
#         "lia",
#         "eddie",
#         "hartman",
#         "sheppard",
#         "sasha"
#     ],
#     "squirrel": [
#         "shaffer",
#         "ginger",
#         "finn"
#     ]
# }
###########################################

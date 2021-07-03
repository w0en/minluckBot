import pickle
import csv

filehandler = open('minluck_dict', 'wb')
base_dict = pickle.load(filehandler)
filehandler.close()

field_names = ["Alias", "Breed"]
with open("alias.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

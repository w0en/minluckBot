import pickle
import pprint

print("Loading alias dictionary")
filehandler = open('alias_dict', 'rb')
alias_dict = pickle.load(file=filehandler)
filehandler.close()
print("Alias dictionary loaded")
print("Current dictionary:")
pprint.pprint(alias_dict)


def add_alias(dictionary):
    key = input("Add a alias:")
    value = input("Now add the mouse this is an alias for:")
    print(f"Do you want to add {key} as an alias for {value}?")
    if input().lower == "yes" or "y":
        alias_dict[key] = value
        print(f"Alias {key} added for mouse {value}")
    else:
        print(f"Aborting addition of {key} as an alias for {value}")
    print("Current alias dictionary:")
    pprint.pprint(alias_dict)


while True:
    response = input("What do you want to do?\nAdd/Remove/Show/Exit").lower()

    if response == "add":
        add_alias(alias_dict)

        addmore = input("Add another key?").lower()
        while addmore == "yes" or addmore == "y":
            add_alias(alias_dict)
            addmore = input("Add another key?").lower()

    elif response == "remove":
        key = input("What do you want to remove?")
        try:
            del alias_dict[key]
            print(f"Alias {key} removed")
        except KeyError:
            print("This is not a known alias")
        pass

    elif response == "exit":
        confirmation = input("Do you really want to exit?").lower()
        if confirmation == "yes" or "y":
            print("Pickling dictionary")
            filehandler = open('alias_dict', 'wb')
            pickle.dump(alias_dict, file=filehandler)
            filehandler.close()
            print("Alias Dictionary successfully pickled")
            exit()

    elif response == "show":
        print(f"Current Alias Dictionary: {len(alias_dict)} known aliases.")
        pprint.pprint(alias_dict)

    else:
        print("That's not a valid response")
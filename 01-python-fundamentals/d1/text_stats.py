sentense = input("Enter a sentence: ")
print(f"characters: {len(sentense)} ")
print(f"words: {len(sentense.split())} ")

number_of_s = sentense.lower().count("s")
print(f"number of 's': {number_of_s} ")

#%%

i = 0

while i <= 4:
    print("Hello everybody")
    i = i + 1 

#%%

beatles = ["John", "Paul","Gerorge", "Ringo"]

numbers = [0,3,49]

mixed_values = [1, True, 0.4, "hola"]

print(type(beatles))

#%%

print(len(beatles))


# %%

beatles = ["John", "Paul","Gerorge", "Ringo"]

print(beatles[2])

# %%

fruits = ["orange", "banana", "lemon", "grape"]

i = 0 

while i < 4:
    print(fruits[i])
    i = i + 1 
# %%

def print_list(list):
    index = 0 

    while index <= len(list) - 1:
        print(list[index])
        index = index + 1 

elements = ["Karmele", "Santiago", "Juan"]
print_list(elements)



# %%

ramones = ["Johnnie", "Joey", "Markee"]

phillippes = ["Pipe", "Pepe"]

print(ramones + phillippes)
print(phillippes * 4)
# %%


beatles = ["John", "Paul","Gerorge", "Ringo"]

beatles[3] = "Pepe"

print(beatles)

# %%

coding_club = []

coding_club.append("Juan")
coding_club.append("Maria")

print(coding_club)

coding_club.pop(0)

print(coding_club)

# %%

def print_list(list):
    for element in list:
        print(element)

elements = ["Karmele", "Santiago", "Juan"]
print_list(elements)


# %%

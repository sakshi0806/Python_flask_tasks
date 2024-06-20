
# Switch-case Program (Method 1)

colour = 'White'

if colour == 'Blue': 
    print("The sky is BLUE.") 

elif colour == "Green": 
    print("Trees are tall and GREEN") 

elif colour == "Yellow": 
    print("The sun is bright and YELLOW in colour") 
    
elif colour == "Red": 
    print("Apples are RED and fresh")

else: 
    print("Rainbow has seven different colours")

# Switch-case Program (Method 2)

day = "Sunday"

switch_dict = {
    "Monday": "It's the start of the week.",
    "Wednesday": "You're halfway through the week.",
    "Friday": "TGIF! It's the end of the week.",
    "Sunday": "Relax and enjoy your weekend.",
}

result = switch_dict.get(day, "Not a special day.")

print(result)


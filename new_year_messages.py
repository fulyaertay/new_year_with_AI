# Import required libraries
import google.generativeai as genai


# Set up Gemini API Key
GOOGLE_API_KEY = "YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Prepare Zodiac Signs
zodiac_signs = {
    1: "Aries",
    2: "Taurus",
    3: "Gemini",
    4: "Cancer",
    5: "Leo",
    6: "Virgo",
    7: "Libra",
    8: "Scorpio",
    9: "Sagittarius",
    10: "Capricorn",
    11: "Aquarius",
    12:"Pisces"
}

# Show Zodiac Signs
def show_options():
    print("\nAvailable Zodiac Signs:")
    for key, description in zodiac_signs.items():
        print(f"{key}: {description}")

    # Input choice from user
    choice = int(input("\nChoose one of the 12 zodiac signs to receive your personalized New Year message or 0 to exit: "))

    # Generate new year message according to the zodiac sign of the user
    prompt = ""
    if choice in zodiac_signs:
        if choice == 1:
            prompt = f"Please generate a new year message according to Aries zodiac sign "
        elif choice == 2:
            prompt = f"Please generate a new year message according to Taurus zodiac sign"
        elif choice == 3:
            prompt = f"Please generate a new year message according to Gemini zodiac sign "
        elif choice == 4:
            prompt = f"Please generate a new year message according to Cancer zodiac sign "
        elif choice == 5:
            prompt = f"Please generate a new year message according to Leo zodiac sign "
        elif choice == 6:
            prompt = f"Please generate a new year message according to Virgo zodiac sign"
        elif choice == 7:
            prompt = f"Please generate a new year message according to Libra zodiac sign"
        elif choice == 8:
            prompt = f"Please generate a new year message according to Scorpio zodiac sign"
        elif choice == 9:
            prompt = f"Please generate a new year message according to Sagittarius zodiac sign"
        elif choice == 10:
            prompt = f"Please generate a new year message according to Capricorn zodiac sign"
        elif choice == 11:
            prompt = f"Please generate a new year message according to Aquarius zodiac sign"
        elif choice == 12:
            prompt = f"Please generate a new year message according to Pisces zodiac sign"
    else:
        print("Exiting the program..")
        exit()
    # Create Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Run model and show results to the user
    response = model.generate_content(prompt)
    print("\nNew Year Message:")
    print(response.text)
    
# Start the program  
show_options()






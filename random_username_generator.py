import random
import string

def load_words():
    adjectives = ["Cool", "Happy", "Crazy", "Brave", "Witty", "Clever", "Swift", "Gentle", "Fierce", "Jolly"]
    nouns = ["Tiger", "Dragon", "Eagle", "Panther", "Wizard", "Knight", "Phoenix", "Samurai", "Pirate", "Ninja"]
    return adjectives, nouns

def generate_username(include_numbers=True, include_special_chars=True, length=10):
    adjectives, nouns = load_words()
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    if include_special_chars:
        username += random.choice("!@#$%^&*")
    
    return username[:length]

def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

def main():
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    length = int(input("Enter the maximum username length (default 10): ") or 10)
    
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
        save_to_file(username)
    
    print(f"\nUsernames saved to usernames.txt")

if __name__ == "__main__":
    main()

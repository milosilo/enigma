
# Initialize colors for cross-platform compatibility
from colorama import init
init()
from termcolor import colored
import time
import random
import string

# ASCII Art for Enigma
print(colored('  _____                    _   _             ', 'cyan'))
print(colored(' | ____|_ __   ___ ___  __| |_(_) ___  _ __  ', 'cyan'))
print(colored(' |  _| | \'_ \ / __/ _ \/ _` | |/ _ \| \'_ \ ', 'cyan'))
print(colored(' | |___| | | | (_|  __/ (_| | | (_) | | | |', 'cyan'))
print(colored(' |_____|_| |_|\___\___|\__,_|_|\___/|_| |_|', 'cyan'))
print(colored('Welcome to Enigma!', 'yellow'))


import time
import random
import string

# All printable ASCII characters including those used in programming
all_chars = string.printable

# Function to generate a random rotor (cipher wheel)
def generate_rotor():
    rotor = list(all_chars)
    random.shuffle(rotor)
    return ''.join(rotor)

# Function to rotate the rotor one step
def rotate(rotor):
    return rotor[-1] + rotor[:-1]

# Function to encode/decode a single character using a rotor
def transform_char(c, rotor):
    index = all_chars.index(c)
    return rotor[index]

# Function to decode a single character using a rotor
def transform_char_decode(c, rotor):
    index = rotor.index(c)
    return all_chars[index]

# Function to create a plugboard
def create_plugboard(swaps):
    plugboard = list(all_chars)
    for char1, char2 in swaps:
        index1, index2 = all_chars.index(char1), all_chars.index(char2)
        plugboard[index1], plugboard[index2] = plugboard[index2], plugboard[index1]
    return ''.join(plugboard)

# Function to apply the plugboard before and after rotor transformations
def apply_plugboard(c, plugboard):
    return plugboard[all_chars.index(c)]

# Enhanced function to encode a message
def enigma_encode_advanced(message, rotors, plugboard):
    print("Starting the encoding process...")
    encoded_message = ""
    for i, c in enumerate(message):
        # Apply plugboard
        c = apply_plugboard(c, plugboard)
        print(f"After plugboard, character becomes: {c}")
        # Apply rotors
        active_rotor = rotors[i % len(rotors)]
        c = transform_char(c, active_rotor)
        print(f"After rotor transformation, character becomes: {c}")
        # Rotate rotor
        rotors[i % len(rotors)] = rotate(active_rotor)
        # Re-apply plugboard
        c = apply_plugboard(c, plugboard)
        print(f"After re-applying plugboard, character becomes: {c}")
        encoded_message += c
    print("Encoding complete.")
    return encoded_message

# Enhanced function to decode a message
def enigma_decode_advanced(encoded_message, rotors, plugboard):
    print("Starting the decoding process...")
    decoded_message = ""
    for i, c in enumerate(encoded_message):
        # Apply plugboard
        c = apply_plugboard(c, plugboard)
        print(f"After plugboard, character becomes: {c}")
        # Apply rotors
        active_rotor = rotors[i % len(rotors)]
        c = transform_char_decode(c, active_rotor)
        print(f"After rotor transformation, character becomes: {c}")
        # Rotate rotor
        rotors[i % len(rotors)] = rotate(active_rotor)
        # Re-apply plugboard
        c = apply_plugboard(c, plugboard)
        print(f"After re-applying plugboard, character becomes: {c}")
        decoded_message += c
    print("Decoding complete.")
    return decoded_message

# Main function to simulate the Enigma machine
def main():
    print("Welcome to Enigma!")
    # time.sleep(2)  # Uncomment this line in your local environment
    print("Generating random rotors for this session...")
    rotor1 = generate_rotor()
    rotor2 = generate_rotor()
    rotor3 = generate_rotor()
    print("Rotors generated.")
    
    print("Creating a plugboard with sample swaps...")
    plugboard_swaps = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H')]
    plugboard = create_plugboard(plugboard_swaps)
    print("Plugboard created.")
    
    # Initialize rotors and plugboard
    rotors = [rotor1, rotor2, rotor3]
    
    print("Please enter a message to encode:")
    message_to_encode = input()
    
    encoded_message = enigma_encode_advanced(message_to_encode, rotors.copy(), plugboard)
    print(f"Encoded message: {encoded_message}")
    
    decoded_message = enigma_decode_advanced(encoded_message, rotors.copy(), plugboard)
    print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()



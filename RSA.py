import sys

prime_one = 2957
prime_two = 3023
n_public_key = prime_one * prime_two

phi = (prime_one - 1) * (prime_two - 1)
# This is the Euler Phi function applied to n_public_key.
# As n_public_key is exactly the product of two primes, it is equal to the product of each of the primes minus one.
#private_key = 510459

for i in range(n_public_key):
    if (i * e_public_key) % phi == 1:
        private_key = i
        break


def encrypt(number):
    return (number ** e_public_key) % n_public_key


def decrypt(number):
    return (number ** private_key) % n_public_key


def get_input():
    print("Would you like to encrypt or decrypt a message?")
    user_input = input("Use comands 'Encrypt', 'Decrypt', or 'Exit' to continue. \n").lower()
    if user_input == "encrypt":
        number_to_encrypt = input("Please enter the number you wish to encrypt: \n")
        encrypted_number = encrypt(int(number_to_encrypt))
        print(encrypted_number)
        get_input()
    elif user_input == "decrypt":
        number_to_decrypt = input("Please enter the number you wish to decrypt: \n")
        decrypted_number = decrypt(int(number_to_decrypt))
        print(decrypted_number)
        get_input()
    elif user_input == "exit":
        sys.exit()
    else:
        print("Sorry, your input was not recognised, please try again")
        get_input()


def main():
    print("WARNING: THIS IS NOT SECURE AND SHOULD NOT BE USED AS SERIOUS ENCRYPTION.")
    get_input()


main()

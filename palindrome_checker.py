import time

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def main():
    print("Palindrome Checker")
    print("==================")
    text = input("Enter a word, number, or phrase: ").strip()
    print("\nChecking...\n")
    time.sleep(1)

    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')

if __name__ == "__main__":
    main()
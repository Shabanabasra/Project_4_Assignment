# Problem Statement
#Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):
#If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"
#If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"#
#If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.
#Here's a sample run of the program (user input is in blue):Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!


def make_sentence(word: str, part_of_speech: int) -> None:
    """Prints a sentence using the given word based on its part of speech."""
    sentence_templates = {
        0: f"I am excited to add this {word} to my vast collection of them!",
        1: f"It's so nice outside today it makes me want to {word}!",
        2: f"Looking out my window, the sky is big and {word}!"
    }

    print(sentence_templates.get(part_of_speech, "Invalid input. Please enter 0, 1, or 2."))

def main() -> None:
    """Gets user input and prints the corresponding sentence."""
    word = input("Please type a noun, verb, or adjective: ")

    while True:
        try:
            part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
            if part_of_speech not in [0, 1, 2]:
                print("Invalid choice. Please enter 0, 1, or 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer (0, 1, or 2).")

    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()

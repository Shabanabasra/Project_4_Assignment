import random
import string
import streamlit as st

# List of words to choose from
words = ["sunshine", "rainbow", "adventure", "galaxy", "treasure", "happiness"]


# Function to get a valid word from the list
def get_valid_word(words):
    word = random.choice(words).upper()
    while "-" in word or " " in word:
        word = random.choice(words).upper()
    return word


# Streamlit UI
st.title("🎮 Hangman Game")

# Session state variables
if "word" not in st.session_state:
    st.session_state.word = get_valid_word(words)
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.alphabet = set(string.ascii_uppercase)
    st.session_state.used_letters = set()
    st.session_state.lives = 6
    st.session_state.game_over = False

# Display game state
st.subheader(f"Lives Remaining: {st.session_state.lives} ❤️")
st.write(f"Used Letters: {', '.join(st.session_state.used_letters) if st.session_state.used_letters else 'None'}")

# Display the word with guessed letters revealed
word_display = [letter if letter in st.session_state.used_letters else "_" for letter in st.session_state.word]
st.subheader("Word: " + " ".join(word_display))

# Input field for guessing
if not st.session_state.game_over:
    user_letter = st.text_input("Guess a letter:", max_chars=1).upper()

    if st.button("Submit Guess") and user_letter:
        if user_letter in st.session_state.alphabet - st.session_state.used_letters:
            st.session_state.used_letters.add(user_letter)

            if user_letter in st.session_state.word_letters:
                st.session_state.word_letters.remove(user_letter)
            else:
                st.session_state.lives -= 1
                st.warning("❌ Wrong guess!")

        elif user_letter in st.session_state.used_letters:
            st.warning("🔄 You already guessed that letter!")

        else:
            st.error("⚠ Invalid input. Please enter a valid letter.")

# Check game over conditions
if st.session_state.lives == 0:
    st.error(f"💀 You lost! The word was: {st.session_state.word}")
    st.session_state.game_over = True

if not st.session_state.word_letters:
    st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}!")
    st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.word = get_valid_word(words)
        st.session_state.word_letters = set(st.session_state.word)
        st.session_state.used_letters = set()
        st.session_state.lives = 6
        st.session_state.game_over = False
        st.experimental_rerun()

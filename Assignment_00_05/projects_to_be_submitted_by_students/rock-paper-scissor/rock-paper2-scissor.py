import random
import streamlit as st

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "🤝 It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "🎉 You win!"
    else:
        return "😞 You lose!"

def main():
    st.title("🎮 Rock, Paper, Scissors Game!")
    
    choices = ["rock", "paper", "scissors"]
    user_choice = st.radio("Choose your move:", choices)
    
    if st.button("Play!"):
        computer_choice = random.choice(choices)
        st.write(f"🖥️ Computer chose: {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        st.subheader(result)

if __name__ == "__main__":
    main()

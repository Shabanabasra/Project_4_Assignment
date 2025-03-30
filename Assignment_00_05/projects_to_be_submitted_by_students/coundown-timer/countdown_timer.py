import time
import streamlit as st

# Streamlit UI
st.title("⏳ Countdown Timer")

# User input for countdown time
seconds = st.number_input("Enter the time in seconds:", min_value=1, step=1, value=10)

# Start button
if st.button("Start Timer"):
    st.write("⏰ Timer started!")
    countdown_placeholder = st.empty()  # Placeholder for countdown updates

    # Countdown loop
    for i in range(seconds, 0, -1):
        countdown_placeholder.markdown(f"## ⏳ {i} seconds remaining")
        time.sleep(1)

    # Display completion message
    countdown_placeholder.markdown("## 🎉 Timer completed! ⏰")

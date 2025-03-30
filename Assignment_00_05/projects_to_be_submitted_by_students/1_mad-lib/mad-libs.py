import random
import streamlit as st

# List of stories to choose from
stories = [
    "One day, {name} was in {place} when a {adjective} {animal} bit them. Suddenly, they could {verb} at the speed of light! ‘I must use my powers to {verb} evil!’ {name} declared. But first, they had to finish their {adjective} homework.",
    "At {place}, {name} decided to prank their {adjective} teacher. They put a {adjective} {animal} inside the teacher’s desk. But when the teacher opened it, the {animal} jumped out and started to {verb}! The whole class laughed until the principal walked in and {verb} at {name}!",
    "At {place}, {name} found a {adjective} hat. When they put it on, a {animal} appeared and started to {verb} {adverb}. ‘This is the best day ever!’ {name} shouted.",
    "Inside {place}, {name} picked up a {adjective} book. Suddenly, a {animal} jumped out and began to {verb} {adverb}. ‘This is the weirdest library ever!’ {name} gasped.",
    "While in {place}, {name} saw a {adjective} spaceship land. A tiny {animal} stepped out and started to {verb} {adverb}. ‘Well, that’s something you don’t see every day!’ {name} whispered.",
    "While at {place}, {name} saw a {adjective} {animal} trying to {verb} {adverb}. It tripped and fell, then stood up like nothing happened. ‘Smooth move!’ {name} laughed.",
]

# Streamlit UI
st.title("🎭 Mad Lib Generator")

# User input fields
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")
verb = st.text_input("Enter a verb:")
adverb = st.text_input("Enter an adverb:")
adjective = st.text_input("Enter an adjective:")

# Button to generate the story
if st.button("Generate Story"):
    if name and place and animal and verb and adverb and adjective:
        selected_story = random.choice(stories).format(
            name=name,
            place=place,
            animal=animal,
            verb=verb,
            adverb=adverb,
            adjective=adjective
        )  # ✅ Fixed: Removed incorrect indentation here
        st.subheader("🎉 Here is your Mad Lib story:")
        st.write(selected_story)
    else:
        st.warning("⚠ Please fill in all the fields to generate a story.")

# Play again button
if st.button("Play Again"):
    st.rerun()  # ✅ Fixed: Replaces the deprecated `st.experimental_rerun()`

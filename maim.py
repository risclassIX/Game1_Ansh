import streamlit as st
import random

# Title
st.header("Please paly game! This game is designed by ANSH")
st.subheader("Please Choose Your Choice From Box Given Below! ANSH")
# User input
u = st.selectbox("Choose any one",["Rock","Paper","Scissors"])

# Dictionary to map choices
dict1 = {"Rock": 1, "Paper": 2, "Scissors": 3}
dict2 = {1: "Rock", 2: "Paper", 3: "Scissors"}

# Random choice for computer
c = random.choice([1, 2, 3])

# User choice
u2 = dict1[u]

# Determine the result
if c == u2:
    st.write("Oh, It's a Draw! 🤝")
elif (c - u2) == -1 or (c - u2) == 2:
    st.write("You Won! 😃🏆")
else:
    st.write("You Lose! 😔😞")


# Show computer's choice
st.write(f"Computer Choosen: {dict2[c]}")
st.write(f"You Choosen: {u}")
st.write(f"Thank You!    ANSH")

fd = st.selectbox("How do you like this game?Choose in between 1 to 5 Star",(1,2,3,4,5))
if fd == 1:
    st.write("Sorry! We will improve our mistakes.")
elif fd == 2:
    st.write("Okay, We'll try to make it better.")
elif fd == 3:
    st.write("It can be a network problem!")
elif fd == 4:
    st.write("I think you enjoyed very much!")
else:
    st.write("Thank You So Much For Giving Your Time!")
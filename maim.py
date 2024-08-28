import streamlit as st
import random

# Ye list ek database ka simulation hai jisme existing usernames store hain
# Asal project me ye usernames database me save hote hain
existing_usernames = []  # Example ke liye kuch usernames

# Session state me username ko initialize kar rahe hain
# Taaki hume pata rahe ki user ka username set ho chuka hai ya nahi
if 'username' not in st.session_state:
    st.session_state.username = None

# Ye function check karega ki username unique hai ya nahi
# Agar username existing_usernames list me nahi hai, to wo unique hai
def is_unique_username(username):
    return(f"{username} not in {existing_usernames}")

# Agar session state me username set nahi hai, to user se ek unique username lene ko kahenge
if st.session_state.username is None:
    st.write("Please Enter your name below!")  # User se username set karne ka message
    
    # Text input box, jisme user apna username enter karega
    username_input = st.text_input("Enter your username")
    
    if username_input:  # Agar user ne kuch username enter kiya hai
        if is_unique_username(username_input):  # Check karenge ki username unique hai ya nahi
           
            st.session_state.username = username_input  # Username session state me save karenge
            st.success(f"Yay! Your Username {username_input} is set successfully!")  # Success message show hoga
            # Username ko list me add kar rahe hain (Yeh asal me database me save hota)
            existing_usernames.append(username_input)
            st.write("Notification: A new username has been set.")  # Notification message
        else:
            st.error("This username is already taken. Please choose another one.")  # Error message agar username taken hai
else:
    st.write(f"Welcome back, {st.session_state.username} Let's Play!")  # Agar username already set hai, to user ko welcome message

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
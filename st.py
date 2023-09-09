import streamlit as st

# Create a text input widget.
text_input = st.text_input("Enter some text:")

# Print the text that the user entered.
st.write("You entered:", text_input)

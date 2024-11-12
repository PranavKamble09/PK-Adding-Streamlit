import streamlit as st

# Set the title and header with custom colors and font sizes
st.markdown(
    "<h1 style='text-align: center; color: #FF6347;'>Fun Adding App for Toddlers</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='text-align: center; color: #4682B4;'>Let's add two numbers together!</h2>",
    unsafe_allow_html=True,
)

# Input fields with friendly prompts
first_number = st.number_input("Enter the first number:", min_value=0, max_value=100, step=1, format="%d")
second_number = st.number_input("Enter the second number:", min_value=0, max_value=100, step=1, format="%d")

# Calculate the sum
result = first_number + second_number

# Display the result with a colorful font
st.markdown(
    f"<h3 style='text-align: center; color: #32CD32;'>The sum is: {result}</h3>",
    unsafe_allow_html=True,
)

# Add an emoji for added fun
st.markdown(
    "<p style='text-align: center;'>✨😊✨</p>",
    unsafe_allow_html=True,
)

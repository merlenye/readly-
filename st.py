import streamlit as st
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import re

# Create a text input widget.
text_input = st.text_input("Enter some text:")

# Print the text that the user entered.
st.write("You entered:", text_input)
key = st.text_input("Enter API key:")
anthropic = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=key,
)
st.write(get_book_chapters())



def get_book_chapters():
  choice = st.text_input("what book are you reading?")

  # Set the model and max_tokens_to_sample parameters.
  model = "claude-2"
  max_tokens_to_sample = 300

  # Create the prompt.
  prompt = f"{HUMAN_PROMPT} how many chapters are in great gatbsy? {AI_PROMPT}"

  # Get the completion.
  completion = anthropic.completions.create(
      model=model,
      max_tokens_to_sample=max_tokens_to_sample,
      prompt=prompt,
  ) 
  return (get_first_number(completion.completion))

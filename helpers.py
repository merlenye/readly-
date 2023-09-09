from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import re

anthropic = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key= input() ,
)
def get_book_chapters():
  choice = input("what book are you reading?")

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

def prompt_chapter_choice(number_of_chapters):
  """
  Gets a list of chapters as long as the number of chapters, then prompts the user to choose a chapter, and returns the number the user chose.

  Args:
    number_of_chapters: The number of chapters.

  Returns:
    The number of the chapter that the user chose.
  """

  chapters = []
  for i in range(number_of_chapters):
    chapters.append(f"Chapter {i + 1}")

  print("Choose a chapter:")
  for i, chapter in enumerate(chapters):
    print(f"{i + 1}: {chapter}")

  choice = input("Enter your choice here (just the number): ")

  try:
    choice = int(choice)
  except ValueError:
    print("Invalid choice.")
    return

  if choice < 1 or choice > len(chapters):
    print("Invalid choice.")
    return

from inline.inlinegpt import InlineGPT
import os

print(os.environ.get('G_API_KEY'))


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    gpt = InlineGPT(os.environ.get('G_API_KEY'))
    gpt.get_solution("test.py", e)

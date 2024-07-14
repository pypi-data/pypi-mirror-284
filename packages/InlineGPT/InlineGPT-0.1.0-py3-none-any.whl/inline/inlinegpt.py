import google.generativeai as genai


class InlineGPT:
    def __init__(self, API_KEY):
        try:
            genai.configure(api_key=API_KEY)
            self.model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        except Exception as e:
            print(f"Error during initialization: {e}")
            print("Please provide a valid API key. It can be found on https://aistudio.google.com/app/apikey")

    def get_solution(self, file_name, error):
        try:
            with open(file_name, "r") as file:
                code = file.read()
                prompt = f"Following is the code:\n{code}\n\nThe following error was encountered:\n{error}\n\nHow can this error be resolved?"
                response = self.model.generate_content(prompt)
                print(response.text)
        except Exception as e:
            print(f"An error occurred: {e}")

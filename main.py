import os
from dotenv import load_dotenv

load_dotenv()
print("Environment variables loaded.")

def main():
    print("Hello from langchaincourse!")
    print(os.environ.get("OPENAI_API_KEY")) 
    print("I am just commiting to GitHub!")

if __name__ == "__main__":
    main()

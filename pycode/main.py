import os  # Imported os to use os.getenv for environment variables
from dotenv import load_dotenv  # Imported load_dotenv to load environment variables from .env file
import argparse
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load the environment variables from the .env file
load_dotenv()  # Added this line to load the API key from the .env file

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# Initialize the OpenAI instance with the API key from the environment variable
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))  # Fixed by passing the API key from .env

code_prompt = PromptTemplate(
  template="Write a very short {language} function that will {task}",
  input_variables=["language", "task"]
)
test_prompt = PromptTemplate(
  input_variables=["language", "code"],
  template="write a test for the following {language} code;\n{code}"
)

code_chain = LLMChain(
  llm=llm,
  prompt=code_prompt,
  output_key="code"
)
test_chain = LLMChain(
  llm=llm,
  prompt=test_prompt,
  output_key="test"
)

# Create sequential chain consisting of priorly defined chains
chain = SequentialChain(
  chains=[code_chain, test_chain],
  input_variables=["task", "language"],
  output_variables=["test", "code"]
)

result = chain({
  "language": args.language,
  "task": args.task
})

print(">>>>>>>> GENERATED CODE")
print(result["code"])

print(">>>>>>>> GENERATED TEST")
print(result["test"])

# to run 
# python main.py --language python --task 'return a list of numbers'

# returns list of numbers as python code
# python main.py --language python --task 'return a list of numbers'
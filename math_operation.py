# TOOL BINDING
from langchain.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@tool
def divide(a: int, b: int) -> int:
    """Divide two numbers."""
    return a / b

from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=api
)

agent = initialize_agent(
    tools=[add, multiply, subtract, divide],
    llm = llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

res = agent.run(input("Enter two numbers and an operation: "))
print(res)

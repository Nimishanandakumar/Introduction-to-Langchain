from langchain.agents_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

agent_execute = create_python_agent(llm=OpenAI(temperature=0, max_tokens=1000), tool=PythonREPLTool(), verbose=True)
agent_execute.run("Find the roots(zeros) if the quadratic function 3* x**2 + 2*x -1")
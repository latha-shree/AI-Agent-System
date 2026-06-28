from core.gemini import ask_gemini


def retriever_agent(task):


    prompt=f"""

You are a research agent.

Topic:
{task}


Return facts.

"""


    result=ask_gemini(prompt)


    return result
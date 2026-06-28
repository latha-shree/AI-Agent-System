from core.gemini import ask_gemini



def analyzer_agent(data):


    prompt=f"""

Analyze this information:

{data}


Give summary and key points.


"""


    return ask_gemini(prompt)
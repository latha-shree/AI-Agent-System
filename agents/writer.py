from core.gemini import ask_gemini



def writer_agent(data):


    prompt=f"""

Create final report from:

{data}


Format:

TITLE

SUMMARY

KEY POINTS

CONCLUSION


"""


    return ask_gemini(prompt)
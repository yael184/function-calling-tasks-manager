import os
import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from todo_service import get_tasks, add_task, delete_task, update_task

# Load environment variables
load_dotenv()

# --- NETFREE / SSL SOLUTION ---
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
# ------------------------------

# Initialize the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Important: Make sure the model name is exactly as expected by the new SDK
MODEL_ID = "gemini-2.5-flash" 

SYSTEM_PROMPT = f"""
You are a highly efficient Personal Task Manager AI. 
Today's date is {datetime.date.today()}.
Use the provided tools to manage the user's tasks. 
Always calculate relative dates (like 'tomorrow' or 'next week') based on today's date.
Keep your responses helpful, concise, and in the user's language.
"""

def agent(query: str):
    # Defining the tools
    tools = [get_tasks, add_task, delete_task, update_task]
    
    try:
        # The new SDK handles function calling via the 'config' parameter
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=tools,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
            )
        )
        return response.text
    except Exception as e:
        # This will help us see exactly what's going wrong if it fails again
        print(f"Error in Agent: {e}")
        return "I'm sorry, I encountered an error while processing your request."
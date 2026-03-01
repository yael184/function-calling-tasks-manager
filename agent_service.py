import os
import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import todo_service

load_dotenv()
os.environ['CURL_CA_BUNDLE'] = '' # SSL Fix
os.environ['REQUESTS_CA_BUNDLE'] = ''

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# Using the latest Gemini 2.5 Flash
MODEL_ID = "gemini-2.5-flash"

tool_definition = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="fetch_all_tasks",
            description="Get the task list. Can filter by status or category.",
            parameters={"type": "object", "properties": {"status": {"type": "string"}, "category": {"type": "string"}}}
        ),
        types.FunctionDeclaration(
            name="create_new_task",
            description="Add a task.",
            parameters={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "notes": {"type": "string"},
                    "category": {"type": "string"},
                    "due_date": {"type": "string"}
                },
                "required": ["title"]
            }
        ),
        types.FunctionDeclaration(
            name="delete_existing_task",
            description="Delete a task by ID.",
            parameters={"type": "object", "properties": {"task_id": {"type": "integer"}}, "required": ["task_id"]}
        )
    ]
)

DISPATCHER = {
    "fetch_all_tasks": todo_service.get_tasks,
    "create_new_task": todo_service.add_task,
    "delete_existing_task": todo_service.remove_task
}

def agent(user_input: str) -> str:
    ctx = f"Role: Task Manager. Date: {datetime.date.today()}."
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=user_input,
        config=types.GenerateContentConfig(tools=[tool_definition], system_instruction=ctx)
    )

    res_content = response.candidates[0].content
    for part in res_content.parts:
        if part.function_call:
            fn, args = part.function_call.name, part.function_call.args
            if fn in DISPATCHER:
                output = DISPATCHER[fn](**args)
                final_res = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[
                        types.Content(role="user", parts=[types.Part(text=user_input)]),
                        res_content,
                        types.Content(role="function", parts=[
                            types.Part.from_function_response(
                                name=fn, 
                                response={"data": output}
                            )
                        ])
                    ],
                    config=types.GenerateContentConfig(system_instruction=ctx)
                )
                return final_res.text
    return response.text
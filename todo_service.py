import datetime

# In-memory database
tasks = []
task_counter = 1

def get_tasks():
    """
    Retrieves the complete list of all tasks currently stored in the system.
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a task 
              containing id, title, description, type, start_date, and status.
    """
    return tasks

def add_task(title: str, description: str, task_type: str, start_date: str = None):
    """
    Creates and stores a new task in the collection. Use this when the user wants 
    to schedule, remember, or add an item to their to-do list.
    
    Args:
        title (str): A concise name or headline for the task.
        description (str): Detailed information or notes about the task.
        task_type (str): The category of the task (e.g., 'Work', 'Personal', 'Urgent').
        start_date (str, optional): The scheduled date in 'YYYY-MM-DD' format. 
                                    If not provided by the user, it defaults to today's date.
                                    
    Returns:
        dict: The newly created task object including its unique generated ID.
    """
    global task_counter
    new_task = {
        "id": task_counter,
        "title": title,
        "description": description,
        "type": task_type,
        "start_date": start_date or str(datetime.date.today()),
        "status": "Open"
    }
    tasks.append(new_task)
    task_counter += 1
    return new_task

def delete_task(task_id: int):
    """
    Removes a specific task from the system based on its unique ID. 
    Use this when the user wants to cancel or delete a task.
    
    Args:
        task_id (int): The unique numerical identifier of the task to be removed.
        
    Returns:
        dict: A confirmation message indicating the task was successfully deleted.
    """
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return {"message": f"Task {task_id} has been successfully deleted."}

def update_task(task_id: int, title: str = None, status: str = None):
    """
    Updates the details of an existing task. Use this when the user wants to 
    change a task's name or mark it as 'Completed'.
    
    Args:
        task_id (int): The ID of the task to update.
        title (str, optional): The new title for the task.
        status (str, optional): The new status (e.g., 'Completed', 'In Progress').
        
    Returns:
        dict: The updated task object or an error message if not found.
    """
    for task in tasks:
        if task['id'] == task_id:
            if title: task['title'] = title
            if status: task['status'] = status
            return task
    return {"error": "Task not found"}
import requests
import sys

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URLs for employee details and TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        employee_name = employee_data["name"]

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todos_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Display the employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"    {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
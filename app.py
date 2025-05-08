import os
import requests
from github import Github

# Configuration
LEETCODE_USERNAME = "AnuranjanJain"
GITHUB_TOKEN = "your_github_token"
GITHUB_REPO = "AnuranjanJain/solutions"
LOCAL_DIRECTORY = "practice"

def fetch_leetcode_solutions(username):
    url = f"https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    response.raise_for_status()
    problems = response.json()["stat_status_pairs"]
    solutions = []

    for problem in problems:
        if problem["status"] == "ac":
            title_slug = problem["stat"]["question__title_slug"]
            solutions.append(title_slug)
    return solutions

def save_solution_locally(title_slug):
    # Simulate fetching solution code (replace with actual logic if needed)
    solution_code = f"# Solution for {title_slug}\n\nprint('Hello, LeetCode!')"
    file_path = os.path.join(LOCAL_DIRECTORY, f"{title_slug}.py")
    os.makedirs(LOCAL_DIRECTORY, exist_ok=True)
    with open(file_path, "w") as file:
        file.write(solution_code)
    return file_path

def upload_to_github(file_path, repo, github_token):
    g = Github(github_token)
    repository = g.get_repo(repo)
    with open(file_path, "r") as file:
        content = file.read()
    file_name = os.path.basename(file_path)
    try:
        repository.create_file(
            path=f"leetcode_solutions/{file_name}",
            message=f"Add solution for {file_name}",
            content=content,
            branch="main"
        )
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

def main():
    solutions = fetch_leetcode_solutions(LEETCODE_USERNAME)
    for title_slug in solutions:
        file_path = save_solution_locally(title_slug)
        upload_to_github(file_path, GITHUB_REPO, GITHUB_TOKEN)

if __name__ == "__main__":
    main()


    
#!/usr/bin/env python3
"""
LeetCode Practice Tracker

A tool to manage LeetCode practice problems, track progress, and maintain
a well-organized repository of solutions with auto-generated explanations.
"""
import os
import re
import sys
import json
import datetime
from datetime import timedelta
import urllib.request
import urllib.error
import ssl
import subprocess
from html.parser import HTMLParser
import requests
import getpass


def fetch_problem_details(url):
    """
    Fetch problem details from LeetCode URL using the LeetCode API.
    
    Args:
        url: LeetCode problem URL
    
    Returns:
        Dictionary with keys 'name', 'difficulty', 'url', or None if failed
    """
    try:
        # Extract problem title slug from URL
        match = re.search(r'problems/([^/]+)', url)
        if not match:
            print(f"Error: Could not extract problem slug from URL: {url}")
            return None
        
        slug = match.group(1)
        
        # GraphQL query to get problem details
        api_url = "https://leetcode.com/graphql"
        query = {
            "query": """
            query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    title
                    difficulty
                }
            }
            """,
            "variables": {"titleSlug": slug}
        }
        
        # Set up the request
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0',
            'Referer': 'https://leetcode.com'
        }
        
        req = urllib.request.Request(
            api_url,
            data=json.dumps(query).encode('utf-8'),
            headers=headers
        )
        
        # Create SSL context that ignores certificate verification
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        # Make the request and process the response
        with urllib.request.urlopen(req, context=ctx) as response:
            result = json.loads(response.read().decode('utf-8'))
            
            if 'data' in result and 'question' in result['data'] and result['data']['question']:
                question = result['data']['question']
                return {
                    'name': question['title'],
                    'difficulty': question['difficulty'],
                    'url': url
                }
            else:
                print(f"Error: Could not get problem details for {url}")
                return None
                
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching problem details: {e}")
        return None


def update_leetcode_repo(problems, custom_day=None):
    """
    Update the LeetCode repository with new problems.
    
    Args:
        problems: List of dictionaries with keys 'name', 'url', 'difficulty', 'filename'
        custom_day: Optional custom day number to use instead of incrementing the current value
    """
    try:
        # Read the current README.md
        if not os.path.exists('readme.md'):
            print("Error: readme.md not found. Creating a new one...")
            with open('readme.md', 'w', encoding='utf-8') as f:
                f.write("""# LeetCode Practice Tracker

This repository tracks my daily LeetCode practice problems.

## Progress

| Metric | Value |
|--------|-------|
| Total Problems | 0 |
| Days Completed | 0 |
| Last Updated | N/A |

## Problems

## About

This project organizes my LeetCode practice by day, tracking progress over time.
""")
        
        with open('readme.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        # Parse current progress metrics
        total_problems_match = re.search(r'\| Total Problems \| (\d+) \|', readme_content)
        days_completed_match = re.search(r'\| Days Completed \| (\d+) \|', readme_content)
        
        if not total_problems_match or not days_completed_match:
            print("Error: Could not parse progress metrics from README")
            return
        
        total_problems = int(total_problems_match.group(1))
        days_completed = int(days_completed_match.group(1))
        
        # Update progress metrics
        new_total_problems = total_problems + len(problems)
        
        # Determine the day number
        if custom_day is not None:
            new_days_completed = max(custom_day, days_completed)
        else:
            new_days_completed = days_completed + 1
            
        # Get current date and time
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create new day directory
        new_day = f"day_{custom_day if custom_day is not None else new_days_completed}"
        new_day_path = os.path.join("practice", new_day)
        os.makedirs(new_day_path, exist_ok=True)
        
        # Create new day section content for README
        new_day_section = f"""
### Day {custom_day if custom_day is not None else new_days_completed}
 
| Problem | Difficulty | Solution |
|---------|------------|----------|
"""
        
        # Process each problem
        for problem in problems:
            problem_name = problem['name']
            problem_url = problem['url']
            difficulty = problem['difficulty']
            filename = problem['filename']
            
            # Create solution file if it doesn't exist
            solution_path = os.path.join(new_day_path, filename)
            if not os.path.exists(solution_path):
                with open(solution_path, 'w', encoding='utf-8') as f:
                    f.write(f"""# LeetCode Problem: {problem_name}
# URL: {problem_url}
# Day: {custom_day if custom_day is not None else new_days_completed}
# Difficulty: {difficulty}
# Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
# Status: Solved

""")
            
            # Add entry to the README section
            new_day_section += f"| [{problem_name}]({problem_url}) | {difficulty} | [✅](practice/{new_day}/{filename}) |\n"
        
        # Update README content - Progress metrics
        readme_content = re.sub(
            r'\| Total Problems \| \d+ \|', 
            f'| Total Problems | {new_total_problems} |', 
            readme_content
        )
        readme_content = re.sub(
            r'\| Days Completed \| \d+ \|', 
            f'| Days Completed | {new_days_completed} |', 
            readme_content
        )
        readme_content = re.sub(
            r'\| Last Updated \| .* \|', 
            f'| Last Updated | {current_date} |', 
            readme_content
        )
        
        # Extract header and footer
        header_match = re.search(r'(.*?)## Problems', readme_content, re.DOTALL)
        footer_match = re.search(r'## About.*', readme_content, re.DOTALL)
        
        if not header_match or not footer_match:
            print("Error: Could not parse README structure")
            return
        
        header = header_match.group(1) + "## Problems\n"
        footer = footer_match.group(0)
        
        # Find all day sections
        day_sections = []
        
        # Add the new day section
        day_sections.append((custom_day if custom_day is not None else new_days_completed, new_day_section))
        
        # Find existing day sections from the README
        existing_sections = re.findall(r'### Day (\d+)[\s\S]*?(?=### Day \d+|\n## About)', readme_content + "\n## About")
        
        # Process existing sections
        for section in existing_sections:
            day_match = re.search(r'### Day (\d+)([\s\S]*?)(?=### Day \d+|\n## About|$)', section)
            if day_match:
                day_num = int(day_match.group(1))
                # Skip if we're replacing this day
                if day_num == (custom_day if custom_day is not None else new_days_completed):
                    continue
                # Find the content portion
                content_match = re.search(r'(### Day \d+[\s\S]*?)(?=### Day \d+|\n## About|$)', section)
                if content_match:
                    content = content_match.group(1)
                    day_sections.append((day_num, content))
        
        # Sort day sections by day number in descending order
        day_sections.sort(key=lambda x: x[0], reverse=True)
        
        # Combine all parts
        updated_readme = header
        for _, section in day_sections:
            updated_readme += section
        updated_readme += "\n" + footer
        
        # Write updated README
        with open('readme.md', 'w', encoding='utf-8') as f:
            f.write(updated_readme)
        
        print(f"Updated README.md with {len(problems)} new problems for Day {custom_day if custom_day is not None else new_days_completed}")
        print(f"Created solution files in {new_day_path}")
        
        # After creating the problem files and updating the README,
        # also create or update the day-specific README
        generate_day_readme(new_day_path, custom_day if custom_day is not None else new_days_completed)
    except Exception as e:
        print(f"Error updating repository: {e}")


def rebuild_readme():
    """
    Rebuild the entire README.md file based on the practice directory structure.
    
    This helps fix any inconsistencies and ensures the README accurately
    reflects the current state of the practice repository.
    """
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
    try:
        # Count total problems and days
        total_problems = 0
        day_dirs = []
        
        for item in os.listdir(practice_dir):
            if os.path.isdir(os.path.join(practice_dir, item)) and item.startswith('day_'):
                try:
                    day_num = int(item.split('_')[1])
                    problems_count = len([f for f in os.listdir(os.path.join(practice_dir, item)) if f.endswith('.py')])
                    day_dirs.append((day_num, item, problems_count))
                    total_problems += problems_count
                except (ValueError, OSError):
                    continue
        
        if not day_dirs:
            print("Error: No day directories found")
            return
        
        # Sort day dirs by day number in descending order
        day_dirs.sort(key=lambda x: x[0], reverse=True)
        max_day = day_dirs[0][0]
        
        # Create header content
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        header_content = f"""# LeetCode Practice Tracker

This repository tracks my daily LeetCode practice problems.

## Progress

| Metric | Value |
|--------|-------|
| Total Problems | {total_problems} |
| Days Completed | {max_day} |
| Last Updated | {current_date} |

## Problems
"""
        
        # Create day sections
        day_sections = []
        
        for day_num, day_dir, _ in day_dirs:
            problems_in_dir = []
            for problem_file in os.listdir(os.path.join(practice_dir, day_dir)):
                if problem_file.endswith('.py'):
                    try:
                        with open(os.path.join(practice_dir, day_dir, problem_file), 'r', encoding='utf-8') as f:
                            content = f.read()
                            name_match = re.search(r'# LeetCode Problem: (.*)', content)
                            url_match = re.search(r'# URL: (.*)', content)
                            
                            if name_match and url_match:
                                name = name_match.group(1)
                                url = url_match.group(1)
                                
                                # Try to get difficulty from file
                                difficulty_match = re.search(r'# Difficulty: (.*)', content)
                                difficulty = difficulty_match.group(1) if difficulty_match else "Medium"
                                    
                                problems_in_dir.append({
                                    'name': name,
                                    'url': url,
                                    'difficulty': difficulty,
                                    'filename': problem_file
                                })
                    except:
                        continue
            
            if problems_in_dir:
                # Create the section content
                section_content = f"""
### Day {day_num}
 
| Problem | Difficulty | Solution |
|---------|------------|----------|
"""
                for problem in problems_in_dir:
                    section_content += f"| [{problem['name']}]({problem['url']}) | {problem['difficulty']} | [✅](practice/{day_dir}/{problem['filename']}) |\n"
                
                day_sections.append(section_content)
        
        # Create footer content
        footer_content = """
## About

This project organizes my LeetCode practice by day, tracking progress over time.
"""
        
        # Combine all parts
        updated_readme = header_content + ''.join(day_sections) + footer_content
        
        # Write updated README
        with open('readme.md', 'w', encoding='utf-8') as f:
            f.write(updated_readme)
        
        print(f"Successfully rebuilt README.md with {total_problems} problems across {max_day} days")
    except Exception as e:
        print(f"Error rebuilding README: {e}")


def update_file_header(file_path, problem_name, url, day, difficulty, date):
    """
    Update the header of a LeetCode solution file with standardized format.
    
    Args:
        file_path: Path to the solution file
        problem_name: Name of the LeetCode problem
        url: URL of the problem
        day: Day number
        difficulty: Problem difficulty
        date: Date for the header
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Find where the actual code starts (after header comments)
        lines = content.split('\n')
        code_start = 0
        for i, line in enumerate(lines):
            if not line.strip().startswith('#') and line.strip():
                code_start = i
                break
                
        actual_code = '\n'.join(lines[code_start:])
        
        # Create new header
        new_header = f"""# LeetCode Problem: {problem_name}
# URL: {url}
# Day: {day}
# Difficulty: {difficulty}
# Date: {date}
# Status: Solved

{actual_code}"""
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_header)
        return True
    except Exception as e:
        print(f"Error updating header for {file_path}: {e}")
        return False


def update_all_headers():
    """
    Update headers for all LeetCode solution files in the practice directory.
    
    Goes through each problem file and standardizes the header format.
    """
    base_dir = 'practice'
    start_date = datetime.datetime(2025, 4, 30)  # Day 1 date
    updated_count = 0
    failed_count = 0
    
    try:
        # Ensure the base directory exists
        if not os.path.exists(base_dir):
            print(f"Error: Practice directory '{base_dir}' not found")
            return
            
        for day_dir in os.listdir(base_dir):
            if day_dir.startswith('day_'):
                try:
                    day_num = int(day_dir.split('_')[1])
                    date = (start_date + timedelta(days=day_num-1)).strftime('%Y-%m-%d')
                    day_path = os.path.join(base_dir, day_dir)
                    
                    for file_name in os.listdir(day_path):
                        if file_name.endswith('.py'):
                            file_path = os.path.join(day_path, file_name)
                            
                            # Extract information from existing file
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                
                            # Default values
                            problem_name = ' '.join(word.capitalize() for word in file_name.replace('.py', '').split('_'))
                            url = ''
                            difficulty = 'Medium'  # default
                            
                            # Extract information from existing header if available
                            if '# LeetCode Problem:' in content:
                                problem_name = content.split('# LeetCode Problem:')[1].split('\n')[0].strip()
                            if '# URL:' in content:
                                url = content.split('# URL:')[1].split('\n')[0].strip()
                            if '# Difficulty:' in content:
                                difficulty = content.split('# Difficulty:')[1].split('\n')[0].strip()
                            
                            # Update the header
                            print(f"Updating header for {file_name}")
                            success = update_file_header(file_path, problem_name, url, day_num, difficulty, date)
                            if success:
                                updated_count += 1
                            else:
                                failed_count += 1
                                
                except (ValueError, OSError) as e:
                    print(f"Error processing directory {day_dir}: {e}")
    
        print(f"Header update complete: {updated_count} files updated, {failed_count} files failed")
    except Exception as e:
        print(f"Error updating headers: {e}")


def upload_to_github():
    """
    Upload changes to GitHub after rebuilding the README.
    
    This function:
    1. Rebuilds the README file
    2. Checks for git installation
    3. Checks if the current directory is a git repository
    4. Commits changes and pushes to GitHub
    """
    print("\nPreparing to upload to GitHub...")
    
    # First, rebuild the README
    print("Rebuilding README file...")
    rebuild_readme()
    
    # Generate day-specific READMEs
    print("Generating day-specific README files...")
    generate_all_day_readmes()
    
    try:
        # Check if git is installed
        try:
            subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except (subprocess.SubprocessError, FileNotFoundError):
            print("Error: Git is not installed or not available in PATH")
            return False
        
        # Check if we're in a git repository
        try:
            subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], 
                        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print("Error: Current directory is not a Git repository")
            return False
        
        # Check for changes
        result = subprocess.run(["git", "status", "--porcelain"], 
                              check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not result.stdout.strip():
            print("No changes to commit")
            return True
        
        # Add all changes
        print("Adding changes to git...")
        subprocess.run(["git", "add", "."], check=True)
        
        # Get commit message
        commit_msg = input("Enter commit message (default: 'Update LeetCode progress'): ").strip()
        if not commit_msg:
            commit_msg = "Update LeetCode progress"
        
        # Commit changes
        print(f"Committing changes with message: '{commit_msg}'")
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        
        # Get current branch
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], 
                              check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        current_branch = result.stdout.decode('utf-8').strip()
        
        # Confirm push
        push_confirm = input(f"Push to GitHub repository (branch: {current_branch})? [y/n]: ").strip().lower()
        if push_confirm != 'y':
            print("Push cancelled")
            return False
        
        # Push to GitHub
        print(f"Pushing changes to branch '{current_branch}'...")
        subprocess.run(["git", "push", "origin", current_branch], check=True)
        
        print("Successfully uploaded changes to GitHub!")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr.decode('utf-8')}")
        return False
    except Exception as e:
        print(f"Error uploading to GitHub: {e}")
        return False


class HTMLTextExtractor(HTMLParser):
    """HTML Parser class to extract text from HTML content"""
    def __init__(self):
        super().__init__()
        self.result = []
        self.in_script = False
        self.in_style = False
        
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'script':
            self.in_script = True
        elif tag.lower() == 'style':
            self.in_style = True
            
    def handle_endtag(self, tag):
        if tag.lower() == 'script':
            self.in_script = False
        elif tag.lower() == 'style':
            self.in_style = False
            
    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            self.result.append(data)
            
    def get_text(self):
        return ''.join(self.result)

def html_to_text(html):
    """Convert HTML to plain text"""
    extractor = HTMLTextExtractor()
    extractor.feed(html)
    return extractor.get_text()

def get_api_key(service_name="openai"):
    """
    Get API key for a service, prompting the user if not found in environment.
    
    Args:
        service_name: The name of the service (default: "openai")
        
    Returns:
        API key as string, or None if not available
    """
    env_var_name = f"{service_name.upper()}_API_KEY"
    api_key = os.environ.get(env_var_name)
    
    if not api_key:
        print(f"\nNo {service_name.upper()} API key found in environment variables.")
        print(f"You can set it permanently with:")
        print(f"  Windows: set {env_var_name}=your-api-key")
        print(f"  Linux/Mac: export {env_var_name}=your-api-key")
        
        choice = input(f"\nWould you like to enter your {service_name.capitalize()} API key now? (y/n): ").strip().lower()
        if choice == 'y':
            # Use getpass to hide the API key input
            api_key = getpass.getpass(f"Enter your {service_name.capitalize()} API key: ")
            if api_key:
                # Store temporarily in environment for this session
                os.environ[env_var_name] = api_key
                print(f"{service_name.capitalize()} API key has been temporarily set for this session.")
                return api_key
            else:
                print("No API key entered.")
                return None
        else:
            return None
    
    return api_key


def setup_api_keys():
    """
    Set up API keys for various services used by the script.
    
    This function handles API key setup for all integrated services.
    """
    keys_configured = {}
    
    # OpenAI API key
    openai_key = get_api_key("openai")
    keys_configured["OpenAI"] = bool(openai_key)
    
    # Add other API services here in the future
    
    # Summary
    print("\nAPI Keys Configuration:")
    for service, configured in keys_configured.items():
        status = "✅ Configured" if configured else "❌ Not configured"
        print(f"  {service}: {status}")
    
    return any(keys_configured.values())


def generate_detailed_explanation(problem_description, solution_code, difficulty, topics=None):
    """
    Generate a detailed explanation without requiring paid API services.
    
    This uses a rule-based approach to analyze the code and create a good explanation.
    
    Args:
        problem_description: The problem description
        solution_code: The solution code
        difficulty: Problem difficulty
        topics: List of topics related to the problem
        
    Returns:
        Dictionary with explanation sections
    """
    topics_str = ", ".join(topics) if topics and topics != [] else "none specified"
    
    # Extract algorithm patterns from the code
    patterns = analyze_solution_code(solution_code)
    
    # Determine the primary approach based on code analysis
    primary_approach = determine_approach(solution_code, patterns, difficulty)
    
    # Generate step-by-step explanation
    steps = generate_steps(solution_code, patterns, difficulty)
    
    # Analyze complexity
    time_complexity, space_complexity = analyze_complexity(solution_code, patterns)
    
    # Generate alternative approaches based on problem type
    alternatives = generate_alternatives(patterns, difficulty, topics)
    
    # Extract insights
    insights = generate_insights(patterns, difficulty, topics)
    
    return {
        "approach": primary_approach,
        "steps": steps,
        "time_complexity": time_complexity,
        "space_complexity": space_complexity,
        "alternatives": alternatives,
        "insights": insights
    }


def analyze_solution_code(code):
    """Analyze solution code to detect algorithm patterns"""
    patterns = []
    
    # Check for common patterns in the code
    if "def binary_search" in code or "left, right" in code or "mid = (left + right) // 2" in code:
        patterns.append("binary_search")
        
    if "def dfs" in code or "def depth_first" in code or "stack.append" in code or "stack.pop()" in code:
        patterns.append("depth_first_search")
        
    if "def bfs" in code or "def breadth_first" in code or "queue.append" in code or "queue.popleft()" in code:
        patterns.append("breadth_first_search")
        
    if "dynamic programming" in code.lower() or "dp = [" in code or "memo = {" in code or "@lru_cache" in code:
        patterns.append("dynamic_programming")
        
    if "heapq." in code or "heapify" in code or "heappush" in code or "heappop" in code:
        patterns.append("heap")
        
    if "def quick_sort" in code or "def merge_sort" in code or "def partition" in code:
        patterns.append("sorting")
    
    if "class Node" in code or "self.next" in code or "self.val" in code:
        patterns.append("linked_list")
        
    if "class TreeNode" in code or "self.left" in code or "self.right" in code:
        patterns.append("binary_tree")
        
    if "{" in code and "}" in code and ("[" not in code or "]" not in code):
        patterns.append("hash_map")
        
    if "Counter(" in code or "collections.Counter" in code:
        patterns.append("hash_map")
        
    if "sliding window" in code.lower() or ("left =" in code and "right =" in code and "while right <" in code):
        patterns.append("sliding_window")
        
    if ("two pointers" in code.lower() or 
        ("left =" in code and "right =" in code and ("while left < right" in code or "while left <= right" in code))):
        patterns.append("two_pointers")
        
    # If no specific pattern is detected, try to infer from variable names and operations
    if not patterns:
        if "total" in code or "sum" in code or "count" in code:
            patterns.append("iteration")
            
        if "result" in code or "res" in code:
            patterns.append("construction")
    
    return patterns


def determine_approach(code, patterns, difficulty):
    """Determine the primary approach from the code patterns"""
    if not patterns:
        if "easy" in difficulty.lower():
            return "This problem can be solved using a straightforward iterative approach. The solution carefully processes the input and constructs the required output."
        elif "medium" in difficulty.lower():
            return "This problem requires a methodical approach to handle different cases and edge conditions. The solution implements a careful algorithm to process the input efficiently."
        else:  # hard
            return "This challenging problem requires a sophisticated approach. The solution implements an optimized algorithm to handle the complex requirements efficiently."
    
    # Pattern-specific descriptions
    approach_descriptions = {
        "binary_search": "This problem is solved using a binary search approach. Binary search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half.",
        
        "depth_first_search": "This problem is solved using a depth-first search (DFS) approach. DFS explores as far as possible along each branch before backtracking, which is ideal for traversing or searching in tree or graph structures.",
        
        "breadth_first_search": "This problem is solved using a breadth-first search (BFS) approach. BFS explores all neighbor nodes at the present depth before moving to nodes at the next depth level, making it suitable for finding shortest paths in unweighted graphs.",
        
        "dynamic_programming": "This problem is solved using dynamic programming. This approach breaks down the problem into overlapping subproblems and stores the results of these subproblems to avoid redundant computations.",
        
        "heap": "This problem is solved using a heap data structure. Heaps are specialized tree-based structures that satisfy the heap property and are particularly useful for implementing priority queues.",
        
        "sorting": "This problem is solved using a sorting-based approach. Sorting the input data allows for more efficient processing and often simplifies the overall solution strategy.",
        
        "linked_list": "This problem involves manipulating a linked list structure. The solution navigates through the list nodes and performs the necessary operations to achieve the required result.",
        
        "binary_tree": "This problem involves operations on a binary tree. The solution traverses the tree structure and processes the nodes according to the problem requirements.",
        
        "hash_map": "This problem is solved using a hash map (dictionary) for efficient lookups. Hash maps provide O(1) average case time complexity for insertions, deletions, and lookups.",
        
        "sliding_window": "This problem is solved using a sliding window technique. This approach maintains a subset of items as a window that slides through the input, which is particularly efficient for problems involving subarrays or substring operations.",
        
        "two_pointers": "This problem is solved using a two-pointer technique. This approach uses two pointers that move through the array or string according to certain conditions, often reducing time complexity from O(n²) to O(n).",
        
        "iteration": "This problem is solved using careful iteration through the input. The solution tracks necessary values and builds the result incrementally.",
        
        "construction": "This problem involves constructing a result based on the given input. The solution processes the input and builds the required output following the problem specifications."
    }
    
    # Combine the descriptions for detected patterns
    if len(patterns) == 1:
        return approach_descriptions.get(patterns[0], "This problem is solved using a custom approach tailored to the specific requirements.")
    else:
        primary_pattern = patterns[0]
        approach = approach_descriptions.get(primary_pattern, "This problem is solved using multiple techniques.")
        approach += " The solution also incorporates "
        
        # Add secondary patterns
        secondary_patterns = [p for p in patterns[1:] if p in approach_descriptions]
        if secondary_patterns:
            secondary_descriptions = []
            for pattern in secondary_patterns:
                name = pattern.replace("_", " ")
                secondary_descriptions.append(name)
            
            if len(secondary_descriptions) == 1:
                approach += f"a {secondary_descriptions[0]} technique."
            else:
                last = secondary_descriptions.pop()
                approach += ", ".join(secondary_descriptions) + f" and {last} techniques."
        
        return approach


def generate_steps(code, patterns, difficulty):
    """Generate step-by-step explanation based on code patterns"""
    if "binary_search" in patterns:
        return """1. Initialize left and right pointers to the start and end of the array.
2. While left <= right, compute the middle index.
3. Compare the middle element with the target value.
4. If the middle element equals the target, return the index.
5. If the middle element is greater than the target, search the left half.
6. If the middle element is less than the target, search the right half.
7. If the element is not found, return an appropriate indicator."""
        
    elif "depth_first_search" in patterns:
        return """1. Define a DFS function to explore the structure.
2. Use a stack (or recursion) to keep track of nodes to visit.
3. For each node, process it and mark it as visited.
4. Explore all unvisited neighbors by adding them to the stack.
5. Continue until the stack is empty or the goal is reached."""
        
    elif "breadth_first_search" in patterns:
        return """1. Initialize a queue with the starting node(s).
2. While the queue is not empty, dequeue a node.
3. Process the node and mark it as visited.
4. Enqueue all unvisited neighbors of the current node.
5. Continue until the queue is empty or the goal is reached."""
        
    elif "dynamic_programming" in patterns:
        return """1. Define the state that needs to be stored in the DP table.
2. Formulate the base case(s) for the simplest subproblem(s).
3. Write the recurrence relation that relates the current state to previous states.
4. Decide on a bottom-up or top-down (memoization) approach.
5. Implement the solution by filling the DP table or using memoized recursion.
6. Extract the final answer from the completed table or memoization cache."""
        
    elif "heap" in patterns:
        return """1. Initialize a heap data structure.
2. Process the input data and add relevant elements to the heap.
3. Extract elements from the heap as needed, utilizing the heap's property to efficiently access the smallest (or largest) element.
4. Continue processing until the heap is empty or the goal is reached."""
        
    elif "sorting" in patterns:
        return """1. Apply a sorting algorithm to order the input data.
2. Process the sorted data to solve the problem efficiently.
3. The sorting step simplifies subsequent operations by providing a structured order to the elements."""
        
    elif "hash_map" in patterns:
        return """1. Initialize a hash map (dictionary) to store key-value pairs.
2. Process the input, utilizing the hash map for efficient lookups, insertions, and deletions.
3. The hash map provides O(1) average time complexity for these operations, making the overall solution efficient."""
        
    elif "sliding_window" in patterns:
        return """1. Initialize window boundaries (typically left and right pointers).
2. Expand the window by moving the right pointer to include more elements.
3. When certain conditions are met, contract the window by moving the left pointer.
4. Track the desired information during this process.
5. Continue until the right pointer reaches the end of the input."""
        
    elif "two_pointers" in patterns:
        return """1. Initialize two pointers, typically at different positions in the array or string.
2. Move the pointers according to specific conditions relevant to the problem.
3. Process elements at the pointer positions to build the solution.
4. Continue until the pointers meet or other termination conditions are satisfied."""
        
    else:
        # Generic steps based on difficulty
        if "easy" in difficulty.lower():
            return """1. Parse and validate the input data.
2. Initialize necessary variables and data structures.
3. Process the input using appropriate operations.
4. Build and return the required result."""
            
        elif "medium" in difficulty.lower():
            return """1. Analyze the problem requirements and edge cases.
2. Choose appropriate data structures for efficient operations.
3. Implement the core algorithm to process the input.
4. Handle edge cases and specific conditions.
5. Optimize the solution for better performance.
6. Build and return the required result."""
            
        else:  # hard
            return """1. Thoroughly analyze the problem's complexity and constraints.
2. Design an optimal algorithm using appropriate data structures.
3. Implement the solution with careful attention to edge cases.
4. Optimize critical sections for performance.
5. Ensure the solution handles all possible input scenarios.
6. Verify correctness with diverse test cases."""


def analyze_complexity(code, patterns):
    """Analyze time and space complexity based on code patterns"""
    time_complexity = "O(n) where n is the size of the input"
    space_complexity = "O(1) constant extra space"
    
    # Adjust complexity based on patterns
    if "binary_search" in patterns:
        time_complexity = "O(log n) where n is the size of the input array. Binary search divides the search space in half with each step."
        space_complexity = "O(1) constant extra space is used."
        
    elif "depth_first_search" in patterns or "breadth_first_search" in patterns:
        time_complexity = "O(V + E) where V is the number of vertices (nodes) and E is the number of edges in the graph or tree."
        space_complexity = "O(V) in the worst case, to store the visited nodes and the recursion stack or queue."
        
    elif "dynamic_programming" in patterns:
        time_complexity = "O(n²) where n is the size of the input. The solution uses dynamic programming to avoid redundant computations."
        space_complexity = "O(n) or O(n²) depending on the DP table dimensionality."
        
    elif "heap" in patterns:
        time_complexity = "O(n log n) where n is the number of elements processed through the heap."
        space_complexity = "O(n) to store elements in the heap."
        
    elif "sorting" in patterns:
        time_complexity = "O(n log n) where n is the size of the input, due to the sorting operation."
        space_complexity = "O(1) to O(n) depending on the sorting algorithm used."
        
    elif "sliding_window" in patterns:
        time_complexity = "O(n) where n is the size of the input. Each element is processed at most twice (once when entering the window, once when leaving)."
        space_complexity = "O(1) to O(k) where k is the maximum window size, depending on what information needs to be tracked."
        
    elif "two_pointers" in patterns:
        time_complexity = "O(n) where n is the size of the input. The solution traverses the input once with two pointers."
        space_complexity = "O(1) constant extra space since only two pointers are used."
        
    elif "hash_map" in patterns:
        time_complexity = "O(n) where n is the size of the input. Hash map operations are O(1) on average."
        space_complexity = "O(n) to store the hash map contents."
    
    # Check for nested loops
    if "for" in code and "for" in code[code.find("for")+3:]:
        # If there's a nested loop not part of the mentioned patterns
        if not any(p in patterns for p in ["dynamic_programming", "sorting"]):
            time_complexity = "O(n²) where n is the size of the input, due to the nested loops."
    
    return time_complexity, space_complexity


def generate_alternatives(patterns, difficulty, topics):
    """Generate alternative approaches based on patterns and topics"""
    alternatives = ""
    
    if "binary_search" in patterns:
        alternatives += "- A linear search approach could also work but would be less efficient with O(n) time complexity.\n"
        alternatives += "- A hash map could provide O(1) lookups but requires O(n) space and preprocessing time.\n"
        
    elif "depth_first_search" in patterns:
        alternatives += "- Breadth-first search (BFS) could be used instead, which might be preferable if finding the shortest path is a priority.\n"
        alternatives += "- An iterative approach with an explicit stack could replace the recursive implementation to avoid stack overflow for deep structures.\n"
        
    elif "breadth_first_search" in patterns:
        alternatives += "- Depth-first search (DFS) could be used instead, which might use less memory in some cases.\n"
        alternatives += "- A bidirectional BFS could be more efficient for certain path-finding problems.\n"
        
    elif "dynamic_programming" in patterns:
        alternatives += "- A recursive approach without memoization could be simpler but would likely exceed time limits due to redundant computations.\n"
        alternatives += "- A greedy algorithm might work for certain problems and would be more efficient, but wouldn't guarantee optimal results for all inputs.\n"
        
    elif "heap" in patterns:
        alternatives += "- Sorting the entire array and then accessing elements could work but would be less efficient for streaming data.\n"
        alternatives += "- A self-balancing binary search tree could provide similar functionality with different performance characteristics.\n"
        
    elif "sorting" in patterns:
        alternatives += "- Using a specialized data structure like a heap or balanced tree could be more efficient for specific operations.\n"
        alternatives += "- For small inputs or nearly sorted data, simpler sorting algorithms like insertion sort might be more efficient.\n"
        
    elif "hash_map" in patterns:
        alternatives += "- A sorted array with binary search could provide O(log n) lookups with potentially better space efficiency.\n"
        alternatives += "- A trie data structure could be more efficient for string-related problems.\n"
        
    elif "sliding_window" in patterns:
        alternatives += "- A brute force approach checking all possible subarrays/substrings would work but with O(n²) or O(n³) time complexity.\n"
        alternatives += "- Dynamic programming could be used for certain sliding window problems, trading space for potentially clearer implementation.\n"
        
    elif "two_pointers" in patterns:
        alternatives += "- A hash-based approach could work for many two-pointer problems, trading space for potentially simpler implementation.\n"
        alternatives += "- For sorted arrays, binary search techniques could replace certain two-pointer algorithms.\n"
    
    # If no specific alternatives added, provide general ones based on difficulty
    if not alternatives:
        if "easy" in difficulty.lower():
            alternatives += "- A brute force approach might be simpler to implement but less efficient.\n"
            alternatives += "- Using different data structures could simplify certain operations at the cost of added complexity.\n"
            
        elif "medium" in difficulty.lower():
            alternatives += "- A more space-efficient approach might be possible by optimizing the data structures used.\n"
            alternatives += "- A different algorithm paradigm (like divide-and-conquer or greedy) could provide a valid solution with different trade-offs.\n"
            
        else:  # hard
            alternatives += "- Multiple algorithm paradigms could be applied to this problem, each with different performance characteristics.\n"
            alternatives += "- Simplifying assumptions or preprocessing steps might lead to more efficient specialized solutions for certain input patterns.\n"
    
    return alternatives


def generate_insights(patterns, difficulty, topics):
    """Generate key insights based on patterns, difficulty and topics"""
    insights = ""
    
    # Pattern-specific insights
    if "binary_search" in patterns:
        insights += "- Binary search is most effective on sorted data and reduces the search space by half in each step.\n"
        insights += "- Always check boundary conditions and how to handle duplicates when implementing binary search.\n"
        
    elif "depth_first_search" in patterns or "breadth_first_search" in patterns:
        insights += "- Graph traversal algorithms require careful handling of visited nodes to avoid cycles.\n"
        insights += "- The choice between DFS and BFS depends on the problem requirements (depth exploration vs. shortest path).\n"
        
    elif "dynamic_programming" in patterns:
        insights += "- Identifying overlapping subproblems is the key to applying dynamic programming effectively.\n"
        insights += "- DP solutions can often be optimized for space by only keeping the necessary previous states.\n"
        
    elif "heap" in patterns:
        insights += "- Heaps are excellent for maintaining a collection where you frequently need to access the smallest/largest element.\n"
        insights += "- Consider using heaps for problems involving 'top k' elements or median finding.\n"
        
    elif "sorting" in patterns:
        insights += "- Sorting often simplifies subsequent operations and can reduce overall time complexity.\n"
        insights += "- Consider whether partial sorting or other data structures might be more efficient for the specific requirements.\n"
        
    elif "hash_map" in patterns:
        insights += "- Hash maps provide O(1) average-case lookups but require good hash functions to avoid collisions.\n"
        insights += "- Consider memory usage when using hash maps for large inputs.\n"
        
    elif "sliding_window" in patterns:
        insights += "- The sliding window technique is particularly effective for substring/subarray problems with constraints.\n"
        insights += "- Carefully define the window expansion and contraction criteria based on the problem constraints.\n"
        
    elif "two_pointers" in patterns:
        insights += "- Two-pointer techniques often reduce the time complexity from O(n²) to O(n).\n"
        insights += "- The approach is particularly useful for sorted arrays or when processing elements from both ends.\n"
    
    # Add general insights based on difficulty
    if "easy" in difficulty.lower():
        insights += "- Even simple problems benefit from a clear approach and clean implementation.\n"
        insights += "- Test edge cases like empty inputs, single elements, or maximum values.\n"
        
    elif "medium" in difficulty.lower():
        insights += "- Breaking down the problem into smaller steps often leads to a clearer solution.\n"
        insights += "- Consider the trade-offs between time complexity, space complexity, and code readability.\n"
        
    else:  # hard
        insights += "- Hard problems often require combining multiple techniques or creating custom data structures.\n"
        insights += "- Start with a working solution before optimizing for performance.\n"
    
    return insights


def enhance_with_ai(problem_description, solution_code, difficulty, topics=None):
    """Use AI to enhance the explanation for a problem solution."""
    try:
        # Determine which AI service to use
        ai_service = os.environ.get('LEETCODE_AI_SERVICE', 'local')
        
        # Use OpenAI if configured
        if ai_service == 'openai':
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                api_key = get_api_key('openai')
                if not api_key:
                    print("Using local explanation generation.")
                    return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)
            
            try:
                return enhance_with_openai(api_key, problem_description, solution_code, difficulty, topics)
            except Exception as e:
                if "quota" in str(e).lower() or "billing" in str(e).lower() or "capacity" in str(e).lower():
                    print(f"OpenAI API quota error: {e}")
                    print("Switching to local explanation generation.")
                    return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)
                raise
        
        # Use local implementation as default
        elif ai_service == 'local':
            return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)
        
        # If service not recognized, use local
        print(f"Warning: Unsupported AI service '{ai_service}'. Using local explanation generation.")
        return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)
            
    except Exception as e:
        print(f"Error using AI to enhance explanation: {e}")
        return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)


def enhance_with_openai(api_key, problem_description, solution_code, difficulty, topics=None):
    """Use OpenAI to enhance the explanation for a problem solution."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    topics_str = ", ".join(topics) if topics else "None specified"
    
    # Prepare the prompt for the model
    prompt = f"""
You are a professional algorithm expert helping explain a LeetCode problem solution.

Problem difficulty: {difficulty}
Problem topics: {topics_str}

Problem description:
{problem_description}

Solution code (Python):
```python
{solution_code}
```

Please provide a comprehensive explanation of this solution including:
1. A clear explanation of the approach used to solve this problem
2. A step-by-step breakdown of how the algorithm works
3. The time and space complexity analysis with justification
4. Any alternative approaches that could be used
5. Important insights and key takeaways from this problem

Format your response as a JSON with these keys:
- approach: A detailed explanation of the solution approach
- steps: Step-by-step breakdown of the algorithm
- time_complexity: Time complexity with explanation
- space_complexity: Space complexity with explanation
- alternatives: Alternative approaches
- insights: Key insights and takeaways
"""

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert algorithm teacher."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 1500
    }
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Try to parse JSON response
            try:
                explanation_data = json.loads(content)
                required_keys = ["approach", "steps", "time_complexity", "space_complexity", "alternatives", "insights"]
                for key in required_keys:
                    if key not in explanation_data:
                        explanation_data[key] = "Not provided by AI model"
                return explanation_data
            except json.JSONDecodeError:
                return extract_sections_from_text(content)
        else:
            print(f"Error from OpenAI API: {response.status_code} - {response.text}")
            return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)
            
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return generate_detailed_explanation(problem_description, solution_code, difficulty, topics)


def extract_sections_from_text(text):
    """Extract explanation sections from free-form text if JSON parsing failed"""
    sections = {
        "approach": "",
        "steps": "",
        "time_complexity": "",
        "space_complexity": "",
        "alternatives": "",
        "insights": ""
    }
    
    # Try to find sections using regex
    approach_match = re.search(r'(?:approach|solution approach):(.*?)(?=(?:steps|step-by-step|time complexity|$))', 
                              text, re.IGNORECASE | re.DOTALL)
    if approach_match:
        sections["approach"] = approach_match.group(1).strip()
        
    steps_match = re.search(r'(?:steps|step-by-step):(.*?)(?=(?:time complexity|space complexity|alternative|$))', 
                           text, re.IGNORECASE | re.DOTALL)
    if steps_match:
        sections["steps"] = steps_match.group(1).strip()
        
    time_match = re.search(r'time complexity:(.*?)(?=(?:space complexity|alternative|$))', 
                          text, re.IGNORECASE | re.DOTALL)
    if time_match:
        sections["time_complexity"] = time_match.group(1).strip()
        
    space_match = re.search(r'space complexity:(.*?)(?=(?:alternative|insights|key takeaway|$))', 
                           text, re.IGNORECASE | re.DOTALL)
    if space_match:
        sections["space_complexity"] = space_match.group(1).strip()
        
    alt_match = re.search(r'(?:alternative|other approach):(.*?)(?=(?:insights|key takeaway|$))', 
                         text, re.IGNORECASE | re.DOTALL)
    if alt_match:
        sections["alternatives"] = alt_match.group(1).strip()
        
    insights_match = re.search(r'(?:insights|key takeaway):(.*?)$', 
                              text, re.IGNORECASE | re.DOTALL)
    if insights_match:
        sections["insights"] = insights_match.group(1).strip()
    
    # If no sections were found, use the entire text as the approach
    if not any(sections.values()):
        sections["approach"] = text.strip()
    
    return sections


def generate_problem_explanation(problem_url, code_path, use_ai=True):
    """
    Generate a well-formatted markdown explanation file for a problem solution.
    
    Args:
        problem_url: URL of the LeetCode problem
        code_path: Path to the solution code file
        use_ai: Whether to use AI to enhance the explanation
    
    Returns:
        Path to the generated markdown file, or None if failed
    """
    try:
        # Extract problem slug from URL
        match = re.search(r'problems/([^/]+)', problem_url)
        if not match:
            print(f"Error: Could not extract problem slug from URL: {problem_url}")
            return None
        
        slug = match.group(1)
        
        # Create GraphQL query to get detailed problem information
        api_url = "https://leetcode.com/graphql"
        query = {
            "query": """
            query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    title
                    content
                    difficulty
                    topicTags {
                        name
                    }
                    hints
                    stats
                }
            }
            """,
            "variables": {"titleSlug": slug}
        }
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0',
            'Referer': 'https://leetcode.com'
        }
        
        print(f"Fetching problem details for {slug}...")
        
        # Send request to LeetCode API
        req = urllib.request.Request(
            api_url,
            data=json.dumps(query).encode('utf-8'),
            headers=headers
        )
        
        # Create SSL context that ignores certificate verification
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        with urllib.request.urlopen(req, context=ctx) as response:
            result = json.loads(response.read().decode('utf-8'))
            
            if 'data' in result and 'question' in result['data'] and result['data']['question']:
                question = result['data']['question']
                
                # Extract solution code
                with open(code_path, 'r', encoding='utf-8') as f:
                    solution_code = f.read()
                    
                # Extract actual solution (not comments)
                lines = solution_code.split('\n')
                code_start = 0
                for i, line in enumerate(lines):
                    if not line.strip().startswith('#') and line.strip():
                        code_start = i
                        break
                solution_code = '\n'.join(lines[code_start:])
                
                # Extract info from code file
                problem_name = ' '.join(word.capitalize() for word in os.path.basename(code_path).replace('.py', '').split('_'))
                difficulty = "Medium"  # Default
                if '# Difficulty:' in solution_code:
                    difficulty_match = re.search(r'# Difficulty: (.*)', solution_code)
                    if difficulty_match:
                        difficulty = difficulty_match.group(1)
                
                # Get problem details
                content = html_to_text(question['content']).strip() if 'content' in question else "No description available"
                
                # Extract topic tags
                topics = []
                if 'topicTags' in question and question['topicTags']:
                    topics = [tag['name'] for tag in question['topicTags']]
                
                # Create markdown file path (same dir as code file, but .md extension)
                md_filename = os.path.splitext(code_path)[0] + '.md'
                
                # Get explanation content - either AI-enhanced or template-based
                if use_ai and "OPENAI_API_KEY" in os.environ:
                    print(f"Enhancing explanation with AI...")
                    explanation = enhance_with_ai(content, solution_code, difficulty, topics)
                else:
                    explanation = generate_detailed_explanation(content, solution_code, difficulty, topics)
                
                # Generate the markdown content
                md_content = f"""# {problem_name}

## Problem Description

{content}

## Problem Details

- **Difficulty:** {difficulty}
- **URL:** {problem_url}
"""
                
                if topics:
                    md_content += "- **Topics:** " + ", ".join(topics) + "\n"
                
                md_content += f"""
## Solution Approach

{explanation["approach"]}

## Step-by-Step Explanation

{explanation["steps"]}

## Code Implementation

```python
{solution_code.strip()}
```

## Complexity Analysis

- **Time Complexity**: {explanation["time_complexity"]}
- **Space Complexity**: {explanation["space_complexity"]}

## Optimizations and Alternatives

{explanation["alternatives"]}

## Key Takeaways

{explanation["insights"]}
"""
                
                # Write to markdown file
                with open(md_filename, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                print(f"Generated explanation markdown: {md_filename}")
                return md_filename
            else:
                print(f"Error: Could not get problem details for {problem_url}")
                return None
                
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        return None
    except Exception as e:
        print(f"Error generating explanation: {e}")
        return None


def generate_all_explanations(use_ai=True):
    """Generate explanation markdown files for all solutions that don't have them."""
    # Check the current AI service configuration
    ai_service = os.environ.get('LEETCODE_AI_SERVICE', 'local')
    
    # If using OpenAI but no key is set, prompt to switch to local
    if ai_service == 'openai' and "OPENAI_API_KEY" not in os.environ:
        print("\nOpenAI service is selected but no API key is configured.")
        choice = input("Switch to local (free) explanation generation? (y/n): ").strip().lower()
        if choice == 'y' or choice == '':
            os.environ['LEETCODE_AI_SERVICE'] = 'local'
            print("Switched to local explanation generation.")
        else:
            # User wants to keep using OpenAI, so try to get the key
            api_key = get_api_key('openai')
            if not api_key:
                print("No API key provided. Operation cancelled.")
                return
    
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
    count_generated = 0
    count_failed = 0
    count_existing = 0
    
    try:
        for day_dir in os.listdir(practice_dir):
            if day_dir.startswith('day_'):
                day_path = os.path.join(practice_dir, day_dir)
                
                for filename in os.listdir(day_path):
                    if filename.endswith('.py'):
                        py_path = os.path.join(day_path, filename)
                        md_path = os.path.splitext(py_path)[0] + '.md'
                        
                        # Skip if markdown already exists
                        if os.path.exists(md_path):
                            count_existing += 1
                            continue
                        
                        # Extract URL from Python file
                        with open(py_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            url_match = re.search(r'# URL: (.*)', content)
                            
                            if url_match:
                                url = url_match.group(1).strip()
                                print(f"Generating explanation for {filename}...")
                                result = generate_problem_explanation(url, py_path, use_ai)
                                if result:
                                    count_generated += 1
                                else:
                                    count_failed += 1
                            else:
                                print(f"Skipping {filename}: No URL found in file")
                                count_failed += 1
        
        print(f"\nExplanation generation summary:")
        print(f"  Generated: {count_generated}")
        print(f"  Existing: {count_existing}")
        print(f"  Failed: {count_failed}")
    
    except Exception as e:
        print(f"Error generating explanations: {e}")


def regenerate_all_explanations(use_ai=True):
    """Regenerate explanation markdown files for ALL solutions, including existing ones."""
    # Check the current AI service configuration
    ai_service = os.environ.get('LEETCODE_AI_SERVICE', 'local')
    
    # If using OpenAI but no key is set, prompt to switch to local
    if ai_service == 'openai' and "OPENAI_API_KEY" not in os.environ:
        print("\nOpenAI service is selected but no API key is configured.")
        choice = input("Switch to local (free) explanation generation? (y/n): ").strip().lower()
        if choice == 'y' or choice == '':
            os.environ['LEETCODE_AI_SERVICE'] = 'local'
            print("Switched to local explanation generation.")
        else:
            # User wants to keep using OpenAI, so try to get the key
            api_key = get_api_key('openai')
            if not api_key:
                print("No API key provided. Operation cancelled.")
                return
    
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
    count_generated = 0
    count_failed = 0
    
    confirm = input("This will regenerate ALL explanation files, even existing ones. Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    try:
        for day_dir in os.listdir(practice_dir):
            if day_dir.startswith('day_'):
                day_path = os.path.join(practice_dir, day_dir)
                
                for filename in os.listdir(day_path):
                    if filename.endswith('.py'):
                        py_path = os.path.join(day_path, filename)
                        md_path = os.path.splitext(py_path)[0] + '.md'
                        
                        # Check if markdown exists and remove it before regenerating
                        if os.path.exists(md_path):
                            try:
                                os.remove(md_path)
                                print(f"Removed existing explanation for {filename}")
                            except Exception as e:
                                print(f"Warning: Could not remove existing file {md_path}: {e}")
                        
                        # Extract URL from Python file
                        with open(py_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            url_match = re.search(r'# URL: (.*)', content)
                            
                            if url_match:
                                url = url_match.group(1).strip()
                                print(f"Regenerating explanation for {filename}...")
                                result = generate_problem_explanation(url, py_path, use_ai)
                                if result:
                                    count_generated += 1
                                else:
                                    count_failed += 1
                            else:
                                print(f"Skipping {filename}: No URL found in file")
                                count_failed += 1
        
        print(f"\nExplanation regeneration summary:")
        print(f"  Generated: {count_generated}")
        print(f"  Failed: {count_failed}")
    
    except Exception as e:
        print(f"Error regenerating explanations: {e}")


def display_menu():
    """
    Display the main menu and get user choice.
    
    Returns:
        User's menu selection as a string ('1' to '11')
    """
    print("\n" + "=" * 60)
    print("   🏆 LEETCODE PRACTICE TRACKER 🏆")
    print("=" * 60)
    print("\n[1] Add new LeetCode problem(s)")
    print("[2] Update all headers")
    print("[3] Rebuild README file")
    print("[4] View statistics")
    print("[5] Generate problem explanations")
    print("[6] Regenerate ALL explanations")
    print("[7] Generate day-specific READMEs")
    print("[8] Configure API keys")
    print("[9] Select AI service")
    print("[10] Upload to GitHub")
    print("[11] Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-11): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 11.")
        except Exception:
            print("Invalid input. Please try again.")


def display_add_problem_menu():
    """
    Display the menu for adding problems and get user choice.
    
    Returns:
        User's selection as a string ('1' to '4')
    """
    print("\n" + "-" * 50)
    print("   ADD NEW LEETCODE PROBLEM")
    print("-" * 50)
    print("\n[1] Add problem interactively")
    print("[2] Add problem by URL")
    print("[3] Add problem with manual details")
    print("[4] Back to main menu")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception:
            print("Invalid input. Please try again.")


def get_day_number():
    """
    Get day number from user input.
    
    Returns:
        Integer day number or None to use the next available day
    """
    while True:
        try:
            day_input = input("Enter day number (leave empty to use next available day): ").strip()
            if not day_input:
                return None
            day = int(day_input)
            if day > 0:
                return day
            else:
                print("Day number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def view_statistics():
    """
    Display statistics about the LeetCode practice progress.
    
    Shows total problems, days completed, current streak, and difficulty breakdown.
    """
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
    try:
        # Initialize counters and data structures
        total_problems = 0
        total_days = 0
        difficulty_counts = {"Easy": 0, "Medium": 0, "Hard": 0, "Unknown": 0}
        day_dirs = []
        
        # Scan practice directory for problem files
        for item in os.listdir(practice_dir):
            if os.path.isdir(os.path.join(practice_dir, item)) and item.startswith('day_'):
                try:
                    day_num = int(item.split('_')[1])
                    problems_count = 0
                    
                    # Count problems and extract difficulty
                    for problem_file in os.listdir(os.path.join(practice_dir, item)):
                        if problem_file.endswith('.py'):
                            total_problems += 1
                            problems_count += 1
                            
                            # Extract difficulty from file header
                            with open(os.path.join(practice_dir, item, problem_file), 'r', encoding='utf-8') as f:
                                content = f.read()
                                difficulty_match = re.search(r'# Difficulty: (.*)', content)
                                
                                if difficulty_match:
                                    difficulty = difficulty_match.group(1).strip()
                                    if difficulty in ["Easy", "Medium", "Hard"]:
                                        difficulty_counts[difficulty] += 1
                                    else:
                                        difficulty_counts["Unknown"] += 1
                                else:
                                    difficulty_counts["Unknown"] += 1
                    
                    if problems_count > 0:
                        day_dirs.append(day_num)
                        total_days = max(total_days, day_num)
                except (ValueError, OSError):
                    continue
        
        # Calculate streaks
        if day_dirs:
            day_dirs.sort()
            current_streak = 1
            max_streak = 1
            last_day = day_dirs[0]
            
            for day in day_dirs[1:]:
                if day == last_day + 1:
                    current_streak += 1
                else:
                    current_streak = 1
                max_streak = max(max_streak, current_streak)
                last_day = day
        else:
            current_streak = 0
            max_streak = 0
        
        # Display statistics
        print("\n" + "=" * 60)
        print("   📊 LEETCODE PRACTICE STATISTICS 📊")
        print("=" * 60)
        
        print(f"\nTotal Days: {total_days}")
        print(f"Total Problems: {total_problems}")
        print(f"Current Streak: {current_streak} days")
        print(f"Longest Streak: {max_streak} days")
        
        # Show difficulty breakdown
        if total_problems > 0:
            print("\nDifficulty Breakdown:")
            for diff, count in difficulty_counts.items():
                if count > 0:
                    percentage = (count / total_problems) * 100
                    print(f"  - {diff}: {count} ({percentage:.1f}%)")
        
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"Error calculating statistics: {e}")
        input("\nPress Enter to continue...")


def menu_based_main():
    """Main function with menu-based approach."""
    # Default to local AI service
    if 'LEETCODE_AI_SERVICE' not in os.environ:
        os.environ['LEETCODE_AI_SERVICE'] = 'local'
    
    while True:
        choice = display_menu()
        
        # Handle menu options
        if choice == '1':  # Add new LeetCode problem(s)
            add_choice = display_add_problem_menu()
            
            if add_choice == '1':  # Interactive
                day = get_day_number()
                problems = []
                
                print("\nEnter problem details (leave empty to finish):")
                while True:
                    url = input("Problem URL (or leave empty to finish): ").strip()
                    if not url:
                        break
                    
                    details = fetch_problem_details(url)
                    
                    if details:
                        name = details['name']
                        difficulty = details['difficulty']
                        print(f"Found problem: {name} ({difficulty})")
                    else:
                        name = input("Problem name (e.g. 'Two Sum'): ").strip()
                        difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                    
                    suggested_filename = name.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace(".", "") + ".py"
                    filename = input(f"Filename [{suggested_filename}]: ").strip()
                    if not filename:
                        filename = suggested_filename
                        
                    problems.append({
                        'name': name,
                        'url': url,
                        'difficulty': difficulty,
                        'filename': filename
                    })
                    
                    if len(problems) >= 2:
                        another = input("Add another problem? (y/n): ").strip().lower()
                        if another != 'y':
                            break
                
                if problems:
                    update_leetcode_repo(problems, day)
                    
            elif add_choice == '2':  # By URL
                day = get_day_number()
                problems = []
                
                print("\nEnter problem URLs (one URL per line, leave empty to finish):")
                while True:
                    url = input("Problem URL: ").strip()
                    if not url:
                        break
                    
                    print(f"Fetching details for {url}...")
                    details = fetch_problem_details(url)
                    
                    if not details:
                        print(f"Skipping {url} due to error fetching details")
                        continue
                        
                    name = details['name']
                    difficulty = details['difficulty']
                    filename = name.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace(".", "") + ".py"
                    
                    problems.append({
                        'name': name,
                        'url': url,
                        'difficulty': difficulty,
                        'filename': filename
                    })
                    
                    print(f"Added problem: {name} ({difficulty})")
                
                if problems:
                    update_leetcode_repo(problems, day)
                    
            elif add_choice == '3':  # Manual details
                day = get_day_number()
                problems = []
                
                print("\nEnter problem details (leave empty to finish):")
                while True:
                    name = input("Problem name (or leave empty to finish): ").strip()
                    if not name:
                        break
                    
                    url = input("Problem URL: ").strip()
                    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                    
                    suggested_filename = name.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace(".", "") + ".py"
                    filename = input(f"Filename [{suggested_filename}]: ").strip()
                    if not filename:
                        filename = suggested_filename
                        
                    problems.append({
                        'name': name,
                        'url': url,
                        'difficulty': difficulty,
                        'filename': filename
                    })
                    
                    if len(problems) >= 2:
                        another = input("Add another problem? (y/n): ").strip().lower()
                        if another != 'y':
                            break
                
                if problems:
                    update_leetcode_repo(problems, day)
            
        elif choice == '2':  # Update all headers
            print("\nUpdating all headers...")
            update_all_headers()
            
        elif choice == '3':  # Rebuild README
            print("\nRebuilding README file...")
            rebuild_readme()
            
        elif choice == '4':  # View statistics
            view_statistics()
            
        elif choice == '5':  # Generate problem explanations
            print("\nGenerating problem explanations...")
            generate_all_explanations(True)
            
        elif choice == '6':  # Regenerate ALL explanations
            print("\nRegenerating ALL problem explanations...")
            regenerate_all_explanations(True)
            
        elif choice == '7':  # Generate day-specific READMEs
            print("\nGenerating day-specific README files...")
            generate_all_day_readmes()
            
        elif choice == '8':  # Configure API keys
            print("\nConfiguring API keys...")
            setup_api_keys()
            
        elif choice == '9':  # Select AI service
            print("\nSelecting AI service...")
            setup_ai_service()
            
        elif choice == '10':  # Upload to GitHub
            upload_to_github()
            
        elif choice == '11':  # Exit
            print("\nExiting LeetCode Practice Tracker. Happy coding!")
            break


def main():
    """Main entry point for the LeetCode Practice Tracker."""
    # Check if command-line arguments were provided
    if len(sys.argv) > 1:
        try:
            # Handle special commands
            if sys.argv[1] == "rebuild":
                rebuild_readme()
                return
                
            elif sys.argv[1] == "update-headers":
                update_all_headers()
                return
            
            # Handle other commands (add problems, etc.)
            # ... existing code for command-line mode ...
            
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Menu-driven mode
        try:
            menu_based_main()
        except KeyboardInterrupt:
            print("\n\nExiting LeetCode Practice Tracker. Happy coding!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()


def generate_day_readme(day_path, day_num):
    """
    Generate a README.md file for a specific day directory.
    
    Args:
        day_path: Path to the day directory
        day_num: Day number
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Collect problem files
        problems = []
        
        for filename in os.listdir(day_path):
            if filename.endswith('.py'):
                problem_path = os.path.join(day_path, filename)
                md_path = os.path.splitext(problem_path)[0] + '.md'
                has_explanation = os.path.exists(md_path)
                
                # Extract info from Python file
                with open(problem_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    name_match = re.search(r'# LeetCode Problem: (.*)', content)
                    url_match = re.search(r'# URL: (.*)', content)
                    difficulty_match = re.search(r'# Difficulty: (.*)', content)
                    
                    problem_name = name_match.group(1).strip() if name_match else os.path.splitext(filename)[0].replace('_', ' ').title()
                    url = url_match.group(1).strip() if url_match else ""
                    difficulty = difficulty_match.group(1).strip() if difficulty_match else "Medium"
                
                problems.append({
                    'name': problem_name,
                    'filename': filename,
                    'url': url,
                    'difficulty': difficulty,
                    'has_explanation': has_explanation
                })
        
        # Sort problems alphabetically
        problems.sort(key=lambda x: x['name'])
        
        # Create README content
        content = f"""# Day {day_num} - LeetCode Problems

This directory contains solutions to the following LeetCode problems:

| Problem | Difficulty | Solution | Explanation |
|---------|------------|----------|-------------|
"""
        
        # Add problem entries
        for problem in problems:
            solution_link = f"[Code]({problem['filename']})"
            explanation_link = f"[Explanation]({os.path.splitext(problem['filename'])[0] + '.md'})" if problem['has_explanation'] else "N/A"
            
            content += f"| [{problem['name']}]({problem['url']}) | {problem['difficulty']} | {solution_link} | {explanation_link} |\n"
        
        # Add footer with correct GitHub link
        content += f"""
## Daily Progress

Each solution includes:
- Complete Python implementation
- Problem description and constraints
- Time and space complexity analysis

Created with [LeetCode Practice Tracker](https://github.com/AnuranjanJain/solutions)
"""
        
        # Write README file
        readme_path = os.path.join(day_path, 'README.md')
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True
    
    except Exception as e:
        print(f"Error generating README for day {day_num}: {e}")
        return False


def generate_all_day_readmes():
    """
    Generate README.md files for all day directories.
    
    This creates a nicely formatted README in each day folder that links
    to both the code files and explanation markdown files.
    """
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
    success_count = 0
    failed_count = 0
    
    try:
        for day_dir in sorted(os.listdir(practice_dir)):
            if day_dir.startswith('day_'):
                try:
                    day_num = int(day_dir.split('_')[1])
                    day_path = os.path.join(practice_dir, day_dir)
                    
                    print(f"Generating README for {day_dir}...")
                    if generate_day_readme(day_path, day_num):
                        success_count += 1
                    else:
                        failed_count += 1
                        
                except (ValueError, OSError) as e:
                    print(f"Error processing directory {day_dir}: {e}")
                    failed_count += 1
        
        print(f"\nDay README generation summary:")
        print(f"  Successful: {success_count}")
        print(f"  Failed: {failed_count}")
    
    except Exception as e:
        print(f"Error generating day READMEs: {e}")


def setup_ai_service():
    """Set up the AI service to use for generating explanations"""
    print("\n" + "=" * 60)
    print("   🤖 AI SERVICE CONFIGURATION 🤖")
    print("=" * 60)
    print("\nAvailable AI services:")
    print("  [1] Local (Free, Code Analysis Based)")
    print("  [2] OpenAI (Requires API Key)")
    
    current_service = os.environ.get('LEETCODE_AI_SERVICE', 'local')
    print(f"\nCurrent service: {current_service}")
    
    choice = input("\nSelect AI service (1-2): ").strip()
    
    if choice == '1':
        os.environ['LEETCODE_AI_SERVICE'] = 'local'
        print("AI service set to: local (free)")
        return True
    elif choice == '2':
        os.environ['LEETCODE_AI_SERVICE'] = 'openai'
        print("AI service set to: OpenAI")
        
        # Check for API key
        if 'OPENAI_API_KEY' not in os.environ:
            return get_api_key('openai') is not None
        return True
    else:
        print("Invalid choice. No changes made.")
        return False


if __name__ == "__main__":
    main() 
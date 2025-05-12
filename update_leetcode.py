#!/usr/bin/env python3
"""
LeetCode Practice Tracker

A tool to manage LeetCode practice problems, track progress, and maintain
a well-organized repository of solutions.

Features:
- Add new LeetCode problems (interactively or by URL)
- Update file headers consistently
- Rebuild README with current progress
- View statistics about your practice
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


def display_menu():
    """
    Display the main menu and get user choice.
    
    Returns:
        User's menu selection as a string ('1' to '6')
    """
    print("\n" + "=" * 60)
    print("   🏆 LEETCODE PRACTICE TRACKER 🏆")
    print("=" * 60)
    print("\n[1] Add new LeetCode problem(s)")
    print("[2] Update all headers")
    print("[3] Rebuild README file")
    print("[4] View statistics")
    print("[5] Upload to GitHub")
    print("[6] Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
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
    """
    Main function with menu-based approach.
    
    Provides an interactive menu for managing LeetCode practice problems.
    """
    while True:
        choice = display_menu()
        
        # [1] Add new LeetCode problem(s)
        if choice == '1':  
            add_choice = display_add_problem_menu()
            
            # [1] Add problem interactively
            if add_choice == '1':
                day = get_day_number()
                problems = []
                
                print("\nEnter problem details (leave empty to finish):")
                while True:
                    # Ask for URL first
                    url = input("Problem URL (or leave empty to finish): ").strip()
                    if not url:
                        break
                    
                    # Try to fetch problem details
                    details = fetch_problem_details(url)
                    
                    if details:
                        name = details['name']
                        difficulty = details['difficulty']
                        print(f"Found problem: {name} ({difficulty})")
                    else:
                        # If fetch failed, ask for details manually
                        name = input("Problem name (e.g. 'Two Sum'): ").strip()
                        difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                    
                    # Generate filename from problem name
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
                    
            # [2] Add problem by URL
            elif add_choice == '2':
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
            
            # [3] Add problem with manual details
            elif add_choice == '3':
                day = get_day_number()
                problems = []
                
                print("\nEnter problem details (leave empty to finish):")
                while True:
                    name = input("Problem name (or leave empty to finish): ").strip()
                    if not name:
                        break
                    
                    url = input("Problem URL: ").strip()
                    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                    
                    # Generate filename from problem name
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
            
        # [2] Update all headers
        elif choice == '2':
            print("\nUpdating all headers...")
            update_all_headers()
            
        # [3] Rebuild README
        elif choice == '3':
            print("\nRebuilding README file...")
            rebuild_readme()
            
        # [4] View statistics
        elif choice == '4':
            view_statistics()
            
        # [5] Upload to GitHub
        elif choice == '5':
            upload_to_github()
            
        # [6] Exit
        elif choice == '6':
            print("\nExiting LeetCode Practice Tracker. Happy coding!")
            break


def main():
    """
    Main entry point for the LeetCode Practice Tracker.
    
    Handles both command-line and menu-driven modes.
    """
    # Check if command-line arguments were provided
    if len(sys.argv) > 1:
        # Command line mode
        try:
            # Special commands
            if sys.argv[1] == "rebuild":
                rebuild_readme()
                return
                
            elif sys.argv[1] == "update-headers":
                update_all_headers()
                return
                
            # Process other command-line options
            problems = []
            custom_day = None
            
            # Check for day parameter
            for i, arg in enumerate(sys.argv):
                if arg.startswith("--day="):
                    try:
                        custom_day = int(arg.split("=")[1])
                        sys.argv.pop(i)  # Remove the day parameter from args
                        break
                    except (IndexError, ValueError):
                        print("Error: Invalid day parameter format. Use --day=number")
                        return
            
            # Interactive mode
            if sys.argv[1] == "interactive":
                print("Enter problem details (leave empty to finish):")
                while True:
                    # Ask for URL first
                    url = input("Problem URL (or leave empty to finish): ").strip()
                    if not url:
                        break
                    
                    # Try to fetch problem details
                    details = fetch_problem_details(url)
                    
                    if details:
                        name = details['name']
                        difficulty = details['difficulty']
                        print(f"Found problem: {name} ({difficulty})")
                    else:
                        # If fetch failed, ask for details manually
                        name = input("Problem name (e.g. 'Two Sum'): ").strip()
                        difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                    
                    # Generate filename from problem name
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
                        
                # Check for day parameter in interactive mode
                if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
                    try:
                        custom_day = int(sys.argv[2])
                    except ValueError:
                        print("Error: Day parameter must be a number")
                        return
            
            # URL mode            
            elif sys.argv[1] == "url":
                # Process URLs provided as arguments
                urls = [arg for arg in sys.argv[2:] if not arg.startswith("--")]
                
                if not urls:
                    print("Error: Please provide at least one URL")
                    return
                
                for url in urls:
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
            
            # LeetCode URL direct input
            elif "leetcode.com/problems/" in sys.argv[1]:
                urls = [arg for arg in sys.argv[1:] if "leetcode.com/problems/" in arg and not arg.startswith("--")]
                
                if not urls:
                    print("Error: No valid LeetCode URLs found")
                    return
                    
                for url in urls:
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
            
            # Manual problem specification
            else:
                # Parse problems from command line arguments
                for arg in sys.argv[1:]:
                    if arg.startswith("--"):
                        break
                        
                    parts = arg.split(',')
                    if len(parts) != 4:
                        print(f"Error: Invalid problem format: {arg}")
                        print("Expected format: problem_name,url,difficulty,filename")
                        return
                        
                    problems.append({
                        'name': parts[0],
                        'url': parts[1],
                        'difficulty': parts[2],
                        'filename': parts[3]
                    })
            
            if not problems:
                print("No problems specified.")
                return
                
            update_leetcode_repo(problems, custom_day)
        
        except Exception as e:
            print(f"Error processing command-line arguments: {e}")
    
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
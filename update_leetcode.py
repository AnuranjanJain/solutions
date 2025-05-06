#!/usr/bin/env python3
import os
import re
import sys
import json
import datetime
import urllib.request
import urllib.error
import ssl


def fetch_problem_details(url):
    """
    Fetch problem details from LeetCode URL using the LeetCode API.
    
    Args:
        url: LeetCode problem URL
    
    Returns:
        Dictionary with keys 'name', 'difficulty', or None if failed
    """
    try:
        # Extract problem title slug from URL
        match = re.search(r'problems/([^/]+)', url)
        if not match:
            print(f"Error: Could not extract problem slug from URL: {url}")
            return None
        
        slug = match.group(1)
        
        # Create a request to the LeetCode GraphQL API
        api_url = "https://leetcode.com/graphql"
        query = {
            "query": """
            query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    title
                    difficulty
                    content
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
    # Read the current README.md
    with open('readme.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Parse current progress
    total_problems_match = re.search(r'\| Total Problems \| (\d+) \|', readme_content)
    days_completed_match = re.search(r'\| Days Completed \| (\d+) \|', readme_content)
    
    if not total_problems_match or not days_completed_match:
        print("Error: Could not parse progress metrics from README")
        return
    
    total_problems = int(total_problems_match.group(1))
    days_completed = int(days_completed_match.group(1))
    
    # Update progress metrics
    new_total_problems = total_problems + len(problems)
    
    # Use custom day if provided, otherwise increment current value
    if custom_day is not None:
        new_days_completed = max(custom_day, days_completed)
    else:
        new_days_completed = days_completed + 1
        
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create new day directory
    new_day = f"day_{custom_day if custom_day is not None else new_days_completed}"
    new_day_path = os.path.join("practice", new_day)
    os.makedirs(new_day_path, exist_ok=True)
    
    # Create new day section content
    new_day_section = f"""
### Day {custom_day if custom_day is not None else new_days_completed}
 
| Problem | Difficulty | Solution |
|---------|------------|----------|
"""
    
    # Add problem entries
    for problem in problems:
        problem_name = problem['name']
        problem_url = problem['url']
        difficulty = problem['difficulty']
        filename = problem['filename']
        
        # Create empty solution file if it doesn't exist
        solution_path = os.path.join(new_day_path, filename)
        if not os.path.exists(solution_path):
            with open(solution_path, 'w', encoding='utf-8') as f:
                f.write(f"# Solution for {problem_name}\n# {problem_url}\n\n")
        
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
    
    # Start over with a clean README
    # Extract header (before Problems section) and footer (About section)
    header_match = re.search(r'(.*?)## Problems', readme_content, re.DOTALL)
    footer_match = re.search(r'## About.*', readme_content, re.DOTALL)
    
    if not header_match or not footer_match:
        print("Error: Could not parse README structure")
        return
    
    header = header_match.group(1) + "## Problems\n"
    footer = footer_match.group(0)
    
    # Find all existing day sections using directory structure
    day_sections = []
    
    # Add the new day section
    day_sections.append((custom_day if custom_day is not None else new_days_completed, new_day_section))
    
    # Find existing day sections from the README
    existing_sections = re.findall(r'### Day (\d+)[\s\S]*?(?=### Day \d+|\n## About)', readme_content + "\n## About")
    
    # Process existing sections
    for section in existing_sections:
        # Extract day number and content
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
    
    # Also check the practice directory for any missing days
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if os.path.exists(practice_dir):
        for item in os.listdir(practice_dir):
            if os.path.isdir(os.path.join(practice_dir, item)) and item.startswith('day_'):
                try:
                    day_num = int(item.split('_')[1])
                    # Check if this day is already in our sections
                    if not any(d[0] == day_num for d in day_sections):
                        # Create a new section for this day
                        problems_in_dir = []
                        for problem_file in os.listdir(os.path.join(practice_dir, item)):
                            if problem_file.endswith('.py'):
                                with open(os.path.join(practice_dir, item, problem_file), 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    name_match = re.search(r'# Solution for (.*)', content)
                                    url_match = re.search(r'# (https://leetcode.com/problems/.*?)/', content)
                                    
                                    if name_match and url_match:
                                        name = name_match.group(1)
                                        url = url_match.group(1) + '/'
                                        # Make a guess at difficulty
                                        difficulty = "Medium"
                                        problems_in_dir.append({
                                            'name': name,
                                            'url': url,
                                            'difficulty': difficulty,
                                            'filename': problem_file
                                        })
                        
                        if problems_in_dir:
                            # Create the section content
                            section_content = f"""
### Day {day_num}
 
| Problem | Difficulty | Solution |
|---------|------------|----------|
"""
                            for problem in problems_in_dir:
                                section_content += f"| [{problem['name']}]({problem['url']}) | {problem['difficulty']} | [✅](practice/{item}/{problem['filename']}) |\n"
                            
                            day_sections.append((day_num, section_content))
                except ValueError:
                    continue
    
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


def rebuild_readme():
    """
    Rebuild the entire README.md file based on the practice directory structure.
    This helps fix any inconsistencies that might have occurred.
    """
    practice_dir = os.path.join(os.getcwd(), 'practice')
    if not os.path.exists(practice_dir):
        print("Error: Practice directory not found")
        return
    
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
                        name_match = re.search(r'# Solution for (.*)', content)
                        url_match = re.search(r'# (https://leetcode.com/problems/.*?)($|\n)', content)
                        
                        if name_match and url_match:
                            name = name_match.group(1)
                            url = url_match.group(1)
                            
                            # Try to get difficulty from LeetCode API
                            try:
                                details = fetch_problem_details(url)
                                difficulty = details['difficulty'] if details else "Medium"
                            except:
                                difficulty = "Medium"  # Default if can't determine
                                
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


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python update_leetcode.py interactive [day_number]")
        print("  python update_leetcode.py url <url1> <url2> ... [--day=day_number]")
        print("  python update_leetcode.py problem_name1,url1,difficulty1,filename1 ... [--day=day_number]")
        print("  python update_leetcode.py rebuild")
        return
    
    # Special command to rebuild the README
    if sys.argv[1] == "rebuild":
        rebuild_readme()
        return
    
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
                
    elif sys.argv[1] == "url":
        # Process URLs provided as arguments
        urls = []
        for i, arg in enumerate(sys.argv[2:], 2):
            if arg.startswith("--"):
                break
            urls.append(arg)
            
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
    # Check if the first argument looks like a LeetCode URL
    elif "leetcode.com/problems/" in sys.argv[1]:
        urls = []
        # Collect all LeetCode URLs from command line arguments
        for arg in sys.argv[1:]:
            if arg.startswith("--"):
                break
            if "leetcode.com/problems/" in arg:
                urls.append(arg)
        
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


if __name__ == "__main__":
    main() 
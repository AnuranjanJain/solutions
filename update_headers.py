import os
from datetime import datetime, timedelta

def update_file_header(file_path, problem_name, url, day, difficulty, date):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Remove existing header comments
    lines = content.split('\n')
    code_start = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith('#') and line.strip():
            code_start = i
            break
            
    actual_code = '\n'.join(lines[code_start:])
    
    new_header = f"""# LeetCode Problem: {problem_name}
# URL: {url}
# Day: {day}
# Difficulty: {difficulty}
# Date: {date}
# Status: Solved
# Solution for {problem_name}
# {url}

{actual_code}"""
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_header)

def main():
    base_dir = 'practice'
    start_date = datetime(2025, 4, 30)  # Day 1 date
    
    for day_dir in os.listdir(base_dir):
        if day_dir.startswith('day_'):
            day_num = int(day_dir.split('_')[1])
            date = (start_date + timedelta(days=day_num-1)).strftime('%Y-%m-%d')
            day_path = os.path.join(base_dir, day_dir)
            
            for file_name in os.listdir(day_path):
                if file_name.endswith('.py'):
                    file_path = os.path.join(day_path, file_name)
                    
                    # Read existing content to extract problem name and URL
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Extract problem name from filename
                    problem_name = ' '.join(word.capitalize() for word in file_name.replace('.py', '').split('_'))
                    
                    # Extract URL and difficulty from existing content
                    url = ''
                    difficulty = 'Medium'  # default
                    
                    # Try to extract from existing header first
                    if '# LeetCode Problem:' in content:
                        problem_name = content.split('# LeetCode Problem:')[1].split('\n')[0].strip()
                    if '# URL:' in content:
                        url = content.split('# URL:')[1].split('\n')[0].strip()
                    if '# Difficulty:' in content:
                        difficulty = content.split('# Difficulty:')[1].split('\n')[0].strip()
                    
                    print(f"Updating header for {file_name}")
                    update_file_header(file_path, problem_name, url, day_num, difficulty, date)

if __name__ == "__main__":
    main()
    print("All headers updated successfully!")
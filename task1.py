import os
def total_salary(path):
    total_sum = 0
    developer_count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() 
                if not line:
                    continue
                
                try:
                    _, salary_str = line.split(',')
                    salary = int(salary_str)
                    total_sum += salary
                    developer_count += 1
                except ValueError:
                    return (0, 0)

    except FileNotFoundError:
        return (0, 0)
    except IOError:
        return (0, 0)

    average_salary = total_sum / developer_count if developer_count > 0 else 0
    
    return (total_sum, average_salary)

# створюємо файл з даними по ЗП

file_path = "salary_file.txt"
file_content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(file_content)

total, average = total_salary(file_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Тестування з відсутнім файлом
total_err, average_err = total_salary("non_existent_file.txt")

os.remove(file_path)
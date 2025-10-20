import os

def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() 
                if not line:
                    continue
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    continue
                
    except FileNotFoundError:
        print(f"❌ Помилка: Файл за шляхом '{path}' не знайдено.")
        return []

    return cats_list

file_path = "cats_file.txt"
file_content = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Invalid_Line_Format"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(file_content)

print("--- Тестування з існуючим файлом ---")
cats_info = get_cats_info(file_path)
print(cats_info)

print("\n--- Тестування з неіснуючим файлом ---")
error_info = get_cats_info("non_existent_cats.txt")
print(f"Повернений список у разі помилки: {error_info}")

os.remove(file_path)
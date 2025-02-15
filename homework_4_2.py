def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    try:
                        age = int(age) #Converting age to number
                        cats_list.append({"id": cat_id, "name": name, "age": age})
                    except ValueError:
                        print(f"Invalid age format for cat {name}")
                        continue

    except FileNotFoundError:
        print(f"File {path} not found.")
    except Exception as e:
        print(f"Error: {e}")
    return cats_list



#Test
cats_info = get_cats_info("/Users/ruslana/Desktop/homework_module_4/cats_file.txt")
print(cats_info)


def total_salary(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    print (f'Incorrect format: {line.strip()}')
                    continue #Skip incorrect line
                try:
                    salary = float(parts[1]) #Converter salary to number
                    salaries.append(salary)
                except ValueError:
                    print (f'Invalid salary value: {parts[1]} in line {line.strip() }')
                    continue #Skip incorrect line
        if not salaries:
            return 0, 0



        total = sum(salaries)
        average = total / len(salaries)


        return total, average


    except FileNotFoundError:
        print(f"File not found.")
        return None #Returns None if file not found

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
#Test
total, average = total_salary("/Users/ruslana/Desktop/homework_module_4/salaries.txt")

if total is not None:
    print(f"Total salary:{total}, Average salary: {average}")
else:
    print("Error")

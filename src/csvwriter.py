def write(list, path="ouput.csv"):
    with open(path, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(list)

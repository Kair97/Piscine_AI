# csv_content = '''name;country;description;score
# Alice;Kazakhstan;"Expert in ML, NLP";92.5
# Bob;France;"Generalist";
# Carol;Germany;"Deep learning, CV specialist";88.0'''

# with open("messy.csv", "w", encoding="utf-8") as f:
#     f.write(csv_content)

# print("messy.csv created successfully!")

import csv 

with open("messy.csv", 'r', encoding='utf-8') as f :
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        name = row["name"]
        description = row["description"]
        score = row["score"]

        if score.strip() == "":
            score = "N/A"
        
        print(f"{name} | {description} | {score}")

print("\nsecond task\n")

def normalize_csv(input_path, output_path):
    cleaned_rows = []

    with open(input_path, 'r', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in, delimiter=";")

        headers = reader.fieldnames

        for row in reader:
            if row["score"] == "":
                row["score"] = 0
            cleaned_rows.append(row)
    with open(output_path, 'w', encoding='utf-8') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=headers)

        writer.writeheader()
        writer.writerows(cleaned_rows)

normalize_csv("messy.csv", "clean.csv")

with open("clean.csv", 'r', encoding='utf-8', newline="") as f:
    print(f.read())
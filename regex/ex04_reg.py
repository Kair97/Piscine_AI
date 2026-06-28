import re 

text = "Order #12345 placed on 2024-03-15 for $149.99"

match = re.search(r"\d+", text)
if match:
    print(f"Match: {match.group()} at position {match.start()}-{match.end()}")

all = re.findall(r"\d+", text)
print(f"All numbers: {all}")

entries = [
    "[ERROR] Connection refused",
    "[INFO] Server started on port 8080",
    "[WARNING] Disk usage at 85%",
    "[ERROR] Timeout after 30s",
]

for ent in entries:
    m = re.search(r"ERROR\]\s+(.*)", ent)

    if m:
        print(m.group(1))

text = "Contact alice@example.com or bob.smith@company.org for support."
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
for match in re.finditer(email_pattern, text):
    print(f"{match.group()} ({match.start()}-{match.end()})")
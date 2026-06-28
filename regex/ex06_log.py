import re

# log_content = """2024-03-15 09:01:23 INFO  Server started on port 8080
# 2024-03-15 09:02:11 INFO  Connected to database
# 2024-03-15 09:05:44 ERROR Failed to parse config: unexpected token at line 7
# 2024-03-15 09:07:02 WARNING Disk usage at 87%
# 2024-03-15 09:12:30 ERROR Timeout connecting to cache (attempt 1/3)
# 2024-03-15 09:12:35 ERROR Timeout connecting to cache (attempt 2/3)
# 2024-03-15 09:12:40 ERROR Timeout connecting to cache (attempt 3/3)
# 2024-03-15 09:15:00 INFO  Cache connection restored"""

# with open("app.log", "w", encoding="utf-8") as f:
#     f.write(log_content)

def parse_log(filepath):
    log_pattern = re.compile(
        r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(?P<level>[A-Z]+)\s+(?P<message>.*)$"
    )
    entries = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = log_pattern.match(line.strip())
            if match:
                entries.append(match.groupdict())
    return entries

parsed_entries = parse_log("app.log")

for entry in parsed_entries:
    print(f"{entry['timestamp']} | {entry['level']:<7} | {entry['message']}")

print()

def summarize_log(entries):
    summary = {}
    for entry in entries:
        level = entry["level"]
        summary[level] = summary.get(level, 0) + 1
    return summary

log_summary = summarize_log(parsed_entries)
print(log_summary)

print()

def extract_errors(entries):
    return [entry["message"] for entry in entries if entry["level"] == "ERROR"]

error_messages = extract_errors(parsed_entries)
for err in error_messages:
    print(err)
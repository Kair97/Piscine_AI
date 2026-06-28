import re 

date_str = "28/06/2026"
date_pattern = r"(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})"
match_date = re.match(date_pattern, date_str)

if match_date:
    reformatted = f"{match_date.group('year')}-{match_date.group('month')}-{match_date.group('day')}"
    print(reformatted)

print()

text_cards = "Card 4111 1111 1111 1111 charged. Backup: 5500-0000-0000-0004 failed."
card_pattern = r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}"
redacted = re.sub(card_pattern, "****-****-****-****", text_cards)
print(redacted)

print()

lines = [
    "def calculate_mean(values):",
    "    total = sum(values)",
    "def variance(data, ddof=0):",
    "class Stats:",
    "def mode(items):",
]

func_pattern = re.compile(r"^def\s+([a-zA-Z_]\w*)\s*\(")
for line in lines:
    m = func_pattern.search(line.strip())
    if m:
        print(m.group(1))
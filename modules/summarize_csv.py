import argparse
import sys
from collections import Counter

# 1. Setup our Argument Parser configuration blueprint
parser = argparse.ArgumentParser(description="A tool to summarize columns from a CSV file.")
parser.add_argument("filepath", help="Path to the target CSV file")
parser.add_argument("--column", default=None, help="The column name to summarize")
parser.add_argument("--top", type=int, default=5, help="Number of top common values to print")
parser.add_argument("--version", action="version", version="summarize_csv v1.0")

# 2. Execute parsing to capture terminal parameters
args = parser.parse_args()

# 3. Read the file into memory lines
lines = []
try:
    with open(args.filepath, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                lines.append(cleaned_line.split(','))
except FileNotFoundError:
    print(f"Error: The file '{args.filepath}' does not exist.", file=sys.stderr)
    sys.exit(1)

# 4. Separate headers from data rows
headers = lines[0]
data_rows = lines[1:]

# 5. Resolve target column tracking index
if args.column is None:
    col_index = 0
    column_name = headers[0]
else:
    if args.column not in headers:
        print(f"Error: Column '{args.column}' not found in CSV headers.", file=sys.stderr)
        sys.exit(1)
    col_index = headers.index(args.column)
    column_name = args.column

# 6. Extract data values and map count frequencies
column_values = []
for row in data_rows:
    if col_index < len(row):
        column_values.append(row[col_index])

value_counts = Counter(column_values)
top_results = value_counts.most_common(args.top)

# 7. Print the cleanly formatted metrics report
print(f"Column: {column_name} | Top {args.top} values")
for item, count in top_results:
    print(f"{item}: {count}")
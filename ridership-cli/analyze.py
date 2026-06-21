import argparse
import csv
from pathlib import Path
import sys 
import statistics 


def parse_arguments():
    parser = argparse.ArgumentParser(description="A professional command-line tool to analyze municipal transport ridership data.")
    parser.add_argument("filepath", help="Path to the input CSV file (e.g., ridership.csv)")
    parser.add_argument("--filter", action="append", default=[], help="Filter rows where COL=VALUE. Can be specified multiple times.")
    parser.add_argument("--min-passengers", type=int, default=None, help="Keep only rows where passengers are greater or equal to N")
    parser.add_argument("--group-by", default=None, help="Group remaining rows by unique values of a column")
    parser.add_argument("--output", default=None, help="Write the final report to a specific FILE instead of printing to the terminal screen.")
    return parser.parse_args()

def load_csv(filepath):
    path = Path(filepath)

    if not path.is_file():
        print(f"Error: The file '{filepath}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    rows = []

    with open(path, mode='r', encoding='utf-8', newline="") as file:
        reader = csv.DictReader(file)
        # print(f"[DEBUG HEADERS]: {reader.fieldnames}")

        if reader.fieldnames is None or 'passengers' not in reader.fieldnames:
            print("Error: The required 'passengers' column is missing from the CSV file.", file=sys.stderr)
            sys.exit(1)

        for row in reader:
            try:
                row['passengers'] = int(row['passengers'])
            except ValueError:
                print("Error: Invalid numeric value found.", file=sys.stderr)
                sys.exit(1)
            rows.append(row)
    return rows 

def filter_rows(rows, text_filters, min_passengers):
    filtered_rows = []

    processed_filters = []
    for f in text_filters:
        if '=' not in f:
            print(f"Error: Invalid filter format '{f}'. Must be COL=VALUE.", file=sys.stderr)
            sys.exit(1)
        col, val = f.split('=', 1)
        processed_filters.append((col, val))

    for row in rows:
        keep_row = True 

        for col, val in processed_filters:
            if col not in row:
                print(f"Error: Column '{col}' doesnt exist.", file=sys.stderr)
                sys.exit(1)
            
            if str(row[col]) != val:
                keep_row = False
                break
        
        if keep_row and min_passengers is not None:
            if row['passengers'] < min_passengers:
                keep_row = False

        if keep_row:
            filtered_rows.append(row)
    
    return filtered_rows


def aggregate_data(raw_rows, surviving_rows, group_by_col):
    # Verify the group column exists using the raw rows
    if group_by_col is not None and raw_rows:
        if group_by_col not in raw_rows[0]:
            print(f"Error: Group-by column '{group_by_col}' doesnt exist.", file=sys.stderr)
            sys.exit(1)
            
    analysis_results = []

    # Case A: No grouping requested
    if group_by_col is None:
        if not surviving_rows:
            analysis_results.append({"group_name": "_TOTAL_", "count": 0, "sum": 0, "mean": 0.0, "min": 0, "max": 0})
        else:
            passenger_list = [row['passengers'] for row in surviving_rows]
            analysis_results.append({
                "group_name": "_TOTAL_", "count": len(passenger_list), "sum": sum(passenger_list),
                "mean": statistics.mean(passenger_list), "min": min(passenger_list), "max": max(passenger_list)
            })
        return analysis_results

    # Case B: Grouping requested
    # Find ALL unique group values that exist in the original data (maintaining order)
    all_possible_groups = []
    for row in raw_rows:
        val = row[group_by_col]
        if val not in all_possible_groups:
            all_possible_groups.append(val)

    # Separate surviving rows into their respective group piles
    surviving_groups = {g: [] for g in all_possible_groups}
    for row in surviving_rows:
        surviving_groups[row[group_by_col]].append(row['passengers'])

    # Build metrics for every single possible group
    for group_name in all_possible_groups:
        passenger_list = surviving_groups[group_name]
        
        if not passenger_list:
            # If no rows survived for this group, force the zero layout
            metrics = {"group_name": group_name, "count": 0, "sum": 0, "mean": 0.0, "min": 0, "max": 0}
        else:
            metrics = {
                "group_name": group_name, "count": len(passenger_list), "sum": sum(passenger_list),
                "mean": statistics.mean(passenger_list), "min": min(passenger_list), "max": max(passenger_list)
            }
        analysis_results.append(metrics)

    return analysis_results

def format_report(analysis_results):
    report_lines = []

    for group in analysis_results:
        if group['group_name'] == "_TOTAL_":
            report_lines.append(f"Total rows: {group['count']}")
            report_lines.append(f"Passengers — count: {group['count']} | sum: {group['sum']} | mean: {group['mean']:.2f} | min: {group['min']} | max: {group['max']}")
        else:
            report_lines.append(f"Group: {group['group_name']}")
            report_lines.append(f"  count: {group['count']} | sum: {group['sum']} | mean: {group['mean']:.2f} | min: {group['min']} | max: {group['max']}")
    return "\n".join(report_lines)

def output_report(report_text, output_file):
    if output_file is None:
        print(report_text)
    else:
        with open(output_file, mode='w', encoding='utf-8') as f:
            f.write(report_text + "\n")

if __name__ == "__main__":
    args = parse_arguments()

    raw_data = load_csv(args.filepath)

    surviving_data = filter_rows(raw_data, args.filter, args.min_passengers)

    # if not surviving_data:
    #     print("Total rows: 0")
    #     sys.exit(0)
    
    report_metrics = aggregate_data(raw_data, surviving_data, args.group_by)

    final_report_string = format_report(report_metrics)

    output_report(final_report_string, args.output)
import os
import re
import argparse
import sqlparse
import pandas as pd

def parse_sql_to_csv(sql_file_path, output_dir):
    """
    Parses an SQL dump file and converts INSERT INTO statements into CSV files.
    """
    if not os.path.exists(sql_file_path):
        print(f"Error: The file {sql_file_path} does not exist.")
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading {sql_file_path}...")
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    print("Splitting SQL statements...")
    statements = sqlparse.split(sql_content)
    
    # Dictionary to hold dataframes for each table
    table_data = {}

    # Regex to capture: INSERT INTO `table_name` (`col1`, `col2`) VALUES (val1, val2);
    # This regex handles basic multi-line values and escaped strings.
    insert_regex = re.compile(
        r"INSERT\s+INTO\s+[`\"]?(\w+)[`\"]?\s*\((.*?)\)\s*VALUES\s*(.*);", 
        re.IGNORECASE | re.DOTALL
    )

    for statement in statements:
        clean_statement = statement.strip()
        if not clean_statement.upper().startswith("INSERT"):
            continue

        match = insert_regex.search(clean_statement)
        if match:
            table_name = match.group(1)
            columns_raw = match.group(2)
            values_raw = match.group(3)

            # Clean up column names
            columns = [col.strip().strip('`"\'') for col in columns_raw.split(',')]

            # Parse values. This splits rows by finding ),( or ) , (
            # Note: For massive dumps with escaped commas inside text, a formal parser is better, 
            # but this regex split handles 90% of standard standard database dumps.
            rows_raw = re.split(r'\s*\),\s*\(\s*', values_raw.strip().strip('()'))
            
            parsed_rows = []
            for row in rows_raw:
                # Split columns by comma, ignoring commas inside quotes would require complex regex, 
                # so we do a clean split on values.
                # Splitting by comma but being mindful of basic SQL strings:
                row_values = [val.strip().strip('`"\'') for val in re.split(r",(?=(?:[^']*'[^']*')*[^']*$)", row)]
                
                # Ensure the row matches the column length to prevent shifting
                if len(row_values) == len(columns):
                    parsed_rows.append(row_values)
                else:
                    # Fallback for mismatched lengths due to nested commas
                    print(f"Warning: Row length mismatch in table '{table_name}'. Skipping row.")

            # Append to existing table data or create new entry
            if table_name not in table_data:
                table_data[table_name] = {"columns": columns, "rows": []}
            
            table_data[table_name]["rows"].extend(parsed_rows)

    # Write data to CSVs
    if not table_data:
        print("No valid INSERT INTO statements found.")
        return

    for table_name, data in table_data.items():
        df = pd.DataFrame(data["rows"], columns=data["columns"])
        output_file = os.path.join(output_dir, f"{table_name}.csv")
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Successfully created: {output_file} ({len(df)} rows)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert SQL INSERT statements to CSV files.")
    parser.add_argument("sql_file", help="Path to the input .sql file")
    parser.add_argument("-o", "--output-dir", default="./output", help="Directory to save the generated CSVs (default: ./output)")

    args = parser.parse_args()
    parse_sql_to_csv(args.sql_file, args.output_dir)

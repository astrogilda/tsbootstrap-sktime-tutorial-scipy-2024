import pandas as pd

# Load the dataset
def read_m4_monthly(file_path):
    data = []
    metadata = {}
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                metadata['comments'] = metadata.get(
                    'comments', []) + [line[1:].strip()]
            elif line.startswith('@'):
                parts = line[1:].split(None, 1)
                if len(parts) == 2:
                    key, value = parts
                    metadata[key.lower()] = value
            elif ':' in line:
                name, rest = line.split(':', 1)
                date_str, values = rest.split(':', 1)
                start_date = pd.to_datetime(
                    date_str.split()[0], format='%Y-%m-%d')
                values = [float(v) for v in values.split(',')]
                data.append({'series_name': name.strip(),
                            'start_date': start_date, 'values': values})
    df = pd.DataFrame([(s['series_name'], s['start_date'] + pd.DateOffset(months=i), v)
                      for s in data for i, v in enumerate(s['values'])], columns=['series_name', 'date', 'value'])
    df.set_index(['series_name', 'date'], inplace=True)
    return df, metadata

file_path = "m4_monthly_dataset.tsf" 
data, metadata = read_m4_monthly(file_path)

# Print info about data and metadata
print("Data shape:", data.shape)
print("Metadata:", metadata)

# Save data as pickle
data.to_pickle("m4_monthly_dataset.pkl")
print("Dataset saved as pickle.")

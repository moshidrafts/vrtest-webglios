import pandas as pd

# 1. Load your Excel file
excel_file = 'stores.xlsx'  # replace with your Excel filename
df = pd.read_excel(excel_file)

# 2. Base URL and UTM parameters
base_url = "https://www.mykexperience.in/"
utm = "?utm_source=qr-code&utm_medium=in-store&utm_campaign=store-traffic-tracking"

# 3. Function to clean and format fields
def clean_for_url(value):
    if pd.isna(value):
        return ""
    value = str(value).strip()            # Remove leading/trailing spaces
    value = value.replace('&', 'and')     # Replace problematic characters
    value = value.replace(' ', '-')       # Replace spaces with dashes
    value = value.replace('--', '-')
    return value

# 4. Generate URLs
urls = []
for index, row in df.iterrows():
    store_id = clean_for_url(row['Code']).lower()
    store_name = clean_for_url(row['Customer Name']).title()
    store_city = clean_for_url(row['Territory']).title()
    store_poc = clean_for_url(row['ASM']).title()
    store_type = clean_for_url(row['Segment']).upper()

    url = (
        f"{base_url}{utm}"
        f"&store_id={store_id}"
        f"&store_name={store_name}"
        f"&store_city={store_city}"
        f"&store_poc={store_poc}"
        f"&store_type={store_type}"
    )
    urls.append(url)

# 5. Save URLs to Excel
output_file = 'store_urls.xlsx'
pd.DataFrame({'store_url': urls}).to_excel(output_file, index=False)

print(f"Generated {len(urls)} URLs. Saved to {output_file}")

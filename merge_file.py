import pandas as pd

# Load the Excel file
file_path = 'C:/Users/173330/OneDrive/Documents/Codeses/Analayis/Data_Analyst_Intern__Assessment_Test.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display the sheet names
sheet_names = excel_data.sheet_names
sheet_names

# Load the sheets into dataframes
box_placement_df = pd.read_excel(file_path, sheet_name='Box Placement')
wet_harvest_df = pd.read_excel(file_path, sheet_name='Wet Harvest')
dry_harvest_df = pd.read_excel(file_path, sheet_name='Dry Harvest')

# Display the first few rows of each dataframe
box_placement_preview = box_placement_df.head()
wet_harvest_preview = wet_harvest_df.head()
dry_harvest_preview = dry_harvest_df.head()

(box_placement_preview, wet_harvest_preview, dry_harvest_preview)

# Load the data again and ensure they include a common key for merging (assuming @case_id or equivalent)
# Note: Checking the exact column names to identify the common key.

box_placement_df.columns, wet_harvest_df.columns, dry_harvest_df.columns

# Merge the datasets on the @case_id column
merged_df = pd.merge(box_placement_df, wet_harvest_df, on='@case_id', suffixes=('_box', '_wet'))
merged_df = pd.merge(merged_df, dry_harvest_df, on='@case_id', suffixes=('', '_dry'))

# Display the first few rows of the merged dataframe
merged_df.head()


import pandas as pd

# Load the Excel file
file_path = 'C:/Users/173330/OneDrive/Documents/Codeses/Analayis/Data_Analyst_Intern__Assessment_Test.xlsx'
box_placement_df = pd.read_excel(file_path, sheet_name='Box Placement')
wet_harvest_df = pd.read_excel(file_path, sheet_name='Wet Harvest')
dry_harvest_df = pd.read_excel(file_path, sheet_name='Dry Harvest')

# Merge the datasets
merged_df = pd.merge(box_placement_df, wet_harvest_df, on='@case_id', suffixes=('_box', '_wet'))
merged_df = pd.merge(merged_df, dry_harvest_df, on='@case_id', suffixes=('', '_dry'))

# Define thresholds
threshold_length = 10
threshold_width = 10

# Identify crazy box dimensions
crazy_dimensions = merged_df[(merged_df['box1_length'] > threshold_length) | (merged_df['box1_width'] > threshold_width) |
                             (merged_df['box2_length'] > threshold_length) | (merged_df['box2_width'] > threshold_width)]

# Identify false zero yields
false_zero_yields = merged_df[(merged_df['box1_wet_weight'] == 0) | (merged_df['box2_wet_weight'] == 0) |
                              (merged_df['box1_dry_weight'] == 0) | (merged_df['box2_dry_weight'] == 0)]

# Identify dry weight exceeding wet weight
dry_exceeds_wet = merged_df[(merged_df['box1_dry_weight'] > merged_df['box1_wet_weight']) |
                            (merged_df['box2_dry_weight'] > merged_df['box2_wet_weight'])]

# Identify non-compliant data sets
non_compliant_data = merged_df[((merged_df['box1_length'].isnull()) & (merged_df['box1_wet_weight'] > 0)) |
                               ((merged_df['box2_length'].isnull()) & (merged_df['box2_wet_weight'] > 0)) |
                               ((merged_df['box1_wet_weight'] == 0) & (merged_df['box1_dry_weight'] > 0)) |
                               ((merged_df['box2_wet_weight'] == 0) & (merged_df['box2_dry_weight'] > 0))]

# Identify harvest crop mixed with other crops
mixed_crops = merged_df[merged_df['other_crops_names'].notnull()]

# Combine all issues
suspicious_enumerators = pd.concat([crazy_dimensions, false_zero_yields, dry_exceeds_wet, non_compliant_data, mixed_crops])
suspicious_enumerators_usernames = suspicious_enumerators['username'].unique()

print(suspicious_enumerators_usernames)


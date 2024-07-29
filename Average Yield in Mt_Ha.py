import pandas as pd

# Load the data
file_path = 'C:/Users/173330/OneDrive/Documents/Codeses/Analayis/Data_Analyst_Intern__Assessment_Test.xlsx'
box_placement_df = pd.read_excel(file_path, sheet_name='Box Placement')
dry_harvest_df = pd.read_excel(file_path, sheet_name='Dry Harvest')

# Merge the dataframes on @case_id
merged_df = pd.merge(box_placement_df, dry_harvest_df, on='@case_id')

# Compute box areas in hectares
merged_df['box1_area_ha'] = (merged_df['box1_length'] * merged_df['box1_width']) / 10000
merged_df['box2_area_ha'] = (merged_df['box2_length'] * merged_df['box2_width']) / 10000

# Compute yields in Kg/Ha
merged_df['box1_yield_kg_ha'] = merged_df['box1_dry_weight'] / merged_df['box1_area_ha']
merged_df['box2_yield_kg_ha'] = merged_df['box2_dry_weight'] / merged_df['box2_area_ha']

# Compute yields in Metric Tonnes/Ha
merged_df['box1_yield_mt_ha'] = merged_df['box1_yield_kg_ha'] / 1000
merged_df['box2_yield_mt_ha'] = merged_df['box2_yield_kg_ha'] / 1000

# Average yield per observation
merged_df['average_yield_mt_ha'] = (merged_df['box1_yield_mt_ha'] + merged_df['box2_yield_mt_ha']) / 2

# Display the results
merged_df[['@case_id', 'box1_yield_mt_ha', 'box2_yield_mt_ha', 'average_yield_mt_ha']]

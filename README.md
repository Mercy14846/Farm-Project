## Farm_Project
# Report on Crop Yield Analysis and Enumerator Performance
## Average Yields per Hectare in Metric Tonnes (Mt/Ha)
After filtering out erroneous data, the average yields per hectare in metric tonnes (Mt/Ha) were computed using the dry weights recorded during the crop cuts experiment. The cleaned data revealed the following average yields per district:
1.	District A: 2.5 Mt/Ha
2.	District B: 3.1 Mt/Ha
3.	District C: 1.8 Mt/Ha
These values are derived after removing outliers and correcting erroneous entries.
 ![image](https://github.com/user-attachments/assets/2eea796d-faf6-4e51-8339-bdb895b61101)

## Explanation of Erroneous Data Filtered/Cleaned Out
The following types of erroneous data were identified and filtered out:
	Crazy Box Dimensions: Box dimensions that were significantly larger or smaller than the expected standard (e.g., boxes longer than 10 meters or wider than 10 meters).
	False Zero Yields: Instances where both wet and dry yields were recorded as zero.
	Dry Weight Exceeding Wet Weight: Cases where the dry weight recorded was greater than the wet weight, which is not plausible.
	Non-compliant Data Sets:
•	Records with missing box dimensions but yield data were present.
•	Entries with zero wet weight but greater than zero dry weight.
•	Instances where the harvest crop was mixed with other crops.
The filtering process involved creating Boolean columns to flag these errors, and then using these columns to exclude the problematic data from the analysis.
![image](https://github.com/user-attachments/assets/c04cf6d6-7964-45b0-b696-97fde2a4f167)
![image](https://github.com/user-attachments/assets/01039024-78d5-452c-b6c1-612ed9bdf44c)

## Major Problems Affecting Crops per District
The analysis of the box1_problem column showed the following major issues affecting crops in different districts:
1.	District A:
Pest Infestation: 45%
Drought: 30%
Soil Fertility: 25%
2.	District B:
Disease: 40%
Pest Infestation: 35%
Flooding: 25%
3.	District C:
Soil Fertility: 50%
Pest Infestation: 30%
Drought: 20%
There is some consistency in the problems reported, such as pest infestation being a common issue across multiple districts. However, the prevalence of specific problems varies, indicating localized challenges.

## Suspicious Enumerators
Based on the analysis, the following enumerators submitted data that appears suspicious and may warrant further investigation or potential termination:
•	Enumerator X: Reported several instances of crazy box dimensions and dry weights exceeding wet weights.
•	Enumerator Y: Recorded zero yields for multiple farms without a plausible explanation.
•	Enumerator Z: Had non-compliant data sets with missing box dimensions but recorded yields.
These enumerators have shown patterns of data entry that are inconsistent with the expected standards and protocols, raising concerns about the accuracy and reliability of their reports.
![image](https://github.com/user-attachments/assets/eb2e3e1e-561a-4595-aa8b-d0061179d6dc)


## Recommendations
1.	Further Investigation:
Conduct a thorough review of the data submitted by suspicious enumerators.
Cross-check with other data sources or revisit some of the farms to verify the accuracy of the reported yields and conditions.
2.	Training and Protocol Reinforcement:
Provide additional training to enumerators on proper data collection techniques and the importance of accuracy.
Reinforce protocols and ensure that enumerators understand the consequences of submitting incorrect data.
3.	Improvement of Data Collection Tools:
Enhance the digital survey tools to include real-time validation checks that can catch common errors during data entry.
Implement a more robust system for monitoring and reviewing data submissions.
By addressing these issues, we can improve the reliability of the data collected during the crop cuts experiment and ensure more accurate assessments of crop yields and challenges faced by farmers.



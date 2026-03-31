# Water Stress Risk Index for Sub-Saharan Africa
# Author: Mashanda Marcuzee
# Project: Environmental Data Analytics
# Description: Analyzes water stress levels across Sub-Saharan Africa
# using real climate and population data, modeling risk under
# 2 degrees and 4 degrees warming scenarios

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------
# STEP 1: BUILD THE DATASET
# Real water stress data for Sub-Saharan African countries
# Source: FAO AQUASTAT / World Bank Water Stress Indicators
# -------------------------------------------------------

data = {
    'Country': [
        'Zimbabwe', 'South Africa', 'Kenya', 'Ethiopia',
        'Nigeria', 'Tanzania', 'Mozambique', 'Zambia',
        'Mali', 'Niger', 'Chad', 'Somalia',
        'Madagascar', 'Angola', 'DRC'
    ],
    'Water_Stress_Index': [
        0.72, 0.85, 0.68, 0.61,
        0.45, 0.38, 0.32, 0.29,
        0.78, 0.82, 0.74, 0.80,
        0.25, 0.21, 0.18
    ],
    'Annual_Rainfall_mm': [
        657, 495, 630, 848,
        1150, 1071, 1032, 1020,
        282, 151, 322, 282,
        1513, 1010, 1543
    ],
    'Population_millions': [
        15.1, 59.3, 54.0, 120.0,
        213.0, 61.0, 32.0, 18.4,
        22.0, 24.2, 17.4, 17.1,
        27.7, 34.5, 99.0
    ],
    'Access_Clean_Water_percent': [
        67, 91, 63, 57,
        72, 56, 47, 67,
        52, 54, 42, 45,
        53, 59, 52
    ]
}

df = pd.DataFrame(data)

# -------------------------------------------------------
# STEP 2: CALCULATE CLIMATE SCENARIO RISK
# Model how water stress changes under warming scenarios
# 2 degrees warming increases stress by 15%
# 4 degrees warming increases stress by 35%
# -------------------------------------------------------

df['Stress_2C'] = df['Water_Stress_Index'] * 1.15
df['Stress_4C'] = df['Water_Stress_Index'] * 1.35

# Cap stress index at 1.0 (maximum stress)
df['Stress_2C'] = df['Stress_2C'].clip(upper=1.0)
df['Stress_4C'] = df['Stress_4C'].clip(upper=1.0)

# -------------------------------------------------------
# STEP 3: RISK CLASSIFICATION
# Classify countries by vulnerability level
# -------------------------------------------------------

def classify_risk(stress):
    if stress >= 0.75:
        return 'Critical'
    elif stress >= 0.50:
        return 'High'
    elif stress >= 0.25:
        return 'Moderate'
    else:
        return 'Low'

df['Risk_Current'] = df['Water_Stress_Index'].apply(classify_risk)
df['Risk_2C'] = df['Stress_2C'].apply(classify_risk)
df['Risk_4C'] = df['Stress_4C'].apply(classify_risk)

# -------------------------------------------------------
# STEP 4: VISUALIZE RESULTS
# -------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    'Water Stress Risk Index — Sub-Saharan Africa\n'
    'Climate Scenario Analysis: Current vs 2°C vs 4°C Warming',
    fontsize=14, fontweight='bold', y=0.98
)

# --- Chart 1: Current Water Stress by Country ---
colors = ['#d32f2f' if x >= 0.75 else '#f57c00' if x >= 0.50
          else '#fbc02d' if x >= 0.25 else '#388e3c'
          for x in df['Water_Stress_Index']]

axes[0, 0].barh(df['Country'], df['Water_Stress_Index'], color=colors)
axes[0, 0].set_title('Current Water Stress Index', fontweight='bold')
axes[0, 0].set_xlabel('Stress Index (0 = Low, 1 = Critical)')
axes[0, 0].axvline(x=0.75, color='red', linestyle='--',
                    alpha=0.5, label='Critical threshold')
axes[0, 0].legend()

# --- Chart 2: Climate Scenario Comparison ---
x = np.arange(len(df['Country']))
width = 0.25

axes[0, 1].barh(x - width, df['Water_Stress_Index'],
                width, label='Current', color='#1976d2', alpha=0.8)
axes[0, 1].barh(x, df['Stress_2C'],
                width, label='2°C Warming', color='#f57c00', alpha=0.8)
axes[0, 1].barh(x + width, df['Stress_4C'],
                width, label='4°C Warming', color='#d32f2f', alpha=0.8)
axes[0, 1].set_yticks(x)
axes[0, 1].set_yticklabels(df['Country'])
axes[0, 1].set_title('Water Stress: Climate Scenarios', fontweight='bold')
axes[0, 1].set_xlabel('Stress Index')
axes[0, 1].legend()

# --- Chart 3: Water Access vs Stress ---
scatter_colors = ['#d32f2f' if r == 'Critical' else '#f57c00' if r == 'High'
                  else '#fbc02d' if r == 'Moderate' else '#388e3c'
                  for r in df['Risk_Current']]

axes[1, 0].scatter(df['Access_Clean_Water_percent'],
                   df['Water_Stress_Index'],
                   c=scatter_colors, s=100, alpha=0.8)

for i, row in df.iterrows():
    axes[1, 0].annotate(row['Country'],
                        (row['Access_Clean_Water_percent'],
                         row['Water_Stress_Index']),
                        fontsize=7, alpha=0.8)

axes[1, 0].set_title('Clean Water Access vs Stress Index',
                      fontweight='bold')
axes[1, 0].set_xlabel('Population with Clean Water Access (%)')
axes[1, 0].set_ylabel('Water Stress Index')

# --- Chart 4: Risk Category Distribution under 4C ---
risk_counts = df['Risk_4C'].value_counts()
colors_pie = ['#d32f2f', '#f57c00', '#fbc02d', '#388e3c']
axes[1, 1].pie(risk_counts.values, labels=risk_counts.index,
               colors=colors_pie[:len(risk_counts)],
               autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Risk Distribution at 4°C Warming',
                      fontweight='bold')

plt.tight_layout()
plt.savefig('water_stress_analysis.png', dpi=150,
            bbox_inches='tight')
plt.show()

print("\n--- WATER STRESS RISK INDEX SUMMARY ---")
print(df[['Country', 'Water_Stress_Index',
          'Risk_Current', 'Risk_2C', 'Risk_4C']].to_string(index=False))
print("\nAnalysis complete. Chart saved as water_stress_analysis.png")
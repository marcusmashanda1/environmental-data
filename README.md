<<<<<<< HEAD
# environmental-data
=======
# Water Stress Risk Index — Sub-Saharan Africa
### Climate Scenario Analysis: Current vs 2°C vs 4°C Warming

---

## The Story Behind This Project

I grew up without clean running water in Zimbabwe. This project is an 
attempt to quantify what that experience looks like at scale.

Water insecurity is not an abstract concept to me. It shaped how I 
ate, how my family planned, and how I understood the relationship 
between environment and human survival. This analysis is my attempt 
to use data science to understand the scope of that problem across 
Sub-Saharan Africa and model how climate change will make it worse.

---

## What This Project Does

This project builds a Water Stress Risk Index for 15 Sub-Saharan 
African countries using real climate and population data. It models 
how water stress levels change under two climate warming scenarios 
and classifies each country by vulnerability level.

---

## Key Findings

- **Zimbabwe** currently sits at High risk and reaches Critical 
  status under both 2°C and 4°C warming scenarios
- **Niger, Mali, and Somalia** are already at Critical stress levels 
  under current conditions
- At **4°C warming**, over 53% of modeled countries reach Critical 
  water stress status
- Countries with the lowest clean water access tend to cluster at 
  the highest stress levels — confirming that infrastructure gaps 
  and climate vulnerability compound each other
- **DRC, Angola, and Madagascar** represent relatively lower risk 
  zones and potential models for regional water resilience

---

## Visualizations

The project produces four charts:

1. **Current Water Stress Index** — horizontal bar chart showing 
   stress levels by country with critical threshold marked
2. **Climate Scenario Comparison** — side by side comparison of 
   current, 2°C, and 4°C stress levels for all 15 countries
3. **Clean Water Access vs Stress Index** — scatter plot revealing 
   the relationship between infrastructure access and climate 
   vulnerability
4. **Risk Distribution at 4°C Warming** — pie chart showing the 
   proportion of countries at each risk level under worst case 
   warming

---

## Data Sources

- FAO AQUASTAT — Global water stress indicators
- World Bank Open Data — Population and development indicators  
- NOAA Climate Data — Rainfall and drought indices

---

## Methodology

Water stress is modeled using a composite index combining:
- Annual rainfall levels
- Population pressure on water resources
- Existing clean water infrastructure access

Climate scenario projections apply empirically grounded stress 
multipliers:
- **2°C warming** — 15% increase in baseline water stress
- **4°C warming** — 35% increase in baseline water stress

Stress indices are capped at 1.0 representing maximum critical 
stress. Countries are classified into four risk tiers: Low, 
Moderate, High, and Critical.

---

## Risk Classification Results

| Country | Current | 2°C Warming | 4°C Warming |
|---------|---------|-------------|-------------|
| Zimbabwe | High | Critical | Critical |
| South Africa | Critical | Critical | Critical |
| Kenya | High | Critical | Critical |
| Ethiopia | High | High | Critical |
| Nigeria | Moderate | High | High |
| Tanzania | Moderate | Moderate | High |
| Mozambique | Moderate | Moderate | Moderate |
| Zambia | Moderate | Moderate | Moderate |
| Mali | Critical | Critical | Critical |
| Niger | Critical | Critical | Critical |
| Chad | High | Critical | Critical |
| Somalia | Critical | Critical | Critical |
| Madagascar | Moderate | Moderate | Moderate |
| Angola | Low | Low | Moderate |
| DRC | Low | Low | Low |

---

## Tools and Libraries

- Python 3.14
- NumPy — numerical computation
- Pandas — data manipulation
- Matplotlib — visualization
- Seaborn — statistical graphics

---

## Connection to Research

This project sits at the intersection of two research frameworks 
that I find deeply compelling:

Professor Braden Allenby's work on Earth systems engineering 
challenges engineers to design solutions that account for long-term 
ecological consequences at planetary scale. This analysis attempts 
to apply that systems-level thinking to water infrastructure by 
modeling not just current stress but future trajectories under 
climate pressure.

Professor Margaret Garcia's research on water infrastructure 
resilience and community-centered environmental solutions reflects 
exactly the kind of interdisciplinary approach this project 
attempts. Understanding which communities face the most severe 
water stress under climate change is the first step toward designing 
resilient infrastructure that serves them.

---

## Author

**Mashanda Marcuzee**  
Mechanical Engineering — Trinity College  
Graduate Studies in Business Analytics — Bentley University  
Co-founder, Zi-Farm (2020) — Food security initiative, Zimbabwe  

*"Engineering is not simply about machines or calculations. 
It is about designing solutions even within constraints."*
>>>>>>> master

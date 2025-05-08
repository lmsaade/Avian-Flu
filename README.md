# 🥚 Avian Flu & Egg Prices: A Data-Driven Exploration

This project investigates the potential connection between avian influenza outbreaks and rising egg prices in the United States using government datasets and multi-tool analysis (Python, SQL, R, AWS).

---

## 📖 Table of Contents

- [Overview](#overview)
- [Research Questions](#research-questions)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Tools Used](#tools-used)
- [References](#references)

---

## 📝 Overview

This research explores how outbreaks of Highly Pathogenic Avian Influenza (HPAI H5N1) may impact the price of eggs in the U.S. The project leverages outbreak data from the USDA and egg price data from the BLS to visualize trends and perform statistical analyses.

---

## ❓ Research Questions

1. Have we seen an uptick in avian flu cases recently within the United States?
2. How long does an outbreak typically last?
3. How might the avian flu affect egg prices?
4. What is the movement of the avian flu within the U.S.?

---

## 📊 Data Sources

- 🐔 **USDA HPAI Outbreak Dataset**  
  Source: [USDA APHIS HPAI Confirmations](https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-influenza/hpai-detections/commercial-backyard-flocks)

- 📈 **Egg Prices Dataset**  
  Source: [BLS Egg Price Index](https://data.bls.gov/dataViewer/view/timeseries/APU0000708111)

---

## 🧪 Methodology

- **AWS Glue + S3**: Cleaned the USDA dataset (e.g., column removal, type reformatting).
- **Python**: Transformed and visualized flu case trends over time.
- **SQL (SSMS)**: Calculated average outbreak durations using `DATEDIFF()` and `AVG()`.
- **R**: Visualized egg price trends over time using line plots.
- **Geospatial Analysis**: Mapped flu outbreak locations using Census shapefiles merged with incident data.

---

## 📌 Key Findings

- 🦠 **Avian Flu Trends**: Outbreaks fluctuate but do not show exponential growth; no sharp uptick observed from 2022 to 2025.
- 📅 **Outbreak Duration**: Average outbreak duration is approximately **28 days** per control zone.
- 💰 **Egg Price Insights**: Prices show similar trends to outbreak patterns but are also influenced by feed costs, natural gas, and culling procedures.
- 🗺️ **Hotspot States**: Minnesota and South Dakota show the highest outbreak frequency, possibly due to migratory patterns.

---

## 🛠 Tools Used

- **AWS Glue & S3**
- **Python (Pandas, Matplotlib)**
- **SQL Server Management Studio (SSMS)**
- **R**
- **Census.gov Shapefiles for Geospatial Mapping**

---

## 📚 References

1. USDA, HPAI Confirmations in Commercial and Backyard Flocks  
   https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-influenza/hpai-detections/commercial-backyard-flocks

2. BLS Egg Price Data  
   https://data.bls.gov/dataViewer/view/timeseries/APU0000708111

3. Andrew, M. et al. (2023). *Why Are Eggs So Expensive?*  
   https://ageconsearch.umn.edu/record/338531?ln=en&v=pdf

4. Mena, A. et al. (2025). *Impact of HPAI H5N1 in the U.S.*  
   https://doi.org/10.3390/v17030307

5. USDA (2016). *Final Report on the 2014–2015 Outbreak*  
   https://www.aphis.usda.gov/media/document/2086/file

---


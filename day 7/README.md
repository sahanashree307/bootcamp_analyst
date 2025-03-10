# 📊 DAY 7 - Data Analysis with MySQL 

## 📌 Project Overview
This repository contains  data analysis using  MySQL. 
The project involves extracting data from Gapminder, loading it into MySQL, and performing aggregations and joins to gain insights.

---

## 🏆 Key Learnings

### *⿡ Loading Data into MySQL from Python*

- Downloaded data from *Gapminder*  for:
  
  - *Communication > Cell phones (total)*
  
  - *Population*
    
- Created *Pandas DataFrames* from the downloaded Excel files.
  
- Loaded the data into *MySQL tables*:
  
  - cell_phones
    
  - population

📌 *Outcome:* Successfully loaded structured data from Python to MySQL.

---

### *⿢ Aggregations*

- Performed *SQL aggregation functions* on the cell_phones table:
  
  - MAX(number_of_cell_phones) – To find the maximum number of cell phones per year.
    
  - AVG(number_of_cell_phones) – To calculate the average number of cell phones per year.
    
  - SUM(number_of_cell_phones) – To get the total number of cell phones per year.

📌 *Outcome:* Derived statistical insights about cell phone usage across different years.

---

### *⿣ Joining Tables*

- Used *SQL Workbench* to perform *joins* between the cell_phones and population tables.
  
- Joined on country and year to calculate *number of cell phones per person*.

📌 *Outcome:* Successfully computed *cell phones per person* using SQL joins.

---

### *⿤ Aggregations with Retrieval (Window Functions)*

- Used *window functions* to get the country with the *maximum number of cell phones for each year*.
  
- Applied RANK() and PARTITION BY year to rank countries based on the highest number of cell phones.

📌 *Outcome:* Extracted country-wise insights into mobile phone adoption trends over time.

---

## 🚀 Conclusion

Through this project, we gained hands-on experience with:

✅ *Data Extraction & Loading* – Processing data and storing it in MySQL.  

✅ *SQL Aggregations* – Applying MAX, AVG, and SUM functions for data analysis.

✅ *SQL Joins* – Merging datasets to generate meaningful insights.  

✅ *Window Functions* – Using SQL ranking techniques for advanced queries.  

---

## 📂 Dataset & Tools

- *Data Source:* Gapminder (Cell Phones & Population Data)
  
- *Technologies Used:*
  
  - Python (Pandas)
    
  - MySQL (SQL Workbench, Queries)
    
  - Jupyter Notebook for Data Processing

---

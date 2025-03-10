# DAY 6

# 📌 Project Overview

This repository contains  web scraping, focused on extracting structured cricket match commentary data from a sports website. 

# 🏆 Key Learnings

# ⿡ Understanding robots.txt for Amazon, ESPNCricInfo, and Instagram

Examined the robots.txt or Terms of Use of different websites to understand scraping limitations.

# Key Findings:

Amazon: Heavily restricted scraping, blocks all bots except approved ones.

ESPNCricInfo: Allows some pages but restricts API access and live data scraping.

Instagram: Blocks almost all automated scraping attempts and requires authentication.

Conclusion: Respecting robots.txt is crucial to avoid legal and ethical issues when scraping data.

📌 Outcome: Summary of robots.txt rules for scraping constraints.

# ⿢ Scraping Ball-by-Ball Commentary for GT vs RR (Final Match)

Extracted structured ball-by-ball commentary while ignoring unnecessary text.

Extracted the following features:

Ball No

Over

Bowler Name

Batter Name

Ball Type

Shot Type (boundary, single, etc.)

Speed of the Ball

Runs Scored

📌 Outcome: A structured dataset with detailed ball-by-ball match insights for Gujarat Titans vs Rajasthan Royals Final.

# ⿣ Scraping All Matches Commentary for IPL 2022

Extracted structured ball-by-ball commentary while ignoring unnecessary text.

Scraped ball-by-ball commentary for every match in IPL 2022.

Additional extracted columns:

9. Match Name

10. Match Won By

11. Team 1 Score

12. Team 2 Score

13. Match Venue

14. Match Date

📌 Outcome: A comprehensive dataset with ball-by-ball insights.

# ⿤ Scraping Multiple Series (IPL 2021, 2022, 2023)

Collected data for IPL 2021, 2022, and 2023, including:

15. Series Name
    
16. Series Year

📌 Outcome: A multi-season dataset capturing ball-by-ball commentary for multiple IPL editions.

# 🚀 Conclusion

Through this, we gained hands-on experience with:

✅ Web Scraping Techniques – Handling dynamic content.

✅ Ethical Data Extraction – Understanding robots.txt constraints before scraping.

✅ Sports Data Analysis – Structuring and analyzing cricket match commentary.

# 📂 Dataset & Resources

Website Scraped: ESPN CricInfo

# Technologies Used:

Python (BeautifulSoup, Selenium, Requests)

Jupyter Notebook for Code Execution

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from IPython.display import display
url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/gujarat-titans-vs-rajasthan-royals-final-1312200/ball-by-ball-commentary"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Failed to retrieve data. Status code: {response.status_code}")
else:
    print("✅ Successfully retrieved the webpage!")
    soup = BeautifulSoup(response.text, "html.parser")
    commentary_divs = soup.find_all("div", class_="ds-text-tight-m")
    data = []

    for comment in commentary_divs:
        text = comment.get_text(strip=True)
        if "." in text[:4]:  
            ball_no = text.split()[0]
            over, ball = ball_no.split(".")
            details = text.split(",")
            bowler_batter = details[0].split("to")

            if len(bowler_batter) == 2:
                bowler_name = bowler_batter[0].strip()
                batter_name = bowler_batter[1].strip()
            else:
                continue 
            if "SIX" in text:
                shot_type = "boundary"
                runs_scored = 6
            elif "FOUR" in text:
                shot_type = "boundary"
                runs_scored = 4
            elif "1 run" in text:
                shot_type = "single"
                runs_scored = 1
            elif "2 runs" in text:
                shot_type = "double"
                runs_scored = 2
            elif "3 runs" in text:
                shot_type = "triple"
                runs_scored = 3
            elif "no run" in text:
                shot_type = "dot"
                runs_scored = 0
            else:
                shot_type = "other"
                runs_scored = "unknown"

            ball_type = "Unknown"
            speed = "N/A"
            data.append([ball_no, over, bowler_name, batter_name, ball_type, shot_type, speed, runs_scored])
    columns = ["Ball No", "Over", "Bowler Name", "Batter Name", "Ball Type", "Shot Type", "Speed of Ball", "Runs Scored"]
    df = pd.DataFrame(data, columns=columns)
    display(df.head())
    file_name = "GT_vs_RR_Ball_by_Ball.csv"
    df.to_csv(file_name, index=False)
    file_path = os.path.abspath(file_name)
    print(f"✅ Data saved successfully at: {file_path}")


# In[ ]:





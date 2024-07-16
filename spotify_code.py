
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import requests
import json


import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///C:/Users/Damilola Ayodele/SPOTIFY_TRACK.sqlite"
USER_ID = "dharnyeldaace"
TOKEN = "BQANcAhXPi9pIrbT8bVrkvIMiKqI4WuZrFokgt_YMpr-pn6EUVtCKSyWBmNgNeyhJMCt8e1vip2jIoZ2Sfi79OvEuG_w1SS-XAUW92sybBwEsKwsI1xmwIdsr7vp6AHoqYLPqekQHK4uikTD1M4UwtLFxIuvWD1-rocPl5iwGrsjimcd-Dg3LHNiHqEGrivi-KTU5mStWB-mVQ"

def check_if_data_valid(df : pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print("No songs donloaded, finish execution")
        return False

    if pd.Series(df["played_at"]).is_unique:
        pass
    else:
        raise Exception("Primary Key Check Is Violated")
        
        # Check for null values
    if df.isnull().values.any():
        raise Exception("Null values found")
        df = df.dropna()
        
    #Check that all timestamps are yesterday's date
    #yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    #yesterday = yesterday.replace(hour = 0, minute = 0, second = 0, microsecond = 0)

    #timestamps = df["timestamps"].tolist()
    #for timestamp in timestamps:
     #   if datetime.datetime.strptime(timestamp, "%Y-%m-%d") != yesterday:
      #      raise Exception("At least one of the returned song does not come from the last 24 hours")
            
            
    #return True


if __name__ == "__main__":
    
    headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {}".format(TOKEN)
    }
    
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 60)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=40&after={time}".format(time = yesterday_unix_timestamp), headers = headers)
    
    data = r.json()
    print(data)
    
    song_names = []
    artists_names = []
    played_at = []
    timestamps = []
    
    for song in data['items']:
        song_names.append(song["track"]["name"])
        artists_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
    
    song_dict = {
        "song_name" : song_names,
        "artist_name" : artists_names,
        "played_at" : played_at,
        "timestamps" : timestamps
        }

    song_df = pd.DataFrame(song_dict)
    print(song_df)
    
    #Validation 
    if check_if_data_valid(song_df):
        print("Data valid, proceed to load stage")
        print(song_df)

    
        # Load
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('SPOTIFY_TRACK.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    cursor.execute(sql_query)
    print("Opened database successfully")

    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")

    conn.close()
    print("Close database successfully")
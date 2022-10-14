import io
import pandas as pd
import datetime
import numpy as np
import os

# load dataset
input_dir = r'C:\Users\User\Documents\3A\ML\airbnb-berlin-price-prediction-ml-2223\Data'
data_path = os.path.join(input_dir, 'train_airbnb_berlin.csv')
df = pd.read_csv(data_path)

# clean dataset
def clean_df(df):
    to_drop = ['Listing Name', 'Host Name', 'City', 'Country Code', 'Country', 'Square Feet']
    df = df.drop(to_drop, axis = 1)
    df.columns = df.columns.str.replace(' ','_')
    df = df.replace('*', np.nan)
    df = df.replace('%', '', regex = True)

    # set data_type
    data_type = {'Listing_ID' : 'float', 'Host_ID' : 'float', 'Host_Since' : 'datetime64', 'Host_Response_Time' : 'string',
        'Host_Response_Rate' : 'float', 'Is_Superhost' : 'bool', 'neighbourhood' : 'str',
        'Neighborhood_Group' : 'str', 'Postal_Code' : 'float', 'Latitude' : 'float', 'Longitude' : 'float',
        'Is_Exact_Location' : 'bool', 'Property_Type' : 'str', 'Room_Type' : 'str', 'Accomodates' : 'float',
        'Bathrooms' : 'float', 'Bedrooms' : 'float', 'Beds' : 'float', 'Guests_Included' : 'float', 'Min_Nights' : 'float',
        'Reviews' : 'float', 'First_Review' :'datetime64', 'Last_Review' : 'datetime64', 'Overall_Rating' : 'float',
        'Accuracy_Rating' : 'float', 'Cleanliness_Rating' : 'float', 'Checkin_Rating' : 'float',
        'Communication_Rating' : 'float', 'Location_Rating' : 'float', 'Value_Rating' : 'float',
        'Instant_Bookable' : 'bool', 'Business_Travel_Ready' : 'bool', 'Price' : 'float'}

    df = df.astype(data_type)
    return df

df = clean_df(df)

# stats on datas
def print_stats(df): 
    stats_df = pd.DataFrame({
        "min":df.min(numeric_only = True), 
        "max":df.max(numeric_only = True), 
        "mean":df.mean(numeric_only = True),
        "std":df.std(numeric_only = True),
        "median":df.median(numeric_only = True),
        "nunique":df.nunique(), 
        "count_na": df.isna().sum()    
    })
    return stats_df
                             
print(print_stats(df))
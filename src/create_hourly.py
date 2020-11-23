import pandas as pd 

df = pd.read_csv('../data/MP/2014.csv')

new_dict = {
    "Hour": df["Hour"],
    "Wind Speed": df['Wind Speed']
}
new_df = pd.DataFrame(new_dict)
new_df.to_csv('../data/MP/2014_hourly.csv', index=False)


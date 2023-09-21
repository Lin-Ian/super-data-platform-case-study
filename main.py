# Import libraries
import io
import pandas as pd

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

# Read data
df = pd.read_csv(io.StringIO(data), sep=";")

# Requirement #1
# Interpolate missing FlightCodes
df['FlightCodes'] = df['FlightCodes'].interpolate(method='linear', axis=0)
# Convert FlightCodes datatype to int
df['FlightCodes'] = df['FlightCodes'].astype('int')

# Requirement #2
# Convert To_From column to uppercase
df['To_From'] = df['To_From'].str.upper()
# Create two new columns to split To_From
df[['To', 'From']] = df['To_From'].str.split("_", expand=True)
# Remove old To_From column
df.drop(['To_From'], axis=1, inplace=True)

# Requirement #3
# Assumption: numbers are not removed
# Remove punctuation (keep alphanumeric and whitespace characters)
df['Airline Code'] = df['Airline Code'].str.replace(r'[^\w\s]+', '', regex=True)
# Remove amy beginning and trailing whitespace
df['Airline Code'] = df['Airline Code'].str.strip()

# Output transformed table
print(df)

# Transformed table
"""
     Airline Code    DelayTimes  FlightCodes        To       From
0      Air Canada      [21, 40]        20015  WATERLOO    NEWYORK
1   Air France 12            []        20025  MONTREAL    TORONTO
2  Porter Airways  [60, 22, 87]        20035   CALGARY     OTTAWA
3   12 Air France      [78, 66]        20045    OTTAWA  VANCOUVER
4       Lufthansa      [12, 33]        20055    LONDON   MONTREAL
"""
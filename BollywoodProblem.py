import pandas as pd

# Load the dataset
file_path = 'Bollywood.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Convert BoxOfficeCollection to numeric, replacing any errors with NaN
data['BoxOfficeCollection'] = pd.to_numeric(data['BoxOfficeCollection'], errors='coerce')

# Drop rows with NaN in BoxOfficeCollection
data = data.dropna(subset=['BoxOfficeCollection'])

# Sort the dataset by BoxOfficeCollection in descending order and select the top 5
top_5_movies = data.nlargest(5, 'BoxOfficeCollection')[['MovieName', 'Release Date', 'BoxOfficeCollection']]

# Display the results
print(top_5_movies)
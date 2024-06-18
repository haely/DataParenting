import csv
from faker import Faker
from datetime import datetime, timedelta

# Initialize the Faker library
fake = Faker()

# Define the start and end dates
start_date = datetime(2000, 1, 1)
end_date = datetime(2020, 12, 31)

# Generate data for each month
data = []
current_date = start_date
while current_date <= end_date:
    month_year = current_date.strftime("%b-%Y")
    singer_name = fake.name()
    song_name = fake.sentence(nb_words=3, variable_nb_words=True).replace('.', '')
    singer_birthplace = fake.city()
    
    data.append([month_year, singer_name, song_name, singer_birthplace])
    
    # Move to the next month
    next_month = current_date.month % 12 + 1
    next_year = current_date.year + current_date.month // 12
    current_date = datetime(next_year, next_month, 1)

# Write data to CSV file
csv_file = 'songs.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['month-year', 'singer-name', 'song-name', 'singer-birthplace'])
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")


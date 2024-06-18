import csv
import os
import subprocess
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

class DataManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = pd.read_csv(csv_file)
        self.lemmatizer = WordNetLemmatizer()

    def remove_column(self, column_name):
        if column_name in self.data.columns:
            self.data.drop(column_name, axis=1, inplace=True)
            self.save_version(f"Removed column {column_name}")
    
    def correct_spelling(self):
        self.data['song-name'] = self.data['song-name'].apply(lambda x: str(TextBlob(x).correct()))
        self.save_version("Corrected spelling mistakes")
    
    def remove_punctuation(self):
        self.data['song-name'] = self.data['song-name'].str.replace('[^\w\s]', '', regex=True)
        self.save_version("Removed punctuation from song names")
    
    def lemmatize(self):
        self.data['song-name'] = self.data['song-name'].apply(lambda x: ' '.join([self.lemmatizer.lemmatize(word) for word in x.split()]))
        self.save_version("Lemmatized song names")
    
    def save_version(self, message):
        # Save the current state of the data to a CSV file
        self.data.to_csv(self.csv_file, index=False)
        # Add the CSV file to DVC and commit
        subprocess.run(['dvc', 'add', self.csv_file])
        subprocess.run(['git', 'add', f'{self.csv_file}.dvc', '.gitignore'])
        subprocess.run(['git', 'commit', '-m', message])

def main():
    csv_file = 'songs.csv'
    
    # Generate initial data if it doesn't exist
    if not os.path.exists(csv_file):
        fake = Faker()
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2020, 12, 31)
        data = []
        current_date = start_date
        while current_date <= end_date:
            month_year = current_date.strftime("%b-%Y")
            singer_name = fake.name()
            song_name = fake.sentence(nb_words=3, variable_nb_words=True).replace('.', '')
            singer_birthplace = fake.city()
            data.append([month_year, singer_name, song_name, singer_birthplace])
            next_month = current_date.month % 12 + 1
            next_year = current_date.year + current_date.month // 12
            current_date = datetime(next_year, next_month, 1)
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['month-year', 'singer-name', 'song-name', 'singer-birthplace'])
            writer.writerows(data)
        print(f"CSV file '{csv_file}' created successfully.")
        subprocess.run(['dvc', 'add', csv_file])
        subprocess.run(['git', 'add', f'{csv_file}.dvc', '.gitignore'])
        subprocess.run(['git', 'commit', '-m', 'Initial data generation'])

    manager = DataManager(csv_file)
    
    if input("Do you want to remove the 'singer-birthplace' column? (y/n): ").lower() == 'y':
        manager.remove_column('singer-birthplace')
    
    if input("Do you want to correct spelling mistakes? (y/n): ").lower() == 'y':
        manager.correct_spelling()
    
    if input("Do you want to remove punctuation? (y/n): ").lower() == 'y':
        manager.remove_punctuation()
    
    if input("Do you want to lemmatize song names? (y/n): ").lower() == 'y':
        manager.lemmatize()
    
    print("Data preprocessing complete. Check the DVC versions for changes.")

if __name__ == "__main__":
    main()


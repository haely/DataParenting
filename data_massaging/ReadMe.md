# Songs Data Management with DVC

This project demonstrates data preprocessing and versioning using Data Version Control (DVC) and git. The dataset consists of song details from January 2000 to December 2020. The project includes preprocessing steps such as removing columns, correcting spelling, removing punctuation, and lemmatization, with data versioning for each step.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Generating Initial Data](#generating-initial-data)
- [Data Preprocessing](#data-preprocessing)
- [Versioning with DVC](#versioning-with-dvc)
- [Viewing Data Versions](#viewing-data-versions)
- [Usage](#usage)

## Introduction

This project demonstrates how to manage and preprocess a dataset of songs, with data versioning using DVC. Each preprocessing step is versioned, allowing you to track changes and revert to previous versions if necessary.

## Setup

### Install Dependencies

1. Install Python packages:
    ```sh
    pip install pandas faker textblob nltk dvc
    ```

2. Install DVC:
    ```sh
    pip install dvc
    ```

### Initialize DVC

1. Initialize DVC in your project directory:
    ```sh
    dvc init
    ```

2. Create a `.gitignore` file if it doesn't exist:
    ```sh
    touch .gitignore
    ```

3. Add common patterns to `.gitignore`:
    ```sh
    echo ".dvc/" >> .gitignore
    echo ".dvc/tmp/" >> .gitignore
    echo "__pycache__/" >> .gitignore
    echo "*.py[cod]" >> .gitignore
    echo ".ipynb_checkpoints/" >> .gitignore
    echo ".DS_Store" >> .gitignore
    echo "Thumbs.db" >> .gitignore
    echo "venv/" >> .gitignore
    ```

## Generating Initial Data

Run the script to generate initial data if the `songs.csv` file doesn't exist:

```sh
python your_script.py
```

This will create a songs.csv file with song details from January 2000 to December 2020.

## Data Preprocessing

The script allows you to perform various preprocessing steps with versioning:

Remove the 'singer-birthplace' column
Correct spelling mistakes
Remove punctuation from song names
Lemmatize song names
Each step is optional and controlled via user input.

## Versioning with DVC

### Adding Data to DVC
Add the data file to DVC:

```
dvc add songs.csv
```
Commit the changes to git:

```
git add songs.csv.dvc .gitignore
git commit -m "Initial data generation"
```
### Save Version for Each Preprocessing Step
The script will save a version for each preprocessing step using the save_version method, which runs the following commands:

Add the CSV file to DVC:

```
dvc add songs.csv
```
Commit the changes to git:

```
git add songs.csv.dvc .gitignore
git commit -m "Description of the change"
```
## Viewing Data Versions

Check DVC Status

```
dvc status
```
View Git Commit History
```
git log --oneline
```
### Checkout a Specific Version
Checkout a specific version:

```
git checkout <commit_hash>
dvc checkout
```
Replace <commit_hash> with the hash of the commit you want to check out.

### Compare Versions
```
dvc diff <previous_commit> <current_commit>
```
Replace <previous_commit> and <current_commit> with the appropriate commit hashes to see what has changed between these two versions.


## Usage

Main Script
Run the main script to preprocess data and manage versions:

```
python your_script.py
```
The script will prompt you to perform preprocessing steps. Respond with 'y' or 'n' to proceed with each step.

## DataManager Class
The DataManager class handles the preprocessing steps and versioning. Methods include:

remove_column(column_name): Removes a specified column.
correct_spelling(): Corrects spelling mistakes in the song-name column.
remove_punctuation(): Removes punctuation from the song-name column.
lemmatize(): Lemmatizes words in the song-name column.
save_version(message): Saves the current state of the data and commits it with a message.

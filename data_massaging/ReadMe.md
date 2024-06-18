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


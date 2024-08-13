# Cryptocurrency Exchange Fraud Detection Project

### Overview
This project aims to detect fraudulent cryptocurrency exchanges using machine learning models. The project is organized into several key components, including data collection and preprocessing, model training, and evaluation. The outputs from the models include performance metrics such as accuracy and others.

### Project Structure

data_prep/: This folder contains scripts and tools used for data collection and preprocessing. It includes everything needed to clean, transform, and prepare the dataset for model training.

models/: This folder includes Colab notebooks for the different models used in this study. The models must be executed in Google Colab. Each notebook is designed to load the preprocessed dataset and train a specific machine-learning model.

data/: This folder should contain the dataset used in this study. The dataset must be loaded from this folder into the model notebooks before running them.
Getting Started

### Data Preparation:
Start by exploring the data_prep/ folder. 

Follow the instructions provided in the scripts to preprocess the raw data.

Ensure that the preprocessed data is saved in the data/ folder.

### Running the Models:
Open the Colab notebooks in the models/ folder.

Load the preprocessed dataset from the data/ folder.

Execute the cells in the notebooks to train and evaluate the models.

Each notebook will output the model's performance metrics, including accuracy.
Requirements

Google Colab: The model notebooks are designed to be run in Google Colab, so no local environment setup is necessary.

Dataset: Ensure the dataset is correctly placed in the data/ folder before running the models.

### Outputs

The primary outputs from running the model notebooks are the accuracy and other performance metrics for each model. These metrics are essential for evaluating the effectiveness of the fraud detection techniques.

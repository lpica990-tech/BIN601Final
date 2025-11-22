BIN601 Final Project Package
Project Overview

This project contains the final package for the BIN601 course. It includes scripts, data files, and documentation needed to replicate the analyses and results. The main goal is to demonstrate skills in data processing, filtering, and visualization in a bioinformatics context.

Project Structure

biosample_filter.py — Main Python script for filtering BioSample data

data/ — Folder containing input data files

output/ — Folder where output files will be saved

requirements.txt — Python dependencies

Installation

Clone the repository and install dependencies:

git clone https://github.com/lpica990-tech/BIN601Final.git
cd BIN601_FINAL_PROJECT_PACKAGE
pip install -r requirements.txt
Usage

Run the main script with a text file of BioSample IDs and a metadata CSV file:

python biosample_filter.py --ids sample_ids.txt --metadata metadata.csv --output filtered_results.csv
Features

Filter datasets based on BioSample IDs

Output CSV files with metadata and survey responses

Easy command-line interface

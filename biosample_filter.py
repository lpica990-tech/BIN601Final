"""
biosample_filter.py
Author: Lydia Picariello
Course: BIN 601 Final Project

Description:
    Standalone Python script that takes a text file containing NCBI BioSample IDs,
    loads a metadata CSV file, filters the dataset based on the IDs provided, and
    outputs a CSV reporting:
        - BioSample ID
        - A selected survey-question column.

Folder Structure (default):
    example_inputs/   -> input ID lists
    metadata/         -> metadata.csv
    outputs/          -> filtered CSV exports

Usage (with defaults):
    python3 biosample_filter.py \
        --ids example_inputs/input1.txt \
        --metadata metadata/metadata.csv \
        --question host_disease \
        --output outputs/filtered.csv
"""

import argparse
import pandas as pd
import sys
import os


def load_ids(path):
    """Load NCBI BioSample IDs from a text file (one ID per line)."""
    try:
        with open(path, "r") as f:
            ids = [line.strip() for line in f if line.strip()]
        return ids
    except FileNotFoundError:
        print(f"ERROR: ID file not found: {path}")
        sys.exit(1)


def load_metadata(path):
    """Load metadata CSV containing BioSample information."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"ERROR: Metadata CSV not found: {path}")
        sys.exit(1)
    except pd.errors.ParserError:
        print("ERROR: Metadata file is not a valid CSV.")
        sys.exit(1)


def main():

    parser = argparse.ArgumentParser(
        description="Filter a metadata CSV using a list of NCBI BioSample IDs."
    )

    # DEFAULT PATHS BASED ON YOUR NEW FOLDER STRUCTURE
    parser.add_argument(
        "--ids",
        default="example_inputs/input1.txt",
        help="Path to text file containing BioSample IDs. Default: example_inputs/input1.txt"
    )

    parser.add_argument(
        "--metadata",
        default="metadata/metadata.csv",
        help="Path to metadata CSV file. Default: metadata/metadata.csv"
    )

    parser.add_argument(
        "--question",
        required=True,
        help="Column name for the survey question to extract."
    )

    parser.add_argument(
        "--output",
        default="outputs/filtered.csv",
        help="Output CSV file path. Default: outputs/filtered.csv"
    )

    parser.add_argument(
        "--id_column",
        default="BioSample",
        help="Column name in metadata containing BioSample IDs (default: BioSample)."
    )

    args = parser.parse_args()

    # Ensure output directory exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load input data
    ids = load_ids(args.ids)
    df = load_metadata(args.metadata)

    # Check required columns exist
    for col in [args.id_column, args.question]:
        if col not in df.columns:
            print(f"ERROR: Column '{col}' not found in metadata.")
            print("Available columns:", ", ".join(df.columns))
            sys.exit(1)

    # Filter metadata by IDs
    filtered = df[df[args.id_column].astype(str).isin(ids)]

    if filtered.empty:
        print("WARNING: No matching IDs found in metadata.")
    else:
        print(f"Found {len(filtered)} matching records.")

    # Save output CSV
    try:
        filtered[[args.id_column, args.question]].to_csv(args.output, index=False)
        print(f"Filtered CSV saved to: {args.output}")
    except Exception as e:
        print("ERROR writing output:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

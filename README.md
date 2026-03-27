University Data Analyzer
Project Overview
This repository contains a Python-based data utility designed to process and clean academic performance records. The tool identifies missing entries within a student dataset and applies statistical imputation to ensure the data remains viable for further analysis. This project demonstrates the application of mathematical logic to practical data engineering challenges.

Core Functionality
Data Imputation: Automatically detects null values and replaces them using the Median of the respective column.

Statistical Integrity: The choice of Median over Mean was made to prioritize robustness against outliers. In datasets where specific individuals may have extreme scores, the Median provides a more accurate representation of the central tendency, preventing skewed results during the cleaning phase.

Automated Filtering: Following imputation, the script performs a secondary check to remove any records that remain critically incomplete, ensuring the final output is ready for high-fidelity reporting.

Dynamic Reporting: Utilizes formatted string literals (f-strings) to generate clean, human-readable summaries of subject averages rounded to two decimal places.

Professional Background
I am an MPhil in Mathematics with seven years of experience as a University Lecturer, specializing in teaching Calculus, Linear Algebra, Differential Equations, and Numerical Computing to Computer Science students.

This project is a key milestone in Week 5 of a 16-week intensive transition into Data Analytics and Software Engineering. My objective is to leverage my academic background in mathematical rigor to build high-integrity data solutions.

Technical Stack
Language: Python

Library: Pandas

Data Format: CSV

Usage Instructions
Clone the repository to your local machine.

Ensure student_scores.csv is located in the root directory.

Execute the analysis script:

Bash
python analyzer.py
The cleaned dataset will be exported as cleaned_student_data.csv.

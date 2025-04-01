#!/usr/bin/env pwsh
# Define the variable for the directory name
$directoryName = ".\2024\14"

# Create the nested directories
New-Item -Path $directoryName -ItemType Directory -Force
echo "a" >> "$directoryName\input";
echo "a" >> "$directoryName\example";
echo "a" >> "$directoryName\part1_jan.py";
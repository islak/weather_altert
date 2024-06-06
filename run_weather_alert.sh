#!/bin/bash

# Navigate to the project directory
cd /Users/hershkalsi/weather_project

# Activate the virtual environment
source venv/bin/activate

# Load environment variables from the .env file
export $(grep -v '^#' .env | xargs)

# Run the weather alert script
./weather_alert.py

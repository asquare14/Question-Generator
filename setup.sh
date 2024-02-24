#!/bin/bash

# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv could not be found, installing..."
    python -m pip install --user virtualenv
fi

# Create virtual environment
if [ ! -d "venv" ]
then
    echo "Creating virtual environment..."
    virtualenv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
if [ -f "requirements.txt" ]
then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found"
fi
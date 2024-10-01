#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

echo "Starting the build process..."

# Step 1: Install Python dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 2: Run Django collectstatic to gather static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 3: Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Step 4: Any additional build steps (if needed)
# Example: Compilation, asset optimization, etc.
echo "Running additional build steps..."
# Add any custom build steps here

echo "Build process completed successfully!"

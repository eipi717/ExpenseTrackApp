# Use a lightweight Python base image
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port that your Flask app runs on (default 5000)
EXPOSE 5000

# Set the environment variables for Flask
# (Adjust or remove FLASK_ENV if you do NOT want debug mode)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Command to run the Flask app
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
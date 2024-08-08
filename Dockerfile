# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /flask_app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy environment variables
RUN cp .env.prod .env

# Expose port 5000 for the Flask app
EXPOSE 5000

# Starting the app
# ---
# Initialize the database, run migrations, and upgrade the database
RUN flask db init || echo "Database already initialized"
RUN flask db migrate -m "Initial migration"
RUN flask db upgrade

# Command to run the web server with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "5", "wsgi:app"]
# ---
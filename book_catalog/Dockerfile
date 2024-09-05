# Your Solution
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /book_catalog

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app/ .

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV DATABASE_URL="postgresql://sit722_part3_7xjc_user:c5pz0A5t53ODkjePvHQ4c5JpnxukHAKR@dpg-crcbh9dsvqrc73cht100-a.oregon-postgres.render.com/sit722_part3_7xjc"

# Command to run the FastAPI app with Uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port 4000
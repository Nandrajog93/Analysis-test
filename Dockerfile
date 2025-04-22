# Use a base Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python application code into the container
COPY . /app
COPY requirements.txt .
# Install dependencies (you'll need a `requirements.txt` file with your app dependencies)
RUN pip install -r requirements.txt



# Expose the port the app will run on
EXPOSE 5100
EXPOSE 8086
# Set the environment variable for MongoDB URI (can be customized in docker-compose.yml)
#ENV MONGO_URI=mongodb://mongo:27017



# Command to run the app
CMD ["python", "main.py"]

# Use an official Python runtime as a parent image
FROM python:3.13.0b1-slim

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container at /dashboard
COPY . /src

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables for local, dev, and prod
ENV ENVIRONMENT local
# ENV ENVIRONMENT dev
# ENV ENVIRONMENT prod

# Run dashboard.py when the container launches
CMD ["python", "dashboard.py"]

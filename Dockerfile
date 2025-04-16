FROM python:3.9-slim

# Install required packages
RUN pip install flask tensorflow pillow

# Copy project files into the container
WORKDIR /app
COPY . .

# Expose port and run the Flask app
EXPOSE 5000
CMD ["python", "server.py"]

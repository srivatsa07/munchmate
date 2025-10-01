# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /code/

# Copy entrypoint script and set permissions
# COPY entrypoint.sh /code/
# RUN chmod +x /code/entrypoint.sh
# ENTRYPOINT ["/code/entrypoint.sh"]

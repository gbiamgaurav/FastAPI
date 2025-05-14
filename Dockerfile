
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
# Set a working directory early for clearer paths
WORKDIR /app

# Copy only the requirements file first to leverage caching
COPY requirements.txt .

# Install pip requirements with no cache directory
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# Uncomment the following lines if you need to run as a non-root user
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "first_api:app"]
CMD ["uvicorn", "first_api:app", "--host", "0.0.0.0", "--port", "8000"]
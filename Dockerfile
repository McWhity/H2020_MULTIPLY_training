# 1. Usage of python 3.10
FROM python:3.10-slim

# 2. Install system dependencies required for Git packages, GDAL, and C-extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    libgdal-dev \
    gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# 3. Set up environment variables so the compiler can find GDAL headers
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app/

# 4. Copy the clean requirements file
COPY requirements.txt /tmp/requirements.txt

# 5. Dynamically match and install the correct Python GDAL bindings first, 
#    then install the rest of your requirements.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir "gdal==$(gdal-config --version).*" && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# 6. Copy everything in root dir to image
COPY . /app/

# 7. Install your local package in editable mode
RUN pip install --no-cache-dir -e .

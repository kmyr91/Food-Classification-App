# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the Node.js dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Install python and pip
RUN apt-get update && apt-get install -y \
  python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the application
CMD [ "node", "src/api/server.js" ]
ENV TF_CPP_MIN_LOG_LEVEL=3 TF_IGNORE_MAX_LOG_LEVEL=gcs

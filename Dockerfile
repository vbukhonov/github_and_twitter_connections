FROM python:3.7.5-alpine3.10

# Set work directory
WORKDIR /usr/src/simple_branching

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/github_and_twitter_connections/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/github_and_twitter_connections/entrypoint.sh

# Copy project
COPY . /usr/src/github_and_twitter_connections/

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/github_and_twitter_connections/entrypoint.sh"]
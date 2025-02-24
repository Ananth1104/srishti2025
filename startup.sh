#!/bin/bash

# Set the number of Gunicorn workers (adjust based on expected load)
WORKERS=4    # Number of worker processes
THREADS=10   # Number of threads per worker

# Start the Gunicorn server
exec gunicorn -w $WORKERS --threads $THREADS -k gthread -b 0.0.0.0:$PORT app:app

echo "running"

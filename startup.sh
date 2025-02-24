echo "gunicorn -w 4 -b 0.0.0.0:\$PORT app:app" > startup.sh
chmod +x startup.sh
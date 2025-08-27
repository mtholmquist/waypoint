FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn
COPY waypoint_server.py ./ 
COPY README.md ./ 
COPY assets ./assets
ENV WAYPOINT_HOST=0.0.0.0 WAYPOINT_PORT=8888
EXPOSE 8888
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:8888", "waypoint_server:app"]

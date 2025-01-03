from flask import Flask
from consul import Consul
import threading
import time

app = Flask(__name__)
consul = Consul()

# Register service with Consul
def register_service():
    # Register Service 1 with Consul, including health check
    consul.agent.service.register(
        name="service1",
        service_id="service 1-1",
        address="127.0.0.1",
        port=5001,
        tags=["python", "flask"],
        check={
            "http": "http://127.0.0.1:5001/health",  # URL for the health check
            "interval": "10s",  # Health check frequency
            "timeout": "5s",  # Timeout for health check
        }
    )
    print("Service 1 registered with Consul")

# Health check function
@app.route('/health')
def health_check():
    return "Service 1 is healthy!", 200  # Simple health check endpoint

# Start service registration and health check in background
def start_registration():
    register_service()

@app.route('/')
def hello():
    return "Hello from Service 1!"

if __name__ == "__main__":
    start_registration()
    app.run(host='0.0.0.0', port=5001)



from flask import Flask, jsonify
from consul import Consul
import requests

app = Flask(__name__)
consul = Consul()

# Discover Service 1 from Consul
def discover_service1():
    try:
        services = consul.catalog.services()[1]
        print("All Services in Consul:", services)  # Log all available services
        if "service1" in services:
            service = consul.catalog.service("service1")[1]
            print("Service details:", service)
            if service:
                service_info = service[0]
                service_address = service_info.get('ServiceAddress', '127.0.0.1')
                service_port = service_info['ServicePort']
                service1_url = f"http://{service_address}:{service_port}/"
                print("Constructed service1_url:", service1_url)
                return service1_url
    except Exception as e:
        print("Error during service discovery:", e)
    return None

@app.route('/')
def call_service1():
    service1_url = discover_service1()
    if service1_url:
        try:
            response = requests.get(service1_url)
            return jsonify({"service1_response": response.text})
        except Exception as e:
            return jsonify({"error": f"Failed to connect to Service 1: {e}"})
    return jsonify({"error": "Service 1 not found in Consul"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

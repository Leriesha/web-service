# Service Discovery in Python Microservices using Consul

This repository demonstrates a basic implementation of microservices in Python with service discovery facilitated by Consul. The setup includes two services:

1. **Service 1** - A simple Flask application registered with Consul, including a health check endpoint.
2. **Service 2** - Another Flask application that discovers and communicates with Service 1 via Consul.

## Prerequisites

Before running the services, ensure the following are installed on your system:

- Python 3.8 or higher
- [Consul](https://developer.hashicorp.com/consul/docs/install)
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/python-microservices-service-discovery.git
   cd python-microservices-service-discovery
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Services

### Step 1: Start Consul Agent

Start a Consul agent in development mode on your local machine:
```bash
consul agent -dev
```

This will start Consul on `http://127.0.0.1:8500`.

### Step 2: Start Service 1

Run the `service1.py` script to start Service 1:
```bash
python service1.py
```

This registers Service 1 with Consul and starts the Flask application on `http://127.0.0.1:5001`.

### Step 3: Start Service 2

Run the `service2.py` script to start Service 2:
```bash
python service2.py
```

Service 2 will discover Service 1 via Consul and start a Flask application on `http://127.0.0.1:5002`.

## Testing the Services

1. Open your browser or use a tool like `curl` or Postman to test Service 1 directly:
   ```bash
   curl http://127.0.0.1:5001/
   ```
   Expected response: `Hello from Service 1!`

2. Test the health check endpoint of Service 1:
   ```bash
   curl http://127.0.0.1:5001/health
   ```
   Expected response: `Service 1 is healthy!`

3. Test Service 2 to see if it can call Service 1:
   ```bash
   curl http://127.0.0.1:5002/
   ```
   Expected response: JSON with the response from Service 1.

## Directory Structure

```
.
├── service1.py   # Code for Service 1
├── service2.py   # Code for Service 2
├── requirements.txt   # Python dependencies
└── README.md     # Project documentation
```

## Key Features

1. **Service Registration**: Service 1 registers itself with Consul, including a health check.
2. **Service Discovery**: Service 2 discovers Service 1 dynamically through Consul.
3. **Health Checks**: Ensures Service 1 is available before communication.

## Dependencies

- `Flask`: Python web framework for building APIs.
- `python-consul`: Python client for interacting with Consul.
- `requests`: Library for making HTTP requests in Python.

## Notes

- Ensure Consul is running before starting the services.
- You can view the registered services in the Consul UI at `http://127.0.0.1:8500`.

## Future Enhancements

- Add more services for demonstrating a more complex microservices architecture.
- Implement load balancing for multiple instances of Service 1.
- Use Docker for containerizing the services and Consul.
- Implement secured communication between services.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


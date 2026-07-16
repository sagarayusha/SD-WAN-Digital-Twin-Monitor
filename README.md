# SD-WAN Digital Twin Monitor

## Project Overview
This project implements a real-time **SD-WAN Network Monitoring System** with a predictive **Digital Twin** concept. It bridges network simulation (Cisco Packet Tracer) with a Python-based backend to monitor the operational status of routers and simulated industrial hardware (turbines).

## Key Features
- **Network Topology**: Simulated SD-WAN environment in Cisco Packet Tracer.
- **Predictive Engine**: A Python backend (FastAPI) that processes sensor data to simulate turbine status.
- **Real-time Monitoring**: Live status dashboard displaying system health (UP/DOWN/CRITICAL).
- **Digital Twin Concept**: Maps real-time network latency and sensor data to a predictive maintenance dashboard.

## Tech Stack
- **Network**: Cisco Packet Tracer
- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML5, Chart.js for real-time visualization

## How it Works
1. The **Packet Tracer** environment simulates the SD-WAN routers.
2. The **backend.py** script performs continuous connectivity checks (ping) and simulates sensor data (vibration/temperature).
3. The **dashboard** (index.html) fetches this data via FastAPI and visualizes the network/turbine status in real-time.

## Setup Instructions
1. Install dependencies: `pip install fastapi uvicorn`
2. Run the backend: `uvicorn backend:app --reload`
3. Open `index.html` in your browser to view the live dashboard.

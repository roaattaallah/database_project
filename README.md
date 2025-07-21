# BookNest: Cloud-Native Bookstore API

## Project Overview

**BookNest** is a scalable, cloud-native RESTful API for managing a digital bookstore, built with Python (Flask) and MongoDB. It demonstrates modern backend engineering practices, including containerization with Docker and orchestration-ready Kubernetes manifests. The API supports full CRUD operations for book records, making it ideal for learning, prototyping, or as a foundation for production-grade microservices.

## Features

- **RESTful API**: Endpoints for creating, reading, updating, and deleting book records.
- **MongoDB Integration**: Uses MongoDB for flexible, document-based storage.
- **Containerized**: Easily deployable with Docker.
- **Kubernetes Ready**: Includes manifests for deployment, service, config, and network policy.
- **Production-Ready**: Configured for Gunicorn WSGI server and scalable deployment.

## Endpoints

- `POST /books` — Add a new book
- `GET /books` — List all books
- `GET /books/<isbn>` — Get details for a specific book
- `PUT /books/<isbn>` — Update a book’s details
- `DELETE /books/<isbn>` — Remove a book

## Tech Stack

- **Backend**: Python 3.8, Flask, Gunicorn
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Kubernetes (YAML manifests included)

## Quick Start

### Prerequisites

- Docker
- (Optional) Kubernetes (minikube, kind, or a cloud provider)

### Local Development

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask app**
   ```bash
   python RoasFlaskApp.py
   ```
   The API will be available at `http://localhost:5007`.

### Docker

1. **Build the image**
   ```bash
   docker build -t booknest-api .
   ```
2. **Run the container**
   ```bash
   docker run -p 5007:5007 booknest-api
   ```

### Kubernetes

- Apply the manifests in your cluster:
  ```bash
  kubectl apply -f mongo-deployment.yaml
  kubectl apply -f mongodb-service.yaml
  kubectl apply -f configmap.yaml
  kubectl apply -f python-deployment.yaml
  kubectl apply -f python-service.yaml
  kubectl apply -f network.yaml
  ```

## Example Book Data

Sample book records are provided in `bookstore.json` for easy import or testing.

## Author

Roa K. A. Attaallah 
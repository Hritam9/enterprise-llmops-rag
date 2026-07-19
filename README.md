# Enterprise LLMOps RAG Platform

## Overview

## Features

## Architecture

## Tech Stack

## Project Structure

## Quick Start

## Configuration

## API Endpoints

## Screenshots

## Monitoring

## Evaluation

## CI/CD

## Deployment

## Future Improvements

## License

# Architecture Diagram (Mermaid)
```mermaid
flowchart TD

User --> Streamlit

Streamlit --> FastAPI

FastAPI --> ChatService

ChatService --> RAGPipeline

RAGPipeline --> HybridRetriever

HybridRetriever --> ChromaDB

HybridRetriever --> BM25

RAGPipeline --> Groq

FastAPI --> SQLite

FastAPI --> MLflow

FastAPI --> Prometheus

Prometheus --> Grafana
```

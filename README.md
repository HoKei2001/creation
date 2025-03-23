# Code Generation Platform

A platform for generating and executing code using LLM in a sandbox environment.

## Features

- Code generation using LLM
- Secure code execution in Docker containers
- Support for multiple programming languages
- Modern React frontend with Material-UI
- FastAPI backend with Docker support

## Prerequisites

- Docker and Docker Compose
- OpenAI API key (for code generation)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd code-generation-platform
```

2. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

3. Build and start the services:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development

### Backend

The backend is built with FastAPI and uses Poetry for dependency management. To run it locally:

```bash
cd app
poetry install
poetry run uvicorn main:app --reload
```

### Frontend

The frontend is built with React and TypeScript. To run it locally:

```bash
cd frontend
npm install
npm start
```

## Security

- Code execution is performed in isolated Docker containers
- Resource limits are enforced on containers
- Network access is disabled for running containers
- Input validation and sanitization are implemented

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# Chatbot with Execution Flow Visualization

This project implements a chatbot with a visual representation of its execution flow, built with React and FastAPI.

## Project Structure

```
app/
├── frontend/          # React frontend
│   ├── src/          # Source code
│   ├── package.json  # NPM dependencies
│   └── tsconfig.json # TypeScript configuration
│
└── backend/          # FastAPI backend
    ├── main.py      # Main application
    └── pyproject.toml # Poetry dependencies
```

## Setup and Installation

### Backend

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Run the backend server:
```bash
cd app/backend
poetry run python main.py
```

### Frontend

1. Install dependencies:
```bash
cd app/frontend
npm install
```

2. Start the development server:
```bash
npm start
```

## Development

- Frontend runs on: http://localhost:3000
- Backend runs on: http://localhost:8000

## Features

- Real-time chat interface
- Visual execution flow display
- Step-by-step task processing visualization
- Modern and responsive UI design

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

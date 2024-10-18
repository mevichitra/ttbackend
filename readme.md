# Tattoo Tattva FastAPI Backend

This repository contains the backend code for the Tattoo Tattva application, built using FastAPI.

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/tattoo-tattva-backend.git
    cd tattoo-tattva-backend
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Rename `constants_copy.py` to `constants.py` in your local environment and update it with your credentials:

    ```sh
    mv constants_copy.py constants.py
    ```

2. Create a `.env` file in the root directory and update it with your environment variables. Use the `.env.example` file as a reference.

### Running the Application

1. Start the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

2. The application will be available at `http://127.0.0.1:8000`.

### API Documentation

You can access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

### License

This project is licensed under the MIT License.
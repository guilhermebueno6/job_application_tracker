# Job Application Tracker

This is a Flask-based web application designed to help track job applications.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)
- Git (optional, if cloning the repository)

### Steps to Install and Run the Application

1. **Clone the Repository (if applicable)**
   ```sh
   git clone <repository-url>
   cd job_application_tracker
   ```

2. **Run the Setup Script**
   ```sh
   python setup.py
   ```
   This script will:
   - Install required dependencies.
   - Prompt you to enter an OPENAI authentication token for the skill summarizing functionality. (If you do not wish to use this feature you may leave it empty)
   - Create a local SQLite database (`main_app_db.db`).
   - Set up the necessary database table.

3. **Run the Application**
   ```sh
   flask run
   ```
   The application will start running on `http://127.0.0.1:5000/` by default.

## Usage
- Open `http://127.0.0.1:5000/` in your browser.
- Use the interface to track job applications.

## Dependencies
This project relies on the following Python packages:
- Flask
- SQLite3
- BeautifulSoup4
- Requests
- OpenAI (for GPT integration)

All dependencies will be installed automatically when running `setup.py`.

## Database Schema
The SQLite database (`main_app_db.db`) contains the following table:

```sql
CREATE TABLE job_application(
    link TEXT,
    company TEXT,
    title TEXT,
    description TEXT,
    skills TEXT,
    stage TEXT,
    date_applied TEXT
);
```

## Troubleshooting
### Common Issues and Solutions
- **Dependencies not installing**: Ensure you have the correct Python version (`python --version`).
- **Database errors**: Delete `main_app_db.db` and re-run `setup.py` to recreate it.
- **Port conflicts**: If Flask fails to start, check if another process is using port 5000 (`lsof -i :5000` on Linux/Mac or `netstat -ano | findstr :5000` on Windows).

## Contributing
If you wish to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them.
4. Push to your fork and create a Pull Request.

## License
This project is licensed under the MIT License.


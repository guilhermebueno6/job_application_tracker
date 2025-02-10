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

3. **(Optional) Add custom URL**
   If you want to utilize the custom url `jobapplication.local` do the following steps:
   - On Windows:
      -  Open Notepad as Administrator
      -  Edit the file: `C:\Windows\System32\drivers\etc\hosts`
   - On Mac:
      -  Open Terminal and run: ```sudo nano /etc/hosts```

   - Add this to the bottom of the file:
      ```127.0.0.1 jobapplication.local```
4. **Run the Application**

   ```sh
   flask run
   ```

   - If using the custom url, run this instead
   ```sh
      sudo python3 app.py
   ```

   The application will start running on `http://127.0.0.1:5000/` by default. (If using the custom url it will be available on `http://jobapplication.local`)

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
- html2text

All dependencies will be installed automatically when running `setup.py`.

## Database Schema
The SQLite database (`main_app_db.db`) contains the following table:

```sql
    CREATE TABLE job_application (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
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
- **If on Mac**: Comment out ``` pywin32==308 ``` on the requirements.txt file if not commented out
- **If on Windows**: Uncomment ``` pywin32==308 ``` on the requirements.txt file if commented out

## Contributing
If you wish to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them.
4. Push to your fork and create a Pull Request.

## License
This project is licensed under the MIT License.


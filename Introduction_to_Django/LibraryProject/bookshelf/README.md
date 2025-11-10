# 📚 Library Project (Task 0: Introduction to Django)

This repository contains the foundational setup for the Django-based "Library Project," created as part of the Alx_DjangoLearnLab curriculum.

---

## 🛠️ Setup and Environment

### Prerequisites

* Python 3.8+
* Git

### Installation and Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/Alx_DjangoLearnLab.git](https://github.com/YourUsername/Alx_DjangoLearnLab.git)
    cd Alx_DjangoLearnLab/Introduction_to_Django
    ```

2.  **Activate Virtual Environment:**
    Ensure your virtual environment (`.venv`) is active:
    ```bash
    # For Git Bash (MINGW64)
    source .venv/Scripts/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install Django
    ```

4.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

The development server will be accessible at: **`http://127.0.0.1:8000/`**

---

## 📂 Project Structure

The project follows the standard Django layout:

* **`manage.py`**: Command-line utility for interacting with the project.
* **`LibraryProject/`**: The inner configuration package containing:
    * `settings.py`: Project configurations (database, static files, etc.).
    * `urls.py`: The project's main URL dispatcher.
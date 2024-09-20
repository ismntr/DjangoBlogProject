
# DjangoBlogProject - UPOD (User Post Dashboard) Project

## Description
The DjangoBlogProject is a web application built with Django (Python) that allows users to manage their personal blog posts. Users can create, view, update, and delete their own posts. Each post contains a title, description, and optionally, an image. The application also includes an admin panel for managing posts and user authentication features for login and registration.

The project is designed to be user-friendly, with features like soft deletion (where deleted posts remain in the database but are hidden from the interface) and personalized post management, ensuring that users can only view and edit their own content. Public users can view all posts but cannot edit them.

## Project Steps

### Step 1: Database Operations (CRUD)
- Implement all CRUD operations (Create, Read, Update, Delete) for posts.
- Posts must include fields for the title, description (both required), and an optional image.
- Admins should be able to manage posts using the Django admin panel (or via Django shell).

### Step 2: Soft Deletion
- Instead of permanently deleting posts from the database, a soft deletion is used.
- Each post has an `is_deleted` field, which is set to `True` when a post is deleted.
- Deleted posts will not be shown on the user interface.

### Step 3: User Authentication and Interface
- Implement user login and registration.
- Each user should only be able to see and edit their own posts.
- Public users (not logged in) can view all posts but cannot edit them.
- Logged-in users can edit their own posts.

## Running the Project

Follow these steps to run the project after downloading:

1. Open a terminal and navigate to the project directory (where the `manage.py` file is located):
   ```bash
   cd /path/to/your/project
   ```

2. Activate your virtual environment (if it's not already activated):
   ```bash
   source venv/bin/activate
   ```

3. Run the project:
   ```bash
   python manage.py runserver
   ```

4. Once the server starts, open your browser and go to:
   - http://127.0.0.1:8000/ 
   - or http://localhost:8000/

Here, you will be able to see the project live.

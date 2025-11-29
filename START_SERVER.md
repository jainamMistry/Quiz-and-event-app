# How to Start the Django Server

## To start the server:

1. Open a terminal/command prompt in the project directory:
   ```
   cd C:\Users\JAINAM MISTRY\OneDrive\Documents\django\quiz_events
   ```

2. Run the following command:
   ```
   python manage.py runserver
   ```

3. You should see output like:
   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

4. Open your browser and visit:
   - http://127.0.0.1:8000/
   - http://127.0.0.1:8000/quizzes/
   - http://127.0.0.1:8000/events/

## If you get a "port already in use" error:

Use a different port:
```
python manage.py runserver 8001
```

Then access: http://127.0.0.1:8001/

## To stop the server:

Press `CTRL+C` in the terminal where the server is running.


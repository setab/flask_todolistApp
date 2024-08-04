from app import app, db  # Import the app and db from your main application file

with app.app_context():  # Create an application context
    db.create_all()  # Create the database tables

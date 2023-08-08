from __init__ import db, create_app

# Create the Flask application instance
app = create_app()

# Run the database creation within the application context
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run()

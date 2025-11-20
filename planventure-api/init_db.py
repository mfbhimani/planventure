#!/usr/bin/env python3
"""
Database initialization script for PlanVenture API.
Run this script to create all database tables.

Usage:
    python init_db.py
"""

from app import app, db
from models import User, TestModel

def init_database():
    """Initialize the database and create all tables."""
    try:
        with app.app_context():
            # Drop all tables (optional - uncomment if you want fresh start)
            db.drop_all()
            print("Dropped all existing tables.")
            
            # Create all tables
            db.create_all()
            print("Created all database tables successfully.")
            
            # Get table information
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\nAvailable tables: {tables}")
            
            # Print columns for each table
            for table in tables:
                columns = inspector.get_columns(table)
                print(f"\nTable '{table}' columns:")
                for col in columns:
                    print(f"  - {col['name']}: {col['type']}")
            
            # Optionally add test data
            add_test_data = input("\nDo you want to add test data? (y/n): ").lower()
            if add_test_data == 'y':
                create_test_data()
                
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        raise

def create_test_data():
    """Create test data for development."""
    try:
        # Check if test data already exists
        existing_test = TestModel.query.first()
        if not existing_test:
            test = TestModel(name="test_record")
            db.session.add(test)
            print("Added TestModel record.")
        else:
            print("TestModel data already exists.")
        
        # Add a test user if needed
        existing_user = User.query.filter_by(email="test@example.com").first()
        if not existing_user:
            from werkzeug.security import generate_password_hash
            test_user = User(
                email="test@example.com",
                password_hash=generate_password_hash("password123")
            )
            db.session.add(test_user)
            print("Added test User.")
        else:
            print("Test User already exists.")
        
        db.session.commit()
        print("\nTest data created successfully!")
        
    except Exception as e:
        db.session.rollback()
        print(f"Error creating test data: {str(e)}")
        raise

if __name__ == '__main__':
    print("=" * 50)
    print("PlanVenture Database Initialization")
    print("=" * 50)
    init_database()
    print("\nDatabase initialization complete!")

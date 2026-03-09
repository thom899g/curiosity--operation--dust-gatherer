import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    """
    Initialize Firebase Admin SDK with the credentials from the environment.
    """
    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
    if not cred_path:
        raise ValueError("FIREBASE_CREDENTIALS_PATH environment variable not set")
    
    # Check if the credentials file exists
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"Firebase credentials file not found at {cred_path}")
    
    # Initialize the app if it hasn't been initialized already
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    
    # Return the Firestore client
    db = firestore.client()
    return db

if __name__ == "__main__":
    db = initialize_firebase()
    print("Firebase initialized successfully.")
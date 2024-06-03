from pymongo import MongoClient
import logging

# Configure logging to save to a file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='animal_shelter.log',  # Log messages are saved to this file
                    filemode='a')  # Use 'a' for append mode; 'w' will overwrite the file each time


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, user='aacuser', password='1234', host='nv-desktop-services.apporto.com', port=31740, db='AAC', col='animals'):
        """Initialize MongoDB connection."""
        # Ensure that the connection string is constructed correctly
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]
    
    def create(self, data):
        """Create a document in the database. Returns True if successful, else False."""
        if data:
            try:
                self.collection.insert_one(data)
                logging.info("Document inserted successfully.")
                return True
            except Exception as e:
                logging.error(f"Insert failed: {e}")
                return False
        else:
            logging.error("Failed to insert: Data parameter is empty.")
            return False
    
    def read(self, query):
        """Read documents from the database. Returns a list of documents or an empty list if query fails."""
        if query:
            try:
                documents = list(self.collection.find(query))
                logging.info(f"Read {len(documents)} documents.")
                return documents
            except Exception as e:
                logging.error(f"Read failed: {e}")
                return []
    
    def delete(self, query):
        """Delete documents based on a query. Returns True if any documents were deleted."""
        if query:
            try:
                result = self.collection.delete_many(query)
                if result.deleted_count > 0:
                    logging.info(f"Deleted {result.deleted_count} documents.")
                    return True
                else:
                    logging.info("No documents matched the query.")
                    return False
            except Exception as e:
                logging.error(f"Delete failed: {e}")
                return False
        else:
            logging.error("Delete failed: Query is empty.")
            return False


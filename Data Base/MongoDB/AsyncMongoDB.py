import asyncio
import os
from dotenv import find_dotenv, load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(find_dotenv())

password = os.environ.get('MONGO_PASS')

async def connect_to_mongodb():
    uri = f"mongodb+srv://miraj:{password}@cluster0.tkzvadc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new async client and connect to the server
    client = AsyncIOMotorClient(uri)
    # Return the connected client
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!\n")
        return client
    except Exception as err:
        print(err)
        return err


async def get_database_names():
    client = await connect_to_mongodb()
    # Access the list_database_names method asynchronously
    dbs = await client.list_database_names()
    return dbs

async def main():
    db_list = await get_database_names()
    return db_list

if __name__ == '__main__':
    # Run the async main function using asyncio.run
    result = asyncio.run(main())
    print(result)

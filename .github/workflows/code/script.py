import os

# Get the secret from environment variables
my_secret = os.getenv('AZURE_CLIENT_ID')

if my_secret:
    print(f"The client value is: {my_secret}")
else:
    print("client id not found!")

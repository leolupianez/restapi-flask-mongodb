from pymongo import MongoClient, errors
from flask import Flask, request, jsonify
import os
from model import User, UserUpdate
from dotenv import load_dotenv
from bson.objectid import ObjectId
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# MongoDB Client Setup
try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client["restapi"]
    users = db["users"]

    client.admin.command("ping")
    print("Connected to MongoDB successfully")
except errors.ConnectionFailure:
    print("Failed to connect to MongoDB: Connection error")
except errors.ConfigurationError:
    print("Failed to connect to MongoDB: Configuration error")
except errors.OperationFailure:
    print("Failed to connect to MongoDB: Authentication error")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

# Add test user if it does not exist
if not users.find_one("66b3d17ce6d8e2f5b93324d3"):
    test_user = User(
        _id="66b3d17ce6d8e2f5b93324d3",
        first_name="Jorge",
        middle_name="Felix",
        last_name="Antinez",
        password="kshierjshnkaoif_9sjsf",
        phone="9999999999",
        session_token="rbvkur79jksfu_shjhu",
        created_datetime="2023-08-07T22:26:12.111Z",
        updated_datetime="2023-08-07T22:26:12.111Z",
    )

    users.insert_one(
        {
            "_id": test_user.id,
            "first_name": test_user.first_name,
            "middle_name": test_user.middle_name,
            "last_name": test_user.last_name,
            "password": test_user.password,
            "phone": test_user.phone,
            "session_token": test_user.session_token,
            "created_datetime": test_user.created_datetime,
            "updated_datetime": test_user.updated_datetime,
        }
    )


# Check if authorized
def authorize_request():
    auth_header = request.headers.get("Authorization")

    if auth_header != "Bearer laurhln7t4gkhlnfsp7ywho_hlsfl":
        return False
    return True


@app.route("/user", methods=["PUT"])
def update_user():
    if not authorize_request():
        return (
            jsonify({"Status": "failure", "reason": "Invalid authorization token"}),
            401,
        )

    try:
        # Validate and parse the request data
        data = request.json

        user_id = data["user_id"]
        user_data = UserUpdate(**data)

        update_data = {k: v for k, v in user_data.model_dump().items() if v is not None}

        # Update user in MongoDB
        result = users.update_one(
            {
                "_id": user_id,
                "session_token": request.headers.get("Session-Token"),
            },
            {"$set": update_data},
        )

        if result.matched_count == 0:
            return (
                jsonify(
                    {
                        "Status": "failure",
                        "reason": "User not found or the session token is not valid",
                    }
                ),
                404,
            )

        return jsonify({"Status": "success"}), 200
    except Exception as e:
        return jsonify({"Status": "failure", "reason": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)

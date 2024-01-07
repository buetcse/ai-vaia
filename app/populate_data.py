from utils import get_db
from app_models.models import User

db = get_db()

db.users.delete_many({})

insert_result = db.users.insert_one({
    "username": "user",  
    "password": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4", # 1234 
    "permissions": {
        "create_post": True,
        "review_post": True,
        "delete_post": True
    }
})

print("Inserted new user: ", insert_result.inserted_id)

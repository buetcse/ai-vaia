from pydantic import BaseModel, constr, PositiveInt
from datetime import datetime
from uuid import uuid4


class FacebookAPICredentials(BaseModel):
    page_id: str
    access_token: str


class TwitterAPICredentials(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str


class UserPermission(BaseModel):
    create_post: bool = False
    review_post: bool = False
    delete_post: bool = False


class User(BaseModel):
    username: str
    password: str
    profile_picture: str = None
    job_title: str = None
    permissions: UserPermission
    organization: str = None


class GenerationDetails(BaseModel):
    success: bool = False
    message: str = ""
    model_name: str = ""
    model_version: str = ""
    generated_at: datetime = datetime.now()


class PostedStatus(BaseModel):
    success: bool = False
    message: str = ""
    posted_at: datetime = datetime.now()
    post_url: str = ""


class Post(BaseModel):
    post_id: str = str(uuid4())
    platform: constr(regex="facebook|twitter") = None
    created_at: datetime = datetime.now()
    created_by: User
    prompt: str = ""  
    system_message: str = ""
    title: str = ""
    content: str = ""
    images: list[str] = []
    videos: list[str] = []
    background: str = ""
    generation_details: GenerationDetails
    posted_status: PostedStatus

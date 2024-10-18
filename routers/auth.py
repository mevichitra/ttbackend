from fastapi import APIRouter, HTTPException, status
from passlib.context import CryptContext
from pymongo.collection import Collection
from bson.objectid import ObjectId
from schemas import UserCreate, UserLogin, UserResponse
from database import db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_collection: Collection = db['users']

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict['password'] = hashed_password
    result = users_collection.insert_one(user_dict)
    new_user = users_collection.find_one({"_id": result.inserted_id})
    return UserResponse(
        id=str(new_user["_id"]),
        first_name=new_user["first_name"],
        last_name=new_user["last_name"],
        email=new_user["email"]
    )

@router.post("/login", response_model=UserResponse)
async def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    return UserResponse(
        id=str(db_user["_id"]),
        first_name=db_user["first_name"],
        last_name=db_user["last_name"],
        email=db_user["email"]
    )

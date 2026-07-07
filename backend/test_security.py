from app.utils.security import hash_password

password = "ShelfShare123"

hashed = hash_password(password)

print(hashed)
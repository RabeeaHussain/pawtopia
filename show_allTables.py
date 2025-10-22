from app import models
from app.database import SessionLocal, engine

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Start a session
db = SessionLocal()

# List of all table classes
tables = [
    models.User,
    models.Pet,
    models.VirtualPet,
    models.UserVirtualPet,
]

for table in tables:
    print(f"\n=== {table.__tablename__} ===")
    rows = db.query(table).all()
    if not rows:
        print("No records found.")
    else:
        for row in rows:
            # Print all attributes except private ones
            data = {k: v for k, v in row.__dict__.items() if not k.startswith("_")}
            print(data)

db.close()

from sqlalchemy import text
from app.database import engine, Base
from app import models

# Drop only app tables (ignore if they don't exist)
with engine.connect() as conn:
    tables_to_drop = ["pets","virtual_pets", "products", "users", "product_orders"]
    for table in tables_to_drop:
        conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))
    conn.commit()

# Recreate all tables based on models
Base.metadata.create_all(bind=engine)

print("✅ Database fully reset and tables recreated!")

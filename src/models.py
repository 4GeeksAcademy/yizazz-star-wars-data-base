from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Float, ForeignKey, relationship
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

favourites_planets = db.Table(
    "favourites_planets",
    db.Column("user_id", ForeignKey("user.id"), primary_key=True),
    db.Column("planets_id", ForeignKey("planets.id"), primary_key=True)
)

favourites_characters = db.Table(
    "favourites_characters",
    db.Column("user_id", ForeignKey("user.id"), primary_key=True),
    db.Column("characters_id", ForeignKey("planets.id"), primary_key=True)
)


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favourites_characters = relationship("Characters", secondary=favourites_characters, back_populates="fans")


class Planets(db.Model):
    __tablename__ = "planets"

    id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(100), nullable=False)
    Population: Mapped[Float] = mapped_column(float(255))


class Characters(db.Model):
    __tablenames__ = "characters"

    id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer(100))
    gender: Mapped[str] = mapped_column(String(50))

    fans = relationship("User", secondary=favourites_characters, back_populates="favourites_characters")







def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

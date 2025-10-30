from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

favourites_planets = db.Table(
    "favourites_planets",
    db.Column("user_id", ForeignKey("user.id"), primary_key=True),
    db.Column("planets_id", ForeignKey("planets.id"), primary_key=True)
)

favourites_characters = db.Table(
    "favourites_characters",
    db.Column("user_id", ForeignKey("user.id"), primary_key=True),
    db.Column("characters_id", ForeignKey("characters.id"), primary_key=True)
)


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favourites_characters = relationship("Characters", secondary=favourites_characters, back_populates="fans_characters")
    favourites_planets = relationship("Planets", secondary=favourites_planets, back_populates="fans_planets")




    def serialize(self):
        return {
        "id": self.id,
        "email": self.email,
        # do not serialize the password, its a security breach
    }


class Planets(db.Model):
    __tablename__ = "planets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[float] = mapped_column(Float)

    fans_planets = relationship("User", secondary=favourites_planets, back_populates="favourites_planets")

class Characters(db.Model):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(50))

    fans_characters = relationship("User", secondary=favourites_characters, back_populates="favourites_characters")



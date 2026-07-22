# SQLAlchemy 2.0-style models map classes to tables; access can be async.
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from datetime import datetime
 
class Base(DeclarativeBase): ...
 
class Conversation(Base):
    __tablename__ = "conversations"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    messages: Mapped[list["Message"]] = relationship(back_populates="conversation")
 
class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    role: Mapped[str]                       # 'user' or 'assistant'
    content: Mapped[str] = mapped_column(Text)
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")

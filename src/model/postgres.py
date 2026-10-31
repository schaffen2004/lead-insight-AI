from sqlalchemy import (
    BigInteger,
    SmallInteger,
    Integer,
    String,
    Numeric,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass

class Lead(Base):
    __tablename__ = "leads"

    lead_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False
    )
    age: Mapped[int | None] = mapped_column(SmallInteger)
    gender: Mapped[str | None] = mapped_column(String(20))


class LeadAcquisition(Base):
    __tablename__ = "lead_acquisition"

    lead_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("leads.lead_id", ondelete="CASCADE"),
        primary_key=True,
    )
    lead_source: Mapped[str | None] = mapped_column(String(50))
    referral_source: Mapped[str | None] = mapped_column(String(50))
    lead_status: Mapped[str | None] = mapped_column(String(20))
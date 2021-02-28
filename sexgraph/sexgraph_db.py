from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class University(Base):
    __tablename__ = "university"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email_domain = Column(String(64))


class Node(Base):
    __tablename__ = "node"

    id = Column(String(256), primary_key=True)
    encrypted_id = Column(String(256))
    university_id = Column(String(64), ForeignKey(University.id))
    gender = Column(String(8))
    major_department = Column(String(64))
    class_year = Column(Integer)

    __table_args__ = (UniqueConstraint("encrypted_id"),)


class NodeEdge(Base):
    __tablename__ = "node_edge"

    node_id = Column(String(256), ForeignKey(Node.id))
    edge_id = Column(String(256))
    sex_quality_rating = Column(Integer)
    relationship_classification = Column(Integer)

    __table_args__ = (PrimaryKeyConstraint("node_id", "edge_id", name="node_edge_pk"),)

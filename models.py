from __future__ import annotations
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, sessionmaker
from typing import List
from datetime import datetime
from enum import Enum
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = 'departments'
    dname: Mapped[str] = mapped_column(String(20), unique=True,nullable=False)
    dnumber: Mapped[int] = mapped_column(primary_key=True)
    emps: Mapped[List["Employees"]] = relationship(back_populates="deps")
    pro: Mapped[List["Project"]] = relationship(back_populates="depart")

    def __str__(self):
        return 'dname'+' '+ self.dname+' '+ 'dnumber'+' ' + str(self.dnumber)


class Employees(Base):
    __tablename__ = 'employees'
    ssn: Mapped[int] = mapped_column(primary_key=True)
    fname: Mapped[str] = mapped_column(String(20), unique=False,nullable=False)
    lname: Mapped[str] = mapped_column(String(20), unique=False,nullable=False)
    salary: Mapped[int] = mapped_column(Integer)
    dno: Mapped[int] = mapped_column(ForeignKey("departments.dnumber"))
    deps: Mapped["Department"] = relationship(back_populates="emps")


    def __str__(self):
        return 'name'+' '+ self.fname+' ' + self.lname+' '+ 'ssn'+' ' + str(self.ssn)+' ' +'salary'+' '+str(self.salary)


class Project(Base):
    __tablename__= 'projects'
    pnumber: Mapped[int]=mapped_column(primary_key=True)
    pname: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    plocation: Mapped[str] = mapped_column(String(30), unique=False, nullable=False)
    dnum: Mapped[int] = mapped_column(ForeignKey("departments.dnumber"))
    depart: Mapped["Department"] = relationship(back_populates="pro")
    # empl: Mapped[List["Employees"]] = relationship(back_populates="pros")

    def __str__(self):
        return 'pname'+' '+ self.pname+' '+ 'pnumber'+' ' + str(self.pnumber) +' '+ 'plocation'+' '+self.plocation + ' '+'dnum' +' '+str(self.dnum)


class Location(Enum):
    ATTIKA = 1
    KRITI = 2
    MAKEDONIA = 3
    THRAKI = 4
    HPEIROS = 5


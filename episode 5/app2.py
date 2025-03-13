from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Table)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Association table
class StudentCourse(Base):
    __tablename__ ='student_course'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    Course_id = Column('course_id', Integer, ForeignKey('courses.id'))
    
    
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary='student_course', back_populates="students")
    
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary='student_course', back_populates="courses")
    
Base.metadata.create_all(engine)

#math = Course(title='Mathematics')
#physics = Course(title='Physics')
#bill = Student(name='Bill', courses=[math, physics])
#rob = Student(name='Rob', courses=[math])

#session.add_all([math, physics,bill,rob])
#session.commit()

rob = session.query(Student).filter_by(name='Rob').first()
courses = [course.title for course in rob.courses]
print(f"Rob's Courses: {','.join(courses)}")

bill = session.query(Student).filter_by(name='Bill').first()
courses = [course.title for course in bill.courses]
print(f"Bill's Courses: {', '.join(courses)}")
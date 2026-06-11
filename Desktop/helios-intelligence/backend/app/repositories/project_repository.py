from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


class ProjectRepository:

    @staticmethod
    def create(
        db: Session,
        project_data: ProjectCreate
    ):
        project = Project(
            **project_data.model_dump()
        )

        db.add(project)

        db.commit()

        db.refresh(project)

        return project

    @staticmethod
    def get_all(
        db: Session
    ):
        return (
            db.query(Project)
            .all()
        )
    
    @staticmethod
    def get_by_id(
        db: Session,
        project_id: int
    ):
        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )
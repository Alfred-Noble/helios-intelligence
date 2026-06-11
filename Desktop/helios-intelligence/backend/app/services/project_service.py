from sqlalchemy.orm import Session

from app.schemas.project import ProjectCreate
from app.repositories.project_repository import ProjectRepository
from app.repositories.lead_repository import LeadRepository


class ProjectService:

    @staticmethod
    def create_project(
        db: Session,
        project_data: ProjectCreate
    ):
        return ProjectRepository.create(
            db,
            project_data
        )

    @staticmethod
    def get_projects(
        db: Session
    ):
        return ProjectRepository.get_all(
            db
        )
    
    @staticmethod
    def rank_leads_for_project(
        db: Session,
        project_id: int
    ):
        project = ProjectRepository.get_by_id(
            db=db,
            project_id=project_id
        )

        if not project:
            return {
                "error": "Project not found"
            }

        leads = LeadRepository.get_all_leads(
            db=db
        )

        ranked_leads = []

        for lead in leads:

            score = 0
            reasons = []

            # Industry Match
            if (
                project.industry
                and lead.industry
                and project.industry.lower()
                in lead.industry.lower()
            ):
                score += 50
                reasons.append("Industry Match")

            # AI Expertise
            if (
                lead.headline
                and "AI" in lead.headline
            ):
                score += 20
                reasons.append("AI Expertise")

            # Research Background
            if (
                lead.headline
                and "Research" in lead.headline
            ):
                score += 15
                reasons.append("Research Background")

            # Founder Experience
            if (
                lead.headline
                and "Founder" in lead.headline
            ):
                score += 15
                reasons.append("Founder Experience")

            # CTO Experience
            if (
                lead.headline
                and "CTO" in lead.headline
            ):
                score += 10
                reasons.append("Technical Leadership")

            # Existing AI Score Bonus
            if lead.ai_score:
                score += int(lead.ai_score / 5)
                reasons.append("High Lead Quality")

            # Cap score at 100
            score = min(score, 100)

            # Recommendation Category
            if score >= 80:
                recommendation = "Strong Match"
            elif score >= 50:
                recommendation = "Potential Match"
            else:
                recommendation = "Low Priority"

            ranked_leads.append({
                "lead_id": lead.id,
                "full_name": lead.full_name,
                "company": lead.company,
                "match_score": score,
                "recommendation": recommendation,
                "reasons": reasons
            })

        ranked_leads.sort(
            key=lambda x: x["match_score"],
            reverse=True
        )

        return {
            "project": project.name,
            "project_industry": project.industry,
            "ranked_leads": ranked_leads[:10]
        }
    
    @staticmethod
    def get_project_dashboard(
        db: Session,
        project_id: int
    ):
        ranking_data = ProjectService.rank_leads_for_project(
            db=db,
            project_id=project_id
        )

        if "error" in ranking_data:
            return ranking_data

        ranked_leads = ranking_data["ranked_leads"]

        total_leads = len(ranked_leads)

        strong_matches = len([
            lead for lead in ranked_leads
            if lead["recommendation"] == "Strong Match"
        ])

        potential_matches = len([
            lead for lead in ranked_leads
            if lead["recommendation"] == "Potential Match"
        ])

        low_priority = len([
            lead for lead in ranked_leads
            if lead["recommendation"] == "Low Priority"
        ])

        avg_score = (
            sum(
                lead["match_score"]
                for lead in ranked_leads
            ) / total_leads
        ) if total_leads > 0 else 0

        top_match = (
            ranked_leads[0]["full_name"]
            if ranked_leads
            else None
        )

        return {
            "project": ranking_data["project"],
            "industry": ranking_data["project_industry"],
            "total_leads_evaluated": total_leads,
            "strong_matches": strong_matches,
            "potential_matches": potential_matches,
            "low_priority": low_priority,
            "average_match_score": round(avg_score, 2),
            "top_match": top_match
        }
    
    @staticmethod
    def generate_project_outreach(
        db: Session,
        project_id: int,
        lead_id: int
    ):
        project = ProjectRepository.get_by_id(
            db=db,
            project_id=project_id
        )

        if not project:
            return {
                "error": "Project not found"
            }

        lead = LeadRepository.get_by_id(
            db=db,
            lead_id=lead_id
        )

        if not lead:
            return {
                "error": "Lead not found"
            }

        message = f"""
    Hi {lead.full_name},

    I am currently working on the project "{project.name}".

    Our goal is:
    {project.goal}

    Your experience as {lead.headline} at {lead.company} and your background in {lead.industry} strongly align with our objectives.

    I would love to connect and learn more about your work and explore potential collaboration opportunities.

    Best regards,
    Alfred Noble
    """.strip()

        return {
            "project": project.name,
            "lead": lead.full_name,
            "message": message
        }
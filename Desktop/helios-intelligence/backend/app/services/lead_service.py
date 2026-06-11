from sqlalchemy.orm import Session
import math
from app.schemas.lead import LeadCreate
from app.repositories.lead_repository import LeadRepository


class LeadService:

    @staticmethod
    def create_lead(db: Session, lead_data: LeadCreate):
        return LeadRepository.create(db, lead_data)
    
    
    @staticmethod
    def get_filtered_leads(
        db: Session,
        page: int = 1,
        limit: int = 20,
        search: str | None = None,
        industry: str | None = None,
        location: str | None = None
    ):
        items, total = LeadRepository.get_filtered_leads(
            db=db,
            page=page,
            limit=limit,
            search=search,
            industry=industry,
            location=location
        )

        return {
            "items": items,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": math.ceil(total / limit) if total > 0 else 0,
            "search": search,
            "industry": industry,
            "location": location
        }
    
    @staticmethod
    def import_csv(
        db: Session,
        leads: list
    ):
        rows_inserted = 0
        duplicates_skipped = 0

        unique_leads = []

        for lead in leads:

            is_duplicate = LeadRepository.exists_by_email_or_linkedin(
                db=db,
                email=lead.email,
                linkedin_url=lead.linkedin_url
            )

            if is_duplicate:
                duplicates_skipped += 1
            else:
                unique_leads.append(lead)
                rows_inserted += 1

        if unique_leads:
            LeadRepository.bulk_create(
                db=db,
                leads=unique_leads
            )

        return {
            "rows_processed": len(leads),
            "rows_inserted": rows_inserted,
            "duplicates_skipped": duplicates_skipped
        }
    
    @staticmethod
    def score_lead(
        db: Session,
        lead_id: int
    ):
        lead = LeadRepository.get_by_id(
            db=db,
            lead_id=lead_id
        )

        if not lead:
            return {"error": "Lead not found"}

        score = 0
        reasons = []

        # Industry Scoring
        if lead.industry:
            if "AI" in lead.industry or "Artificial Intelligence" in lead.industry:
                score += 50
                reasons.append("AI industry background")

            if "FinTech" in lead.industry:
                score += 10
                reasons.append("FinTech industry")

            if "SaaS" in lead.industry:
                score += 10
                reasons.append("SaaS industry")

            if "Blockchain" in lead.industry:
                score += 15
                reasons.append("Blockchain industry")

        # Headline Scoring
        if lead.headline:
            if "Founder" in lead.headline:
                score += 25
                reasons.append("Founder experience")

            if "CTO" in lead.headline:
                score += 20
                reasons.append("Technical leadership")

            if "Engineer" in lead.headline:
                score += 15
                reasons.append("Engineering expertise")

            if "Research" in lead.headline:
                score += 15
                reasons.append("Research background")

            if "Manager" in lead.headline:
                score += 10
                reasons.append("Management experience")
            
            if "AI" in lead.headline:
                score += 30
                reasons.append("AI expertise")

        # Company Bonus
        if lead.company:
            score += 5
            reasons.append("Professional experience")

        # Cap score at 100
        score = min(score, 100)

        # Lead Tier
        if score >= 70:
            tier = "High Potential"
        elif score >= 40:
            tier = "Medium Potential"
        else:
            tier = "Low Potential"

        lead.ai_score = score
        lead.ai_reason = ", ".join(reasons)

        LeadRepository.save(
            db=db,
            lead=lead
        )

        return {
            "lead_id": lead.id,
            "score": score,
            "tier": tier,
            "reason": lead.ai_reason
        }
    
    @staticmethod
    def generate_message(
        db: Session,
        lead_id: int
    ):
        lead = LeadRepository.get_by_id(
            db=db,
            lead_id=lead_id
        )

        if not lead:
            return {"error": "Lead not found"}

        message = f"""
    Hi {lead.full_name},

    I noticed your work as {lead.headline} at {lead.company}.

    Your experience in {lead.industry} caught my attention.

    I am currently building Helios Intelligence and would love to connect and learn more about your journey.

    Best regards,
    Alfred Noble
    """.strip()

        lead.outreach_message = message

        LeadRepository.save(
            db=db,
            lead=lead
        )

        return {
            "lead_id": lead.id,
            "message": message
        }
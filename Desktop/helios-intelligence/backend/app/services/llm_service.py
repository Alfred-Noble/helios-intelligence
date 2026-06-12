class LLMService:

    @staticmethod
    def score_lead(lead):

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

            # Executive Leadership

            if lead.headline and "CEO" in lead.headline:
                score += 25
                reasons.append("Executive Leadership")

            if lead.headline and "Co-Founder" in lead.headline:
                score += 25
                reasons.append("Founder Experience")

            if lead.headline and "Director" in lead.headline:
                score += 15
                reasons.append("Strategic Leadership")

            if lead.headline and "VP" in lead.headline:
                score += 15
                reasons.append("Senior Leadership")

            if lead.headline and "Head" in lead.headline:
                score += 15
                reasons.append("Department Leadership")

            # Product & Research

            if lead.headline and "Product Manager" in lead.headline:
                score += 10
                reasons.append("Product Leadership")

            if lead.headline and "Scientist" in lead.headline:
                score += 15
                reasons.append("Research Expertise")

            if lead.headline and "Architect" in lead.headline:
                score += 15
                reasons.append("Technical Architecture")

            # GTM

            if lead.headline and "Sales" in lead.headline:
                score += 10
                reasons.append("Revenue Ownership")

            if lead.headline and "GTM" in lead.headline:
                score += 15
                reasons.append("Go-To-Market Expertise")

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

        return score, reasons, tier
        

    @staticmethod
    def classify_persona(lead):

        headline = (
            lead.headline or ""
        ).lower()

        if "founder" in headline:
            return "Decision Maker"

        if "ceo" in headline:
            return "Executive Buyer"

        if "cto" in headline:
            return "Technical Buyer"

        if "vp" in headline:
            return "Senior Stakeholder"

        if "director" in headline:
            return "Strategic Influencer"

        if "manager" in headline:
            return "Influencer"

        if "sales" in headline:
            return "Revenue Owner"

        return "General Contact"

    @staticmethod
    def generate_outreach(lead):

        return f"""
Hi {lead.full_name},

I noticed your work as {lead.headline} at {lead.company}.

Your experience in {lead.industry} caught my attention, and I believe there may be opportunities for collaboration.

I am currently building Helios Intelligence, an AI-powered GTM and relationship intelligence platform focused on lead discovery, prioritization, and outreach automation.

I would love to connect and learn more about your experience and insights.

Best regards,

Alfred Noble
Founder, Helios Intelligence
""".strip()
class EmberService:
    def get_daily_guidance(self):
        return {
            "status": "ready",
            "suggestions": [
                "Feed Doughlene within 30 minutes",
                "Prepare levain for tomorrow",
                "Inventory check: flour stock trending low",
                "Cold retard schedule optimal"
            ]
        }

    def analyze_production(self):
        return {
            "timeline_ok": True,
            "conflicts": [],
            "recommendation": "Production schedule healthy"
        }


ember_service = EmberService()
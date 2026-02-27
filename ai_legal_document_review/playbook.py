PLAYBOOK = {
    "Confidentiality": {
        "description": "Ensure mutual protection of confidential information. Look for standard exclusions (publicly known, court order).",
        "risk_indicators": ["Unilateral obligations (only one party protected)", "Missing standard exclusions", "Indefinite term for non-trade-secrets"]
    },
    "Indemnification": {
        "description": "Protection against third-party claims.",
        "risk_indicators": ["Uncapped liability", "Broad 'all claims' language", "No defense control for the indemnifying party"]
    },
    "Termination": {
        "description": "Rules for ending the agreement.",
        "risk_indicators": ["No termination for convenience", "Excessive notice periods (>90 days)", "Automatic renewal without notice"]
    },
    "Limitation of Liability": {
        "description": "Caps on potential damages.",
        "risk_indicators": ["No cap stated", "Cap > 2x contract value", "Exclusion of indirect/consequential damages missing"]
    },
    "Governing Law": {
        "description": "Jurisdiction for disputes.",
        "risk_indicators": ["Foreign jurisdiction", "Arbitration only (if not preferred)", "Unclear venue"]
    }
}

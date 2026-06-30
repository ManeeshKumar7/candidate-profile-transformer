class SkillNormalizer:
    """
    Converts different representations of skills
    into a canonical format.
    """

    SKILL_MAP = {

        "ml": "Machine Learning",

        "machine learning": "Machine Learning",

        "ai": "Artificial Intelligence",

        "artificial intelligence": "Artificial Intelligence",

        "dl": "Deep Learning",

        "deep learning": "Deep Learning",

        "py": "Python",

        "python3": "Python",

        "cpp": "C++",

        "c plus plus": "C++",

        "js": "JavaScript",

        "nodejs": "Node.js",
        
        "sql": "SQL"

    }

    @classmethod
    def normalize(cls, skill: str) -> str:

        if not skill:
            return ""

        skill = skill.strip().lower()

        return cls.SKILL_MAP.get(skill, skill.title())
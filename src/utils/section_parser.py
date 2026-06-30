SECTION_HEADERS = {
    "education": [
        "education",
        "academic background",
        "qualification",
    ],
    "experience": [
        "experience",
        "work experience",
        "employment",
        "professional experience",
    ],
    "skills": [
        "skills",
        "technical skills",
        "technical expertise",
    ],
    "projects": [
        "projects",
        "personal projects",
    ],
}


class SectionParser:

    def parse(self, text: str):

        sections = {}

        current = "general"

        sections[current] = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            found = False

            for section, headers in SECTION_HEADERS.items():

                if line.lower() in headers:

                    current = section

                    sections[current] = []

                    found = True

                    break

            if not found:

                sections[current].append(line)

        return {

            key: "\n".join(value)

            for key, value in sections.items()

        }
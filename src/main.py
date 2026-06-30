import json

from src.extractors.csv_extractor import CSVExtractor
from src.extractors.resume_extractor import ResumeExtractor
from src.mergers.profile_merger import ProfileMerger
from src.normalizers.candidate_normalizer import CandidateNormalizer
from src.projection.projector import Projector
from src.readers.csv_reader import CSVReader
from src.readers.resume_reader import ResumeReader
from src.validators.profile_validator import ProfileValidator


CSV_PATH = "data/input/recruiter.csv"

RESUME_PATH = "data/input/resume.pdf"

CONFIG_PATH = "data/config/config.json"

OUTPUT_PATH = "data/output/candidate_profile.json"


def load_config(path):

    with open(path, "r") as file:

        return json.load(file)


def save_output(profile, path):

    with open(path, "w", encoding="utf-8") as file:

        json.dump(
            profile,
            file,
            indent=4,
            ensure_ascii=False,
        )


def main():

    # -----------------------------
    # Readers
    # -----------------------------

    csv_reader = CSVReader()

    resume_reader = ResumeReader()

    # -----------------------------
    # Read input
    # -----------------------------

    recruiter_dataframe = csv_reader.read(CSV_PATH)

    resume_text = resume_reader.read(RESUME_PATH)

    # -----------------------------
    # Extract
    # -----------------------------

    csv_candidate = CSVExtractor().extract(
        recruiter_dataframe
    )

    resume_candidate = ResumeExtractor().extract(
        resume_text
    )

    # -----------------------------
    # Normalize
    # -----------------------------

    normalizer = CandidateNormalizer()

    csv_candidate = normalizer.normalize(
        csv_candidate
    )

    resume_candidate = normalizer.normalize(
        resume_candidate
    )

    # -----------------------------
    # Merge
    # -----------------------------

    merged_candidate = ProfileMerger().merge(
        csv_candidate,
        resume_candidate,
    )

    # -----------------------------
    # Projection
    # -----------------------------

    config = load_config(CONFIG_PATH)

    projected = Projector().project(
        merged_candidate,
        config,
    )

    # -----------------------------
    # Validation
    # -----------------------------

    validator = ProfileValidator()

    result = validator.validate(projected)

    if not result["valid"]:

        print("Validation Failed")

        print(result["missing_fields"])

        return

    # -----------------------------
    # Save Output
    # -----------------------------

    save_output(projected, OUTPUT_PATH)

    print("\nCandidate profile generated successfully.\n")

    print(json.dumps(projected, indent=4))


if __name__ == "__main__":

    main()
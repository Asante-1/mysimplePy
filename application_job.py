def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']} with a mail :", applicant['email_address'])

applicants = [
    {
        "name": "Devon Laryea",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Theophilus Asante",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": True,
        "email_address": "asantetheophilus660@gmail.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": False,
        "email_address": "sam@email.com",
    },
]
for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["years_of_experience"] >= 2

    meets_criteria = (
        knows_python
        or experienced_dev
        or applicant["has_degree"]
    )
    if meets_criteria:
        schedule_interview(applicant)

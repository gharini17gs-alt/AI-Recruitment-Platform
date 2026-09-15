# WEEK 3 - Job Matching

job_description = """
Python Developer

We are looking for a Python Developer.

Required Skills:
Python
SQL
Git
AWS

Required Education:
Bachelor

Required Experience:
3 years
"""

print("JOB DESCRIPTION")
print(job_description)


# Job Information

job_title = "Python Developer"

required_skills = [
    "Python",
    "SQL",
    "Git",
    "AWS"
]

required_education = "Bachelor"

required_experience = 3


print("\nEXTRACTED JOB INFORMATION")

print("\nJob Title:", job_title)

print("\nRequired Skills:")

for skill in required_skills:
    print("-", skill)

print("\nRequired Education:", required_education)

print("Required Experience:", required_experience, "years")

# Candidate Resume Information

candidate_name = "John Smith"

candidate_skills = [
    "Python",
    "SQL",
    "Java",
    "AWS"
]

candidate_education = "Bachelor"

candidate_experience = 8


print("\nCANDIDATE INFORMATION")

print("Name:", candidate_name)

print("\nCandidate Skills:")

for skill in candidate_skills:
    print("-", skill)

print("\nEducation:", candidate_education)

print("Experience:", candidate_experience, "years")

# Skills Comparison

matched_skills = []
missing_skills = []

for skill in required_skills:
    if skill in candidate_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)


print("\nSKILLS COMPARISON")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)
    
# Match Score Calculation

total_required_skills = len(required_skills)
total_matched_skills = len(matched_skills)

match_score = (total_matched_skills / total_required_skills) * 100

print("\nMATCH SCORE")

print("Matched Skills:", total_matched_skills)
print("Total Required Skills:", total_required_skills)
print("Match Score:", match_score, "%")

# Education and Experience Matching

education_match = candidate_education == required_education

experience_match = candidate_experience >= required_experience


print("\nEDUCATION AND EXPERIENCE MATCHING")

if education_match:
    print("Education: Match")
else:
    print("Education: Not Match")


if experience_match:
    print("Experience: Match")
else:
    print("Experience: Not Match")
    
    # Skill Gap Analysis

print("\nSKILL GAP ANALYSIS")

if missing_skills:
    print("Missing Skills:")
    
    for skill in missing_skills:
        print("-", skill)
else:
    print("No skill gaps found. Candidate has all required skills.")
    
    # Multiple Candidates Ranking

candidates = [
    {
        "name": "John Smith",
        "skills": ["Python", "SQL", "Java", "AWS"],
        "education": "Bachelor",
        "experience": 8
    },
    {
        "name": "Michael Brown",
        "skills": ["Python", "R", "SQL", "TensorFlow"],
        "education": "Master",
        "experience": 5
    },
    {
        "name": "Robert Taylor",
        "skills": ["JavaScript", "React", "Node.js", "SQL"],
        "education": "Bachelor",
        "experience": 6
    }
]

results = []

for candidate in candidates:

    matched = []

    for skill in required_skills:
        if skill in candidate["skills"]:
            matched.append(skill)

    score = (len(matched) / len(required_skills)) * 100

    results.append({
        "name": candidate["name"],
        "score": score,
        "matched_skills": matched
    })


# Sort candidates by score

results.sort(key=lambda x: x["score"], reverse=True)


print("\nCANDIDATE RANKING")

for rank, candidate in enumerate(results, start=1):

    print("\nRank:", rank)
    print("Name:", candidate["name"])
    print("Match Score:", candidate["score"], "%")
    print("Matched Skills:", ", ".join(candidate["matched_skills"]))
    
    # Best Candidate Recommendation

best_candidate = results[0]

print("\nBEST CANDIDATE RECOMMENDATION")

print("Name:", best_candidate["name"])
print("Match Score:", best_candidate["score"], "%")
print("Matched Skills:", ", ".join(best_candidate["matched_skills"]))

print("\nRecommendation:")
print(best_candidate["name"], "is the most suitable candidate for this job.")

import pandas as pd

# Load expanded resume dataset
df = pd.read_csv("resumes_expanded.csv")

print("\n" + "=" * 50)
print("ALL CANDIDATES JOB MATCHING")
print("=" * 50)

candidate_results = []

# Compare every candidate with job requirements
for index, candidate in df.iterrows():

    # Convert skills text into a list
    candidate_skills_list = [
        skill.strip()
        for skill in candidate["skills"].split(",")
    ]

    # Find matched skills
    matched = []

    for skill in required_skills:
        if skill.lower() in [s.lower() for s in candidate_skills_list]:
            matched.append(skill)

    # Find missing skills
    missing = []

    for skill in required_skills:
        if skill not in matched:
            missing.append(skill)

    # Calculate match score
    score = (len(matched) / len(required_skills)) * 100

    # Education matching
    education_match = (
        candidate["education_level"].lower()
        == required_education.lower()
    )

    # Experience matching
    experience_match = (
        candidate["years_experience"]
        >= required_experience
    )

    # Store candidate result
    candidate_results.append({
        "name": candidate["first_name"] + " " + candidate["last_name"],
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "education_match": education_match,
        "experience_match": experience_match
    })


# Rank candidates by score
candidate_results.sort(
    key=lambda x: x["score"],
    reverse=True
)


print("\nCANDIDATE RANKING")

for rank, candidate in enumerate(candidate_results, start=1):

    print("\nRank:", rank)
    print("Name:", candidate["name"])
    print("Match Score:", candidate["score"], "%")
    print("Matched Skills:", ", ".join(candidate["matched_skills"]))

    if candidate["missing_skills"]:
        print(
            "Missing Skills:",
            ", ".join(candidate["missing_skills"])
        )
    else:
        print("Missing Skills: None")

    print(
        "Education:",
        "Match" if candidate["education_match"] else "Not Match"
    )

    print(
        "Experience:",
        "Match" if candidate["experience_match"] else "Not Match"
    )


# Best Candidate
best_candidate = candidate_results[0]

print("\n" + "=" * 50)
print("BEST CANDIDATE RECOMMENDATION")
print("=" * 50)

print("Name:", best_candidate["name"])
print("Match Score:", best_candidate["score"], "%")
print(
    "Matched Skills:",
    ", ".join(best_candidate["matched_skills"])
)

print(
    "Missing Skills:",
    ", ".join(best_candidate["missing_skills"])
    if best_candidate["missing_skills"]
    else "None"
)

print("\nRecommendation:")
print(
    best_candidate["name"],
    "is the most suitable candidate for the",
    job_title,
    "position."
)
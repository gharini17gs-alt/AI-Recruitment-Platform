import pandas as pd

df = pd.read_csv("resumes.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nEducation Details:")
print(df[["first_name", "education_level", "degree_field"]])

print("\nExperience Details:")
print(df[["first_name", "job_title", "years_experience"]])

print("\nEducation Count:")
print(df["education_level"].value_counts())

print("\nExperience Summary:")
print(df["years_experience"].describe())

print("\nMissing Values:")
print(df.isnull().sum())

output = df[
    ["first_name", "education_level", "degree_field", "years_experience"]
]

output.to_csv("education_experience.csv", index=False)

print("\nEducation and Experience data saved successfully!")

# Candidate Profile

candidate = df.iloc[0]

print("\nCandidate Profile:")
print("Name:", candidate["first_name"], candidate["last_name"])
print("Job Title:", candidate["job_title"])
print("Education:", candidate["education_level"])
print("Degree:", candidate["degree_field"])
print("Experience:", candidate["years_experience"], "years")
print("Skills:", candidate["skills"])

# All Candidate Profiles

print("\nAll Candidate Profiles:")

for index, candidate in df.iterrows():
    print("\nCandidate", index + 1)
    print("Name:", candidate["first_name"], candidate["last_name"])
    print("Job Title:", candidate["job_title"])
    print("Education:", candidate["education_level"])
    print("Experience:", candidate["years_experience"], "years")
    print("Skills:", candidate["skills"])


# Resume Classification

def classify_job(job_title):
    title = job_title.lower()

    if "software" in title or "developer" in title:
        return "Software Development"
    elif "data" in title:
        return "Data Science"
    elif "manager" in title:
        return "Management"
    elif "security" in title:
        return "Cybersecurity"
    elif "architect" in title:
        return "Cloud / Architecture"
    elif "designer" in title:
        return "Design"
    elif "devops" in title:
        return "DevOps"
    elif "business" in title:
        return "Business Analysis"
    elif "financial" in title:
        return "Finance"
    else:
        return "Other"


print("\nResume Classification:")

for index, candidate in df.iterrows():
    category = classify_job(candidate["job_title"])
    print(candidate["first_name"], "->", category)
    
    # Job Recommendation

def recommend_job(category):
    recommendations = {
        "Software Development": "Software Developer",
        "Data Science": "Data Scientist",
        "Management": "Project Manager",
        "Cloud / Architecture": "Cloud Architect",
        "Design": "UI/UX Designer",
        "DevOps": "DevOps Engineer",
        "Business Analysis": "Business Analyst",
        "Finance": "Financial Analyst",
        "Cybersecurity": "Cybersecurity Analyst"
    }

    return recommendations.get(category, "General IT Role")


print("\nJob Recommendations:")

for index, candidate in df.iterrows():
    category = classify_job(candidate["job_title"])
    recommendation = recommend_job(category)

    print(candidate["first_name"], "->", recommendation)
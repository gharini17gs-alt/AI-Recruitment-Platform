with open("job_description.txt", "r") as file:
    job = file.read()

print("Job Description:")
print(job)

skills = ["Python", "SQL", "Git"]

print("\nRequired Skills:")
for skill in skills:
    print(skill)
    
education = "Bachelor"

print("\nRequired Education:")
print(education)

experience = 3

print("\nRequired Experience:")
print(experience, "years")

# Resume + Job Comparison

required_skills = ["Python", "SQL", "Git"]

candidate_skills = ["Python", "SQL", "Git"]

print("\nSkills Comparison:")

for skill in required_skills:
    if skill in candidate_skills:
        print(skill, ": Match")
    else:
        print(skill, ": Not Match")
        
        # Final Candidate Matching Result

total_requirements = 5
matched_requirements = 5

score = (matched_requirements / total_requirements) * 100

print("\nFinal Candidate Matching Result:")
print("Matched Requirements:", matched_requirements)
print("Total Requirements:", total_requirements)
print("Matching Score:", score, "%")

if score >= 70:
    print("Result: Selected")
else:
    print("Result: Not Selected")
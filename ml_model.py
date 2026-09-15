import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load expanded dataset
df = pd.read_csv("resumes_expanded.csv")

# Create category
def classify_job(job_title):
    title = job_title.lower()

    if "software" in title or "developer" in title:
        return "Software Development"
    elif "data" in title or "machine learning" in title:
        return "Data Science"
    elif "manager" in title:
        return "Management"
    elif "security" in title:
        return "Cybersecurity"
    elif "architect" in title or "cloud" in title:
        return "Cloud / Architecture"
    elif "designer" in title:
        return "Design"
    elif "devops" in title or "site reliability" in title:
        return "DevOps"
    elif "business" in title:
        return "Business Analysis"
    elif "financial" in title or "finance" in title:
        return "Finance"
    else:
        return "Other"


df["category"] = df["job_title"].apply(classify_job)

# Combine job title + skills
X = df["job_title"] + " " + df["skills"]
y = df["category"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train ML model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("ML Model Training Completed!")
print("Total Dataset:", len(df))
print("Training Samples:", len(y_train))
print("Testing Samples:", len(y_test))
print("Model Accuracy:", accuracy * 100, "%")

print("\nModel Evaluation:")
print(classification_report(y_test, y_pred))
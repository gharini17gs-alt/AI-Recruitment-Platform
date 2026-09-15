from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os
import re
import fitz
import pytesseract
from PIL import Image


app = Flask(__name__)


# ==========================================
# CONFIGURATION
# ==========================================

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "pdf",
    "jpg",
    "jpeg",
    "png"
}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ==========================================
# TESSERACT PATH
# ==========================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ==========================================
# SKILLS DATABASE
# ==========================================

SKILLS = [
    "python",
    "java",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "excel",
    "c",
    "c++",

    "react",
    "node.js",
    "nodejs",
    "flask",
    "django",

    "machine learning",
    "deep learning",
    "data analysis",
    "data analytics",
    "data science",
    "artificial intelligence",
    "nlp",

    "aws",
    "azure",
    "docker",
    "git",
    "github",

    "power bi",
    "tableau",

    "mongodb",
    "pandas",
    "numpy",
    "tensorflow",
    "scikit-learn",

    "web development"
]


# ==========================================
# ALLOWED FILE CHECK
# ==========================================

def allowed_file(filename):

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


# ==========================================
# EXTRACT TEXT FROM PDF
# ==========================================

def extract_text_from_pdf(filepath):

    text = ""

    try:

        pdf = fitz.open(filepath)

        for page in pdf:

            text += page.get_text()

        pdf.close()

    except Exception as error:

        print("PDF ERROR:", error)

    return text


# ==========================================
# EXTRACT TEXT FROM IMAGE
# ==========================================

def extract_text_from_image(filepath):

    try:

        image = Image.open(filepath)

        # Improve OCR reading
        image = image.convert("RGB")

        text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )

        return text

    except Exception as error:

        print("IMAGE OCR ERROR:", error)

        return ""


# ==========================================
# CLEAN TEXT
# ==========================================

def clean_text(text):

    text = text.replace("\r", "\n")

    text = re.sub(r"\n+", "\n", text)

    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


# ==========================================
# NAME EXTRACTION
# ==========================================

def extract_name(text):

    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if line:
            lines.append(line)


    invalid_words = [

        "resume",
        "curriculum vitae",
        "profile",
        "about me",
        "career objective",
        "objective",
        "education",
        "experience",
        "skills",
        "technical skills",
        "personal details",
        "contact",
        "email",
        "phone",
        "projects",
        "certifications",
        "languages",
        "hobbies",
        "declaration",
        "summary",
        "professional summary",
        "computer skills",
        "academic",

        "bachelor",
        "master",

        "enter your major",
        "high school",
        "college",
        "university",

        "student",
        "fresher"
    ]


    candidates = []


    # Check first 15 lines
    for index, line in enumerate(lines[:15]):

        lower_line = line.lower()


        # Skip unwanted headings
        if any(word in lower_line for word in invalid_words):
            continue


        # Skip email
        if "@" in line:
            continue


        # Skip phone
        if re.search(r"\d{5,}", line):
            continue


        # Skip year
        if re.search(r"\b(19|20)\d{2}\b", line):
            continue


        # Remove unwanted characters
        candidate = re.sub(
            r"[^A-Za-z.\s]",
            "",
            line
        ).strip()


        # Remove multiple spaces
        candidate = re.sub(
            r"\s+",
            " ",
            candidate
        )


        words = candidate.replace(".", " ").split()


        # Name should have 2 to 4 words
        if 2 <= len(words) <= 4:

            # Avoid long sentences
            if len(candidate) <= 35:

                score = 0


                # Top lines priority
                score += 20 - index


                # Uppercase names
                if line.isupper():
                    score += 10


                # Short name gets better priority
                if len(words) <= 3:
                    score += 5


                candidates.append(
                    (score, candidate)
                )


    if candidates:

        candidates.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        name = candidates[0][1]

        return name.title()


    return "Candidate Name Not Found"


# ==========================================
# EMAIL EXTRACTION
# ==========================================

def extract_email(text):

    # Normal email pattern
    pattern = (
        r"[A-Za-z0-9._%+-]+"
        r"@"
        r"[A-Za-z0-9.-]+"
        r"\."
        r"[A-Za-z]{2,}"
    )

    match = re.search(
        pattern,
        text
    )

    if match:

        return match.group()


    # OCR sometimes adds spaces
    text_no_spaces = re.sub(
        r"\s+",
        "",
        text
    )

    match = re.search(
        pattern,
        text_no_spaces
    )

    if match:

        return match.group()


    return "Email Not Found"


# ==========================================
# PHONE EXTRACTION
# ==========================================

def extract_phone(text):

    # Remove spaces and special characters
    cleaned_text = re.sub(
        r"[^\d+]",
        "",
        text
    )


    # Indian mobile number
    pattern = r"(?:\+91)?[6-9]\d{9}"


    match = re.search(
        pattern,
        cleaned_text
    )


    if match:

        phone = match.group()


        # Remove +91 for display
        if phone.startswith("+91"):

            phone = phone[3:]


        return phone


    return "Phone Not Found"


# ==========================================
# SKILLS EXTRACTION
# ==========================================

def extract_skills(text):

    found_skills = []

    text_lower = text.lower()


    for skill in SKILLS:

        if skill.lower() in text_lower:

            if skill.title() not in found_skills:

                found_skills.append(
                    skill.title()
                )


    return found_skills


# ==========================================
# EDUCATION EXTRACTION
# ==========================================

def extract_education(text):

    education_keywords = [

        "b.sc",
        "bsc",
        "bca",

        "b.e",
        "be ",
        "b tech",
        "b.tech",
        "btech",

        "m.sc",
        "msc",
        "mca",

        "m.e",
        "m tech",
        "m.tech",
        "mtech",

        "bachelor",
        "master",

        "computer science",
        "information technology"
    ]


    lines = text.split("\n")


    for line in lines:

        clean_line = line.strip()


        if not clean_line:
            continue


        lower_line = clean_line.lower()


        for keyword in education_keywords:

            if keyword in lower_line:

                return clean_line


    return "Education Not Found"


# ==========================================
# EXPERIENCE EXTRACTION
# ==========================================

def extract_experience(text):

    text_lower = text.lower()


    if "fresher" in text_lower:

        return "Fresher"


    patterns = [

        r"(\d+)\+?\s*years?\s*(?:of\s*)?experience",

        r"experience\s*[:\-]?\s*(\d+)\+?\s*years?",

        r"(\d+)\+?\s*yrs?\s*(?:of\s*)?experience"
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text_lower
        )


        if match:

            years = match.group(1)

            return years + " Years Experience"


    return "Fresher"


# ==========================================
# JOB ROLE RECOMMENDATION
# ==========================================

def recommend_job_role(skills):

    skills_lower = " ".join(skills).lower()


    if (
        "python" in skills_lower
        and (
            "tensorflow" in skills_lower
            or "deep learning" in skills_lower
        )
    ):

        return "Machine Learning Engineer"


    if (
        "python" in skills_lower
        and "machine learning" in skills_lower
    ):

        return "Data Scientist"


    if (
        "sql" in skills_lower
        and (
            "excel" in skills_lower
            or "power bi" in skills_lower
            or "data analysis" in skills_lower
        )
    ):

        return "Data Analyst"


    if (
        "html" in skills_lower
        and "css" in skills_lower
        and "javascript" in skills_lower
    ):

        return "Web Developer"


    if (
        "python" in skills_lower
        and "flask" in skills_lower
    ):

        return "Python Developer"


    if "java" in skills_lower:

        return "Java Developer"


    if (
        "html" in skills_lower
        and "css" in skills_lower
    ):

        return "Frontend Developer"


    return "Software Developer"


# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

def get_missing_skills(job_role, skills):

    role_requirements = {

        "Data Scientist": [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas",
            "Numpy"
        ],

        "Machine Learning Engineer": [
            "Python",
            "Machine Learning",
            "Tensorflow",
            "Docker"
        ],

        "Data Analyst": [
            "Excel",
            "SQL",
            "Power BI",
            "Python"
        ],

        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ],

        "Frontend Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ],

        "Python Developer": [
            "Python",
            "Flask",
            "SQL",
            "Git"
        ],

        "Java Developer": [
            "Java",
            "SQL",
            "Git"
        ],

        "Software Developer": [
            "Python",
            "Java",
            "SQL",
            "Git"
        ]
    }


    required_skills = role_requirements.get(
        job_role,
        []
    )


    user_skills_lower = [

        skill.lower()

        for skill in skills
    ]


    missing_skills = []


    for skill in required_skills:

        if skill.lower() not in user_skills_lower:

            missing_skills.append(
                skill
            )


    return missing_skills


# ==========================================
# RESUME SCORE
# ==========================================

def calculate_score(

    name,
    email,
    phone,
    skills,
    education,
    experience
):

    score = 0


    if name != "Candidate Name Not Found":

        score += 15


    if email != "Email Not Found":

        score += 15


    if phone != "Phone Not Found":

        score += 10


    if "No Skills Found" not in skills:

        skill_score = min(

            len(skills) * 5,

            25
        )

        score += skill_score


    if education != "Education Not Found":

        score += 20


    if experience:

        score += 15


    return min(
        score,
        100
    )


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template(

        "index.html",

        analysis=None,

        error=None
    )


# ==========================================
# ANALYZE RESUME
# ==========================================

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    # Check file
    if "resume" not in request.files:

        return render_template(

            "index.html",

            analysis=None,

            error="Please upload a resume file."
        )


    file = request.files["resume"]


    # Check empty file
    if file.filename == "":

        return render_template(

            "index.html",

            analysis=None,

            error="Please select a resume file."
        )


    # Check extension
    if not allowed_file(file.filename):

        return render_template(

            "index.html",

            analysis=None,

            error="Only PDF, JPG, JPEG and PNG files are supported."
        )


    # Secure filename
    filename = secure_filename(
        file.filename
    )


    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],

        filename
    )


    # Save file
    file.save(filepath)


    # Get extension
    extension = filename.rsplit(

        ".",

        1

    )[1].lower()


    text = ""


    # PDF
    if extension == "pdf":

        text = extract_text_from_pdf(
            filepath
        )


    # IMAGE
    elif extension in [

        "jpg",

        "jpeg",

        "png"
    ]:

        text = extract_text_from_image(
            filepath
        )


    # Clean text
    text = clean_text(text)


    # Check extracted text
    if not text:

        return render_template(

            "index.html",

            analysis=None,

            error="Could not read text from this resume."
        )


    # DEBUG
    print("\n==============================")
    print("RESUME TEXT")
    print("==============================")
    print(text)
    print("==============================\n")


    # ======================================
    # EXTRACT INFORMATION
    # ======================================

    candidate_name = extract_name(
        text
    )


    email = extract_email(
        text
    )


    phone = extract_phone(
        text
    )


    skills = extract_skills(
        text
    )


    education = extract_education(
        text
    )


    experience = extract_experience(
        text
    )


    # No skills
    if not skills:

        skills = [
            "No Skills Found"
        ]


    # ======================================
    # JOB ROLE
    # ======================================

    job_role = recommend_job_role(
        skills
    )


    # ======================================
    # MISSING SKILLS
    # ======================================

    missing_skills = get_missing_skills(

        job_role,

        skills
    )


    # ======================================
    # SCORE
    # ======================================

    score = calculate_score(

        candidate_name,

        email,

        phone,

        skills,

        education,

        experience
    )


    # ======================================
    # ANALYSIS DATA
    # ======================================

    analysis = {

        "name": candidate_name,

        "email": email,

        "phone": phone,

        "skills": skills,

        "education": education,

        "experience": experience,

        "job_role": job_role,

        "missing_skills": missing_skills,

        "score": score
    }


    return render_template(

        "index.html",

        analysis=analysis,

        error=None
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
import pandas as pd

# Original dataset
df = pd.read_csv("resumes.csv")

# 40 additional synthetic/demo candidates
new_data = [
    [11,"James","Miller","james.miller@email.com","555-0111","Dallas TX","Software Developer","CodeTech","Technology",3,"Bachelor","Computer Science","Python, Java, Git, SQL","Python Certification",75000],
    [12,"Olivia","Wilson","olivia.w@email.com","555-0112","Houston TX","Software Engineer","SoftWorks","Technology",4,"Bachelor","Information Technology","Python, Java, Git, Docker","AWS Certification",82000],
    [13,"Daniel","Moore","daniel.m@email.com","555-0113","Boston MA","Web Developer","WebTech","Technology",3,"Bachelor","Computer Science","HTML, CSS, JavaScript, React","Web Development Certification",70000],
    [14,"Sophia","Taylor","sophia.t@email.com","555-0114","Seattle WA","Backend Developer","CloudCode","Technology",5,"Bachelor","Computer Science","Python, Django, SQL, Git","Python Certification",85000],
    [15,"Matthew","Anderson","matthew.a@email.com","555-0115","Denver CO","Frontend Developer","FrontendPro","Technology",3,"Bachelor","Computer Science","JavaScript, React, HTML, CSS","React Certification",72000],

    [16,"Emma","Thomas","emma.t@email.com","555-0116","Chicago IL","Data Analyst","DataCorp","Analytics",3,"Bachelor","Data Analytics","Python, SQL, Excel, Tableau","Google Data Analytics",78000],
    [17,"William","Jackson","william.j@email.com","555-0117","New York NY","Data Scientist","AnalyticsHub","Analytics",6,"Master","Data Science","Python, R, SQL, Machine Learning","Azure Data Scientist",110000],
    [18,"Ava","White","ava.w@email.com","555-0118","Austin TX","Machine Learning Engineer","MLTech","Analytics",5,"Master","Artificial Intelligence","Python, TensorFlow, Scikit-learn, SQL","ML Certification",108000],
    [19,"Alexander","Harris","alex.h@email.com","555-0119","Miami FL","Data Analyst","DataWorks","Analytics",4,"Bachelor","Statistics","SQL, Python, Power BI, Excel","Power BI Certification",80000],
    [20,"Isabella","Martin","isabella.m@email.com","555-0120","Portland OR","Data Scientist","AI Solutions","Analytics",5,"Master","Data Science","Python, SQL, Pandas, TensorFlow","Data Science Certification",105000],

    [21,"Ethan","Thompson","ethan.t@email.com","555-0121","San Francisco CA","DevOps Engineer","DevCloud","Technology",4,"Bachelor","Information Systems","Linux, Docker, Jenkins, Git","AWS Certification",90000],
    [22,"Mia","Garcia","mia.g@email.com","555-0122","Dallas TX","Cloud Engineer","CloudWorks","Technology",5,"Bachelor","Computer Science","AWS, Azure, Linux, Terraform","AWS Cloud Certification",98000],
    [23,"Noah","Martinez","noah.m@email.com","555-0123","Austin TX","DevOps Engineer","TechCloud","Technology",6,"Bachelor","Information Technology","Docker, Kubernetes, Jenkins, Terraform","Kubernetes Certification",102000],
    [24,"Charlotte","Robinson","charlotte.r@email.com","555-0124","Seattle WA","Cloud Engineer","CloudSystems","Technology",4,"Master","Cloud Computing","AWS, Azure, GCP, Docker","Azure Certification",97000],
    [25,"Lucas","Clark","lucas.c@email.com","555-0125","Denver CO","Site Reliability Engineer","ReliabilityTech","Technology",5,"Bachelor","Computer Engineering","Linux, Kubernetes, Monitoring, Git","Cloud Certification",100000],

    [26,"Amelia","Rodriguez","amelia.r@email.com","555-0126","Boston MA","UI Designer","CreativeStudio","Design",3,"Bachelor","Graphic Design","Figma, Sketch, Adobe XD, Prototyping","UX Certification",72000],
    [27,"Henry","Lewis","henry.l@email.com","555-0127","New York NY","UX Designer","DesignWorks","Design",4,"Bachelor","Design","Figma, User Research, Wireframing, Prototyping","UX Designer Certification",78000],
    [28,"Harper","Lee","harper.l@email.com","555-0128","Chicago IL","UI/UX Designer","CreativeTech","Design",5,"Master","Interaction Design","Figma, Adobe XD, User Testing, Sketch","UX Certification",85000],
    [29,"Benjamin","Walker","benjamin.w@email.com","555-0129","Miami FL","Graphic Designer","DesignHub","Design",3,"Bachelor","Graphic Design","Photoshop, Illustrator, Figma, Branding","Adobe Certification",68000],
    [30,"Evelyn","Hall","evelyn.h@email.com","555-0130","Portland OR","UX Designer","UXStudio","Design",4,"Bachelor","Visual Design","Figma, Wireframing, Prototyping, User Testing","UX Certification",76000],

    [31,"James","Allen","james.a@email.com","555-0131","Dallas TX","Business Analyst","BusinessTech","Consulting",4,"Bachelor","Business Administration","SQL, Excel, Tableau, Agile","Business Analyst Certification",78000],
    [32,"Abigail","Young","abigail.y@email.com","555-0132","Seattle WA","Business Analyst","ConsultPro","Consulting",6,"Master","Business Analytics","SQL, Power BI, Excel, Requirements Analysis","IIBA Certification",88000],
    [33,"Michael","King","michael.k@email.com","555-0133","Boston MA","Business Analyst","DataConsult","Consulting",5,"Bachelor","Management","SQL, Tableau, Agile, Business Analysis","Business Analyst Certification",82000],
    [34,"Ella","Wright","ella.w@email.com","555-0134","Chicago IL","Business Analyst","ConsultTech","Consulting",3,"Bachelor","Business Administration","Excel, SQL, Requirements Analysis, Agile","Agile Certification",75000],
    [35,"Sebastian","Lopez","sebastian.l@email.com","555-0135","Denver CO","Business Analyst","BusinessWorks","Consulting",5,"Master","Business Analytics","SQL, Excel, Tableau, Process Analysis","IIBA Certification",85000],

    [36,"Camila","Hill","camila.h@email.com","555-0136","Miami FL","Financial Analyst","FinanceTech","Finance",3,"Bachelor","Finance","Excel, SQL, Tableau, Financial Modeling","CFA Level 1",78000],
    [37,"Jack","Scott","jack.s@email.com","555-0137","New York NY","Financial Analyst","FinanceHub","Finance",5,"Bachelor","Finance","Excel, Python, SQL, Financial Analysis","CFA Level 1",88000],
    [38,"Luna","Green","luna.g@email.com","555-0138","Boston MA","Finance Analyst","GlobalFinance","Finance",4,"Master","Finance","Excel, SQL, Financial Modeling, Power BI","Financial Planning Certification",84000],
    [39,"Owen","Adams","owen.a@email.com","555-0139","Austin TX","Financial Analyst","FinanceWorks","Finance",6,"Bachelor","Accounting","Excel, SQL, Python, Financial Modeling","CFA Level 1",92000],
    [40,"Grace","Baker","grace.b@email.com","555-0140","Seattle WA","Financial Analyst","FinCorp","Finance",3,"Bachelor","Finance","Excel, Tableau, SQL, Budgeting","Finance Certification",76000],

    [41,"Logan","Nelson","logan.n@email.com","555-0141","Portland OR","Project Manager","ProjectTech","Technology",5,"Master","MBA","Project Planning, Agile, Scrum, Leadership","PMP Certification",95000],
    [42,"Chloe","Carter","chloe.c@email.com","555-0142","Chicago IL","Product Manager","ProductWorks","Technology",4,"Master","MBA","Product Strategy, Agile, Market Research, Analytics","CSPO Certification",98000],
    [43,"Aiden","Mitchell","aiden.m@email.com","555-0143","Denver CO","Project Manager","ManageTech","Consulting",6,"Bachelor","Business Administration","Project Management, Agile, Scrum, Leadership","PMP Certification",92000],
    [44,"Nora","Perez","nora.p@email.com","555-0144","Dallas TX","Product Manager","InnovateSoft","Technology",5,"Master","MBA","Product Strategy, User Research, Agile, Data Analysis","CSPO Certification",102000],
    [45,"Jackson","Roberts","jackson.r@email.com","555-0145","New York NY","Project Manager","ProjectHub","Consulting",4,"Bachelor","Management","Project Planning, Scrum, Agile, Risk Management","PMP Certification",90000],

    [46,"Riley","Turner","riley.t@email.com","555-0146","San Francisco CA","Cloud Architect","CloudEnterprise","Technology",8,"Master","Computer Science","AWS, Azure, GCP, Cloud Architecture, Solution Design","AWS Solutions Architect",125000],
    [47,"Leo","Phillips","leo.p@email.com","555-0147","Seattle WA","Solutions Architect","EnterpriseCloud","Technology",7,"Master","Computer Science","AWS, Azure, Enterprise Architecture, Cloud Security","AWS Certification",120000],
    [48,"Zoe","Campbell","zoe.c@email.com","555-0148","Austin TX","Cloud Architect","CloudTech","Technology",6,"Bachelor","Information Technology","AWS, GCP, Terraform, Architecture Design","Google Cloud Certification",115000],
    [49,"Wyatt","Parker","wyatt.p@email.com","555-0149","Boston MA","Solutions Architect","TechEnterprise","Technology",9,"Master","Computer Science","AWS, Azure, GCP, Enterprise Architecture","AWS Professional Certification",130000],
    [50,"Lily","Evans","lily.e@email.com","555-0150","New York NY","Cloud Architect","CloudSolutions","Technology",7,"Master","Cloud Computing","AWS, Azure, Kubernetes, Solution Design","Azure Architect Certification",118000]
]

columns = [
    "id", "first_name", "last_name", "email", "phone", "location",
    "job_title", "company", "industry", "years_experience",
    "education_level", "degree_field", "skills", "certifications",
    "salary_expectation"
]

new_df = pd.DataFrame(new_data, columns=columns)

# Combine original + new data
expanded_df = pd.concat([df, new_df], ignore_index=True)

# Save expanded dataset
expanded_df.to_csv("resumes_expanded.csv", index=False)

print("Dataset expansion completed!")
print("Original rows:", len(df))
print("New rows:", len(new_df))
print("Total rows:", len(expanded_df))
print("File created: resumes_expanded.csv")
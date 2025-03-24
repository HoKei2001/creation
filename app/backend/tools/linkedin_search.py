import random
from typing import List, Dict, Any, Optional
import datetime
from faker import Faker

# Initialize Faker with multiple locales for international profiles
fake = Faker(['en_US', 'en_GB', 'zh_CN'])

def generate_mock_candidates(
    keywords: List[str], 
    count: int = 100,
    min_experience: int = 0,
    max_experience: int = 20
) -> List[Dict[str, Any]]:
    """
    Generate mock LinkedIn candidate profiles based on job keywords.
    
    Args:
        keywords (List[str]): List of job keywords to generate relevant candidates
        count (int): Number of candidate profiles to generate (default: 100)
        min_experience (int): Minimum years of experience
        max_experience (int): Maximum years of experience
        
    Returns:
        List[Dict[str, Any]]: List of mock LinkedIn candidate profiles
    """
    # Common job titles related to given keywords
    job_titles = {
        "python": ["Python Developer", "Python Engineer", "Backend Developer", "Data Scientist", "Full Stack Developer"],
        "java": ["Java Developer", "Java Engineer", "Backend Developer", "Software Engineer", "Java Architect"],
        "frontend": ["Frontend Developer", "Web Developer", "UI Engineer", "React Developer", "JavaScript Developer"],
        "ai": ["AI Engineer", "Machine Learning Engineer", "Data Scientist", "AI Researcher", "ML Specialist"],
        "data": ["Data Analyst", "Data Engineer", "Business Intelligence", "Data Scientist", "Analytics Manager"],
        "product": ["Product Manager", "Product Owner", "UX Designer", "Product Specialist", "Business Analyst"],
        "marketing": ["Marketing Specialist", "Digital Marketer", "Brand Manager", "Content Strategist", "SEO Specialist"],
        "sales": ["Sales Representative", "Account Manager", "Business Development", "Sales Executive", "Client Manager"],
        "hr": ["HR Specialist", "Recruiter", "Talent Acquisition", "HR Manager", "People Operations"],
        "finance": ["Financial Analyst", "Accountant", "Finance Manager", "Financial Controller", "Investment Analyst"],
    }
    
    # Common skills related to keywords
    skills_map = {
        "python": ["Python", "Django", "Flask", "FastAPI", "Data Analysis", "pandas", "NumPy", "API Development", "SQL", "Git"],
        "java": ["Java", "Spring", "Microservices", "REST APIs", "Hibernate", "Maven", "JUnit", "Design Patterns", "SQL", "CI/CD"],
        "frontend": ["JavaScript", "React", "Angular", "Vue.js", "HTML", "CSS", "TypeScript", "Webpack", "UI/UX", "Responsive Design"],
        "ai": ["Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "NLP", "Computer Vision", "Python", "Data Analysis", "Neural Networks", "Algorithms"],
        "data": ["SQL", "ETL", "Data Warehousing", "Power BI", "Tableau", "Python", "R", "Data Visualization", "Statistical Analysis", "Big Data"],
        "product": ["Product Strategy", "Market Research", "User Stories", "Agile", "Wireframing", "Product Roadmap", "User Testing", "JIRA", "Competitive Analysis", "Requirements Gathering"],
        "marketing": ["Digital Marketing", "SEO", "Content Marketing", "Social Media", "Google Analytics", "Email Marketing", "Marketing Strategy", "CRM", "Marketing Automation", "Campaign Management"],
        "sales": ["Sales Strategy", "Client Relations", "Negotiation", "CRM", "Salesforce", "Lead Generation", "Account Management", "B2B Sales", "Sales Analytics", "Pipeline Management"],
        "hr": ["Recruiting", "Talent Management", "Onboarding", "Performance Reviews", "Employee Relations", "HRIS", "Training & Development", "Compensation", "Benefits", "HR Policies"],
        "finance": ["Financial Analysis", "Budgeting", "Forecasting", "Excel", "Financial Modeling", "Accounting", "Financial Reporting", "ERP Systems", "Risk Assessment", "Balance Sheets"],
    }
    
    # Common education degrees
    degrees = ["Bachelor", "Master", "MBA", "PhD", "Associate"]
    
    # Common education fields
    fields = ["Computer Science", "Business Administration", "Marketing", "Engineering", "Information Technology", 
              "Data Science", "Economics", "Finance", "Human Resources", "Psychology", 
              "Communications", "Mathematics", "Statistics", "Electrical Engineering", "Software Engineering"]
    
    # Generate candidate profiles
    candidates = []
    
    for _ in range(count):
        # Random locale for this profile
        locale = random.choice(['en_US', 'en_GB', 'zh_CN'])
        local_fake = Faker(locale)
        
        # Pick relevant keywords for this candidate
        relevant_keywords = random.sample(keywords, min(len(keywords), random.randint(1, 3)))
        relevant_keywords_lower = [k.lower() for k in relevant_keywords]
        
        # Determine relevant job titles and skills based on keywords
        possible_job_titles = []
        possible_skills = []
        
        for keyword in relevant_keywords_lower:
            for key in job_titles:
                if keyword in key or key in keyword:
                    possible_job_titles.extend(job_titles[key])
            for key in skills_map:
                if keyword in key or key in keyword:
                    possible_skills.extend(skills_map[key])
        
        # If no matches found, use generic options
        if not possible_job_titles:
            possible_job_titles = ["Professional", "Specialist", "Manager", "Consultant"]
        if not possible_skills:
            possible_skills = ["Communication", "Teamwork", "Leadership", "Problem Solving"]
        
        # Basic profile info
        gender = random.choice(["male", "female"])
        first_name = local_fake.first_name_male() if gender == "male" else local_fake.first_name_female()
        last_name = local_fake.last_name()
        name = f"{first_name} {last_name}"
        
        # Current position for headline
        current_title = random.choice(possible_job_titles)
        current_company = local_fake.company()
        headline = f"{current_title} at {current_company}"
        
        # Generate work experiences
        num_experiences = random.randint(1, 4)
        experiences = []
        
        current_date = datetime.datetime.now()
        total_exp_years = random.randint(min_experience, max_experience)
        exp_end_date = current_date
        
        for i in range(num_experiences):
            job_title = random.choice(possible_job_titles)
            company = current_company if i == 0 else local_fake.company()
            
            # Duration for this job
            job_duration = random.randint(1, max(1, total_exp_years // num_experiences))
            total_exp_years -= job_duration
            
            exp_start_date = exp_end_date - datetime.timedelta(days=job_duration*365)
            
            experiences.append({
                "title": job_title,
                "company": company,
                "location": local_fake.city(),
                "start_date": exp_start_date.strftime("%b %Y"),
                "end_date": "Present" if i == 0 else exp_end_date.strftime("%b %Y"),
                "description": local_fake.paragraph(nb_sentences=2)
            })
            
            exp_end_date = exp_start_date - datetime.timedelta(days=random.randint(30, 180))
            
            if total_exp_years <= 0:
                break
        
        # Education
        num_educations = random.randint(1, 2)
        educations = []
        
        edu_end_year = current_date.year - random.randint(1, 15)
        
        for _ in range(num_educations):
            degree_type = random.choice(degrees)
            field_of_study = random.choice(fields)
            school = local_fake.university()
            
            start_year = edu_end_year - random.randint(1, 5)
            
            educations.append({
                "school": school,
                "degree": f"{degree_type} of {field_of_study}",
                "start_year": start_year,
                "end_year": edu_end_year
            })
            
            edu_end_year = start_year - random.randint(1, 3)
        
        # Select random skills
        selected_skills = list(set(random.sample(
            possible_skills,
            min(len(possible_skills), random.randint(5, 10))
        )))
        
        # Create the candidate profile
        candidate = {
            "id": local_fake.uuid4(),
            "name": name,
            "headline": headline,
            "location": f"{local_fake.city()}, {local_fake.country()}",
            "summary": local_fake.paragraph(nb_sentences=3),
            "experiences": experiences,
            "education": educations,
            "skills": selected_skills,
            "languages": random.sample(["English", "Chinese", "Spanish", "French", "German"], 
                                      random.randint(1, 3)),
            "industry": random.choice([
                "Technology", "Finance", "Healthcare", "Education", "Retail", 
                "Manufacturing", "Consulting", "Media", "Marketing", "Telecommunications"
            ]),
            "connections": random.choice([f"{random.randint(1, 500)}+", "500+", "1000+"]),
            "contact_info": {
                "email": local_fake.email(),
                "phone": local_fake.phone_number() if random.random() > 0.5 else None
            },
            "open_to_work": random.choice([True, False]),
            "years_of_experience": sum([exp.get("duration", 0) for exp in experiences]),
            "profile_url": f"https://www.linkedin.com/in/{first_name.lower()}-{last_name.lower()}-{random.randint(10000, 99999)}/",
            "last_active": f"{random.randint(1, 30)} days ago"
        }
        
        candidates.append(candidate)
    
    return candidates

def search_linkedin(query: str, count: int = 100) -> List[Dict[str, Any]]:
    """
    Mock function to search LinkedIn for candidates based on query.
    
    Args:
        query (str): Search query string (job keywords)
        count (int): Number of results to return
        
    Returns:
        List[Dict[str, Any]]: List of LinkedIn candidate profiles
    """
    keywords = query.split()
    return generate_mock_candidates(keywords, count)

import random
from typing import List, Dict, Any, Optional
import datetime
from faker import Faker

# Initialize Faker with Chinese locale
fake = Faker(['zh_CN'])

def generate_mock_resumes(
    keywords: List[str], 
    count: int = 100,
    min_experience: int = 0,
    max_experience: int = 15
) -> List[Dict[str, Any]]:
    """
    Generate mock resume data based on job keywords.
    
    Args:
        keywords (List[str]): List of job keywords to generate relevant resumes
        count (int): Number of resumes to generate (default: 100)
        min_experience (int): Minimum years of experience
        max_experience (int): Maximum years of experience
        
    Returns:
        List[Dict[str, Any]]: List of mock resume data
    """
    # Common job titles related to given keywords
    job_titles = {
        "python": ["Python开发工程师", "Python后端工程师", "Python全栈工程师", "数据分析师", "爬虫工程师"],
        "java": ["Java开发工程师", "Java架构师", "后端工程师", "Spring开发", "Java全栈工程师"],
        "前端": ["前端开发工程师", "Web前端工程师", "UI/UX开发", "React工程师", "Vue工程师"],
        "人工智能": ["AI工程师", "机器学习工程师", "深度学习研究员", "算法工程师", "NLP工程师"],
        "数据": ["数据工程师", "数据分析师", "大数据开发", "BI分析师", "数据科学家"],
        "产品": ["产品经理", "产品运营", "产品设计师", "需求分析师", "产品助理"],
        "运营": ["运营专员", "用户运营", "内容运营", "活动运营", "新媒体运营"],
        "销售": ["销售代表", "销售经理", "客户经理", "销售主管", "商务拓展"],
        "市场": ["市场专员", "市场经理", "品牌经理", "市场策划", "营销主管"],
        "hr": ["HR专员", "人力资源经理", "招聘专员", "HRBP", "人才培养经理"],
    }
    
    # Common skills related to keywords
    skills_map = {
        "python": ["Python", "Django", "Flask", "FastAPI", "爬虫", "数据分析", "pandas", "numpy", "PyTorch", "TensorFlow"],
        "java": ["Java", "Spring", "SpringBoot", "微服务", "MVC", "JVM", "Maven", "MyBatis", "JPA", "设计模式"],
        "前端": ["JavaScript", "TypeScript", "React", "Vue", "Angular", "HTML", "CSS", "SASS", "Webpack", "响应式设计"],
        "人工智能": ["机器学习", "深度学习", "NLP", "计算机视觉", "强化学习", "TensorFlow", "PyTorch", "神经网络", "算法", "数学"],
        "数据": ["SQL", "数据仓库", "数据建模", "ETL", "BI工具", "大数据", "Hadoop", "Spark", "Hive", "数据可视化"],
        "产品": ["产品设计", "用户调研", "需求分析", "产品规划", "原型设计", "用户体验", "市场分析", "项目管理", "产品生命周期", "商业分析"],
        "运营": ["用户运营", "内容运营", "活动策划", "数据分析", "用户增长", "社区运营", "新媒体运营", "用户留存", "转化率优化", "KPI制定"],
        "销售": ["销售技巧", "客户管理", "谈判能力", "渠道拓展", "市场分析", "客户关系", "目标达成", "销售策略", "商务沟通", "团队管理"],
        "市场": ["市场策划", "品牌推广", "营销策略", "SEM", "SEO", "内容营销", "社交媒体", "市场调研", "用户画像", "营销活动"],
        "hr": ["人力资源管理", "招聘", "绩效管理", "培训发展", "员工关系", "薪酬福利", "人才规划", "组织发展", "员工体验", "劳动法规"],
    }
    
    # Common education backgrounds
    educations = ["计算机科学与技术", "软件工程", "信息管理", "数据科学", "人工智能", 
                  "电子工程", "自动化", "工商管理", "市场营销", "人力资源管理",
                  "通信工程", "机械工程", "金融学", "经济学"]
    
    # Common companies
    companies = ["阿里巴巴", "腾讯", "百度", "字节跳动", "美团", "京东", "华为", "小米", 
                 "网易", "滴滴", "拼多多", "快手", "携程", "陌陌", "bilibili", 
                 "OPPO", "VIVO", "联想", "中兴", "TCL", "科大讯飞"]
    
    # Generate resumes
    resumes = []
    
    for _ in range(count):
        # Pick relevant keywords for this resume
        relevant_keywords = random.sample(keywords, min(len(keywords), random.randint(1, 3)))
        
        # Determine relevant job titles and skills based on keywords
        possible_job_titles = []
        possible_skills = []
        
        for keyword in relevant_keywords:
            if keyword.lower() in job_titles:
                possible_job_titles.extend(job_titles[keyword.lower()])
            if keyword.lower() in skills_map:
                possible_skills.extend(skills_map[keyword.lower()])
        
        # Generate resume with faker
        gender = random.choice(["male", "female"])
        name = fake.name_male() if gender == "male" else fake.name_female()
        
        # Generate work experiences
        num_experiences = random.randint(1, 4)
        experiences = []
        
        current_date = datetime.datetime.now()
        total_exp_years = random.randint(min_experience, max_experience)
        exp_end_date = current_date
        
        for i in range(num_experiences):
            # Duration for this job
            job_duration = random.randint(1, max(1, total_exp_years // num_experiences))
            total_exp_years -= job_duration
            
            exp_start_date = exp_end_date - datetime.timedelta(days=job_duration*365)
            
            experiences.append({
                "company": random.choice(companies),
                "position": random.choice(possible_job_titles) if possible_job_titles else fake.job(),
                "start_date": exp_start_date.strftime("%Y-%m"),
                "end_date": exp_end_date.strftime("%Y-%m") if i > 0 else "至今",
                "description": fake.paragraph(nb_sentences=3)
            })
            
            exp_end_date = exp_start_date - datetime.timedelta(days=random.randint(30, 180))
            
            if total_exp_years <= 0:
                break
        
        # Select random skills
        selected_skills = random.sample(
            possible_skills if possible_skills else ["沟通能力", "团队协作", "问题解决", "项目管理"],
            min(len(possible_skills) if possible_skills else 4, 
                random.randint(3, 8))
        )
        
        # Create the resume
        resume = {
            "id": fake.uuid4(),
            "name": name,
            "age": random.randint(22, 45),
            "gender": "男" if gender == "male" else "女",
            "education": {
                "degree": random.choice(["学士", "硕士", "博士", "大专"]),
                "school": fake.university(),
                "major": random.choice(educations),
                "graduation_year": current_date.year - random.randint(1, 20)
            },
            "experiences": experiences,
            "skills": selected_skills,
            "expected_salary": f"{random.randint(5, 40)}k-{random.randint(45, 80)}k",
            "location": fake.city(),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "last_updated": fake.date_time_this_year().strftime("%Y-%m-%d")
        }
        
        resumes.append(resume)
    
    return resumes

def search_liepin(query: str, count: int = 100) -> List[Dict[str, Any]]:
    """
    Mock function to search Liepin for candidates based on query.
    
    Args:
        query (str): Search query string (job keywords)
        count (int): Number of results to return
        
    Returns:
        List[Dict[str, Any]]: List of candidate resumes
    """
    keywords = query.split()
    return generate_mock_resumes(keywords, count)

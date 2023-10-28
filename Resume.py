def generate_resume(name, contact, education, experience, skills):
    print(f"Name: {name}")
    print(f"Contact: {contact}")
    print(f"\nEducation:")
    for degree in education:
        print(f"- {degree}") 
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")

# Example data
name = "Esakki Devi"
contact = "esakkidevi42@gmail.com | (555) 555-5555"
education = ["Bachelor of Science in Computer Science, Rani Anna College, 2023"]
skills = ["Python", "Java", "HTML/CSS", "JavaScript"]

# Generate the resume
generate_resume(name, contact, education, skills)

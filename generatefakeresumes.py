import random
import pandas as pd

first_names = ["Alex", "Skylar", "Jordan", "Casey", "Taylor", "Morgan", "Riley", "Jamie"]
last_names = ["Quantum", "Starborn", "Blaze", "Shadow", "Storm", "Night", "Phoenix", "Moon"]

companies = [
    "FutureTech Inc.", "Mythical Creatures Corp", "ShadowOps Ltd.",
    "Galactic Ventures", "DreamWorks Magic", "CyberNinjas LLC"
]

skills = [
    "Quantum computing", "Teleportation logistics", "Brainwave hacking",
    "Dragon taming", "Fairy dust production", "Cloud sculpting",
    "Stealth algorithms", "Cyber espionage", "Ninja star throwing",
    "Time manipulation", "Alien language translation", "Teleportation"
]

educations = [
    "PhD in Multiverse Engineering from Atlantis University",
    "Bachelor's degree in Magical Arts from Hogwarts School of Witchcraft and Wizardry",
    "Certified Assassin from The Secret Order of Shadows",
    "Master’s in Cybernetic Wizardry from Cyberland University",
    "Diploma in Dragon Handling from Mythical Academy"
]

achievements = [
    "Invented a device that stops time for 5 minutes",
    "Awarded “Best Enchanter of the Year” for 7 consecutive years",
    "Completed 100+ covert missions globally",
    "Discovered a new dimension of reality",
    "Successfully tamed a wild dragon",
    "Created the first AI-powered magic wand"
]

languages = [
    "English", "Martian", "Binary", "Elvish", "Ancient Runes", "Japanese",
    "Python", "C++", "Klingon", "Dragonese"
]

contacts = [
    "futuremail.com", "magicmail.com", "shadowops.net", "galacticmail.com", "dreamworks.net"
]

def generate_fake_resume():
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    company = random.choice(companies)
    skill_list = random.sample(skills, k=3)
    education = random.choice(educations)
    achievement = random.choice(achievements)
    language_list = random.sample(languages, k=3)
    contact_domain = random.choice(contacts)

    resume = f"""
Name: {name}
Experience: {random.randint(5, 15)} years working as a {random.choice(skill_list)} specialist at {company}
Skills: {', '.join(skill_list)}
Education: {education}
Achievements: {achievement}
Languages: {', '.join(language_list)}
Contact: {first.lower()}.{last.lower()}@{contact_domain}
"""
    return resume.strip()

if __name__ == "__main__":
    n = 100  # How many fake resumes to generate
    data = []

    for _ in range(n):
        fake_resume = generate_fake_resume()
        data.append({"text": fake_resume, "label": "fake"})

    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("fake_resumes.csv", index=False)
    print(f"Generated {n} fake résumés and saved to fake_resumes.csv")

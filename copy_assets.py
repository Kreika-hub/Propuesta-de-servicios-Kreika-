import shutil
import os

src_hero = r"C:\Users\HP\.gemini\antigravity\brain\d1022548-9dd0-468e-a81b-490ad4359fdf\hero_model_1785267616136.png"
src_about = r"C:\Users\HP\.gemini\antigravity\brain\d1022548-9dd0-468e-a81b-490ad4359fdf\about_model_1785267628915.png"

dest_hero = "./hero_model.png"
dest_about = "./about_model.png"

try:
    shutil.copy(src_hero, dest_hero)
    print("Copied hero_model.png successfully!")
except Exception as e:
    print(f"Error copying hero_model: {e}")

try:
    shutil.copy(src_about, dest_about)
    print("Copied about_model.png successfully!")
except Exception as e:
    print(f"Error copying about_model: {e}")

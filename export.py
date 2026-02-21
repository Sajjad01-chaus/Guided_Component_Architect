import os

def export_component(component, folder="generated_component"):
    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/component.ts", "w", encoding="utf-8") as f:
        f.write(component["typescript"])

    with open(f"{folder}/component.html", "w", encoding="utf-8") as f:
        f.write(component["html"])

    with open(f"{folder}/component.css", "w", encoding="utf-8") as f:
        f.write(component["css"])
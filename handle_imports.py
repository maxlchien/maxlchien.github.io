import shutil
import json
import os


for file in os.listdir("aux_files/downloads"):
    shutil.copy(f"aux_files/downloads/{file}", f"downloads/{file}")

with open("aux_files/notes.json", "r") as f:
    notes = json.load(f)
    sem_num = 0
    within_sem = 1
    last_sem = ""
    for note in notes:
        if note["semester_name"] != last_sem:
            sem_num += 1
            within_sem = 1
            last_sem = note["semester_name"]
        else:
            within_sem += 1
        note_path = f"_notes/{note["md_path"]}"
        with open(note_path, "w") as f:
            f.write("---\n")
            f.write(f"title: {note["title"]}\n")
            if "class_code" in note:
                f.write(f"class_code: {note["class_code"]}\n")
            f.write(f"semester_name: {note["semester_name"]}\n")
            f.write(f"semester_order: {sem_num}\n")
            f.write(f"order: {within_sem}\n")
            if "status" in note:
                f.write(f"status: {note["status"]}\n")
            if "post_url" in note:
                f.write(f"post_url: {note["post_url"]}\n")
            if "post_date" in note:
                f.write(f"date: {note["post_date"]}\n")
            if "downloads" in note:
                f.write("downloads:\n")
                for download in note["downloads"]:
                    f.write(f"  - label: {download["label"]}\n")
                    f.write(f"    url: {download["url"]}\n")
            if "texts" in note:
                f.write("texts:\n")
                for text in note["texts"]:
                    if "title" in text:
                        f.write(f"  - title: {text["title"]}\n")
                    if "author" in text:
                        f.write(f"    author: {text["author"]}\n")
                    if "pdf_url" in text:
                        f.write(f"    pdf_url: {text["pdf_url"]}\n")
            f.write("---")

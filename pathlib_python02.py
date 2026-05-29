from pathlib import Path



base_dir = Path().home() / "Desktop"


text_files = list(base_dir.glob("*.txt"))



for txt in text_files:
    txt.write_text(txt.read_text() + "\n" + "Hi this is new text")


# for txt in text_files:
#     if (txt.parent.name) == "Text Files":
#         print(txt.read_text())
# #     print(txt.name)




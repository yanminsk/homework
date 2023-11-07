text=input("Введите текст: ").strip()
changed_text=text.replace(" ","-")
print(changed_text)

changed_text=text.split()
changed_text="-".join(changed_text)
print(changed_text)
from pyscript import document

def generate_message(event):
    # this is for clearing the previous output to avoid redundancy
    document.querySelector("#output").innerText = ""

    # this is to get the input values
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # this is to assign strings using variables 
    intro = "🎓✨ Student Profile ✨🎓\n"
    line1 = f"👤 Name:\t{name.title()}"
    line2 = f"🎂 Age:\t{age}"
    line3 = f"🏫 School:\t{school.upper()}"

    # I used multiline string with escape characters + a formal bio for the student to make the website look more organized :)
    profile = f"""{intro}
{line1}
{line2}
{line3}

\"{name.title()}\" is currently enrolled at {school.upper()} and is {age} years old.
📌 This information was gathered through input fields and displayed using a multiline string in Python via PyScript.
""" #i added some emojis here so that it doesnt look that boring and plain :]

    # This part is to display the formatted message
    document.querySelector("#output").innerText = profile
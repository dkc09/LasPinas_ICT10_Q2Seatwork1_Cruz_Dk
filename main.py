from pyscript import document

def verify_candidate(event):
    # 1. List of ICT Club Members
    club_members = [
        "Dk Cruz",
        "Yousef DelaFuente",
        "Ryan Dye",
        "Jacob Opilla",
        "Joaquin Cheng",
        "Aaron DeGuzman"
    ]

    
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()
    full_name = f"{first_name} {last_name}"

   
    is_member = full_name in club_members

    
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

    styles = [
        "mt-4 p-3 text-center alert alert-danger border-0 d-block",
        "mt-4 p-3 text-center alert alert-success border-0 d-block"
    ]

    status_index = int(is_member)


    result_message = messages[status_index]
    result_style = styles[status_index]

    
    result_element = document.getElementById("result-area")
    result_element.innerText = result_message
    result_element.className = result_style

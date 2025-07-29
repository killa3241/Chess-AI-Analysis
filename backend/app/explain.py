def generate_advice(feedback_list):
    advice = []

    for comment in feedback_list:
        move_num = comment.split(":")[0].replace("Move", "").strip()
        parts = comment.split("You played")
        if len(parts) < 2:
            advice.append(comment)  # fallback
            continue

        played, best = parts[1].split("but the best move was")
        played = played.strip().strip(".")
        best = best.strip().strip(".")

        message = f"On move {move_num}, you played {played}, but the engine recommends {best}. Try reviewing this position!"
        advice.append(message)

    return advice

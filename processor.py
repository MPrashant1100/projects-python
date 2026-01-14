def calculate_grade(avg_score):
    if avg_score >= 90:
        return "A"
    elif avg_score >= 75:
        return "B"
    elif avg_score >= 60:
        return "C"
    else:
        return "D"


def process_scores(data):
    scores = data["scores"]

    total = sum(scores)
    count = len(scores)
    average = total / count

    result = {
        "user": data["user"],
        "average": round(average, 2),
        "max": max(scores),
        "min": min(scores),
        "grade": calculate_grade(average)
    }

    return result
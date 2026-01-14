def validate_input(data):
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary")

    if "user" not in data:
        raise ValueError("Missing 'user' field")

    if "scores" not in data:
        raise ValueError("Missing 'scores' field")

    if not isinstance(data["user"], str):
        raise TypeError("'user' must be a string")

    scores = data["scores"]

    if not isinstance(scores, list):
        raise TypeError("'scores' must be a list")

    if len(scores) == 0:
        raise ValueError("'scores' list cannot be empty")

    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All scores must be numbers")

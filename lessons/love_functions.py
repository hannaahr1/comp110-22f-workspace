"""Some tender, loving functions. """

def love (subject: str) -> str:
    """Given a subject as a parameter, returns a loving string. """
    return f"I love you {subject} !"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    counter_variable: int = 0

    while counter_variable < n: 
        # TO DO: The real work
        love_note += love(to) + "\n"
        counter_variable += 1
    return love_note 
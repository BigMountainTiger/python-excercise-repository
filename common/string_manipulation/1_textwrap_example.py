import textwrap

def get_a_string():
    the_string = """
        This is a string with leading whitespace.
        It is indented by 8 spaces.
        The dedent function will remove this indentation.
    """
    return textwrap.dedent(the_string).strip()

if __name__ == "__main__":
    print(get_a_string())
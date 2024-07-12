def escape_id(identifier):
        # semicolon for breaking up statements, period for scoping, equals sign, inline comment
        naively_cleaned_identifier = identifier.replace(";", "").replace(".", "").replace("=", "").replace("--", "")
        # start with double quote
        escaped = '"'
        for char in naively_cleaned_identifier:
            if char == '"':
                # double the double quotes to escape
                escaped = escaped + char
            escaped = escaped + char
        # end with double quote
        return escaped + '"'   

def escape_li(literal):
    escaped = ""
    for char in literal:
        if char == "'":
            # double the single quotes to escape
            escaped = escaped + char
        escaped = escaped + char
    return escaped

def double_quote(identifier):
    return '"{}"'.format(identifier)

def single_quote(literal):
    return "'{}'".format(literal)

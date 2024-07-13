from enum import StrEnum


def promptable(cls):
    # TODO: error out if class is not a StrEnum?
    def prompt(prefix=None):
        values = list(cls)
        options = "/".join(x.lower() for x in values)
        # TODO remove leading space
        if prefix:
            prompt_text = f"{prefix} [{options}] "
        else:
            prompt_text = f"[{options}] "
        while True:
            # TODO: support default option
            user_input = input(prompt_text)
            # TODO: implement better matching algorithm (trie?)
            for value in values:
                if value.lower().startswith(user_input):
                    return value
            print("Sorry, I didn't understand that.")

    cls.prompt = prompt
    return cls

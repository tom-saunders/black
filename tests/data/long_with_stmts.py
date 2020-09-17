with some_context_manager("taking a string") as first, another_context_manager() as second, x(a_short_context_manager="", but_with_really_long_kwargs="which might themselves be really long strings? long enough that it can't possibly be expected to fit all together on one line. In fact it may even take up three or more lines... like four or five... but probably just three.") as also_really_long_name_for_the_response_just_in_case, and_this():
    pass


# output


with \
    some_context_manager("taking a string") as first, \
    another_context_manager() as second, \
    x(
        a_short_context_manager="",
        but_with_really_long_kwargs=(
            "which might themselves be really long strings? long enough that it can't"
            " possibly be expected to fit all together on one line. In fact it may even"
            " take up three or more lines... like four or five... but probably just"
            " three."
        ),
    ) as also_really_long_name_for_the_response_just_in_case, \
    and_this() \
:
    pass

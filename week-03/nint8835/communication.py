print(
    (
        input(),
        (
            lambda _, __: _.whitespace[0].join(
                __[___] for ___ in [int(____) for ____ in input().split()]
            )
        )(
            __import__(str.__name__ + int.__name__[:-1] + globals.__name__[0]),
            {_____ ^ ((_____ << 1) % 256): str(_____) for _____ in range(256)},
        ),
    )[-1]
)

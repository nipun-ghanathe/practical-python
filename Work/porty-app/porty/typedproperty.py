# ruff: noqa: ANN001,ANN201,ANN202,N802

# typedproperty.py
#
# Exercise 7.7


def typedproperty(name: str, expected_type: type):
    private_name = f"_{name}"

    @property  # type: ignore[misc]
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            message = f"Expected {expected_type}"
            raise TypeError(message)
        setattr(self, private_name, value)

    return prop


def String(name):
    return typedproperty(name, str)


def Integer(name):
    return typedproperty(name, int)


def Float(name):
    return typedproperty(name, float)

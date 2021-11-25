import uuid


class IdGenerator:

    def __init__(self, default_scope=None):
        """

        Parameters
        ----------
        default_scope   scope to use for subsequent generate calls when do scope is provided
        """
        self.default_scope = default_scope if default_scope is not None else "sdk_example"
        self._scope_and_codes = set()

    def generate_scope_and_code(self, entity, scope=None, code_prefix=None):
        """
        Generate a scope ond code

        Parameters
        ----------
        entity : str
            User defined string to describe the entity the scope and code is being generated for. This is returned
            when calling ``pop_scope_and_codes``
        scope : str, optional
            Scope to use, if not supplied the default one will be used
        code_prefix : str, optional
            Prefix for the generated code

        Returns
        -------
        (str, str, str)
            The generated (entity, scope, code)

        """
        scope = scope if scope is not None else self.default_scope

        code = str(uuid.uuid4())
        code = code if code_prefix is None else f"{code_prefix}{code}"

        item = (entity, scope, code)

        self._scope_and_codes.add(item)
        return item

    def clear(self):
        """
        Clears all generated ids
        """
        self._scope_and_codes.clear()

    def pop_scope_and_codes(self):
        """
        Generator returning the generated scope and code. Generated ids are deleted after being returned

        Yields
        -------
        (str, str, str)
            The generated (entity, scope, code)
        """
        while self._scope_and_codes:
            yield self._scope_and_codes.pop()

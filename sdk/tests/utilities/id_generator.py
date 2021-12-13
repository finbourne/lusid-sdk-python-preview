import uuid


class IdGenerator:

    default_scope = "sdk_example"

    def __init__(self, scope=default_scope):
        """

        Parameters
        ----------
        scope : str, optional
          scope to use for subsequent calls to generate ids, when no scope is provided defaults
          to `sdk_example`
        """
        self.scope = scope if scope is not None else self.default_scope
        self._scope_and_codes = set()

    def generate_scope_and_code(self, entity, scope=None, code_prefix=None):
        """
        Generate a scope and code

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
        scope = scope if scope is not None else self.scope

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

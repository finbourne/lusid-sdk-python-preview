import unittest

from . import IdGenerator
from parameterized import parameterized


class IdGeneratorTests(unittest.TestCase):

    def test_use_default_scope_when_not_specified(self):
        id_generator = IdGenerator()
        self.assertEqual(IdGenerator.default_scope, id_generator.scope)

    @parameterized.expand([
        ["custom-scope"],
        [""]
    ])
    def test_uses_provided_scope(self, scope):
        id_generator = IdGenerator(scope)
        self.assertEqual(scope, id_generator.scope)

    def test_explicit_none_scope_uses_default(self):
        id_generator = IdGenerator(None)
        self.assertEqual(IdGenerator.default_scope, id_generator.scope)

    @parameterized.expand([
        ["default scope", None, IdGenerator.default_scope],
        ["override scope", "new-scope", "new-scope"]
    ])
    def test_generate_scope_and_code(self, _, scope, expected_scope):
        id_generator = IdGenerator()
        gen_entity, gen_scope, gen_code = id_generator.generate_scope_and_code("portfolio", scope=scope)

        self.assertEqual("portfolio", gen_entity)
        self.assertEqual(expected_scope, gen_scope)
        self.assertIsNotNone(gen_code)
        self.assertIsNot("", gen_code)

    def test_generate_scope_and_code_with_scope_prefix(self):
        code_prefix= "abc-"
        id_generator = IdGenerator()
        gen_entity, gen_scope, gen_code = id_generator.generate_scope_and_code("portfolio", code_prefix=code_prefix)

        self.assertEqual("portfolio", gen_entity)
        self.assertEqual(IdGenerator.default_scope, gen_scope)
        self.assertIsNotNone(gen_code)
        self.assertTrue(gen_code.startswith(code_prefix))

    def test_clear_scope_and_code(self):
        id_generator = IdGenerator()
        id_generator.generate_scope_and_code("portfolio")

        vals = id_generator.pop_scope_and_codes()
        self.assertEqual(1, len(list(vals)))

        id_generator.clear()

        self.assertEqual(0, len(list(vals)))

    def test_get_scope_and_code(self):
        id_generator = IdGenerator()
        entity, scope, code = id_generator.generate_scope_and_code("portfolio")

        val = next(id_generator.pop_scope_and_codes(), None)

        self.assertEqual(scope, val[1])

        val = next(id_generator.pop_scope_and_codes(), None)
        self.assertIsNone(val)

    def test_get_multiple_scope_and_codes(self):
        id_generator = IdGenerator()
        n = 5

        vals = {
            id_generator.generate_scope_and_code("portfolio")
            for _ in range(n)
        }

        gen_vals = set(id_generator.pop_scope_and_codes())
        self.assertEqual(n, len(gen_vals))
        self.assertSetEqual(vals, gen_vals)

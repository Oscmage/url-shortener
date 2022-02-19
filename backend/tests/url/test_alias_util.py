from unittest import TestCase

from app.url.alias_util import AliasUtil


class TestAliasUtil(TestCase):

    def test_generate_alias_length(self):
        l = 6
        res = AliasUtil.generate_alias(l)

        self.assertEqual(len(res), l)

    def test_generate_alias_valid_characters(self):
        res = AliasUtil.generate_alias(6)

        for c in res:
            self.assertIn(c, AliasUtil.VALID_CHARACTERS_SET)

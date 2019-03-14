import yaml
import rpn
import unittest

result = rpn.calculate("1 1 +")
document = str(result)
unittest.TestCase.assertEqual(2, result)
print(yaml.dump(yaml.load(document)))
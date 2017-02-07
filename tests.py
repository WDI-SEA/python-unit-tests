import unittest

test_modules = [
  'specs.item_spec'
  #'specs.book_spec',
  #'specs.cd_spec',
  #'specs.bluray_spec',
  #'specs.digitalitem_spec'
]

suite = unittest.TestSuite()

for test in test_modules:
  suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

unittest.TextTestRunner(verbosity=2).run(suite)

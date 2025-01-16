# «TestSuite» — это набор тестов, которые мы собираем, добавляя в них различные тестовые случаи.
# При необходимости мы можем создавать несколько «test_suite» и запускать их по отдельности,
# что будет идеальным решением для нас.
# Такая структура подходит для серьезного промышленного уровня разработки.
import unittest
import module_12_1_test
import module_12_2_test

test_ST = unittest.TestSuite()

test_ST.addTests(unittest.TestLoader().loadTestsFromTestCase(module_12_1_test.RunnerTest))

test_ST.addTests(unittest.TestLoader().loadTestsFromTestCase(module_12_2_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(test_ST)
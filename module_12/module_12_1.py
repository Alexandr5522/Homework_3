import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Метод, в котором создаётся объект класса Runner с произвольным именем.
        Вызов метода walk у этого объекта 10 раз.
        Методом assertEqual сравнивается distance этого объекта со значением 50."""
        run_name = runner.Runner('Vasya')
        for i in range(10):
            run_name.walk()
        self.assertEqual(run_name.distance, 50)

    def test_run(self):
        """Метод, в котором создаётся объект класса Runner с произвольным именем.
        Вызывается метод run у этого объекта 10 раз.
        Методом assertEqual сравнивается distance этого объекта со значением 100."""
        run_name = runner.Runner('Vasya')
        for i in range(10):
            run_name.run()
        self.assertEqual(run_name.distance, 100)

    def test_challenge(self):
        """Метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Дистанции должны быть разными, используется метод assertNotEqual, чтобы убедится в неравенстве результатов."""
        run_name1 = runner.Runner('Vasya')
        run_name2 = runner.Runner('Vasya')
        for i in range(10):
            run_name1.run()
        for i in range(10):
            run_name2.walk()
        self.assertNotEqual(run_name1.distance, run_name2.distance)


"""Запускается кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку"""
if __name__ == "__main__":
    unittest.main()

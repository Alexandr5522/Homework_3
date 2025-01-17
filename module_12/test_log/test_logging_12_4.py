import unittest
import rt_with_exceptions
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False  # меняя на True определяем не выполнять проверку метода тестом

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # Метод, в котором создаётся объект класса Runner с произвольным именем.
        # Вызов метода walk у этого объекта 10 раз.
        # Методом assertEqual сравнивается distance этого объекта со значением 50.
        try:
            run_name = rt_with_exceptions.Runner('Vasya')
            for i in range(10):
                run_name.walk()
            self.assertEqual(run_name.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        # Метод, в котором создаётся объект класса Runner с произвольным именем.
        # Вызывается метод run у этого объекта 10 раз.
        # Методом assertEqual сравнивается distance этого объекта со значением 100.
        try:
            run_name = rt_with_exceptions.Runner(['Seva'])
            for i in range(10):
                run_name.run()
            logging.info('"test_run" выполнен успешно', exc_info=True)
            self.assertEqual(run_name.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        # Метод в котором создаются 2 объекта класса Runner с произвольными именами.
        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        # Дистанции должны быть разными, используется метод assertNotEqual, чтобы убедится в неравенстве результатов.
        run_name1 = rt_with_exceptions.Runner('Vasya')
        run_name2 = rt_with_exceptions.Runner('Fedya')
        for i in range(10):
            run_name1.run()
        for i in range(10):
            run_name2.walk()
        self.assertNotEqual(run_name1.distance, run_name2.distance)
        logging.info('"test_challenge" выполнен успешно', exc_info=True)


# записываются логи в файл
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

# Запускается кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку
if __name__ == "__main__":
    unittest.main()


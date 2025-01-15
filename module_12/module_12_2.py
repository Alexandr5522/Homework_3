import unittest
from module_12.runner import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Создаёт атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усейн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # выводятся данные all_results по очереди в столбец
        res = {}
        for key, value in sorted(cls.all_results.items()):
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def test_usain(self):
        tour = Tournament(90, self.runner_usain, self.runner_nik)
        result = tour.start()
        self.all_results[1] = result
        self.assertTrue(self.runner_nik.name == result[2])

    def test_andrey_nik(self):
        tour = Tournament(90, self.runner_andrey, self.runner_nik)
        result = tour.start()
        self.all_results[2] = result
        self.assertTrue(self.runner_nik.name == result[2])

    def test_andrey_usain_nik(self):
        tour = Tournament(90, self.runner_andrey, self.runner_usain, self.runner_nik)
        result = tour.start()
        self.all_results[3] = result
        self.assertTrue(self.runner_nik.name == result[3])


if __name__ == '__main__':
    unittest.main()

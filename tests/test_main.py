from utils import  space , amount , screen , description, data_sorted , view_screem

def test_1():
   assert space() == []

def test_2():
   assert amount(data_sorted, y=0) == ['48150.39', 'USD']

def test_3():
   assert amount(data_sorted, y=1) == ['30153.72', 'руб.']

def test_4():
   assert screen(data_sorted, y=0) == ['Classic', '2842', '87**', '****', '9012', '-->', 'Счет', '**3655']

def test_5():
   assert screen(data_sorted, y=1) == ['Maestro', '7810', '84**', '****', '5568', '-->', 'Счет', '**2869']

def test_6():
   assert description(data_sorted, y=0) == ['2019-12-07', 'Перевод организации']

def test_7():
   assert description(data_sorted, y=4) == ['2019-09-29', 'Перевод со счета на счет']

def test_8():
   assert view_screem(data_sorted) == ['2019-12-07', 'Перевод организации', 'Classic', '2842', '87**', '****', '9012', '-->', 'Счет', '**3655', '48150.39', 'USD', '2019-11-19', 'Перевод организации', 'Maestro', '7810', '84**', '****', '5568', '-->', 'Счет', '**2869', '30153.72', 'руб.', '2019-11-13', 'Перевод со счета на счет', 'Счет', '3861', '14**', '****', '9794', '-->', 'Счет', '**8125', '62814.53', 'руб.', '2019-10-30', 'Перевод с карты на счет', 'Gold', '7756', '67**', '****', '2839', '-->', 'Счет', '**9453', '23036.03', 'руб.', '2019-09-29', 'Перевод со счета на счет', 'Счет', '3542', '14**', '****', '9637', '-->', 'Счет', '**4961', '45849.53', 'USD']

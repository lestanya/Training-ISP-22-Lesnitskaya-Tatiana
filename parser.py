import cianparser

# формат кода

locations = [ 'Москва', 'Черноголовка', 'Одинцово', 'Электросталь', 'Щёлково',
    'Дрезна', 'Клин', 'Егорьевск', 'Высоковск', 'Лыткарино', 'Чехов',
    'Хотьково', 'Сергиев Посад', 'Павловский Посад', 'Красногорск',
    'Химки', 'Дмитров', 'Яхрома', 'Долгопрудный', 'Троицк', 'Балашиха',
    'Подольск', 'Мытищи', 'Люберцы', 'Королёв', 'Домодедово', 'Серпухов',
    'Коломна', 'Раменское', 'Реутов', 'Пушкино', 'Жуковский', 'Видное',
    'Орехово-Зуево', 'Ногинск', 'Воскресенск', 'Ивантеевка', 'Лобня',
    'Дубна', 'Котельники', 'Фрязино', 'Дзержинский', 'Краснознаменск',
    'Кашира', 'Звенигород', 'Истра', 'Красноармейск', 'Волоколамск',
    'Озёры', 'Кубинка', 'Пущино', 'Талдом', 'Руза', 'Краснозаводск',
    'Пересвет', 'Можайск']

for location in locations:
    parser = cianparser.CianParser(location=location)

    data = parser.get_flats(deal_type='sale', rooms=(1, 2, 3, 4), with_saving_csv=True, additional_settings={'start_page': 1, 'end_page': 50})

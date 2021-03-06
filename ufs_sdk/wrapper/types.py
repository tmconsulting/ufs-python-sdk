class BonusCardType:
    BONUS_CARD = 'BonusCard'
    UNIVERSAL_CARD = 'UniversalCard'
    RZHD_BINNUS_DISCOUNT = 'RzdBonusDiscount'


class SegmentType:
    # Неопределенный
    UNKNOWN = 'Unknow'
    # Одиночный ЖД сегмент
    RAILWAY = 'Railway'
    # Паромный сегмент
    FERRY = 'Ferry'
    # ЖД сегмент, но в заказе еще есть паромный сегмент
    RAILWAY_FERRY = 'Railwaywithferry'
    # Автобусный сегмент
    BUS = 'Bus'
    # ЖД сегмент, но в заказе есть еще сегмент с автобусом
    RAILWAY_BUS = 'Railwaywithbus'
    # ЖД сегмент, но в заказе есть еще паромный сегмент и сегмент с автобусом
    RAILWAY_BUS_FERRY = 'Railwaywithbusandferry'
    # Направление туда
    THERE = 'There'
    # Направление обратно
    BACK = 'Back'
    # ЖД сегмент, направление туда
    RAILWAY_THERE = 'Railwaythere'
    # ЖД сегмент, направление обратно
    RAILWAY_BACK = 'Railwayback'

class DocType:
    PASSPORT = 'ПН'
    BIRTH_CERTIFICATE = 'СР'
    RUSSIAN_FOREIGN_PASSPORT = 'ЗП'
    FOREIGN_PASSPORT = 'ЗЗ'
    PASSPORT_SEAMAN = 'ПМ'
    MILITARY_ID = 'ВБ'
    USSR_PASSPORT = 'ПС'
    MILITARY_OFFICER_CARD = 'УВ'
    STATELESS_PERSON_ODENTITY_CARD = 'БГ'
    RESIDENCE_PERMIT = 'ВЖ'
    RUSSIAN_TEMPORARY_IDENTITY_CARD = 'СУ'


class TimeSw:
    # Временной интервал не учитывается
    NO_SW = 0
    # Временной интервал применяется к моменту отправки поезда
    # (параметры Time_from, Time_to в таком случае принимаются целочисленным типом в интервале [0;24])
    TRAIN_DISPATCH = 1
    # Временной интервал применяется к моменту прибытия поезда
    # (параметры Time_from, Time_to в таком случае принимаются целочисленным типом в интервале [0;23])
    TRAIN_ARRIVAL = 2


class DirectionGroup:
    # Внутригосударственное сообщение, а также международное сообщение
    # со странами-участниками СНГ, Литовской, Латвийской, Эстонской, республиками, Республикой Абхазия
    INTERNAL = 0
    # Международное сообщение в дальнем зарубежье по глобальным ценам. Направление Россия-Финляндия
    RUSSIAN_FINLAND = 1
    # Международное сообщение в дальнем зарубежье по глобальным ценам. Направление Восток-Запад
    EAST_WEST = 2


class Lang:
    RU = 'Ru'
    EN = 'En'
    DE = 'De'


class TrainWithSeat:
    # Получение информации о поездах со свободными местами
    FREE_PLACE = 1
    # Получение информации обо всех поездах
    ALL = 0


class GrouppingType:
    # Группировка поездов по типу вагона
    TYPE = 0
    # Группировка поездов по типу вагона и по классу обслуживания
    TYPE_AND_SERVICE = 1
    # Группировка по типу вагона и по признакам QM/DM
    TYPE_AND_QM_DM = 2
    # Группировка по типу мест и цене
    PLACE_TYPE_AND_PRICE = 3
    # Группировка по номеру вагона и цене
    CAR_NUMBER_AND_PRICE = 4
    # Без группировки
    NONE = 5


class JoinTrains:
    # Получение списка поездов со склейкой
    WITH_BONDING = 0
    # Получение списка поездов без склеивания. Используется в случае, если в одном и том же поезде разные вагоны имеют разное время прибытия
    WITHOUT_BONDING = 1


class SearchOption:
    # Обычный поиск
    DEFAULT = 0
    # Включить в поиск маршруты в Крымский федеральный округ
    CRIMEA = 1
    # Включить в поиск мультимодальные перевозки
    MULTIMODAL = 2
    # Включить в поиск маршруты в Крымский федеральный округ и мультимодальные перевозки
    CRIMEA_AND_MULTIMODAL = 3
    # Включить в поиск маршруты с пересадкой
    TRANSFER = 4
    # Включить в поиск маршруты в Крымский федеральный округ и маршруты с пересадкой
    CRIMEA_AND_TRANSFER = 5
    # Включить в поиск мультимодальные перевозки и маршруты спересадкой
    MULTIMODAL_AND_TRANSFER = 6
    # Включить в поиск маршруты в Крымский федеральный округ, маршруты с пересадкой и мультимодалные перевозки
    ALL = 7


class AllowedDocType:
    PASSPORT = 'ПН'
    BIRTH_CERTIFICATE = 'СР'
    MILITARY_ID = 'ВБ'
    PASSPORT_SEAMAN = 'ПМ'
    RUSSIAN_FOREIGN_PASSPORT = 'ЗП'
    FOREIGN_PASSPORT = 'ЗЗ'


class Services:
    EAT = 'EAT'
    PAP = 'PAP'
    TV = 'TV'
    TRAN = 'TRAN'
    COND = 'COND'
    BED = 'BED'
    SAN = 'SAN'
    WIFI = 'WIFI'


class LoyaltyCards:
    # Начисление баллов "РЖД Бонус"
    RZHD_BONUS_SCORING = 'RzhdB'
    # Дорожная карта
    RZHD_MAP = 'RzhdU'
    # Скидка по карте "РЖД Бонус"
    RZHD_BONUS_DISCOUNT = 'RzhdSU'


class CarCategories:
    # Купейный вагон РИЦ (KV = КУПЕ)
    KUPE = 'РИЦ'
    # Мягкий вагон РИЦ (KV=МЯГК)
    SOFT = 'РИЦ'
    # Мягкий вагон Вагон Люкс (KV=МЯГК)
    SOFT_LUX = 'ЛЮКС'
    # Вагон класса люкс Вагон СВ (KV = ЛЮКС)
    LUX = 'СВ'


class AvailableTariffs:
    # Полный
    FULL = 1
    # Детский (до 10 лет)
    CHILD_TO_10 = 2
    # Детский без места (до 5 лет)
    CHILD_WITHOUT_PLACE_TO_5 = 3
    # SENIOR (60+) в Сапсан
    SENIOR_SAPSAN = 4
    # SENIOR (от 60 лет) ГЕНИАЛЬНО
    SENIOR = 5
    # JUNIOR (от 12 до 26 лет)
    JUNIOR = 6
    # Детский (до 12 лет)
    CHILD_TO_12 = 7
    # Детский без места (до 4 лет)
    CHILD_WITHOUT_PLACE_TO_4 = 8
    # Детский (до 17 лет)
    CHILD_TO_17 = 9
    # Детский без места (до 6 лет)
    CHILD_WITHOUT_PLACE_TO_6 = 10
    # Детский (до 7 лет)
    CHILD_TO_7 = 11
    # Детский без места(до 10 лет)
    CHILD_WITHOUT_PLACE_TO_10 = 12
    # Детский (от 10 до 17 лет)
    CHILD_FROM_10_TO_17 = 13
    # Школьник (для учащихся от 10 лет)
    SCHOOLBOY_FROM_10 = 14
    # Детский без места (для детей до 12 лет)
    CHILD_WITHOUT_PLACE_TO_12 = 15
    # Детский без места (для детей до 6 лет) ЧТО ? В ЧЁМ ТУТ РАЗНИЦА С ПУНКТОМ ВЫШЕ ? УФСМАТЬВАШУ
    CHILD_2_WITHOUT_PLACE_TO_6 = 16
    # Молодежный ЮНИОР (для лиц от 10 до 21 года)
    JUNIOR_FROM_10_TO_21 = 17
    # Праздничный
    FESTIVE = 18
    # Свадебный
    WEDDING = 19
    # Семейный
    FAMILY = 20


class PlaceTypeNumber:
    # Нижний ярус
    TOP = 'Н'
    # Верхний ярус
    BOTTOM = 'В'
    # Средний ярус
    MIDDLE = 'С'
    # (для сидячих вагонов) Для пассажира с животным
    ANIMALS = 'Ж'
    # (для сидячих вагонов) Для матери и ребенка
    MOTHER_CHILD = 'М'
    # (для сидячих вагонов) Для пассажира с детьми
    CHILDREN = 'Р'
    # (для сидячих вагонов) Для инвалидов
    INVALID = 'И'
    # (для сидячих вагонов) Переговорная
    MEETING_ROOM = 'Г'
    # (для сидячих вагонов) Не у стола
    NOT_TABLE = 'Н'
    # (для сидячих вагонов) У стола
    TABLE = 'П'
    # (для сидячих вагонов) У детской площадки
    PLAYGROUND = 'В'
    # (для сидячих вагонов) У стола рядом с детской площадкой
    TABLE_PLAYGROUND = 'Б'
    # (для сидячих вагонов) Рядом с местами для пассажиров с животными
    BESIDE_ANIMALS = 'Д'
    # (для сидячих) Откидное
    FOLDING = 'О'
    # (для сидячих вагонов) Отсек (купе) в поезде Ласточка
    SITTING_KUPE = '7'


class Confirm:
    # Отказ от зарезервированного заказа
    REFUSE = 0
    # Подтверждение зарезервированного заказа
    CONFIRM = 1
    # Выбрано трехчасовое резервирование заказа
    THREE_HOURS = 2


class ElectronicRegistration:
    # Отказ от электронной регистрации
    REFUSE = 0
    # Согласие на электронную регистрацию
    CONFIRM = 1
    # Установка ЭР не возможна
    IMPOSSIBLE = 3
    # Промежуточный статус, устанавливается до отмены ЭР
    PRE_REFUSE= 4
    # Промежуточный статус, устанавливается до подтверждения заказа.
    PRE_CONFIRM = 5
    # Статус ЭР не известен
    NO_DATA = 6
    # Бланк с ЭР распечатан
    PRINTED = 7
    # Статусы ЭР в бланках одного заказа различаются
    DIFFERENT_DATA = 8
    # Ошибочный статус ЭР
    ERROR_STATUS = 20


class Test:
    # Покупка настоящая (после её подтверждения деньги будут списаны)
    REAL = 0
    # Покупка тестовая, обращения на резервирование мест в АСУ «Экспресс-3» не было
    TEST = 1


class PrintFlag:
    # Не распечатан
    NOT_PRINTED = 0
    # Распечатан
    PRINTED = 1


class RzhdStatus:
    # Без электронной регистрации
    WITHOUT_ELECTRONIC_REGISTRATION = 0
    # Электронная регистрация
    ELECTRONIC_REGISTRATION = 1
    # Оплата не подтверждена
    FAILED_PAYMENT = 2
    # Аннулирован
    CANCELED = 3
    # Возвращен
    RETURNED = 4
    # Возвращены места
    RETURNED_PLACES= 5
    # Выдан посадочный купон (проездной документ) на бланке строгой отчетности
    TICKET_ISSUED = 6
    # Отложенная отплата (статус возвращается после создания бронирования)
    DEFERRED_PAYMENT = 7


class Registration:
    REFUSE = 0
    CONFIRM = 1


class ReferenceCode:
    CO_SERVICES = 'CO_SERVICES'
    LOYALTY_CARDS = 'LOYALTY_CARDS'


class InOneKupe:
    # Требование не задано
    NONE = 0
    # В одном купе/в одном ряду (для вагонов с местами для сидения)
    IN_ONE_KUPE_OR_ROW = 1
    # Не боковые места
    NOT_SIDE = 2
    # Места в одном отсеке
    IN_ONE_COMPARTMENT = 3


class Bedding:
    # В стоимость билета не включено постельное белье
    NO_LINENS = 0
    # В стоимость билета включено постельное белье
    LINENS = 1


class FullKupe:
    # Выкуп купе целиком
    ALL_KUPE = 1
    # Выкуп СВ целиком
    ALL_SV = 2


class RemoteCheckIn:
    # Без электронной регистрации
    WITHOUT_ELECTRONIC_REGISTRATION = 0
    # Электронная регистрация
    ELECTRONIC_REGISTRATION = 1
    # Если ЭР возможна, то при подтверждении ЭР устанавливается автоматически
    TRY_AUTO_ER = 2


class PayType:
    # Оплата наличными
    CASH = 'Cash'
    # Credit card. Оплата банковской картой. Данный тип оплаты доступен не всем партнерам.
    CREDIT_CARD = 'CC'


class Storey:
    # Требования к этажу не заданы
    NONE = 0
    # Первый этаж вагона
    FIRST_STOREY = 1
    # Второй этаж вагона
    SECOND_STOREY = 2


class PlaceDemands:
    # Места не у стола
    NO_TABLE = 'Н'
    # Места у стола (обычные места)
    TABLE = 'П'
    # Места рядом с детской площадкой и не у стола
    PLAYGROUND_NO_TABLE = 'В'
    # Места рядом с детской площадкой и у стола
    PLAYGROUND_TABLE = 'Б'
    # Места рядом с местами для пассажиров с животными
    BESIDE_ANIMALS = 'Д'
    # Любое место у стола (включая рядом с местами для пассажиров с животными, детской площадкой и т.д)
    ANY_TABLE = 'СТОЛ'
    # Места не у стола, включая места рядом с детской площадкой и рядом с местами для пассажиров с животными.
    # Обобщающее требование. Рекомендуется использовать в случае, если не выбран номер вагона
    PLAYGROUND_ANIMALS_NO_TABLE = 'НСТ'
    # Места рядом с детской площадкой
    PLAYGROUND = 'ДЕТ'
    # Места для инвалидов
    INVALID = 'И'
    # Места для пассажиров с животными
    FOR_ANIMALS = 'Ж'
    # Отсек (купе)
    KUPE = '7'
    # Откидное место
    HINGED_SEAT = 'О'
    # Место матери и ребенка до 1 года
    MOTHER_AND_CHILDREN_TO_1 = 'М'
    # Места для пассажиров с детьми
    MOTHER_AND_CHILDREN = 'Р'


class TicketFormat:
    HTML = 'html'
    PDF = 'pdf'


class Gender:
    MALE = 'мужское'
    FEMALE = 'Женское'
    MIXED = 'Смешаное'


class AllLanguages:
    # Ответ на всех доступных языках;
    ALL = 1
    # Ответ только на одном конкретном языке, который указан в элементе Lang
    AS_LANG = 0

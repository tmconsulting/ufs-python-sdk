import logging
from . import request
from .utils import get_item
from .session import Session
from .wrapper.requests import RequestWrapper
from .utils import get_array, get_bool_item, get_datetime, get_list_from_string, get_money
from .wrapper.types import (TimeSw, Lang, TrainWithSeat, GrouppingType, JoinTrains, SearchOption, Confirm, Registration,
                            ReferenceCode, InOneKupe, Bedding, FullKupe, RemoteCheckIn, PayType, Storey, PlaceDemands,
                            TicketFormat, PayType)
from .wrapper import (Clarify, TimeTable, AdditionalInfoStationRoute, RouteParamsStationRoute, TrainList,
                      GeneralInformation, TrainCarListEx, Blank, DateTime, BlankUpdateOrderInfo, Order,
                      BlankElectronicRegistration, Food, BlankRefund, Cards, PassDoc, TicketInfo, Fee, Warnings,
                      PrintPoints, OrderItemXml, OrderTransInfo)


class API(object):
    def __init__(self, username: str, password: str, terminal: str, logger: logging.Logger=None, ssl_verify=True):
        self.__session = Session(username, password, terminal, logger, ssl_verify)
        self.__request_wrapper = RequestWrapper(self.__session)

    def time_table(self, from_: 'str or int', to: 'str or int', day: int, month: int, time_sw: TimeSw=TimeSw.NO_SW,
                   time_from: int=None, time_to: int=None, suburban: bool=None):
        xml, json = self.__request_wrapper.make_request('TimeTable', from_=from_, to=to, day=day, month=month,
                                                        time_sw=time_sw, time_from=time_from, time_to=time_to,
                                                        suburban=suburban)
        return TimeTableBuilder(xml, json['S'])

    def station_route(self, day: int, month: int, from_: 'str or int', use_static_schedule: bool, suburban=None):
        xml, json = self.__request_wrapper.make_request('StationRoute', from_=from_, day=day, month=month,
                                                        use_static_schedule=use_static_schedule,
                                                        suburban=suburban)
        return StationRoute(xml, json['S'])

    def train_list(self, from_: 'str or int', to: 'str or int', day: int, month: int, advert_domain: str=None,
                   lang: str=Lang.RU, time_sw: TimeSw=TimeSw.NO_SW, time_from: int=TimeSw.TRAIN_DISPATCH, time_to: int=None,
                   train_with_seat: TrainWithSeat=TrainWithSeat.FREE_PLACE, join_train_complex: bool=False, grouping_type: GrouppingType=GrouppingType.TYPE,
                   join_trains: JoinTrains=JoinTrains.WITH_BONDING, search_option: SearchOption=SearchOption.DEFAULT):
        xml, json = self.__request_wrapper.make_request('TrainList', from_=from_, to=to, day=day, month=month,
                                                        advert_domain=advert_domain, time_sw=time_sw, lang=lang,
                                                        time_from=time_from, time_to=time_to, train_with_seat=train_with_seat,
                                                        join_train_complex=join_train_complex, groupping_type=grouping_type,
                                                        join_trains=join_trains, search_option=search_option)
        return TrailListBuilder(xml, json)

    def car_list_ex(self, from_: 'str or int', to: 'str or int', day: int, month: int, train: 'str or int',
                    time: str=None, lang: Lang=Lang.RU, type_car=None, advert_domain: str=None,
                    groupping_type: GrouppingType=None):
        xml, json = self.__request_wrapper.make_request('CarListEx', from_=from_, to=to, day=day, month=month,
                                                        train=train, time=time, lang=lang, type_car=type_car,
                                                        advert_domain=advert_domain, groupping_type=groupping_type)
        return CarListEx(xml, json['S'])

    def buy_ticket(self, from_: 'str or int', to: 'str or int', day: int, month: int, train, type_car: str,
                   pass_doc: PassDoc, in_one_kupe: InOneKupe, remote_check_in: RemoteCheckIn,  pay_type: PayType,
                   n_car: int=None, service_class: str=None, sex: str=None, diapason=None, n_up: int=None,
                   n_down: int=None, bedding: Bedding=None, stan: str=None, advert_domain: str=None, phone: int=None,
                   lang: Lang=Lang.RU, id_cust: int=None, storey: Storey=None, time=None, comment: str=None,
                   placedemands: PlaceDemands=None, international_service_class=None, full_kupe: FullKupe=None):
        xml, json = self.__request_wrapper.make_request('BuyTicket', from_=from_, to=to, day=day, month=month,
                                                        train=train, type_car=type_car, pass_doc=pass_doc.pass_doc,
                                                        in_one_kupe=in_one_kupe, remote_check_in=remote_check_in,
                                                        pay_type=pay_type, n_car=n_car, service_class=service_class,
                                                        sex=sex, diapason=diapason, n_up=n_up, n_down=n_down,
                                                        bedding=bedding, stan=stan, advert_domain=advert_domain,
                                                        phone=phone, lang=lang, id_cust=id_cust, storey=storey,
                                                        time=time, comment=comment, placedemands=placedemands,
                                                        international_service_class=international_service_class,
                                                        full_kupe=full_kupe)
        return BuyTicket(xml, json)

    def buy_tickets_xml(self, segments: [request.Segment], passengers: [request.Passenger], formpay: PayType,
                        lang: Lang=Lang.RU, phone: str=None, email: str=None):
        
        order = request.Order(segments, passengers, formpay, lang, phone, email)

        xml, json = self.__request_wrapper.make_request('BuyTicketXml', order.xml)

        return OrderXML(xml, json['Order'])

    def confirm_ticket(self, id_trans: int, confirm: Confirm, site_fee: int=None, lang: Lang=Lang.RU):
        xml, json = self.__request_wrapper.make_request('ConfirmTicket', id_trans=id_trans, confirm=confirm,
                                                        site_fee=site_fee, lang=lang)
        return ConfirmTicket(xml, json)

    def update_order_info(self, id_trans: int):
        xml, json = self.__request_wrapper.make_request('UpdateOrderInfo', id_trans=id_trans)
        return UpdateOrderInfo(xml, json)

    def electronic_registration(self, id_trans: int, reg: Registration, id_blank: [int]=None):
        if id_blank is not None:
            id_blank = ','.join([str(item) for item in id_blank])
        xml, json = self.__request_wrapper.make_request('ElectronicRegistration', id_trans=id_trans, reg=reg,
                                                        id_blank=id_blank)
        return ElectronicRegistration(xml, json)

    def get_ticket_blank(self, id_trans: int, format: TicketFormat=TicketFormat.PDF, blank_id=None):
        response = self.__request_wrapper.make_request('GetTicketBlank', id_trans=id_trans, format=format,
                                                       blank_id=blank_id)
        return GetTicketBlank(response, format)

    def available_food(self, id_trans: int, advert_domain: str, lang: Lang.RU=Lang.RU):
        xml, json = self.__request_wrapper.make_request('AvailableFood', id_trans=id_trans, advert_domain=advert_domain,
                                                        lang=lang)
        return AvailableFood(xml, json)

    def change_food(self, id_trans: int, blanks_id: int, food_allowance_code: str, advert_domain: str,
                    lang: Lang.RU=Lang.RU):
        xml, json = self.__request_wrapper.make_request('ChangeFood', id_trans=id_trans, blanks_id=blanks_id,
                                                        food_allowance_code=food_allowance_code,
                                                        advert_domain=advert_domain, lang=lang)
        return ChangeFood(xml, json['PIT'])

    def refund_amount(self, id_trans: int, id_blank: [int], doc: int, lang: Lang.RU=Lang.RU):
        if id_blank is not None:
            id_blank = ','.join([str(item) for item in id_blank])
        xml, json = self.__request_wrapper.make_request('RefundAmount', id_trans=id_trans, id_blank=id_blank,
                                                        doc=doc, lang=lang)
        return RefundAmount(xml, json)

    def refund(self, id_trans: int, id_blank: [int], doc: int, stan: str=None, lang: Lang.RU=Lang.RU):
        if id_blank is not None:
            id_blank = ','.join([str(item) for item in id_blank])
        xml, json = self.__request_wrapper.make_request('Refund', id_trans=id_trans, id_blank=id_blank,
                                                        doc=doc, stan=stan, lang=lang)
        return Refund(xml, json)

    def get_catalog(self, code: ReferenceCode, all_languages: int=None, lang: Lang.RU=Lang.RU,
                    is_description: bool=None):
        xml, json = self.__request_wrapper.make_request('GetCatalog', code=code, all_languages=all_languages, lang=lang,
                                                        is_description=is_description)
        return GetCatalog(xml, json)

    def trans_info(self, id_trans: int, n_born: int=None, stan: str=None, lang: Lang=Lang.RU):

        xml, json = self.__request_wrapper.make_request('TransInfo', id_trans=id_trans, n_born=n_born, stan=stan, lang=lang)

        return TransInfo(xml, json)

    @property
    def last_response(self):
        return self.__session.last_response_data

    @property
    def last_request(self):
        return self.__session.last_request_data


class TimeTableBuilder(object):
    def __init__(self, xml, json):
        # Признак уточнения станции
        self.is_clarify = get_bool_item(json.get('UC', None))
        if self.is_clarify:
            # Признак начальной или конечной станции следования
            self.train_point = json.get('parameter', None)
            self.data = Clarify(json)
        else:
            self.data = TimeTable(json)

        self.xml = xml
        self.json = json


class StationRoute(object):
    def __init__(self, xml, json):
        # УФС слишком крутые, им не надо описание данного поля. Нам, видимо, тоже...
        self.additional_info = get_item(json.get('Z1'), AdditionalInfoStationRoute)
        self.route_params = get_item(json.get('PP'), RouteParamsStationRoute)

        self.xml = xml
        self.json = json


class TrailListBuilder(object):
    def __init__(self, xml, json):
        # Признак уточнения станции
        self.is_clarify = get_bool_item(json['S'].get('UC', None))
        if self.is_clarify:
            # Признак начальной или конечной станции следования
            self.train_point = json['S'].get('parameter', None)
            self.data = Clarify(json['S'])
        else:
            self.data = TrainList(json['S'])
            self.balance = get_money(json.get('Balance'))
            self.balance_limit = get_money(json.get('BalanceLimit'))

        self.xml = xml
        self.json = json


class CarListEx(object):
    def __init__(self, xml, json):
        # Общая информация по запросу
        self.general_information = get_item(json.get('Z3'), GeneralInformation)
        # Информация о поезде
        self.train = get_item(json.get('N'), TrainCarListEx)

        self.xml = xml
        self.json = json


class ConfirmTicket(object):
    def __init__(self, xml, json):
        self.status = get_item(json.get('Status'), int)
        self.transaction_id = get_item(json.get('TransID'), int)
        self.confirm_time_limit = get_item(json.get('ConfirmTimeLimit'), DateTime)
        self.electronic_registration = get_item(json.get('RemoteCheckIn'), int)
        self.order_number = get_item(json.get('OrderNum'), int)
        self.electronic_registration_expire = get_item(json.get('ExpireSetEr'), DateTime)
        self.blank = get_array(json.get('Blank'), Blank)
        self.is_test = get_item(json.get('IsTest'), int)
        self.reservation = json.get('Reservation')

        self.xml = xml
        self.json = json


class UpdateOrderInfo(object):
    def __init__(self, xml, json):
        # Текущий статус операции: «0» - успешная операция «1»- неуспешная операция
        self.status = get_item(json.get('Status'), int)
        # Информация о билете заказа
        self.blank = get_array(json.get('Blank'), BlankUpdateOrderInfo)
        # Дата и время, до которого можно воспользоваться услугой смены РП.
        # Атрибут «timeOffset="+ЧЧ:ММ"» содержит информацию о часовом поясе для данного элемента, где "+ЧЧ:ММ"
        # разница в часах и минутах от UTC(Всемирное координированное время) конкретного места.
        # Доступно для заказов с возможностью выбора РП
        self.change_food_before = get_item(json.get('ChangeFoodBefore'), DateTime)
        # Информация о заказе
        self.order = get_item(json.get('Order'), Order)

        self.xml = xml
        self.json = json


class ElectronicRegistration(object):
    def __init__(self, xml, json):
        # Текущий статус операции: «0» – успешная
        self.status = get_item(json.get('Status'), int)
        # Информация о билете заказа
        self.blanks = get_array(json.get('Blank'), BlankElectronicRegistration)

        self.xml = xml
        self.json = json


class GetTicketBlank(object):
    def __init__(self, response, format):
        self.format = format
        self.__data = response

    def save_blank(self, path):
        open(path, 'wb').write(self.content)

    @property
    def content(self):
        if self.format == TicketFormat.PDF:
            return self.__data.content
        return self.__data.text


class AvailableFood(object):
    def __init__(self, xml, json):
        self.change_food_before = get_item(json.get('ChangeFoodBefore'), DateTime)
        self.food = get_array(json['FoodAllowances'].get('Food'), Food) if json.get('FoodAllowances') is not None else None

        self.xml = xml
        self.json = json


class ChangeFood(object):
    def __init__(self, xml, json):
        # Порядковый номер документа
        self.number = json.get('PR')
        # Номер поезда
        self.train_number = json.get('N')
        # Дата отправления поезда
        self.departure_date = json.get('D')
        # Код станции отправления
        self.departure_number = get_item(json.get('C1'), int)
        # Код станции прибытия
        self.arrival_number = get_item(json.get('C2'), int)
        # Номер вагона
        self.car_number = get_item(json.get('B'), int)
        # Класс обслуживания
        self.service_class = json.get('KV')
        # Номера мест
        self.place_number = get_item(json.get('M'), int)
        # Количество пассажиров
        self.passengers_amount = get_item(json.get('KOL'), int)
        # Номер электронного билета
        self.electronic_number = get_item(json.get('NEB'), int)
        # Код РП
        self.food_code = json.get('V')
        # Название РП
        self.food_name = json.get('NAME')
        # Описание РП
        self.food_description = json.get('DESC')

        self.xml = xml
        self.json = json


class RefundAmount(object):
    def __init__(self, xml, json):
        # Статус операции: «0» – успешная
        self.status = get_item(json.get('Status'), int)
        # Сумма сервисного сбора за возврат
        self.fee = get_money(json.get('Fee'))
        # Величина комиссионного сбора УФС в %, В случае, если комиссия является фиксированной величиной,
        # то передается в данном параметре «0»
        self.tax_percent = get_item(json.get('TaxPercent'), float)
        # Общая сумма к возврату
        self.amount = get_money(json.get('Amount'))
        # Информация о билете заказа
        self.blanks = get_array(json.get('Blank'), BlankRefund)

        self.xml = xml
        self.json = json


class Refund(object):
    def __init__(self, xml, json):
        # Статус операции: «0» – успешная
        self.status = get_item(json.get('Status'), int)
        # Номер транзакции возврата
        self.refund_id = get_item(json.get('RefundTransID'), int)
        # Время осуществления возврата
        self.refund_date = get_datetime(json.get('RefundTime'))
        # Сумма сервисного сбора за возврат
        self.fee = get_money(json.get('Fee'))
        # Величина комиссионного сбора УФС в %, В случае, если комиссия является фиксированной величиной,
        # то передается в данном параметре «0»
        self.tax_percent = get_item(json.get('TaxPercent'), float)
        # Общая сумма к возврату
        self.amount = get_money(json.get('Amount'))
        # Информация о билете заказа
        self.blanks = get_array(json.get('Blank'), BlankRefund)

        self.xml = xml
        self.json = json


class GetCatalog(object):
    def __init__(self, xml, json):
        self.loyalty_cards = get_array(json.get('LOYALTY_CARDS'), Cards)
        self.co_services = get_array(json.get('CO_SERVICES'), Cards)

        self.xml = xml
        self.json = json


class BuyTicket(object):
    def __init__(self, xml, json):
        # Дата создания резервирования
        self.creation_date = json.get('D2')
        # Компания-перевозчик
        self.carrier = json.get('PER')
        # ИНН перевозчика
        self.carrier_inn = get_item(json.get('INN'), int)
        # Время резервирования
        self.reservation_time = json.get('TB')
        # Да Номер поезда (последняя буква – принадлежность «нитке»)
        self.train_number = json.get('N1')
        # Дата отправления
        self.departure_date = json.get('D3')
        # Время отправления
        self.departure_time = json.get('T1')
        # Категория поезда
        self.train_category = json.get('KN')
        # Название поезда
        self.train_name = json.get('KN1')
        # Бренд поезда
        self.train_brand = json.get('BRN')
        # Станция отправления
        self.origin = json.get('C')[0]
        # Станция прибытия
        self.destination = json.get('C')[1]
        # Код станции отправления
        self.origin_code = get_item(json.get('CC1'), int)
        # Код станции прибытия
        self.destination_code = get_item(json.get('CC2'), int)
        # Номер вагона
        self.car_number = get_item(json.get('VH'), int)
        # Тип сегмента (Таблица 106)
        self.segment_type = get_item(json.get('SegmentType'), int)
        # Категория вагона (Таблица 54)
        self.car_category = json.get('KV')
        # Класс обслуживания вагона (см. Приложение № 2)
        self.service_class = json.get('KL')
        # Признак купе «МУЖСКОЕ» / «ЖЕНСКОЕ». Если купе смешанное, значение не ставится.
        self.kupe_sex = json.get('R')
        # Название перевозчика
        self.carrier_name = json.get('VB')
        # Количество мест в заказе
        self.places_amount = get_item(json.get('M1'), int)
        # Номера мест в заказе
        self.place_number = get_list_from_string(json.get('H'), int)
        # Общая стоимость заказа с учетом НДС
        self.total_price = get_money(json.get('TF0'))
        # Уведомление пассажира об особых условиях поездки
        self.special_conditions = json.get('GA')
        # Информация о времени отправления
        self.departure_time_info = json.get('GB')
        # Признак вагона повышенной комфортности
        self.high_comfort = json.get('R0')
        # Дата прибытия
        self.arrival_date = json.get('D1')
        # Время прибытия
        self.arrival_time = json.get('T4')
        # Информация о заказанных билетах
        self.tickets_info = get_array(json.get('ET'), TicketInfo)
        # Время и дата отправления поезда
        self.departure_datetime = get_item(json.get('DepartureTime'), DateTime)
        # Время и дата прибытия поезда
        self.arrival_datetime = get_item(json.get('ArrivalTime'), DateTime)
        # Общая стоимость полученных билетов
        self.amount = get_money(json.get('Amount'))
        # Номер транзакции в системе «УФС»
        self.id_trans = get_item(json.get('IDTrans'), int)
        # Статус операции
        self.status = get_item(json.get('Status'), int)
        # Текущий баланс Агента
        self.balance = get_money(json.get('Balance'))
        # Актуальный кредит Агента в ЖД шлюзе
        self.balance_limit = get_money(json.get('BalanceLimit'))
        # Точка распечатки (пункт выдачи заказа)
        self.print_point = json.get('PrintPoint')
        # Телефон пункта выдачи билетов заказа
        self.print_point_phone = get_item(json.get('PrintPointPhone'), int)
        # Рекомендуется сверять значение этого признака со статусом терминала, использованного в запросе
        # (значения не должны противоречить друг другу)
        self.test = get_item(json.get('Test'), int)
        # Возможность распечатки электронного билета на станции отправления клиента
        self.is_eticket_print_point = get_bool_item(json.get('IsEticketPrintPoint'))
        # Дата и время, до которого можно подтвердить заказ.
        # Атрибут «timeOffset=»+ЧЧ:ММ»» содержит информацию о часовом поясе для данного элемента,
        # где «+ЧЧ:ММ» разница в часах и минутах от UTC(Всемирное координированное время) конкретного места
        self.confirm_time_limit = get_item(json.get('ConfirmTimeLimit'), DateTime)
        # Reservation B Нет Возможность осуществления трехчасового резервирования с целью проведения отложенной оплаты
        self.reservation = get_bool_item(json.get('Reservation'))
        # ReservationType EN Да Вид бронирования (Таблица 105)
        self.reservation_type = get_item(json.get('ReservationType'), int)
        # ClientFee N Да Вознаграждение агента
        self.client_fee = get_money(json.get('ClientFee'))
        # OrderId N Да Идентификатор заказа
        self.order_id = get_item(json.get('OrderId'), int)
        # Информирование о повторном бронировании
        if json.get('Warnings') is not None:
            self.warnings = get_array(json['Warnings'].get('Warning'), Warnings)
        else:
            self.warnings = None
        # Информация о станциях распечатки ЭБ
        if json.get('printPoints') is not None:
            self.print_points = get_array(json['printPoints'].get('EPrintPoint'), PrintPoints)
        else:
            self.print_points = None

        self.xml = xml
        self.json = json


class OrderXML(object):
    def __init__(self, xml, json):
        # Номер заказа в системе «УФС»
        self.order_id = get_item(json.get('Id'), int)
        # Сумма всего заказа
        self.amount = get_money(json.get('Amount'))
        # Идентификатор родительской транзакции
        self.transaction_id = get_item(json.get('RootTransId'), int)
        # Информация о каждом сегменте
        self.items = get_array(json.get('OrderItems', {}).get('OrderItem'), OrderItemXml)
        # Комиссия с клиента за оформленный заказ
        self.client_fee = get_money(json.get('ClientFee'))
        # Процент по комиссии
        self.client_tax_percent = get_item(json.get('ClientTaxPercent'), float)

        self.json = json


class TransInfo(object):
    def __init__(self, xml, json):
        self.transaction_id = get_item(json.get('TransID'), int)
        self.previous_transaction_id = get_item(json.get('PrevTransID'), int)
        self.lang = get_item(json.get('Lang'), str)
        self.last_refund_transaction_id = get_item(json.get('LastRefundTransID'), int)
        self.stan = get_item(json.get('STAN'), str)
        self.status = get_item(json.get('TStatus'), int)
        self.detailed_status = get_item(json.get('RStatus'), int)
        self.order_num = get_item(json.get('OrderNum'), int)
        self.segment_type = get_item(json.get('SegmentType'), str)
        self.is_terminal_only_return = get_bool_item(json.get('IsReturnedOnRailwayTerminal'))
        self.comment = get_item(json.get('Comment'), str)
        self.type = get_item(json.get('Type'), int)
        self.create_at = get_item(json.get('CreateTime'), DateTime)
        self.confirmed_at = get_item(json.get('ConfirmTime'), DateTime)
        self.booked_at = get_item(json.get('BookingTime'), DateTime)
        self.confirm_till = get_item(json.get('ConfirmTimeLimit'), DateTime)
        self.amount = get_money(json.get('Amount'))
        self.fee = get_money(json.get('Fee'))
        self.places_qunatity = get_item(json.get('PlaceCount'), int)
        self.train_number = get_item(json.get('TrainNum'), str)
        self.car_number = get_item(json.get('CarNum'), int)
        self.car_type = get_item(json.get('CarType'), str)
        self.departure_at = get_item(json.get('DepartTime'), DateTime)
        self.delta_departure_tz = get_item(json.get('DeltaDepartureLocalDate'), int)
        self.delta_arrival_tz = get_item(json.get('DeltaArrivalLocalDate'), int)
        self.phone = get_item(json.get('Phone'), str)
        self.email = get_item(json.get('Email'), str)
        self.service_class = get_item(json.get('ServiceClass'), str)
        self.origin = json.get('StationFrom', {}).get('data')
        self.origin_code = json.get('StationFrom', {}).get('Code')
        self.destination = json.get('StationTo', {}).get('data')
        self.destination_code = json.get('StationTo', {}).get('Code')
        self.gender_cabin = get_item(json.get('GenderClass'), int)
        self.arrival = get_item(json.get('ArrivalTime'), DateTime)
        self.carrier = get_item(json.get('Carrier'), str)
        self.carrier_inn = get_item(json.get('CarrierInn'), int)
        self.time_desc = get_item(json.get('TimeDescription'), str)
        self.ereg_expire_at = get_item(json.get('ExpireSetEr'), DateTime)
        self.direction = get_item(json.get('GroupDirection'), int)
        self.terminal = get_item(json.get('Terminal'), str)
        self.is_test = get_item(json.get('IsTest'), int)
        self.domain = get_item(json.get('Domain'), str)
        self.formpay = get_item(json.get('PayTypeId'), str)
        self.ufs_profit = get_money(json.get('UfsProfit'))
        self.is_suburban = get_bool_item(json.get('IsSuburbanTrain'))
        self.full_return = get_bool_item(json.get('QM')) or get_bool_item(json.get('DM'))
        self.is_international = get_bool_item(json.get('IsInternational'))        
        self.order = get_item(json.get('Order'), OrderTransInfo)
        self.change_food_till = get_item(json.get('ChangeFoodBefore'), DateTime)

        self.json = json

from enum import Enum, auto

class Status(Enum):
    """
    Provides status of the unit.
    """
    PRESENT = "0"
    PLANNED_ANTICIPATED_SUSPECT = "1"
    FULLY_CAPABLE = "2"
    DAMAGED = "3" 
    DESTROYED = "4"
    FULL_TO_CAPACITY = "5"

class Mobility(Enum):
    """
    Provides mobility of the unit. 
    """
    UNSPECIFIED = auto()
    WHEELED_LIMITED_CROSS_COUNTRY = auto()
    WHEELED_CROSS_COUNTRY = auto()
    TRACKED = auto()
    WHEELED_AND_TRACKED_COMBINATION = auto()
    TOWED = auto()

def set_mobility(sidc, mobility):
    """
    Set's mobility for disignated unit
    """
    if mobility == Mobility.WHEELED_LIMITED_CROSS_COUNTRY:
        sidc = set_char_at_position(sidc, '3', 8)
        sidc = set_char_at_position(sidc, '1', 9)
    elif mobility == Mobility.WHEELED_CROSS_COUNTRY:
        sidc = set_char_at_position(sidc, '3', 8)
        sidc = set_char_at_position(sidc, '2', 9)
    elif mobility == Mobility.TRACKED:
        sidc = set_char_at_position(sidc, '3', 8)
        sidc = set_char_at_position(sidc, '3', 9)
    elif mobility == Mobility.TOWED:
        sidc = set_char_at_position(sidc, '3', 8)
        sidc = set_char_at_position(sidc, '5', 9)
    else:  # Mobility.UNSPECIFIED or any other case
        sidc = set_char_at_position(sidc, '0', 8)
        sidc = set_char_at_position(sidc, '0', 9)
    return sidc

def set_char_at_position(sidc, character, position):
    "Replaces characters by gives ones"
    replacement = list(sidc)
    replacement[position] = character
    return ''.join(replacement)


class UnitDesignator:
    """
    Accepts a name of the unit and returns a SIDC code.
    """
    @staticmethod
    def calculate_icon(name: str) -> str:
        return UnitDesignator.calculate_icon_with_flag(name, True)

    @staticmethod
    def calculate_icon_with_flag(name: str, calculate_icon: bool) -> str:
        if calculate_icon and name:
            sidc = UnitDesignator.get_unit(name.upper())
            return "30062500001313000000" if sidc is None else sidc
        return "30062500001313000000"

    @staticmethod
    def get_unit(name: str) -> str:
        mobility = Mobility.UNSPECIFIED
        if "БУКСИРОВАНИЙ" in name:
            mobility = Mobility.TOWED
            name = name.replace("БУКСИРОВАНИЙ", "")

        sidc = UnitDesignator.designate_icon(name)

        if any(keyword in name for keyword in ["МАКЕТ", "МУЛЯЖ"]):
            if sidc is not None:
                return set_char_at_position(sidc, "1", 7)

        if any(keyword in name for keyword in ["УРАЖЕНО", "УРАЖЕНА", "ПОШКОДЖЕНА", "ПОШКОДЖЕНО", "ПОШКОДЖЕНІ"]):
            if sidc is not None:
                return set_char_at_position(sidc, Status.DAMAGED.value, 6)

        if any(keyword in name for keyword in ["ЗНИЩЕНОГО", "ЗНИЩЕНА", "ЗРУЙНОВАНО", "ЗНИЩЕНО"]):
            if sidc is not None:
                return set_char_at_position(sidc, Status.DESTROYED.value, 6)

        if "ВІДНОВЛЕНО" in name:
            if sidc is not None:
                return set_char_at_position(sidc, Status.FULL_TO_CAPACITY.value, 6)

        if any(keyword in name for keyword in ["ЙМОВІРНО", "МОЖЛИВО", "ЙМОВІРНА"]):
            if sidc is not None:
                return set_char_at_position(sidc, Status.PLANNED_ANTICIPATED_SUSPECT.value, 6)

        if  mobility != Mobility.UNSPECIFIED:
            sidc_with_mobility = set_mobility(sidc, mobility)
            return sidc_with_mobility

        return sidc

    @staticmethod
    def designate_icon(name: str) -> str:
        if any(keyword in name for keyword in ["ПРОТИТАНКОВИЙ РІВ ТА ПІРАМІДИ",
                                                "ПРОТИТАНКОВІ НАДОВБИ", "ПРОТИТАНКОВІ ПІРАМІДИ"]):
        # "ПРОТИТАНКОВИЙ РІВ ТА ПІРАМІДИ","30062500002819010000"   
            return "30062500002819010000"
        

        # не розумію чому тут так. Це ж майже такий самий патерн???
        if any(keyword in name for keyword in ["ПРОТИТАНКОВІ ПЕРЕШКОДИ", "ПРОТИТАНКОВІ НАДОВБИ", "ПРОТИТАНКОВИЙ", "ПРОТИТАНКОВИЙ РІВ"]):
            return None
        
        if any(keyword in name for keyword in ["РЛК ЯСТРЕБ АВ", "ROLL PARK"]):
            # "РЛК ЯСТРЕБ АВ","30061500322203000000"
            return "30061500322203000000"

        if any(keyword in name for keyword in ["Р-934БМВ", "Р-330Ж", "РЕБ", "КОМСТАНЦІЯ ПОДАВЛЕННЯ НАВІГАЦІЇПЛЕКС ПРОТИДІЇ БПЛА", "РБ-301Б", "ROSC 1", "ROSC-1",
                        "СТАНЦІЯ ПОДАВЛЕННЯ НАВІГАЦІЇ", "СТАНЦІЯ ПОДАВЛЕННЯ НАВІГАЦІЇ", "ПОЛЕ-21", "ПРИДУШЕННЯ ЗВ'ЯЗКУ",
                        "СТАНЦІЯ ПЕРЕШКОД СИСТЕМ НАВІГАЦІЇ", "КОМПЛЕКС ПРИДУШЕННЯ СИГНАЛІВ НАВІГАЦІЙНИХ СИСТЕМ",
                        "БОРИСОГЛЕБСЬК-2", "P-934БМВ", "Р-934", "СТВОРЕННЯ ПЕРЕШКОД", "EW", "TOOTH RIDGE",
                        "NAVIGATION JAMMER"]):
            # "СТАНЦІЯ ПОДАВЛЕННЯ НАВІГАЦІЇ","30061000001505040000"
            return "30061000001505040000"
        
        if any(keyword in name for keyword in ["ПЕЛЕНГ АЗАРТУ", "АНТЕНА", "ПЕЛЕНГ P-440", "ПЕЛЕНГ R-419", "АНТЕНИ",
                        "ПЕЛЕНГ ДМХ ЗВ'ЯЗКУ", "Р-440", "BROADCAST ANTENNA"]):
            # "ПЕЛЕНГ АЗАРТУ","30061500002001000000"
            return "30061500002001000000"
        
        if any(keyword in name for keyword in ["Р-444", "R-444", "P-187", "Р-187", "R-187", "R-168", "Р-168", "P-168", "Р-392", "DMR",
                        "ПЕЛЕНГ УКХ ЗВ'ЯЗКУ", "P-392", "АМ ЗВ'ЯЗКУ"]):
            # "ПЕЛЕНГ УКХ ЗВ'ЯЗКУ","30061000001110010000"
            return "30061000001110010000"
        
        if any(keyword in name for keyword in ["СТАНЦІЯ СУПУТНИКОВОГО ЗВ`ЯЗКУ", "ПЕЛЕНГ VSAT", "ПЕЛЕНГАЦІЯ РАДІОСТАНЦІЇ    VSAT",
                        "ПЕЛЕНГ РАДІОСТАНЦІЇ VSAT", "ПЕЛЕНГ ТЕРМІНАЛУ СУПУТНИКОВОГО ЗВ'ЯЗКУ", "Р-438", "ПЕЛЕНГ R-438",
                        "P-438", "VSAT", "Р-441", "Р-423", "GROUND SATELLITES"]):
            # "ПЕЛЕНГ VSAT","30061000001110040000"
            return "30061000001110040000"
        
        if any(keyword in name for keyword in ["Р-419", "Р-415", "Р-409", "РЕЛЕ ЗВ’ЯЗКУ"]):
            # "Р-409","30061000001110020000"
            return "30061000001110020000"
        
        if ("ШТАБ" in name):
            # "ШТАБ", "30061002001100000000"
            return "30061002001100000000"
        
        if any(keyword in name for keyword in ["ПАНЦИР-С1", "ЗРГК ПАНЦИРЬ", "ПАНЦИРЬ-С1", "ЗГРК 96К6", "ПАНЦИР-S1", "ПАНЦИР-C1",
                        "ПАНЦИРЬ-С", "96К6", "ПАНЦИРЬ-С2", "ЗРГК ПАНЦИР", "ПАНЦИР С1", "ПАНЦИР С2", "ПАНЦИР-С2", "SA-22"]):
            # "ПАНЦИР-С1","30061500321111040000"
            return "30061500321111040000"
        
        if any(keyword in name for keyword in ["РЛС 9С18М1 КУПОЛ", "9С36", "9С32", "АРК-1", "9С18", "9С15"]):
            # "РЛС 9С18М1 КУПОЛ","30061500332203000000"
            return "30061500332203000000"
        
        if any(keyword in name for keyword in ["96L6E", "1Л125", "1L125", "НЕБО-СВУ", "НЕБО СВУ", "РЛС П-12", "TIN SHIELD", "NEBO-SVU"]):
            # "96L6E","30061500352203000000"
            return "30061500352203000000"
        
        if any(keyword in name for keyword in ["ЗРК БУК", "БУК-М3", "БУК-М1", "9К317М", "БУК М2", "БУК-М2", "БУК М1", "9К37", "БУК М3",
                        "БУК", "9А317", "BUK M2", "BUK M3", "SA-11", "SA-17", "SA-27"]):
            # "9К317М","30061500331111040000"
            return "30061500331111040000"
        
        if ("СПОСТЕРЕЖНИЙ ПУНКТ (СП)" in name):
            # "СПОСТЕРЕЖНИЙ ПУНКТ (СП)","30062500001601000000"
            return "30062500001601000000"
        
        if any(keyword in name for keyword in ["ПЕЛЕНГ С2", "С2", "C2", "КОМАНДНО-СПОСТЕРЕЖНИЙ ПУНКТ", "КСП", "COMMAND AND CONTROL"]):
            # "КОМАНДНО-СПОСТЕРЕЖНИЙ ПУНКТ","30061000001100000000"
            return "30061000001100000000"
        
        if any(keyword in name for keyword in ["ПУ / КШМ", "ПУНКТ УПРАВЛІННЯ", "КОМАНДНИЙ ПУНКТ", "ПУ/КШМ",
                "ПІДРОЗДІЛ УПРАВЛІННЯ", "РОСІЙСЬКИЙ ПУ", " ПУ ", " КП "]):
            # "РОСІЙСЬКИЙ ПУ","30061000001100000000"
            commandUnit = "30061000001100000000"

            if any(keyword in name for keyword in ["ПВК ВАГНЕРА", "ПВК ВАГНЕР"]):
                # "ПВК ВАГНЕРА","30061000001211008400"
                commandUnit = "30061000001211008400"
            
            return commandUnit
        
        if ("КШМ" in name):
            # "КШМ","30061500001201020000"
            return "30061500001201020000"
        
        if any(keyword in name for keyword in ["РЕМ.БАЗА", "РЕМБАЗА", "РЕМОНТНА БАЗА", "БАЗА РЕМОНТУ"]):
            # "РЕМ.БАЗА","30062000001213060000"
            return "30062000001213060000"
        
        if any(keyword in name for keyword in ["РЛС ТЕРЕК", "КАСТА", "91Н6", "92Н6Е", "96Л6Е", "96Л6-ЦП", "48Я6-К1", "96L6-TSP",
                        "96L6-ЦП", "55Ж6М", "NEBO-M", "91N6", "НІОБІЙ-СВ", "96Л6", "76Н6", "SPOON REST", "CHEESE BOARD"]):
            # "96L6-ЦП","30061500322203000000"
            return "30061500322203000000"
        
        if any(keyword in name for keyword in ["ТЗМ БУК-М1", "ТЗМ 9Т234 РСЗВ 9К58"]):
            # "ТЗМ БУК-М1","30061500331111040000"
            return "30061500331111040000"
        
        if ("ПУСКО-ЗАРЯДНА УСТАНОВКА" in name):
            if ("БУК" in name):
                return "30061500331111050000"
            
            return None
        
        if any(keyword in name for keyword in ["С-300ВМ", "С-300В М", "С-300В", "SA-23"]):
            # "С-300В М","30061500331111070000"
            return "30061500331111070000"
        
        if any(keyword in name for keyword in ["С-300ПМ", "С-300", "С-400", "C-300ПС", "C-400", "SA-21"]):
            # "C-300ПС","30061500321111070000"
            return "30061500321111070000"
        
        if any(keyword in name for keyword in ["ТОР-М2", "ЗРК ТОР", "ТОР-M2", "ТОР -M2", "9К330", "ТОР-М", "ТОР М2", "TOP М1",
                        "ТОР М1", "SAM TOR M2", "SAM TOR M1/M2", "SA-15"]):
            # "TOP М1","30061500331111050000"
            return "30061500331111050000"
        
        if any(keyword in name for keyword in ["ЗРК 9К33 ОСА", "ЗРК ОСА", "9K33 OSA", "9K33 ОСА", "ППО ОСА", "ОСА", "SA-8"]):
            # "ЗРК ОСА","30061500321111050000"
            return "30061500321111050000"
        
        if any(keyword in name for keyword in ["СТРІЛА 10", "СТРІЛА-10", "СТРЕЛА-10", "СТРІЛА-2М", "9К32", "СТРІЛА-3", "9К34"]):
            # "СТРЕЛА-10","30061500331111010000"
            return "30061500331111010000"
        
        if any(keyword in name for keyword in ["ТУНГУСКА", "2С6", "SA-19"]):
            # "ТУНГУСКА","30061500331111010000"
            return "30061500331111010000"
        
        if any(keyword in name for keyword in ["ЗСУ-23-4", "ШИЛКА"]):
            # "ЗСУ-23-4","30061500331105010000"
            return "30061500331105010000"
        
        if any(keyword in name for keyword in ["1L122 1E", "РЛС", "АІСТЕНОК", "АІСТЬОНОК", "РЕР", "1Л122-1E", "1L1221E", "1L122-1E",
                        "AISTENOK", "1Л122-1Е"]):
            # "AISTENOK","30061500002203000000"
            return "30061500002203000000"
        
        if any(keyword in name for keyword in ["ППО", "ЗРК"]):
            # "ППО","30061500001111000000"
            return "30061500001111000000"
        
        if any(keyword in name for keyword in ["ЗООПАРК", "ZOOPARK"]):
            return "30061500332203000000"
        
        if ("СУ-34" in name):
            # "СУ-34","30060100001101050000"
            return "30060100001101050000"
        
        if any(keyword in name for keyword in ["СУ-30", "СУ-35С"]):
            # "СУ-30","30060100001101040000"
            return "30060100001101040000"
        
        if ("СУ-25" in name):
            # "СУ-25","30060100001101020000"
            return "30060100001101020000"
        
        if any(keyword in name for keyword in ["МІ-24", "КА-52", "МІ-28", "ML-24", "KA-52"]):
            # "МІ-28","30060100001102000100"
            return "30060100001102000100"
        
        if any(keyword in name for keyword in ["МІ-8", "ML-8"]):
            # "МІ-8","30060100001102000300"
            return "30060100001102000300"
        
        if any(keyword in name for keyword in ["ТОС-1А", "ТОС-1", "ТОС СОНЦЕПЬОК"]):
            # "ТОС СОНЦЕПЬОК","30061500331116030000"
            return "30061500331116030000"
        
        if any(keyword in name for keyword in ["БМ-30"]):
            # "БМ-30","30061500321116030000"
            return "30061500321116030000"
        
        if any(keyword in name for keyword in ["БМ-27", "РСЗВ 9К57"]):
            # "РСЗВ 9К57","30061500321116030000"
            return "30061500321116030000"
        
        if any(keyword in name for keyword in ["ГРАД", "9К51М", "ТОРНАДО-Г", "БМ-21"]):
            # "ТОРНАДО-Г","30061500321116020000"
            return "30061500321116020000"
        
        if ("РСЗВ" in name):
            # "РСЗВ","30061500321116000000"
            return "30061500321116000000"
        
        if any(keyword in name for keyword in ["РОСІЙСЬКИЙ ПІДРОЗДІЛ ПВК", "ПВК ВАГНЕРА", "ПВК ВАГНЕР", "ПВК"]):
            "РОСІЙСЬКИЙ ПІДРОЗДІЛ ПВК","30061000001211008400"
            return "30061000001211008400"
        
        if ("2С7" in name):
            # "2С7","30061500331109030000"
            return "30061500331109030000"
        
        if any(keyword in name for keyword in ["ГІАЦИНТ-С", "2С5"]):
            # "2С5","30061500331107030000"
            return "30061500331107030000"
        
        if any(keyword in name for keyword in ["МСТА-С", "2С3", "2С19"]):
            # "2С19","30061500331109020000"
            return "30061500331109020000"
        
        if any(keyword in name for keyword in ["2С1", "2С9", "ГВОЗДИКА"]):
            # "ГВОЗДИКА","30061500331109010000"
            return "30061500331109010000"
        
        if ("САУ" in name):
            # "САУ","30061500331109000000"
            return "30061500331109000000"
        
        if any(keyword in name for keyword in ["ГІАЦИНТ-Б", "2А36"]):
            # "2А36","30061500351107030000"
            return "30061500351107030000"
        
        if any(keyword in name for keyword in ["Д-20", "МСТА-Б", "2А65"]):
            # "Д-20","30061500351109020000"
            return "30061500351109020000"
        
        if any(keyword in name for keyword in ["Д-30", "Д-44", "Д- 30"]):
            # "Д-44","30061500351109010000"
            return "30061500351109010000"

        
        if any(keyword in name for keyword in ["МТ-12", "РАПІРА"]):
            # "РАПІРА","30061500351106010000"
            return "30061500351106010000"
        
        if any(keyword in name for keyword in ["ТЮЛЬПАН", "2С4"]):
            # "ТЮЛЬПАН","30061500331114030000"
            return "30061500331114030000"
        
        if any(keyword in name for keyword in ["ВОГНЕВА ПОЗИЦІЯ", "ВП АРТИЛЕРІЇ", "ВП З РСЗО", "АРТИЛЕРІЯ НА ВОГНЕВИХ ПОЗИЦІЯХ",
                        "АРТ. ПОЗИЦІЯ", "ВОГНЕВІ ПОЗИЦІЇ"]):
            # "ВОГНЕВА ПОЗИЦІЯ","30062500002501000000"
            return "30062500002501000000"
        
        if any(keyword in name for keyword in ["ГАРМАТИ", "ПОЛЬОВА АРТИЛЕРІЯ", "ГАРМАТА", "ГАРМАТ", "ОРУДИЕ"]):
            # "ГАРМАТИ","30061500351107000000"
            return "30061500351107000000"
    
        if any(keyword in name for keyword in ["ГАБИЦІ", "БУКСИРУВАНА АРТИЛЕРІЯ", "ГАУБИЦЯ", "ДАЛЕКОБІЙНА АРТИЛЕРІЯ", "ГАУБИЦІ",
                        "СТВОЛЬНА АРТИЛЕРІЯ", "АРТИЛЕРІЯ", "АРТИЛЕРІЙСЬКІ УСТАНОВКИ", "ARTILLERY", "ГАУБИЦА"]):
            # "ДАЛЕКОБІЙНА АРТИЛЕРІЯ","30061500351109000000"
            return "30061500351109000000"
        
        if any(keyword in name for keyword in ["Т-72", "Т-80", "Т-64","Т-62", "Т-90"]):
            # "Т-80","30061500001202020000"
            return "30061500001202020000"
        
        if ("ПТРК" in name):
            # "ПТРК","30061500001112000000"
            return "30061500001112000000"
        
        if ("ПУСКОВА УСТАНОВКА ПРОТИТАНКОВОЇ РАКЕТИ" in name):
            # "ПУСКОВА УСТАНОВКА ПРОТИТАНКОВОЇ РАКЕТИ","30061500001117000000"
            return "30061500001117000000"
        
        if any(keyword in name for keyword in ["ОБТ", "ТАНК"]):
            # "ТАНК","30061500001202000000"
            return "30061500001202000000"
        
        if any(keyword in name for keyword in ["ББМ", "МТЛБ", "БМП", "МТ-ЛБ", "БМД", "БОЙОВА БРОНЬОВАНА МАШИНА",
                        "БРОНЬОВАНІ МАШИНИ"]):
            # "БРОНЬОВАНІ МАШИНИ","30061500001201010000"
            return "30061500001201010000"
        
        if any(keyword in name for keyword in ["БТР", "БРОНЕТРАНСПОРТЕР"]):
            # "БРОНЕТРАНСПОРТЕР","30061500001201030000"
            return "30061500001201030000"
        
        if ("МІНОМЕТ 120 ММ" in name):
            # "МІНОМЕТ 120 ММ","30061500001114030000"
            return "30061500001114030000"
        
        if ("СЕРЕДНІЙ МІНОМЕТ" in name):
            # "СЕРЕДНІЙ МІНОМЕТ","30061500001114020000"
            return "30061500001114020000"
        
        if any(keyword in name for keyword in ["МІНОМЕТ", "MORTAR"]):
            # "МІНОМЕТ","30061500001114000000"
            return "30061500001114000000"
        
        if any(keyword in name for keyword in ["БРЕМ-1"]):
            # "БРЕМ-1","30061500001203020000"
            return "30061500001203020000"
        
        if any(keyword in name for keyword in ["ЗЕМЛЕРИЙНА МАШИНА", "ЗЕМЛЕРИЙНІ МАШИНИ", "ЕКСКАВАТОР"]):
            # "ЗЕМЛЕРИЙНІ МАШИНИ","30061500001308000000"
            return "30061500001308000000"
        
        if ("БАТ-2" in name):
            # "БАТ-2","30061500001311000000"
            return "30061500001311000000"
        
        if any(keyword in name for keyword in ["ІНЖЕНЕРНА ТЕХНІКА", "ІНЖЕНЕРНОЇ ТЕХНІКИ", "ІНЖЕНЕРНА МАШИНА", "ІНЖЕНЕРНИХ МАШИН",
                        "ІНЖЕНЕРНІ МАШИНИ", "ІНЖ. ТЕХ", "ІНЖЕНЕРНА  МАШИНА"]):
            # "ІНЖЕНЕРНОЇ ТЕХНІКИ","30061500001300000000"
            return "30061500001300000000"
        
        if ("МТЗ" in name):
            # "МТЗ","30061000001617000000"
            return "30061000001617000000"
        
        if any(keyword in name for keyword in ["ПЕРЕПРАВА", "МІСТ", "ПЕРЕПРАВУ", "BRIDGE CONSTRUCTION"]):
            # "ПЕРЕПРАВА","30062000001107010000"
            return "30062000001107010000"
        
        if any(keyword in name for keyword in ["ПАЛИВОЗАПРАВНИК", "БЕНЗОВОЗІВ", "ТРАНСПОРТ ПММ", "ТОПЛИВОЗАПРАВНИКИ"]):
            # "ПАЛИВОЗАПРАВНИК","30061500321409000000"
            return "30061500321409000000"
        
        if any(keyword in name for keyword in ["ВАТ", "ВАНТАЖІВКА", "ВАНТАЖНИЙ АВТОМОБІЛЬ", "ЛОГІСТИЧНОЇ ТЕХНІКИ",
                        "ВАНТАЖНИЙ ВІЙСЬКОВИЙ АВТОМОБІЛЬ", "ВАНТАЖНІ ВІЙСЬКОВІ АВТОМОБІЛІ",
                        "ВАНТАЖНИХ ВІЙСЬКОВИХ АВТОМОБІЛІВ", "УРАЛ", "КАМАЗ З ТЕНТОМ",
                        "КАМАЗ", "ЛОГІСТИЧНИЙ ТРАНСПОРТ", "КАМАЗ", "ВАНТАЖНІ АТ", "ВАНТАЖНІ ВА", "ВАНТАЖНИХ ВА",
                        "ГАЗ-66", "ТРАНСПОРТНІ ЗАСОБИ ЛОГІСТИКИ", " ВА ", "MILITARY CARGO VEHICLES"]):
            # "ЛОГІСТИЧНИЙ ТРАНСПОРТ","30061500001408000000"
            return "30061500001408000000"
        
        if any(keyword in name for keyword in ["БРОНЕАВТОМОБІЛЬ", "ТІГР"]):
            # "БРОНЕАВТОМОБІЛЬ","30061500001201100000"
            return "30061500001201100000"
        
        if ("ПЛОЩАДКА ДЛЯ ПОСАДКИ ВЕРТОЛЬОТІВ" in name):
            # "ПЛОЩАДКА ДЛЯ ПОСАДКИ ВЕРТОЛЬОТІВ","30061500321111050000"
            return "30061500321111050000"
        
        if any(keyword in name for keyword in ["ГЕЛІКОПТЕР", "ВЕРТОЛІТ"]):
            # "ВЕРТОЛІТ","30060100001102000000"
            return "30060100001102000000"
        
        if any(keyword in name for keyword in ["ОВТ", "ОІВТ", "ВТ/ВА", " ВТ "]):
            "ОІВТ","30061500001200000000"
            return "30061500001200000000"
        
        if any(keyword in name for keyword in ["НАМЕТ", "НАКРИТТЯ"]):
            # "НАКРИТТЯ","30061500002013000000"
            return "30061500002013000000"
        
        if any(keyword in name for keyword in ["УСТ-56", "М-10", "ПА-10"]):
            # "ПА-10","30061500002013020000"
            return "30061500002013020000"
        
        if any(keyword in name for keyword in ["НСУ", "НСУ БПЛА", "НАЗЕМНА СТАНЦІЯ УПРАВЛІННЯ БПЛА", "БЕЗПІЛОТНІ ПОВІТРЯНІ СИСТЕМИ",
                        "GCS", "НАЗЕМНА СТАНЦІЯ КЕРУВАННЯ БПЛА", "UAV GCS"]):
            # "БЕЗПІЛОТНІ ПОВІТРЯНІ СИСТЕМИ","30061000111219000021"
            return "30061000111219000021"
        
        if any(keyword in name for keyword in ["РОСІЙСЬКІ БОЙОВИКИ", "ОС РОВ", "ПІХОТА", "INFANTRY"]):
            # "INFANTRY","30061000001211000000"
            return "30061000001211000000"
        
        if ("МОТОСТРІЛЕЦЬКИЙ ПІДРОЗДІЛ" in name):
            # "МОТОСТРІЛЕЦЬКИЙ ПІДРОЗДІЛ","30061000001211040000"
            return "30061000001211040000"
        
        if any(keyword in name for keyword in ["ВІЙСЬКОВИЙ ПІДРОЗДІЛ", "ВІЙСЬКОВИЙ ПІДРОЗДІЛ", "РОСІЙСЬКІ ПІДРОЗДІЛИ",
                        "НЕВИЗНАЧЕНИЙ ПІДРОЗДІЛ", "НЕВИЗНАЧЕНІ ПІДРОЗДІЛИ", "ТАКТИЧНИЙ ПІДРОЗДІЛ СВ ЗС РФ"]):
            # "НЕВИЗНАЧЕНИЙ ПІДРОЗДІЛ","30061000001200000000"
            return "30061000001200000000"
        
        if ("ІНЖЕНЕРНИЙ ПІДРОЗДІЛ" in name):
            # "ІНЖЕНЕРНИЙ ПІДРОЗДІЛ","30061000001407000000"
            return "30061000001407000000"
        
        if ("ВОДОВОЗ" in name):
            # "ВОДОВОЗ","30061500321410000000"
            return "30061500321410000000"
        
        if ("МТОР" in name):
            # "МТОР","30061000001611000000"
            return "30061000001611000000"
        
        if any(keyword in name for keyword in ["ПМП", "FLOATING BRIDGE"]):
            # "FLOATING BRIDGE","30061500001304000000"
            return "30061500001304000000"
        
        if any(keyword in name for keyword in ["МІКРОАВТОБУС", "УАЗ-452", "БУХАНКА"]):
            # "УАЗ-452","30061500001603000000"
            return "30061500001603000000"
        
        if any(keyword in name for keyword in ["ДЖИП", "УАЗ-469"]):
            # "УАЗ-469","30061500001605000000"
            return "30061500001605000000"
        
        if any(keyword in name for keyword in ["ПІКАП", "УАЗ-39094"]):
            # "УАЗ-39094","30061500001602000000"
            return "30061500001602000000"
        
        if any(keyword in name for keyword in ["БОЄПРИПАСИ", "СКЛАД БОЄПРИПАСІВ", "СКЛАД ОЗБРОЄННЯ ТА БОЄПРИПАСІВ", "СКЛАД БК",
                        "СКЛАДИ БОЄПРИПАСІВ", "AMMUNITION CACHE"]):
            # "СКЛАДИ БОЄПРИПАСІВ","30062000001103000000"
            return "30062000001103000000"
        
        if ("СУДНО ВМС" in name):
            # "СУДНО ВМС","30063000001200000000"
            return "30063000001200000000"
        
        if ("БПЛА" in name):
            # "БПЛА","30060100001103000000"
            return "30060100001103000000"
        
        if any(keyword in name for keyword in ["ІЛ-76", "АН-140", "АН-26", "АН-72"]):
            # "ІЛ-76","30060100001101070000"
            return "30060100001101070000"
        
        if any(keyword in name for keyword in ["ЛІКАРНЯ / ГОСПІТАЛЬ", "ШПИТАЛЬ", "СТАБІЛІЗАЦІЙНИЙ МЕДИЧНИЙ ПУНКТ", "MEDICAL FACILITY"]):
            # "ЛІКАРНЯ / ГОСПІТАЛЬ","30062000001207020000"
            return "30062000001207020000"
        
        if any(keyword in name for keyword in ["СКЛАД ПММ", "СЛУЖБА ПММ"]):
            # "СКЛАД ПММ","30062000001205050000"
            return "30062000001205050000"
        
        if any(keyword in name for keyword in ["БЛОК-ПОСТИ", "БЛОК-ПОСТ", "БЛОК ПОСТИ", "БЛОК ПОСТ", "БЛОКПОСТ"]):
            # "БЛОК ПОСТ","30062500001303000000"
            return "30062500001303000000"
        
        if any(keyword in name for keyword in ["ЛЕГКОВИЙ АВТОМОБІЛЬ", "ЛЕГКОВИЙ ВІЙСЬКОВИЙ АВТОМОБІЛЬ", "ЛЕГКОВІ ВІЙСЬКОВІ АВТОМОБІЛІ",
                        "ЛАТ", "ЛЕГКОВИХ ВІЙСЬКОВИХ АВТОМОБІЛІВ", "АВТОМОБІЛЬ"]):
            # "ЛЕГКОВИЙ ВІЙСЬКОВИЙ АВТОМОБІЛЬ","30061500001601000000"
            return "30061500001601000000"
        
        if any(keyword in name for keyword in ["ІФО", "ОКОПИ", "БЛІНДАЖ", "ФОРТ", "ТРАНШЕЇ", "КАПОНІР", "ТРАНШЕЯ", "ОКОП", "ФОМ"]):
            # "БЛІНДАЖ","30062500002812000000"
            return "30062500002812000000"
        
        if ("УКРИТТЯ" in name):
            # "УКРИТТЯ","30062500002809000000"
            return "30062500002809000000"
        
        if any(keyword in name for keyword in ["ТЕЛЕКОМУНІКАЦІЙНА ВЕЖА", "ТЕЛЕВЕЖА", "ВЕЖА МОБІЛЬНОГО ЗВ'ЯЗКУ", "ВЕЖА ТЕЛЕКОМУНІКАЦІЙ",
                        "ВЕЖА ЗВ'ЯЗКУ"]):
            # "ТЕЛЕКОМУНІКАЦІЙНА ВЕЖА","30062000001212030000"
            return "30062000001212030000"
        
        if any(keyword in name for keyword in ["ТОЧКА ПІДБОРУ МЕДИЧНОЇ ЕВАКУАЦІЇ", "ТОЧКА ЕВАКУАЦІЇ", "ГРУПА ЕВАКУАЦІЇ"]):
            # "ТОЧКА ПІДБОРУ МЕДИЧНОЇ ЕВАКУАЦІЇ","30062500003211000000"
            return "30062500003211000000"
        
        if ("МЕДИЧНА ЕВАКУАЦІЯ" in name):
            # "МЕДИЧНА ЕВАКУАЦІЯ","30061500001403000000"
            return "30061500001403000000"
        
        if ("УР-77" in name):
            # "УР-77","30061500001309020000"
            return "30061500001309020000"
        
        if ("НАЗЕМНА МІНА" in name):
            "НАЗЕМНА МІНА","30062500002806000000"
            return "30062500002806000000"
        
        if any(keyword in name for keyword in ["КАЗАРМИ", "МІСЦЕ ПРОЖИВАННЯ", "КАЗАРМА", "ПРОЖИВАННЯ ОС"]):
            # "МІСЦЕ ПРОЖИВАННЯ","30062000001208000000"
            return "30062000001208000000"
        
        if ("СКЛАД" in name):
            # "СКЛАД","30062000001120000000"
            return "30062000001120000000"
        
        if any(keyword in name for keyword in ["МІННЕ ПОЛЕ", "РАЙОН МІНУВАННЯ"]):
            # "МІННЕ ПОЛЕ","30062500002707010000"
            return "30062500002707010000"
        
        if any(keyword in name for keyword in ["НАФТОБАЗА", "PETROL STATION"]):
            # "НАФТОБАЗА","30062000001205040000"
            return "30062000001205040000"
        
        if ("ВОГНЕВЕ УРАЖЕННЯ" in name):
            # "ВОГНЕВЕ УРАЖЕННЯ","30064000001106000000"
            return "30064000001106000000"
        
        if any(keyword in name for keyword in ["МЕТИС-М", "9К115-2"]):
            # "МЕТИС-М","30061500001112030000"
            return "30061500001112030000"
        
        if any(keyword in name for keyword in ["АМ ЗВ’ЯЗКУ", "ПЕЛЕНГ НЕВСТАНОВЛЕНОГО ОБЛАДНАННЯ", "AR-2", "COMMS STATION"]):
            # "ПЕЛЕНГ НЕВСТАНОВЛЕНОГО ОБЛАДНАННЯ","30061000001110000000"
            return "30061000001110000000"
        
        if any(keyword in name for keyword in ["ЕЛЕКТРОПІДСТАНЦІЯ", "ЕЛЕКТРИЧНА ПІДСТАНЦІЯ"]):
            # "ЕЛЕКТРОПІДСТАНЦІЯ","30062000001205010000"
            return "30062000001205010000"
        
        if ("ІСКАНДЕР" in name):
            # "ІСКАНДЕР","30061500321113000000"
            return "30061500321113000000"
        
        if any(keyword in name for keyword in ["ВІДЕО (БОЙОВА КАМЕРА)", "ВІДЕОКАМЕРА"]):
            # "ВІДЕОКАМЕРА","30061000001112000000"
            return "30061000001112000000"
        
        if ("ГРАНАТОМЕТ" in name):
            # "ГРАНАТОМЕТ","30061500001103000000"
            return "30061500001103000000"
        
        if any(keyword in name for keyword in ["НАВЧАЛЬНИЙ ТАБІР", "НАВЧАЛЬНИЙ ПОЛІГОН РОВ"]):
            # "НАВЧАЛЬНИЙ ТАБІР","30062000001119020000"
            return "30062000001119020000"
        
        if ("КУЛЕМЕТ" in name):
            # "КУЛЕМЕТ","30061500001102000000"
            return "30061500001102000000"
        
        if any(keyword in name for keyword in ["ЗАЛІЗНИЧНА СТАНЦІЯ", "ЗАЛІЗНИЧНІ СТАНЦІЇ", "ЛОКОМОТИВНЕ ДЕПО"]):
            # "ЗАЛІЗНИЧНА СТАНЦІЯ","30062000001213070000"
            return "30062000001213070000"
        
        if ("МІСЦЕ ПЕРЕЗАРЯДЖЕННЯ" in name):
            # "МІСЦЕ ПЕРЕЗАРЯДЖЕННЯ","30062500003202000000"
            return "30062500003202000000"
        
        if ("ТМ-62" in name):
            # "ТМ-62","30061500002103000000"
            return "30061500002103000000"
        
        if any(keyword in name for keyword in ["ПУНКТ ЗАГАЛЬНОГО ПОСТАЧАННЯ", "TROOP SUSTAINMENT", "WEAPONS / EQUIPTMENT SHIPMENT"]):
            # "ПУНКТ ЗАГАЛЬНОГО ПОСТАЧАННЯ","30062500003217000000"
            return "30062500003217000000"
        
        if ("WATER SUPPLY INFRASTRUCTURE" in name):
            # "WATER SUPPLY INFRASTRUCTURE","30062000001214000000"
            return "30062000001214000000"
        
        if ("ENERGY FACILITY" in name):
            # "ENERGY FACILITY","30062000001205000000"
            return "30062000001205000000"
        

        return None
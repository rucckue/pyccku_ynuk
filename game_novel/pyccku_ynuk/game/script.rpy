﻿# СЦЕНАРИЙ ТУТ

# Определение персонажей игры.
define gg = Character('Слава', color="#c8ffc8")# метка для реплик главного героя
define kira = Character('Кира', color="#9966FF")# метка для реплик Киры
define kiril = Character('Кирилл', color="#999999")# метка для реплик Кирила
define nikita = Character('Никита', color="#0066CC")# метка для реплик Никиты
define vitya = Character('Витя', color="#fc3903")#метка для реплик Вити
define noname = Character('?', color="#999999")# метка для реплик ПЕРСОНАЖЕЙ КОГДА МЫ ИХ ЕЩЕ НЕ ЗНАЕМ (изменил с "?" на "noname", т.к. игра не воспринимает ? нормально и выдает ошибку {Димасек})
define t1 = Character('Учитель1', color="#FFFAFA")# метка для реплик учителя информатики
define t2 = Character('Учитель2', color="#FFFAFA")# метка для реплик учителя физики
define t3 = Character('Учтель3', color="#FFFAFA")# метка для реплик учителя программирования
define t4 = Character('Учитель4', color="#FFFAFA")# метка для реплик учителя английского
define t5 = Character('Скаляр Валерий Григорьевич', color="#FFFAFA")# метка для реплик учителя математики
define config.mouse = {"default" : [("gui/cursors/pointer.png", 0, 0)]}



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show blackcitybg #здесь я вижу какой-нибуть темный бг города из окна, или темный потолок комнаты гг

    "Это был обычный серый день"
    " Лежа в уже две недели как своей съемной квартире. Мне в голову, то и дело прилетали очень странные мысли."
    " А что если я не справлюсь?"
    " Что если {b}это место станет{\b} для меня адом?"
    " Все же оно одно из лучших в стране."
    " ... " # типо пауза
    " А как меня примут учителя?"
    " Будут ли надо мной глумится однокласники если я из глубинки?"
    " ... " # типо пауза
    " Я вроде обычный парень, не гений и не какой-нибуть двоечник"
    " Кошмар..."
    " Слава богу сон таки одолел меня и из своих мыслей, я перенесся в пучину своих собственных грез"

    return

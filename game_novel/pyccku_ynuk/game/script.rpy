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

#Музыка(СНАЧАЛА ИНИЦИАЛИЗИРОВАТЬ!!!!):
define audio.sadsymphony1 = "musics/sadsymphony1.mp3"
define audio.melancholic = "musics/melancholic.ogg"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    play music melancholic
    
    scene blackcitybg_darken #норм?
    with fade

    #show это для персонажа, my bad

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
# часть с Никитой (ЧАСТЬ)
    #"Вот и закончился мой первый учебный день."
    #"Неспеша выходить из класса, пока все толпились у двери, я погрузился в свои размышления."
    #"Пары в первый же день конечно меня удивили, но надо бы и законтачиться с кем-то, все же новые люди и новые возможности летают то тут, то там."
    #"Там на математике было парочку умников, по хорошему с кем-нибуть вроде него познакомится..."
    #"Выходя с этими мыслями из класса, я побрел примерно в сторону выхода, хотя и помнил, чем закончилась моя утреняя походка наугад."
    #"Примерно через две минуты ходьбы предо мной открылся вид на коридор, ведущий к выходу."
    #"Мдааа, чувствую себя как идущий к реке, пока шел в это прекрасное место, постиг бесконечное вечное, на триллионах и триллиардах планет."
    #"Выходя из универа, я заприметил одного парня, очень похожего на моего одногруппника."
    #"Этот студент, с виду выглядел доволно неплохо."
#возможно сюда добавить пикчу где он далеко стоит
    #"В черной футболке с белым принтом, обычных джинсах, в очках, еще с какими-то бумажками наперевес."
    #"Да, таких парней много, но мне показалось, что он как раз тот, который выходил к доске на матане."
    #"Чтож, раз я для себя решил с такими людьми водится, попробовать сделать это в своем стиле."
#начало непосредственно диалога
    # show nikita_basic
    # gg  "Бу, испугался?? Это я, твой одногруппник. Не бойся меня."
    # "хоть это был и заезжанный мем, но он всё ещё вполне юзабельный."
    # show nikita_scared
    # noname "Ёперный театр (эмоция: напуган, рука к сердцу), напугал"
    # gg "Это ты меня напгуал, когда с ходу ответил на все вопросы от препода по (предмет)-у."
    # show nikita_basic
    # noname "Да это фигня, а не вопросы были. Вот в моём ПТУ№17 вопросы были мама не горюй."
    # "так он ещё и старый"
    # gg "Так ты уже бывалый?"
    # noname "Ну можно и так выразиться."
    # "потерев нос, я посмотрел за его спину и уже хотел выдвинуться к выходу..."
    # noname "Гвоздь мне в кеды, уравнение забыл показать"
    # gg "ТАК ВСЁ УЖЕ, ДОМОЙ ПОРА"
    # noname "До дома, который мне не дом, идти 1200 шагов со средней скоростью 6 м/с."
    # gg "Ты считал ???(эмоция смеха)"
    # noname "Египетская сила! Это ведь база."
    # gg "А-а.. Это и вправду интересно..."
    # "Никогда бы не подумал, что такая информация – база"
    # noname "Куда путь держишь, странник?"
    # "что за вопрос такой?"
    # gg "( И кто тут странный...)"[тихо произнёс]
    # noname "АА! Чоооо? я немного глуховат.."
    # gg "«(Испугался, что он услышал.(не хватало ещё в первый день врагов наживать))"
    # gg "Мне в сторону дома"
    # noname "Ээ, хорошо. А как-то поконкретнее?"
    # "вспомнив, как я получал прописку в мою квартиру, в моей голове всплыл документ с моим адресом (Нужно сделать картинку документа, в котором будет адрес и что-то неофициальное отсылка)"
    # gg "(название улицы)"
    # noname "О, так до точки B нам по пути"
    # "ха, а мне тогда придется защищать ее что ли? А я как на зло дефы не купил..."
    # gg "Чее? какачя точка B, Ты террорист,а я за кт-шника?"
    # noname "У меня батя спецназовец, какой еще терорист???"
    # gg "Понял, то есть на вопрос что такое Теория Гаусса ты ответил, а на этот не можешь?"
    # noname "А ты не знаешь? Это же материал 1ого гойда..."
    # "чувствую, что началось время прекрасных историй.."
    # gg "Блин, ты ещё скажи, что в садике самолёты собирают."
    # noname "Ну я так то собрал макет Ил»76 в дошкольно1 группе."
    # "Он что сам Ильюшин, что ли // мб пояснить где нибуть что Ильюшин « Авиоконструктор «известный»"
    # gg "Прости, ещё раз, как тебя зовут?"
    # noname "Да я так, просто железный человек."
    # "Так, он гений,миллиардер, филиантроп или просто.. местный сумасшедший?.."
    # gg "У тебя всё хорошо?"
    # noname "А что-то не так?"
    # gg "Я только спросил как тебя зову.., А, точно, ты Никита, я вспомнил"
    # nikita "Японский магнитафон, ну вот, поздравляю) Ты решил задачку сам. Крюков с ПТУ бы оценил"
    # "Вот это я понимаю, человек « голова, даже в моей школе таких деревянных не припомню"
    # gg "Да, я очень старался и справился с этой сложной задачей."
    # "Тем временем, мы прошли уже половину пути до «точки B», минуя местный парк и бристоль. Сегодняшний солнечный день уже близился к концу, но саммо солнце и не собиралось садится. Решив все же продолжить диалог с Никитой я спросил у него:"


    return

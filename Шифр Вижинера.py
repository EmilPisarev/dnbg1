import  sys   # sys нужен для передачи argv в QApplication
из  PyQt5  импортировать  QtWidgets
импорт  дизайна   # конвертируем файл дизайна
от  itertools  импорта  цикла

класс  WindowApp ( QtWidgets . QMainWindow , design . Ui_MainWindow ):
    def  __init__ ( сам ):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        супер (). __init__ ()
        я . setWindowTitle ( "Шифр Виженера" )
        я . setupUi ( самостоятельно )

        я . pushButton . щелкнул . подключиться ( self . b1_clicked )
        я . pushButton_2 . щелкнул . подключиться ( self . b2_clicked )

    def  b1_clicked ( сам ):
        ключ  =  сам . textEdit_2 . toPlainText (). заменить ( '' , '' ). нижний ()
        текст  =  сам . textEdit_3 . toPlainText (). заменить ( '' , '' ). нижний ()
        я . textEdit_4 . setText ( encode_vijn ( текст , ключ ))

    def  b2_clicked ( сам ):
        ключ  =  сам . textEdit_2 . toPlainText (). заменить ( '' , '' ). нижний ()
        текст  =  сам . textEdit_4 . toPlainText (). заменить ( '' , '' ). нижний ()
        я . textEdit_3 . setText ( decode_vijn ( текст , ключ ))

def  main ():
    приложение  =  QtWidgets . QApplication ( sys . Argv )   # Новый экземпляр QApplication
    window  =  WindowApp ()   # Создаём объект класса WindowApp
    окно . show ()   # Показываем окно
    sys . exit ( app . exec_ ())   # Запускаем приложение

    text  =  'iwanttobelieve'
    ключ  =  'картофель'

    e  =  encode_vijn ( текст , ключ )
    печать ( е )
    print ( decode_vijn ( e , ключ ))

alp  =  'abcdefghijklmnopqrstuvwxyz'

def  encode_vijn ( текст , ключ ):
    f  =  лямбда-  аргумент : alp [( alp . index ( arg [ 0 ]) + alp . index ( arg [ 1 ]) % 26 ) % 26 ]]
    вернуться  '' . присоединиться ( карта ( f , zip ( текст , цикл ( ключ ))))


def  decode_vijn ( кодированный_текст , ключ ):
    f  =  лямбда-  аргумент : alp [ alp . index ( arg [ 0 ]) - alp . индекс ( аргумент [ 1 ]) % 26 ]
    вернуться  '' . присоединиться ( карта ( f , zip ( кодированный_текст , цикл ( ключ ))))

если  __name__  ==  '__main__' :
    main ()

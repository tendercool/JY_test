from PyQt5.QtCore import QSettings

class MyForm():
    def __init__(self):
        super().__init__()

        self.settings = QSettings('config.ini',QSettings.IniFormat)
        self.baud = self.settings.value('SETUP/BAUD_VALUE')
        self.databit = self.settings.value('SETUP/DATABIT_VALUE') 
        self.polarity = self.settings.value('SETUP/POLARITY_VALUE')
        self.stopbit = self.settings.value('SETUP/STOPBIT_VALUE')

        if self.polarity == 'Odd':
            self.polarity = '奇校验'
        elif self.polarity == 'Even':
            self.polarity = '偶校验'
        elif self.polarity == 'None':
            self.polarity = '无'
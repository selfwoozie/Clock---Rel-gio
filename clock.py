from datetime import datetime


class Clock:
    """
    Obtém informações de tempo do sistema
    """
    def get_now(self):
        """
        Hora atual do sistema
        :return: Hora do sistema em HH:MM:SS
        """
        return datetime.now().strftime("%H:%M:%S")

    def get_today(self):
        """
        Data atual do sistema
        :return: Data do sistema em DD/MM/AAA
        """
        return datetime.now().strftime("%d/%m/%Y")

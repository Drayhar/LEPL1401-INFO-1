class SMSStore:

    def __init__(self):
        self.__inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.__inbox.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.__inbox)

    def get_unread_indexes(self):
        ind = []
        for i in range(len(self.__inbox)):
            if not self.__inbox[i][0]:
                ind.append(i)
        return ind

    def get_message(self, i):
        # l'index sur ingenious commence à 1
        try:
            i = i-1
            tup = self.__inbox[i]
            self.__inbox[i] = (True, tup[1], tup[2], tup[3])
            return self.__inbox[i][1:]
        except:
            return None

    def delete(self, i):
        del self.__inbox[i-1]

    def clear(self):
        self.__inbox = []

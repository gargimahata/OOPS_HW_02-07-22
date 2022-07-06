import logging
logging.basicConfig(filename="List.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
class list_ops:
    #reverse a list
    def reverse(self, l):
        reverse = l[::-1]
        logging.debug(reverse)

    #try to access 234 & 456 out of this list
    def access(self, l):
        access_235 = l[7][0]
        access_456 = l[5][1]
        logging.debug(access_235)
        logging.debug(access_456)
    #extract only a list collection form list l
    def extract(self, l):
        extract1 = l[5]
        extract2 = l[8]['key1']
        logging.debug(extract1)
        logging.debug(extract2)

    #Try to list all the key in dict element avaible in list
    def dict_key(self, l):
        keys = l[8].keys()
        logging.debug(keys)
    #Try to extract all the value element form dict available in list
    def dict_values(self, l):
        values = l[8].values()
        logging.debug(values)
try:
    l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    if len(l) != 0 or type(l) == list:
        logging.info("It's a non empty list.")
except Exception as e:
    logging(e)
List = list_ops()
List.reverse(l)
List.access(l)
List.extract(l)
List.dict_key(l)
List.dict_values(l)
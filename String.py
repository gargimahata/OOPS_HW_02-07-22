import logging
logging.basicConfig(filename="String.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
class strng_ops:

    # string_indexing
    def string_indexing(self, string1):
        logging.info("We are inside function")
        rev = string1[::-1]
        new_string1 = string1[1:300:3]
        logging.info(new_string1)
        logging.info(rev)

    #uppercase_split
    def uppercase_split(self, string1):
        uppercase_split_string1= string1.upper().split()
        logging.info(uppercase_split_string1)

    #lower case
    def lower_case(self, string1):
        low = string1.lower()
        logging.info(low)

    #capitalize the whole string
    def capitalize(self, string1):
        caps = string1.capitalize()
        logging.info(caps)

    #Replace a string charecter by another charecter
    def replace(self, string1):
        replace = string1.replace("string", "class")
        logging.info(replace)
try:
    string1 = "this is My First Python programming class and i am learNING python string and its function"
    if len(string1) != 0 or type(string1) == str:
        logging.info("It is a string.")
except Exception as e:
        logging.debug(e)
example = strng_ops()
example.string_indexing(string1)
example.uppercase_split(string1)
example.lower_case(string1)
example.capitalize(string1)
example.replace(string1)


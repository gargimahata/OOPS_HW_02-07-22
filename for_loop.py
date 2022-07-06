import logging
logging.basicConfig(filename="for_loop.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
class for_loop:
    #Try to extract all the list entity
    def all_the_list(self,l):
        for i in l:
            if type(i) == list:
                logging.debug(i)
    #Try to extract all the dict entity
    def dicts(self,l):
        for i in l:
            if type(i) == dict:
                logging.debug(i)
    #Try to extract all the tuples entities
    def tuples(self,l):
        for i in l:
            if type(i) == tuple:
                logging.debug(i)
    #Try to extract all the numerical data it can be a part of dict key and values.
    def numericals(self,l):
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        logging.debug(j)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int or type(v) == int:
                        logging.debug(k)
                        logging.debug(v)
    #Try to give summation of all the numeric data
    def sum(self,l):
        l1 = []
        l2 = []
        l3 = []
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        l1.append(j)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int or type(v) == int:
                        l2.append(k)
                        l3.append(v)
        s1 = sum(l1)
        s2 = sum(l2)
        s3 = sum(l3)
        s = s1 + s2 + s3
        logging.debug(s)
    # Try to filter out all the odd values out all numeric data which is a part of a list
    def odds(self,l):
        l4 = []
        for i in l:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        if j % 2 == 0:
                            l4.append(j)
        logging.debug(l4)
    #Try to extract "ineruon" out of this data.
    def ineuron(self,l):
        for i in l:
            if type(i) == list:
                for j in i:
                    if str(j) == "ineuron":
                        logging.debug(j)
            if type(i) == dict:
                for k, v in i.items():
                    if str(k) == "ineuron":
                        logging.debug(k)
                    elif str(v) == "ineuron":
                        logging.debug(v)
    #Try to find out a number of occurances of all the data.
    def data(self,l):
        l1 = []
        l2 = []
        l3 = []
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    l1.append(j)
            if type(i) == dict:
                for k, v in i.items():
                    l2.append(k)
                    l3.append(v)
        l4 = l1 + l2 + l3
        for n in set(l4):
            k = l4.count(n)
            logging.debug("No of %s is %s", n,k)

    #Try to find out number of keys in dict element.
    def dict_elements(self,l):
        l1 = []
        for i in l:
            if type(i) == dict:
                for k, v in i.items():
                    l1.append(k)
        logging.debug("no of keys = %s", len(l1))
    #Try to filter out all the string data.
    def strings(self,l):
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == str:
                        logging.debug(j)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == str or type(v) == str:
                        logging.debug(k)
                        logging.debug(v)
    #Try to Find out alphanum in data.
    def alphanums(self,l):
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == str:
                        y= (j, ':', j.isalnum())
                        logging.debug(y)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == str or type(v) == str:
                        y = (k,':',k.isalnum())
                        z = (v,':',v.isalnum())
                        logging.debug(y)
                        logging.debug(z)
    #Try to find out multiplication of all numeric value in the individual collection inside dataset.
    def multiplication(self,l):
        l1 = []
        l2 = []
        l3 = []
        s1 = 1
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        l1.append(j)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int or type(v) == int:
                        l2.append(k)
                        l3.append(v)
        l4 = l1 + l2 + l3
        logging.debug(l4)
        for n in l4:
            s1 = s1 * n
        logging.debug(s1)
    # Try to unwrap all the values inside collection and create a flat List.
    def unwrap(self,l):
        l1 = []
        l2 = []
        l3 = []
        for i in l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    l1.append(j)
            if type(i) == dict:
                for k, v in i.items():
                    l2.append(k)
                    l3.append(v)
        l4 = l1 + l2 + l3
        logging.debug(l4)
try:
    l = [[1,2,3,4], (2,3,4,5,6),(3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {"k1":"sudh", "k2":"ineuron", "k3":"kumar", 3:6,7:8}, ["ineuron", "data science"]]
    logging.debug("It's the entry %s", l)
except Exception as e:
    logging.debug(e)
output = for_loop()
output.all_the_list(l)
output.dicts(l)
output.tuples(l)
output.numericals(l)
output.sum(l)
output.odds(l)
output.ineuron(l)
output.data(l)
output.dict_elements(l)
output.strings(l)
output.alphanums(l)
output.multiplication(l)
output.unwrap(l)
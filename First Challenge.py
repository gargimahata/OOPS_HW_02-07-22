import logging
logging.basicConfig(filename="First Challenge.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
class challange:
    # 1. Try to print all the number divisible by 3 in between a range of 40 - 400
    def by_three(self,i):
        try:
            while i <= 400:
                if i % 3 == 0:
                    logging.debug(i)
                i = i + 1
        except Exception as e:
            logging.debug(e)
    #2. Try to filter out all the vowels form below text by using while loop :  """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]Python consistently ranks as one of the most popular programming languagesc"""

    def vowles(self,s):
        try:
            i = 0
            while i < len(s):
                if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                    logging.debug("%s",s[i])
                i += 1
        except Exception as e:
            logging.debug(e)
    #3. Try to generate all the even number between 1- 1000

    def even(self,lim):
        try:
            i = 1
            while i <= lim:
                if i % 2 == 0:
                    logging.debug(i)
                i += 1
        except Exception as e:
            logging.debug(e)

    #4. Try to print a prime number in between 1 to 1000.
    def isprime(self,u):
        '''isprime'''
        try:
            for i in range(2, u):
                if i > 1:
                   for j in range(2, i):
                       if (i % j) == 0:
                           break
                   else:
                       logging.debug(i)
        except Exception as e:
            logging.debug(e)
    #5. Try to write a function which is a replica of list append, extend and pop function.
    def list_append(self, *a):
        try:
            l = [2, 3, 4]
            for i in a:
                l = l + [i]
            logging.debug(l)
        except Exception as e:
            logging.debug(e)


op = challange()
op.by_three(40)
op.vowles("""Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34] Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36] Python consistently ranks as one of the most popular programming languagesc""")
op.even(1000)
op.isprime(1000)
op.list_append(2,3,4,10)

import numpy
import numpy.linalg as linalg
def teht1():
    aKysymys = numpy.array([[2, 0, 0], [1, 3, 0], [5, 4, 1]])
    aVastaus = linalg.inv(aKysymys)
    print(aVastaus)

    bKysymys = numpy.array([[5, 1, 2], [1, 4, 2], [2, 2, 2]])
    bVastaus = linalg.inv(bKysymys)
    print(bVastaus)

def teht2():
    #tämän voisi (suhteellisen) helposti tehdä myös käsin kun on 2x2 matriiseja,
    #adj(a) = pää lävistäjä numerot vaihtavat paikkoja ja muut kaksi arvoa kerrotaan -1
    #jonka jälkeen se kerrotaan 1/det(a)
    aKysymys = numpy.array([[4, 5], [3, 7]])
    aVastaus = linalg.inv(aKysymys)
    print(aVastaus)

    bKysymys = numpy.array([[5, 10], [-8, 6]])
    bVastaus = linalg.inv(bKysymys)
    print(bVastaus)

def teht3_1():
    A = numpy.array([[2, 3, 2], [1, 2, -2], [4, 5, 3]])
    B = numpy.array([[1],[10],[4]])
    Ainv = linalg.inv(A)
    X = numpy.dot(Ainv, B)
    print(X)#x=2,y=1,z=-3

def teht3_2():
    A = numpy.array([[1, -4], [3, 2]])
    B = numpy.array([[4],[1]])
    Ainv = linalg.inv(A)
    X = numpy.dot(Ainv, B)
    print(X)#x=~0,857,y=~-0,786

    A = numpy.array([[1, 4, 2], [4, -3, 0], [2, 2, 2]])
    B = numpy.array([[10],[6],[14]])
    Ainv = linalg.inv(A)
    X = numpy.dot(Ainv, B)
    print(X)#x=0,y=-2,z=9

if __name__ == '__main__':
    #1. Tehtävä 1 kpl 5.5.1s 145
    teht1()

    #2. kpl 5.5.2, teht. 2 s 148
    teht2()

    #3. kpl 5.6.2, teht 2 s 152
    teht3_1()
    teht3_2()

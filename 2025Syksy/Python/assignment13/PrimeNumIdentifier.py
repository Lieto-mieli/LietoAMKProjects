from flask import Flask, request
prime_number = Flask(__name__)
@prime_number.route('/prime_number')
def prime_or_not():
    args = request.args
    num = int(args.get("num"))
    jaolliset = []
    onAlkuluku = True
    for i in range(2, num):
        if num % i == 0:
            onAlkuluku = False
            jaolliset.append(i)
    returndict = {"Number":num, "isPrime":onAlkuluku}
    return returndict

if __name__ == '__main__':
    prime_number.run(use_reloader=True, host='127.0.0.1', port=5000)

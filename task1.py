from flask import Flask, request

app = Flask(__name__)


@app.route('/alkuluku/<int:number>')
def alkuluku(number):
    Number = number

    return f"Number:{Number}, isPrime:{prime(Number)}"


def prime(Number):
    if Number < 2:
        return False
    for i in range(2, int(Number ** 0.5) + 1):
        if Number % i == 0:
            return False
    return True


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
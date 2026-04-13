from flask import Flask, render_template

app = Flask(__name__)

mamlakatlar = ["Xitoy", "Rossiya", "Germaniya", "Fransiya", "Braziliya", "Hindiston", "Misr"]

@app.route('/mamlakatlar')
def mamlakatlar_royxati():
    kop = [m for m in mamlakatlar if len(m) >= 7]
    kam = [m for m in mamlakatlar if len(m) < 7]

    return render_template(
        'mamlakatlar.html',
        kop=kop,
        kam=kam
    )

if __name__ == "__main__":
    app.run(debug=True)

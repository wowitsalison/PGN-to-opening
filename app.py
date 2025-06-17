from flask import Flask, render_template, request
import chess.pgn
import io

app = Flask(__name__)

# ECO opening dictionary (simplified- replace with opening book)
ECO_OPENINGS = {
	"C20": "King's Pawn Game",
    "C50": "Italian Game",
    "C60": "Ruy Lopez",
    "D10": "Queen's Gambit Declined",
    "E60": "King's Indian Defense",
    "B01": "Scandinavian Defense",
    "B20": "Sicilian Defense",
    "A00": "Uncommon Opening"
}

# Simplified function to detect ECO code based on moves
# Replace with opening book or extended mapping
from chess.polyglot import open_reader

def classify_opening(pgn_str):
    game = chess.pgn.read_game(io.StringIO(pgn_str))
    if not game:
        return None, None

    board = game.board()
    for move in game.mainline_moves():
        board.push(move)

    try:
        with open_reader("./eco.pgn") as reader:
            entry = reader.find(board)
            if entry:
                return entry.epd.split(';')[0], entry.name
    except Exception:
        pass

    # Fallback: look up based on first move
    moves = [move.uci() for move in board.move_stack[:6]]
    if moves[:2] == ['e2e4', 'e7e5']:
        return "C20", ECO_OPENINGS["C20"]
    elif moves[:2] == ['e2e4', 'c7c5']:
        return "B20", ECO_OPENINGS["B20"]

    return "A00", ECO_OPENINGS["A00"]


@app.route("/", methods=["GET", "POST"])
def home():
    opening_name = None
    eco_code = None
    pgn = ""
    if request.method == "POST":
        pgn = request.form.get("pgn")
        eco_code, opening_name = classify_opening(pgn)
    return render_template("base.html", pgn=pgn, eco_code=eco_code, opening_name=opening_name)

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
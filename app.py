from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def game_mode_selection():  # put application's code here
    game_mode = request.args.get('gameMode')

    if game_mode == 'SingleMode':
        return render_template('username_single.html')
    elif game_mode == 'TwoPlayersMode':
        return render_template('username_multi.html')

    return render_template('index.html')


@app.route('/game_mode_selection/username_single.html')
def username_input():
    player_1_name = request.args.get('player1Name')

    game_config = {
        'game_mode': 'SingleMode',
        'player_1_name': player_1_name,
        'player_2_name': 'bot',
    }

    return render_template('game/index.html', game_config=game_config)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
    # app.run()

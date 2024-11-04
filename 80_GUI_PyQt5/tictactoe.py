import PySimpleGUI as sg

class TicTacToe:
    def __init__(self):
        self.board = [[None for j in range(3)] for i in range(3)] #Leere 3x3 Liste
        self.current_player = 'X'
        self.winner = None
        self.window = None  # Instanzvariable, um auf das Fenster zuzugreifen

    def set_window(self, window):
        self.window = window

    def make_move(self, row, col):
        if not self.winner and not self.board[row][col]:
            self.board[row][col] = self.current_player
            self.window[(row, col)].update(self.current_player)  # Aktualisiere das aktuelle Feld
            self.check_winner()
            if not self.winner:  # Nur wechseln, wenn es keinen Gewinner gibt
                self.switch_player()

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                self.winner = self.current_player

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                self.winner = self.current_player

        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            self.winner = self.current_player

    def is_board_full(self):
        return all(all(cell for cell in row) for row in self.board)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.window['-PLAYER-'].update(f'Player: {self.current_player}')

    def reset_game(self):
        self.board = [[None for j in range(3) ] for i in range(3)] #Leere 3x3 Liste
        self.current_player = 'X'
        self.winner = None
        for i in range(3):
            for j in range(3):
                self.window[(i, j)].update('')  # Setze alle Felder zurück
        self.window['-PLAYER-'].update(f'Player: {self.current_player}')

def main():
    tictactoe = TicTacToe()

    layout = [
        [sg.Button('', size=(6, 3), key=(i, j), pad=(0, 0), font=('Helvetica', 20)) for j in range(3)] for i in range(3)
    ] + [
        [sg.Text(f'Player: {tictactoe.current_player}', key='-PLAYER-')],
        [sg.Button('Restart'), sg.Button('Quit')]
    ]
    print (layout[0][0])

    window = sg.Window('Tic Tac Toe', layout)
    tictactoe.set_window(window)  # Übergeben Sie das Fensterobjekt an die TicTacToe-Klasse

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Quit':
            break

        if event == 'Restart':
            tictactoe.reset_game()
            continue

        if isinstance(event, tuple):
            row, col = event
            tictactoe.make_move(row, col)

            if tictactoe.winner:
                sg.popup(f'Player {tictactoe.winner} wins!', auto_close=True, auto_close_duration=2)
                if sg.popup_yes_no('Play again?') == 'Yes':
                    tictactoe.reset_game()
                else:
                    break

            elif tictactoe.is_board_full():
                if sg.popup_yes_no('It\'s a draw! Play again?') == 'Yes':
                    tictactoe.reset_game()
                else:
                    break

    window.close()

if __name__ == '__main__':
    main()

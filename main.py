import time
class Song:

    def __init__(self, title, author, lenght):
        self.title = title
        self.author = author
        self.lenght = lenght


class Player:

    def __init__(self, song_list):
        self.song_list = song_list


    def start(self):
        self._show_menu()
        choice = self._get_choice()
        song = self.song_list[choice]
        if self.song_list[choice]:
            self._prep(song)


    def _show_menu(self):
        show_lines(40)
        print('Hello!!! This is the Music Player!!!\n'
              'and this is the Play List.')
        for i, Song in enumerate(self.song_list):
            print(f'{i + 1}. {Song.title.ljust(10)}  **  author: {Song.author.rjust(10)}   **  lenght: {Song.lenght}')


    def _get_choice(self):
        show_lines(40)
        choice = input('Which song do you want (number)?')
        try:
            choice = int(choice)
            if 0 > choice or len(self.song_list) < choice:
                raise ValueError
        except ValueError:
            print('Your choice should be a number from menu.')
            choice = self._get_choice()
        return choice-1

    def _prep(self, Song):
        print('Playing song...')
        time.sleep(0.5)
        print(f'Enjoy the song "{Song.title}",  by author "{Song.author}"')
        print('Thanks for your order!')

    def edit(self):
        editinig = input('Do yo want to edit the Playlist?(y/n)')
        if editinig == 'y':
            l = input('if you want: a) add some music - print "a",\n'
                  '              b) remove some music - print "b":')
            if l == 'a':
                self.adding()
            elif l == 'b':
                self.removing()
        else:
            pass

    def adding(self):
        adding = input('Do you wanna add new song? (y/n)')
        if adding == 'y':
            print('Add song as "Song name","Author","Lenght"')
            Song.title = input('Print name of your song:')
            Song.author = input('Print author:')
            Song.lenght = float(input('Print lenght:'))
            new_song = [f'{Song({Song.title}, {Song.author}, {Song.lenght})}']
            new_list = self.song_list + new_song
            print('You successfully add new song.\n Added song:')
            for number, songs in enumerate(new_song):
                print(f'{number + 1}.title: {Song.title.ljust(10)}  **  author: {Song.author.rjust(10)}   **  lenght: {Song.lenght}')
        else:
            pass


    def removing(self):
        removing = input('Do you wanna remove the song from menu? (y/n)')
        if removing == 'y':
            rmv_num = int(input('Print number of song which you want to remove:'))
            del song_list[rmv_num-1]
            print('You successfully remove that song!')
            for i, Song in enumerate(song_list):
                print(f'{i + 1}.{Song.title.ljust(10)}  **  author {Song.author.rjust(10)}   **  lenght {Song.lenght}')
        else:
            pass


def show_lines(n=20):
    print('-' * n)


song_list = [
    Song('Im bad', 'M. Jackson', 3.2),
    Song('Poker Face', 'Lady Gaga', 4.3),
    Song('Alena', 'Claydee', 3.7),
    Song('One Love', 'Dr. Alban', 4.2),
    Song('Love Story', 'Indila', 2.8),
]


Player = Player(song_list)
Player.start()
Player.edit()

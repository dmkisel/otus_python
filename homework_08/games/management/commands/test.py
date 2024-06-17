from _manual import (category,
                      age_group,
                      status_game,
                      games)



def main():
    for game in games:
        it = status_game[game["status"]]
        print(it)

if __name__ == '__main__':
    main()
from Character import Character

def main():
    player : Character = Character((15, 20), 100, 100)
    print(f"Player is at {player.position}")
    player.move((16, 20))
    player.take_damage(20)
    print(f"Player took 20 damage! Player has {player.current_health} HP.")
    player.take_damage(80)
    print(f"Player took 80 damage! Player was killed!")
    print(player.current_health) # player still exists because there is still a reference to it
    del player
    try:
        print(player)
    except:
        print("Player no longer exists")

if __name__ == "__main__":
    main()
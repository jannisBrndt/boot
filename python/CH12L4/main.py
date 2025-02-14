def get_player_record(player_id):
        if player_id == 1:
            return {"name": "Slayer", "level": 128}
        if player_id == 2:
            return {"name": "Dorgoth", "level": 300}
        if player_id == 3:
            return {"name": "Saruman", "level": 4000}
        raise ValueError(f"player id not found")
def main():
    try:
        get_player_record(4)
    except ValueError as e:
        print(e)

main()

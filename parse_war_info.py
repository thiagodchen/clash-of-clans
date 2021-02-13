import json

if __name__ == '__main__':
    with open("war_info.json", "r") as f:
        war_info = json.load(f)

    clan_members = war_info['clan']['members']
    opponent_members = war_info['opponent']['members']

    clan_members = sorted(clan_members, key=lambda c : c['mapPosition'])

    for clan_member in clan_members:
        name = clan_member['name']
        tag = clan_member['tag']
        mp = clan_member['mapPosition']

        print('%d -- %s %s' % (mp, name, tag))

        if 'attacks' not in clan_member:
            print('\t*NAO ATACOU!*\n')
            continue

        for attack in clan_member['attacks']:
            stars = attack['stars']
            order = attack['order']

            defender_tag = attack['defenderTag']

            defender_member = next(item for item in opponent_members if item['tag'] == defender_tag)
            defender_name = defender_member['name']
            defender_tag = defender_member['tag']
            defender_mp = defender_member['mapPosition']

            # print('\t%d -- %s %s - (%d*)' % (defender_mp, defender_name, defender_tag, stars))
            print('\t(%d*) --> %d' % (stars, defender_mp))

        print()

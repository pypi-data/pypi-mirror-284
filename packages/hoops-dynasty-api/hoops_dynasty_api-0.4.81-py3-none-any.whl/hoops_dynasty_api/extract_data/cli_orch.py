from datetime import datetime
import logging
from hoops_dynasty_api.classes import Player, Team
from hoops_dynasty_api.web import WebBrowser
import sys
import pandas as pd


def extract_team_data_v2(team_ids: list, save_files_flag: bool, save_path) -> list:
    """ handles pulling the team data off of the hoops dynasty website

    :param team_ids: list of team ids
    :param save_files_flag: flag to save files or not
    :param save_path: path to save the output file
    :return: a list of team objects that have team data in them
    """
    browser = WebBrowser()

    if sys.platform == 'darwin':
        logging.basicConfig(level=logging.DEBUG,
                            filename=f'/Users/zach/gitrepos/hoops-dynasty-data/logs/hd_logs_'
                                     f'{datetime.now().strftime("%m%d%Y")}.log')
    team_data = []
    team_excel_data = []
    for team_id in team_ids:
        team = Team(browser=browser, team_id=team_id)
        #if team.division == 'I':
        logging.info(f'team data: adding data for {team.team_name}')
        team_data.append(team)
        if save_files_flag:
            team_excel_data.append(team.team_details())
            teams_df = pd.DataFrame(team_excel_data)
            filename = f'{save_path}/team_{team_id}_{int(datetime.now().timestamp())}.xlsx'
            teams_df.to_excel(
                filename,
                index=False)
    return team_data



def extract_player_data_v2(player_ids: list, save_files_flag: bool, save_path) -> list:
    """ extracts player data from a list of player ids

    :param save_files_flag: flag if the files are to be saved to google bucket
    :param save_path: path to save the output file
    :return: list of player objects from hoops dynasty
    """
    browser = WebBrowser()
    player_data = []
    player_excel_data = []
    for player_id in player_ids:
        player = Player(browser=browser, player_id=player_id)
        logging.info(f'player data: adding data for {player.name} for team {player.team_name}, {player_id}')
        player_data.append(player)
        if save_files_flag:
            player_excel_data.append(player.player_details())
            player_df = pd.DataFrame(player.player_details())
            expanded_df = pd.concat([player_df.drop(columns=['game_log']), player_df['game_log'].apply(pd.Series)], axis=1)

            filename = f'{save_path}/player_{player_id}_{int(datetime.now().timestamp())}.xlsx'
            expanded_df.to_excel(
                filename,
                index=False)
    return player_data

# add a cli command to grab a teams playesr data

def extract_players_from_team_id_v2(team_ids: list, save_files_flag: bool, save_path):
    browser = WebBrowser()
    for team_id in team_ids:
        team = Team(browser=browser, team_id=team_id)
        team_players_data = []
        for player_id in team.player_ids:
            player = Player(browser=browser, player_id=player_id)
            team_players_data.append(player.player_details())
            
        if save_files_flag:
            filename = f'{save_path}/team_{team_id}_player_{player_id}_{int(datetime.now().timestamp())}.xlsx'
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                for player_data in team_players_data:
                    player_df = pd.DataFrame(player_data)
                    expanded_df = pd.concat([player_df.drop(columns=['game_log']), player_df['game_log'].apply(pd.Series)], axis=1)
                    print(f'writing {player_data["player_name"]}')
                    expanded_df.to_excel(
                        writer,
                        sheet_name=player_data['player_name'].replace(' ', ''),
                        index=False)

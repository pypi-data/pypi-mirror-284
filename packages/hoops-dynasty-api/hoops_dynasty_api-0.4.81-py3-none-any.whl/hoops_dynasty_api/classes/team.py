from selenium import webdriver
from hoops_dynasty_api.exceptions import WebBrowserCreationError


class Team:
    from .common_funcs import _sim_check

    def __init__(self, browser: webdriver, team_id: int):
        #self.build_web_browser(team_ratings_base_url + str(team_id))
        self.browser = browser
        self.team_ratings_base_url = 'https://www.whatifsports.com/hd/TeamProfile/Ratings.aspx?tid='
        self.team_roster_base_url = 'https://www.whatifsports.com/hd/TeamProfile/Roster.aspx?tid='
        self.team_history_base_url = 'https://www.whatifsports.com/hd/TeamProfile/History.aspx?tid='
        self.team_id = team_id  
        self.pull_data()

    def pull_data(self):
        url_to_open = self.team_ratings_base_url + str(self.team_id)
        soup = self.browser.open_and_soup(url_to_open)
        try:
            self.team_name = str(soup.find('a', {'class': 'teamlink'},).findAll(text=True)[0])
        except AttributeError:
            raise WebBrowserCreationError()
        print(f'getting info for team -> {self.team_name}')
        if self._sim_check(str(soup.find('div', {'class': 'rightHeaderInfoBar hideAtSmall'}))):
            self.coach = 'Sim AI'
        else:
            self.coach = str(soup.find('a', {'title': 'Open Coach Profile'}).findAll(text=True)[0])
        campus_location = str(soup.find(
            'span', {'id': 'ctl00_ctl00_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_span_team'}).findAll(
            text=True)[0]).split(' - ')[1].strip()
        self.campus_city = campus_location.split(',')[0].strip()
        self.campus_state = campus_location.split(',')[1].strip()
        self.division = str(soup.find(
            'span', {'id': 'ctl00_ctl00_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_span_team'}).findAll(
            text=True)[0]).split(' - ')[0].split(' ')[1]
        self.homecourt = soup.find(
            'span', {'id': 'ctl00_ctl00_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_span_homecourt'}).findAll(
            text=True)[0].split(' ')[1]
        self.prestige = str(soup.find('div', {'class': 'rightHeaderInfoBar hideAtSmall'}).find_all(
            'span', {'class': 'headerLabel'})[3].find('span', {'class': 'headerValue'}).findAll(
            text=True)[0])
        self.conference = str(soup.find('div', {'class': 'rightHeaderInfoBar hideAtSmall'}).find_all(
            'span', {'class': 'headerLabel'})[1].find('span', {'class': 'headerValue'}).findAll(
            text=True)[0])
        player_data = soup.find('div', {'class': 'teamratings_control'}).find_all(
            'a', {'title': 'Open Player Profile'})
        self.player_ids = []
        for player in player_data:
            url = str(player).split('pid=')[1].split('"')[0]
            if url not in self.player_ids:
                self.player_ids.append(url)
        # todo add in schollie # for each team
        url_to_open = self.team_roster_base_url + str(self.team_id)
        soup = self.browser.open_and_soup(url_to_open)
        roster_details = soup.find('table', {'id': 'tbl_Roster_Bkgrd'})
        self.freshmen = str(roster_details).count('Fr.')
        self.sophomores = str(roster_details).count('So.')
        self.juniors = str(roster_details).count('Jr.')
        self.seniors = str(roster_details).count('Sr.')
        self.fifth_seniors = str(roster_details).count('Sr/5')
        self.schoarlships_available = 12 - (self.freshmen + self.sophomores + self.juniors)
        self.walk_ons = 0
        self.redshirts = 0
        roster_table_details = roster_details.find_all('tr')
        for line in roster_table_details:
            try:
                status = line.find_all('td')[3].find('span').findAll(text=True)[0]
                if status == 'W':
                    self.walk_ons += 1
                if status == 'R':
                    self.redshirts += 1
            except IndexError:
                continue
        url_to_open = self.team_history_base_url + str(self.team_id)
        soup = self.browser.open_and_soup(url_to_open)
        self.season = str(soup.find('table', {'id': 'tbl_History'}).find_all(
                      'td', {'class': 'left'})[0].findAll(text=True)[0])
        #self.sql = self._build_sql()
        #self.browser.quit()

    def team_details(self) -> dict:
        return {'team_name': self.team_name, 'conference': self.conference, 'coach': self.coach,
                'prestige': self.prestige, 'open_ships': self.schoarlships_available,
                'seniors': self.seniors, 'juniors': self.juniors, 'sophomores': self.sophomores,
                'freshmen': self.freshmen, 'fifth_yr_seniors': self.fifth_seniors,
                'walk_ons': self.walk_ons, 'division': self.division,
                'campus_city': self.campus_city, 'campus_state': self.campus_city,
                'homecourt': self.homecourt, 'player_ids': self.player_ids,
                'season': self.season, 'id': self.team_id}


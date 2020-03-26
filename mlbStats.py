#import pip
import json
import requests

class retPlayerStat:
	def __init__(self, hostA, mplayer):
		self.mplayer = mplayer
		self.hostA = hostA
	def pullPlayId(self):
		def pullStats(self):
			reqPt = "sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='2019'&player_id='" + playerID + "'"
			myapi = requests.get(self.hostA + reqPt).json()
			statGet = myapi["sport_hitting_tm"]["queryResults"]["row"]
			for x in statGet:
				print(x)
		plyerG = "search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='" + self.mplayer + "%25'"
		myapi = requests.get(self.hostA + plyerG).json()
		plGet = myapi["search_player_all"]
		playerID = plGet["queryResults"]["row"]["player_id"]

		pullStats(self)
#for x in playerID["queryResults"]["row"]:  These to check rows returned
#	print(x)

#print(playerID)

#for x in playerID:
	#if "playerid" in x:
#		print(x)

hostA = "http://lookup-service-prod.mlb.com/json/named."

callIt = retPlayerStat(hostA, "Eaton")
callIt.pullPlayId()
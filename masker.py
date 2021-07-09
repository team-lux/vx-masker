# Name: Mask Message
# Description: Send a message inside a message - wat??
# Author: checksum (@0daySkid)
# Original founder: unknown

import requests
import sys
import colorama
from colorama import Fore as col
from colorama import Style as st
from colorama import init, Fore, Style, Back
init(convert=True)
s = st.BRIGHT
c = col.LIGHTYELLOW_EX

class Exploit:

    def __init__(self, token, channel, message, hidden_message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.hidden_message = hidden_message
        self.headers = {'Authorization': token}


    def _generate_message(self, m1, m2):
        """ generate masked message inside message using strange unicode/spoiler bug """
        return m1 + ('||\u200b||' * 200) + m2


    def execute(self):
        """ send masked message """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message, self.hidden_message)})

   ## Noob Friendly CLI Tweak by vx#1234 
def main():
    print(f"""{c}
    
                                                               
{col.LIGHTYELLOW_EX}@@@@@@@@@@    @@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
{col.LIGHTYELLOW_EX}@@@@@@@@@@@  @@@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  
{col.LIGHTYELLOW_EX}@@! @@! @@!  @@!  @@@  !@@       @@!  !@@  @@!       @@!  @@@  
{col.LIGHTYELLOW_EX}!@! !@! !@!  !@!  @!@  !@!       !@!  @!!  !@!       !@!  @!@  
{col.LIGHTYELLOW_EX}@!! !!@ @!@  @!@!@!@!  !!@@!!    @!@@!@!   @!!!:!    @!@!!@!   
{col.LIGHTYELLOW_EX}!@!   ! !@!  !!!@!!!!   !!@!!!   !!@!!!    !!!!!:    !!@!@!    
{col.LIGHTYELLOW_EX}!!:     !!:  !!:  !!!       !:!  !!: :!!   !!:       !!: :!!   
{col.LIGHTYELLOW_EX}:!:     :!:  :!:  !:!      !:!   :!:  !:!  :!:       :!:  !:!  
{col.LIGHTYELLOW_EX}:::     ::   ::   :::  :::: ::    ::  :::   :: ::::  ::   :::  
{col.LIGHTYELLOW_EX} :      :     :   : :  :: : :     :   :::  : :: ::    :   : :  
{col.LIGHTYELLOW_EX}  
{col.LIGHTYELLOW_EX}               Discord Message Masker by VX
{col.LIGHTYELLOW_EX}        use your browser to get the channel id for dms
{col.LIGHTYELLOW_EX}-------------------------------------------------------------


    """)
    
    token = input("Token: ")
    channel_id = input("Channel ID:")
    message = input("Message: ")
    hidden_message = input("Hidden Message: ")

    exploit = Exploit(token, channel_id, message, hidden_message)

    exploit.execute()
main()


if __name__ == '__main__':
    main()

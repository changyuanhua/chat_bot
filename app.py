import sys
from io import BytesIO

import telegram
import youtube_dl

from flask import Flask, request, send_file

from fsm import TocMachine

import urllib.request

from urllib.request import urlopen


API_TOKEN = '356618024:AAElDMxCEDCCodg27fr-ewUtoNFmmruPi3s'
WEBHOOK_URL = 'https://07567b0d.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1000',
        'state1',
        'state2',
        'state3',
        'state5',
        'state25',
        'state45',
        'state65',
        'state6',
        'state7',
        'state17',
        'state27',
        'state171',
        'state172',
        'state271',
        'state272',
        'state77',
        'state78',
        'state9',
        'state29',
        'state49',
        'state69',
        'state10',
        'state11',
        'state13',
        'state23',
        'state33',
        'state43',
        'state15',
        'state100'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1000',
            'conditions': 'is_going_to_state1000'
        },
        {
            'trigger': 'advance',
            'source': 'state1000',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1000',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state1000',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
#******food**********************************
# 1->food, 9->yes, 19->no, 102->back
# 5->breakfast, 25->lunch, 45->dinner, 65->lunch
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#*********************************************
#breakfast
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
#breakfast_back
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state1',
            'conditions': 'is_going_to_state102'
        },
#lunch
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
#lunch_back
        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state1',
            'conditions': 'is_going_to_state102'
        },
#dinner
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state45',
            'conditions': 'is_going_to_state45'
        },
#dinner_back
        {
            'trigger': 'advance',
            'source': 'state45',
            'dest': 'state1',
            'conditions': 'is_going_to_state102'
        },
#late-night supper
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state65',
            'conditions': 'is_going_to_state65'
        },
#late-night supper_back
        {
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state1',
            'conditions': 'is_going_to_state102'
        },
#*********************************************
#*********************************************
#breakfast_menu
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
#breakfast_not_menu
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state5',
            'conditions': 'is_going_to_state19'
        },
#breakfast_back
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state5',
            'conditions': 'is_going_to_state102'
        },
#breakfast_back_food
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#lunch_menu
        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state29',
            'conditions': 'is_going_to_state9'
        },
#lunch_not_menu
        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state25',
            'conditions': 'is_going_to_state19'
        },
#lunch_back
        {
            'trigger': 'advance',
            'source': 'state29',
            'dest': 'state25',
            'conditions': 'is_going_to_state102'
        },
#lunch_back_food
        {
            'trigger': 'advance',
            'source': 'state29',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#dinner_menu
        {
            'trigger': 'advance',
            'source': 'state45',
            'dest': 'state49',
            'conditions': 'is_going_to_state9'
        },
#dinner_not_menu
        {
            'trigger': 'advance',
            'source': 'state45',
            'dest': 'state45',
            'conditions': 'is_going_to_state19'
        },
#dinner_back
        {
            'trigger': 'advance',
            'source': 'state49',
            'dest': 'state45',
            'conditions': 'is_going_to_state102'
        },
#dinner_back_food
        {
            'trigger': 'advance',
            'source': 'state49',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#late-night supper_menu
        {
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state69',
            'conditions': 'is_going_to_state9'
        },
#late-night supper_not_menu
        {
            'trigger': 'advance',
            'source': 'state65',
            'dest': 'state65',
            'conditions': 'is_going_to_state19'
        },
#late-night supper_back
        {
            'trigger': 'advance',
            'source': 'state69',
            'dest': 'state65',
            'conditions': 'is_going_to_state102'
        },
#late-night supper_back_food
        {
            'trigger': 'advance',
            'source': 'state69',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#*********************************************
#*********************************************
#breakfast_information
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state13',
            'conditions': 'is_going_to_state9'
        },
#breakfast_back
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state9',
            'conditions': 'is_going_to_state102'
        },
#lunch_information
        {
            'trigger': 'advance',
            'source': 'state29',
            'dest': 'state23',
            'conditions': 'is_going_to_state9'
        },
#lunch_back
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state29',
            'conditions': 'is_going_to_state102'
        },
#dinner_information
        {
            'trigger': 'advance',
            'source': 'state49',
            'dest': 'state33',
            'conditions': 'is_going_to_state9'
        },
#dinner_back
        {
            'trigger': 'advance',
            'source': 'state33',
            'dest': 'state49',
            'conditions': 'is_going_to_state102'
        },
#late-night supper_information
        {
            'trigger': 'advance',
            'source': 'state69',
            'dest': 'state43',
            'conditions': 'is_going_to_state9'
        },
#late-night supper_back
        {
            'trigger': 'advance',
            'source': 'state43',
            'dest': 'state69',
            'conditions': 'is_going_to_state102'
        },
#*********************************************
#*********************************************
#breakfast_food
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#lunch_food
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#dinner_food
        {
            'trigger': 'advance',
            'source': 'state33',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#late-night supper_food
        {
            'trigger': 'advance',
            'source': 'state43',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
#*********************************************
#*********************************************
#breakfast_together
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
#lunch_together
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
#dinner_together
        {
            'trigger': 'advance',
            'source': 'state33',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
#late-night supper_together
        {
            'trigger': 'advance',
            'source': 'state43',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
#*********************************************
#breakfast,lunch,dinner,late-night supper back to finish
        {
            'trigger': 'go_back',
            'source': 'state100',
            'dest': 'user',
        },
#*********************************************
#*********************************************
#music
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
#*********************************************
#music_information_yes
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state6',
            'conditions': 'is_going_to_state9'
        },
#music_information_no
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'user',
            'conditions': 'is_going_to_state19'
        },
#*********************************************
#music_play_yes
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state10',
            'conditions': 'is_going_to_state9'
        },
#music_play_no
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state6',
            'conditions': 'is_going_to_state19'
        },
#*********************************************
#music_replay_yes
        {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state6',
            'conditions': 'is_going_to_state9'
        },
#music_replay_no
        {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
#*********************************************
#*********************************************
#chat
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
#*********************************************
#chat_hw
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
#*********************************************
#chat_hw_1
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state11',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state171',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state271',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_hw_2
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state15',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state172',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state272',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_other
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state17',
            'conditions': 'is_going_to_state17'
        },
#*********************************************
#chat_other_1
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state15',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state171',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state271',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_other_2
        {
            'trigger': 'advance',
            'source': 'state171',
            'dest': 'state15',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state171',
            'dest': 'state172',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state171',
            'dest': 'state272',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_freind
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state27',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_freind_1
        {
            'trigger': 'advance',
            'source': 'state27',
            'dest': 'state11',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state27',
            'dest': 'state171',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state27',
            'dest': 'state271',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#chat_freind_2
        {
            'trigger': 'advance',
            'source': 'state271',
            'dest': 'state15',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state271',
            'dest': 'state172',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state271',
            'dest': 'state272',
            'conditions': 'is_going_to_state27'
        },
#*********************************************
#*********************************************
#chat_last
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state77',
            'conditions': 'is_going_to_state78'
        },
        {
            'trigger': 'advance',
            'source': 'state172',
            'dest': 'state77',
            'conditions': 'is_going_to_state78'
        },
        {
            'trigger': 'advance',
            'source': 'state272',
            'dest': 'state77',
            'conditions': 'is_going_to_state78'
        },
#*********************************************
#*********************************************
#chat_last_last
        {
            'trigger': 'advance',
            'source': 'state77',
            'dest': 'state78',
            'conditions': 'is_going_to_state78'
        },
#*********************************************
#chat_last_last_last
        {
            'trigger': 'advance',
            'source': 'state78',
            'dest': 'state100',
            'conditions': 'is_going_to_state19'
        },
        {
            'trigger': 'advance',
            'source': 'state78',
            'dest': 'state3',
            'conditions': 'is_going_to_state9'
        },
#*********************************************
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
    machine.get_graph().draw('my_state_diagram.png', prog='dot')

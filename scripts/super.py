import csv
import os
from textwrap import TextWrapper

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

break_line = "\n----------\n"

def make_agency(title, agents, powers, head, acronym):
    return {
        'acronym': acronym,
        'agents': agents,
        'head' : head,
        'powers': powers,
        'title': title,
    }

def get_event_data(row):
    data = {}
    data['date'] = row[0]
    data['event'] = row[1]
    event_type = data['event'].lower()[0]
    if event_type == 'w':
        data['history'] = "{0} - Superintendent's Weekly Report Published".format(data['date'])
    elif event_type == 'm':
        data['history'] = "{0} - Superintendent's Monthly Report Published".format(data['date'])
    else:
        data['head'] = row[2]
        data['title'] = row[3]
        data['acronym'] = row[4]
        if event_type == 'e':
            data['agents'] = row[5]
            data['powers'] = row[6]
            data['history'] = "{0} - {1} establishes {2}".format(data['date'], data['head'], data['acronym'])
        elif event_type == 'r':
             data['history'] = "{0} - {1} revokes {2}".format(data['date'], data['head'], data['acronym'])
        elif event_type == 'c':
            data['agents'] = row[5]
            data['powers'] = row[6]
            data['history'] = "{0} - {1} changes {2}".format(data['date'], data['head'], data['acronym'])
        else:
            print("!!ERROR!! - Unknown event" + event_type)
            data['history'] = "SOMETHING WENT VERY WRONG"
    return data

a_by_acro = {}
event_log = []
def populate_data():
    with open(os.path.join(__location__, 'events.csv')) as csvfile:
         event_reader = csv.reader(csvfile, escapechar='\\')
         for row in event_reader:
            data = get_event_data(row)
            event_type = data['event'].lower()[0]

            if event_type == 'e':
                if data['acronym'] in a_by_acro:
                    print("Illegal Agency Creation: " + str(data))
                else:
                    a_by_acro[data['acronym']] = make_agency(data['title'],
                                                            data['agents'],
                                                            data['powers'],
                                                            data['head'],
                                                            data['acronym'])
            elif event_type == 'r':
                if data['acronym'] not in a_by_acro:
                    print("Illegal Agency Revocation " + str(data))
                else:
                    a_by_acro.pop(data['acronym'])

            elif event_type == 'c':
                if data['acronym'] not in a_by_acro:
                    print("Illegal Agency Change " + str(data))
                else:
                    for prop in ['title', 'powers', 'agents']:
                        if data[prop]:
                            a_by_acro[data['acronym']][prop] = data[prop]



            event_log.append(data['history'])


# Weekly Report Info
def short_list():
    print("Short List of agencies:\n")
    for key,value in sorted(a_by_acro.items()):
        print("{0} - Head: {1}".format(value['acronym'], value['head']))
    print

def long_list():
    # Monthly Report Info
    powers_wrapper = TextWrapper(initial_indent="",
                          subsequent_indent="  ")
    print("Long List of agencies:")
    for key,value in sorted(a_by_acro.items()):
        print("\n{0}  ({1})\nHead: {2}".format(value['title'],
                                                     value['acronym'],
                                                     value['head']))

        for line in str.splitlines("Agents:  " + value['agents']):
            print(powers_wrapper.fill(line))

        for line in str.splitlines("Powers:  " + value['powers']):
            print(powers_wrapper.fill(line))
        print("----")

    print

def event_history():
    print("A History of agency related events:\n")
    event_log.reverse()
    for log in event_log:
        print(log)

def section_break():
    print(break_line)

def generate_monthly_report():
    print("Superintendent's Monthly Report\n")
    populate_data()
    long_list()
    event_history()

def generate_weekly_report():
    print("Superintendent's Weekly Report\n")
    populate_data()
    short_list()
    #new_list()
    #changed_list()
    event_history()

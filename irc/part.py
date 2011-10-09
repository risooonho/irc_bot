# Copyright 2011 orabot Developers
#
# This file is part of orabot, which is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sqlite3

def parse_event(self, recv):
    conn = sqlite3.connect('../db/openra.sqlite')   # connect to database
    cur=conn.cursor()
    irc_part_nick = recv.split( "!" )[ 0 ].split( ":" ) [ 1 ]
    supy_host = recv.split()[0].split('!')[1]
    chan = recv.split()[2].strip()
    ###logs
    self.logs(irc_part_nick, chan, 'part', supy_host, '')
    ###
    ### for ]last  and logs
    sql = """SELECT channels FROM users
            WHERE user = '"""+irc_part_nick+"""'
    """
    cur.execute(sql)
    records = cur.fetchall()
    conn.commit()
    channel_from_db = ''
    if ( len(records) != 0 ):
        if not (( records[0][0] == '' ) or ( records[0][0] == None )):
            db_channels = records[0][0].split(',')
            if chan in db_channels:
                chan_index = db_channels.index(chan)
                del db_channels[chan_index]
                channel_from_db = ",".join(db_channels)
            else:
                channel_from_db = ",".join(db_channels)
    sql = """UPDATE users
            SET date = strftime('%Y-%m-%d-%H-%M-%S'), state = 0, channels = '"""+channel_from_db+"""'
            WHERE user = '"""+irc_part_nick+"'"+"""
    """
    cur.execute(sql)
    conn.commit()
    ### for ping me
    sql = """DELETE FROM pingme
            WHERE who = '"""+irc_part_nick+"""'
    """
    cur.execute(sql)
    conn.commit()
    ### for ]pick
    modes = ['1v1','2v2','3v3','4v4','5v5']
    diff_mode = ''
    for diff_mode in modes:
        sql = """DELETE FROM pickup_"""+diff_mode+"""
                WHERE name = '"""+irc_part_nick+"""'
        """
        cur.execute(sql)
        conn.commit()
    ### for notify
    sql = """DELETE FROM notify
            WHERE user = '"""+irc_part_nick+"""' AND timeout <> 'f' AND timeout <> 'forever'
    """
    cur.execute(sql)
    conn.commit()
    cur.close()
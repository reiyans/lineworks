# coding: utf-8

import logging
from logging.config import fileConfig

from lineworks import TalkBotApi


fileConfig(r".\logging.ini")
logger = logging.getLogger()


# LINE WORKS API情報
api_id = "jp1emQYyrXJfg"
server_api_consumer_key = "k8AvhKzfNx7BwVvstvU5"
server_id = "63b0d0b27ccc410db346bb30c9754c7b"
private_key = """\
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCKtR7F8gEGoPkB
zP1ub+C+qINLFcFIrAviQx/IcukM+oDXtRbBvaCCwVO8aQYv7emwnXm6JkziO7Vz
vJDanO5gXBlSv5tGjwB8E7aInvadwvdJOudcnBy7tia6nkf1RDsiElz8kwFMlM5t
C7/DoqymFGFvv2NHWtg2al4mnmxs+cb9nl4hL/VUMG95r9Ll75ORUz6mXZEVUGwX
/ZQH5w4EQ42pPD/I5MQG4RUCEJ/sl+Mo7oAVxYmU4Qsnh8HYZw4MwqiCKin9D0MW
qKQNmxVIl23FkdyTwc4WYiB7KB7VlrT3QnaTfwvC0DmpTYB7/PWCjphDjpiRT88C
doFnkTMNAgMBAAECggEAJUcJ7y7b4bkvUrGRxrVglDzblDlTicFbLELX7tobEfbc
25v6crUQxzNH2tHq7MSm0mVwCnwym3ZqjKE32NjmI5V85MVD6NGT0sTFgLAgHUQB
i3e+KCB4hGYuwGa7dgoRTlXbEbI8XiV72MiYj+5PMg82JH8uIkYi53TsurpG735I
Desin0cm7tMz3zMCpwtBtSIS1YZ5qyZwY+HsonoE42GMCPYBULoVOgOpV/Io8/ta
Lx+qkkGX80NWSif0OfffXwKTYpvvkJzgKNeRqvOWSiCU+wgMYoBLxaw21B8QjR6D
R/4ouq/yvYhl8RhsIZBf2gICXL9rImXNSHq5h1EHIQKBgQDBwzmGeevmS/Fnsqw7
zA2p35gwdAmBY9ALCKbOqae3p9aDd4Ykx9+t8/vXYV23EDTRLLIP0UuTlieswpen
nZwviLbTz5lFjV3XJvWtCfwRDBvxn9SZBYz+YicXdmbbNqWtznQs+9Rx6otjFm+P
MGg5KiB0KCoRrWCkH93CPPAlhQKBgQC3Qs6H8GD3GAdpESSOoGcRrHF3dn3f93/G
fjhBTMRlu6L1I/m3i/sDq+O5UuqQhE1aXHy3K0GbWBRRp5rorpMYNK/674jSsisf
x0voBXLmcbmTYSglasLA4QqVbwFaO/WK3Zx+3Uraw6+LkT+RqDBaWMf10UTQWfx0
9uqE2kXp6QKBgQDAZxAXRbgGngCf3R8D3dLvjRS9gGvz7N4oJrYk3vio+OOc9jHh
Egw92tmH/KonXtNjpkNGS6kFa4QIG86l5W6zEMmjODDVjNPTEl/ALPr9Ho4c934P
WSCxdVumA6+NHA2WsjxQctx5JdK1WRD8GbBUm01QqpVjqksdjnsRJpu8VQKBgHwB
5fWQ0FyD0wfixMUKf5QzBzjaYoT6Wmk7od92DfP1S2jsZh8wxrOOTfNqyzTtgdZi
fTYJPETdDirO6oEHGJwpkuePzRsd2xaO6qtffIe5buTuupbPLmgMH/hMfDLOHfJQ
0YP7RJrSDei4abarg8SvDOgnKpR+P9n592nctbB5AoGARzemFsOqyHjWOVhWwB9V
cLyTe9Zdkt94C9Ce0WFxhX9BLlrweuktmOPeCr/W4a1RStF42hBDbMd7WgRWigo4
cfJxCdDgkG8alFyAoqC8EdhuAgrsE4eiuXQBqN8MeTjQUWLzdDpwbNAZchO+j3cA
8GWf3fPblnbUiNAP8hE0MEY=
-----END PRIVATE KEY-----"""
domain_id = "10078518"


def main():
    talk_bot = TalkBotApi(api_id, server_api_consumer_key, server_id, private_key, domain_id, "668966")
    talk_bot.send_text_message("test", "rei@re1yan")


if __name__ == "__main__":
    main()

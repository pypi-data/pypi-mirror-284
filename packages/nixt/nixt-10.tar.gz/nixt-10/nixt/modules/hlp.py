# This file is placed in the Public Domain.


"help"


SEP = "/"
NAME = __file__.split(SEP)[-3]
TXT = f"""{NAME.upper()} - you have been {NAME}

    {NAME}  <cmd> [key=val] [key==val]
    {NAME}d

OPTIONS

    -h     show help
    -i     start services
    -v     use verbose

COMMANDS
    
    $ {NAME} cmd
    cfg,cmd,dpl,err,exp,imp,mod,mre,nme,pwd,rem,res,rss,thr

"""


def hlp(event):
    "show help"
    event.reply(TXT)

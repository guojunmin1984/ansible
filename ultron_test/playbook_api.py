#作者：郭俊民
import ansible
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils
from ansible.inventory import Inventory
import json
import os,sys





def pb():
    stats=callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats)
    inventory=Inventory('/export/servers/Ultron/ultron_test/ghosts')
    res = ansible.playbook.PlayBook(
        playbook="/etc/ansible/playbook/jengined_install.yml",
        stats=stats,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        check=False,
        inventory=inventory,
        extra_vars={"ansible_ssh_pass":"YM5fT%S7UDKwHxff"})
    return res.run()
# MCDReforged-Tpa 
# Copyright(C) DrLee_lihr 2020
# GNU General Public License v3.0



def on_load(server,old):
    server.add_help_message('!!tpa <playername>','向玩家名为§7<playername>§r的玩家发出一个传送请求')
    server.add_help_message('!!tpahere <playername>','向玩家名为§7<playername>§r的玩家发出传送到这里的请求')
    server.add_help_message('!!tpaccept <request id>','批准编号为§7<request id>§r的传送请求')


request_list=[["requester","berequester",0,0]]
def tpahere(server,info):
    requester=info.player
    berequester=info.content.lstrip('!!tpahere '+requester)
    request_list.append([requester,berequester,len(a),0])
    server.tell(berequester,requester+'请求你传送到他那里。')
    server.tell(berequester,'使用\"!!tpaccept '+len(a)+"\"来批准这个请求。")
    
def tpa(server,info):
    requester=info.player
    berequester=info.content.lstrip('!!tpa '+requester)
    request_list.append([requester,berequester,len(a),1])
    server.tell(berequester,requester+'请求传送到你这里。')
    server.tell(berequester,'使用\"!!tpaccept '+len(a)+"\"来批准这个请求。")
    
def tpaccept(server,info):
    request_id=int(info.content.lstrip('!!tpaccept '))
    if request_list[request_id][1]==info.player and request_list[request_id][3]==0:
        server.execute('tp '+request_list[request_id][2]+' '+request_list[request_id][1])
    if request_list[request_id][1]==info.player and request_list[request_id][3]==1:
        server.execute('tp '+request_list[request_id][1]+' '+request_list[request_id][2])
    
def on_user_info(server,info):
    if info.content.startswith("!!tpa"):
        tpa(server,info)
    if info.content.startswith("!!tpahere"):
        tpahere(server,info)
    if info.content.startswith("!!tpaccept"):
        tpaccept(server,info)

def on_mcdr_stop(server):
    request_list.clear()

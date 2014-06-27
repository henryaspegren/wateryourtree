import hypchat

def message_room(token, room, name, location):
  hc_account = hypchat.HypChat(token)
  hc_room = hc_account.get_room(room)
  hc_room.topic('Fertilizer Update!')
  hc_room.message(name+' has fertilized the '+str(location)+' (tree) (poo)', 'green', True, 'text')

templates = ["textadventure"]
def inittext():
  pass
def init():
  conf = open("game.conf")
  config = conf.read
  exec(config)
  try:
    foo = GFRAME
  except:
    raise SystemError("GFRAME is undefined, unknown game template.")
  if foo not in templates:
    raise SystemError("GFRAME is undefined, unknown game template.")
  if foo == "textadventure":
    inittext()

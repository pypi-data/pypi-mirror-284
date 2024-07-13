from .colors import colors

class p:
  def setColor(mtype, color): 
    if mtype == 'logs':
      colors["logs"] = color
    elif mtype == 'log' or mtype == 'success' or mtype == 'error' or mtype == 'warning': # no idea what this does, im just porting it
      raise TypeError(f'Unknown property "{mtype}". Cannot set property color as the default one.')
    else:
      colors[mtype] = color


  def success(message):
    mtype = 'success';
    color = colors[mtype];
    logType = mtype.upper();
    coloredLogType = f'{color}[{logType}]\x1b[0m'
    print(f'{coloredLogType}: {message}')

  def error(message):
    mtype = 'error';
    color = colors[mtype];
    logType = mtype.upper();
    coloredLogType = f'{color}[{logType}]\x1b[0m'
    print(f'{coloredLogType}: {message}')

  def warning(message):
    mtype = 'warning';
    color = colors[mtype];
    logType = mtype.upper();
    coloredLogType = f'{color}[{logType}]\x1b[0m'
    print(f'{coloredLogType}: {message}')

  def log(message):
    mtype = 'logs';
    color = colors[mtype];
    logType = mtype.upper();
    coloredLogType = f'{color}[{logType}]\x1b[0m'
    print(f'{coloredLogType}: {message}')

from .colors import colors

class p:
    @staticmethod
    def setColor(mtype, color): 
        if mtype == 'logs':
            colors["logs"] = color
        elif mtype == 'log' or mtype == 'success' or mtype == 'error' or mtype == 'warning':
            raise TypeError(f'Unknown property "{mtype}". Cannot set property color as the default one.')
        else:
            colors[mtype] = color

    @staticmethod
    def _format_message(mtype, message, options=None):
        color = colors[mtype]
        logType = mtype.upper()
        
        if options and options.get('filled', False):
            coloredLogType = f'{color}[{logType}]'
            coloredMessage = f'{color}{message}\x1b[0m'
            return f'{coloredLogType}: {coloredMessage}'
        else:
            coloredLogType = f'{color}[{logType}]\x1b[0m'
            return f'{coloredLogType}: {message}'

    @staticmethod
    def success(message, options=None):
        formatted_message = p._format_message('success', message, options)
        print(formatted_message)

    @staticmethod
    def error(message, options=None):
        formatted_message = p._format_message('error', message, options)
        print(formatted_message)

    @staticmethod
    def warning(message, options=None):
        formatted_message = p._format_message('warning', message, options)
        print(formatted_message)

    @staticmethod
    def log(message, options=None):
        formatted_message = p._format_message('logs', message, options)
        print(formatted_message)
import datetime as dt
import os
from app.settings import FILES_PATH
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    files = []
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    for f in os.listdir(path=FILES_PATH):
        t_details = os.stat(f'{FILES_PATH}/{f}')
        info = {'name': f, 'ctime': dt.datetime.fromtimestamp(t_details.st_ctime),
                'mtime': dt.datetime.fromtimestamp(t_details.st_mtime)}
        if date is not None:
            if info['ctime'].date() == dt.datetime.strptime(date, '%Y-%m-%d').date():
                files.append(info)
        else:
            files.append(info)
        print(dt.date.fromtimestamp(os.stat(f'{FILES_PATH}/{f}').st_ctime))
    if date is not None:
        context = {
            'files': files,
            'date': dt.datetime.strptime(date, '%Y-%m-%d').date()
        }
    else:
        context = {
            'files': files,
        }

    return render(request, template_name, context)


def file_content(request, name=None):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    if name in os.listdir(path=FILES_PATH):
        content = ''
        with open(f'{FILES_PATH}/{name}', newline='') as file:
            for row in file:
                content += row

        return render(
            request,
            'file_content.html',
            context={'file_name': str(name), 'file_content': content}
        )
    else:
        context = {'back': True}
        return render(request, 'index.html', context)

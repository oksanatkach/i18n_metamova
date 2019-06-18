from babel.messages.pofile import read_po, write_po
from babel._compat import StringIO
from babel.messages import Catalog
from app import babel
import os, json
import datetime

translations = next(babel.translation_directories)
# app_path = translations.replace('/app/translations', '')
app_path = translations.replace('\\app\\translations', '')


def export_strings(source='en', target=None):

    # source_str = StringIO(open(translations + '\\' + source + '\LC_MESSAGES\messages.po' , 'r', encoding='utf-8').read())
    source_str = StringIO(open(translations + '/' + source + '/LC_MESSAGES/messages.po' , 'r', encoding='utf-8').read())
    source_catalog = read_po(source_str)
    for_tron = { message.id: {source: message.string} for message in source_catalog if message.id }

    if not target:
        for locale in os.listdir((translations)):
            if locale not in ['pseudo', source] and not locale.startswith('.'):
                # target_str = StringIO(open(translations + '\\' + locale + '\LC_MESSAGES\messages.po', 'r', encoding='utf-8').read())
                target_str = StringIO(open(translations + '/' + locale + '/LC_MESSAGES/messages.po', 'r', encoding='utf-8').read())
                target_catalog = read_po(target_str)

                for message in target_catalog:
                    if message.id and message.id in for_tron.keys():
                        for_tron[message.id][locale] = message.string
    else:
        target_str = StringIO(
            # open(translations + '\\' + target + '\LC_MESSAGES\messages.po', 'r', encoding='utf-8').read())
            open(translations + '/' + target + '/LC_MESSAGES/messages.po', 'r', encoding='utf-8').read())
        target_catalog = read_po(target_str)

        for message in target_catalog:
            if message.id and message.id in for_tron.keys():
                for_tron[message.id][target] = message.string

    os.rename(app_path + '/json_strings/strings.json', app_path + '/json_strings/bak/' + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7] + '_strings.json')
    with open(app_path + '/json_strings/strings.json', 'w', encoding='utf-8') as outfile:
        json.dump(for_tron, outfile, ensure_ascii=False)


def import_strings(filename=None, source='en', target=None):
    if filename:
        from_tron = json.loads(open(filename, 'r', encoding='utf-8').read())
    else:
        from_tron = json.loads(open(app_path + '/json_strings/strings.json', 'r', encoding='utf-8').read())

    template_str = StringIO(open('messages.pot', 'r', encoding='utf-8').read())
    # template_str = StringIO(open(app_path + '/messages.pot', 'r', encoding='utf-8').read())
    # template_str = StringIO(open(app_path + '\messages.pot', 'r', encoding='utf-8').read())
    template = read_po(template_str)

    if not target:
        for locale in babel.list_translations():
            if locale not in ['pseudo', source]:
                new_catalog = Catalog()
                for id in from_tron:
                    if target in from_tron[id].keys():
                        new_catalog.add(id, from_tron[id][locale])
                new_catalog.update(template)
                # os.rename(translations + '\\' + locale + '\LC_MESSAGES\messages.po', translations + '\\' + locale + '\LC_MESSAGES\\bak\\' + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7] + '_messages.po')
                os.rename(translations + '/' + locale + '/LC_MESSAGES/messages.po', translations + '/' + locale + '/LC_MESSAGES/bak/' + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7] + '_messages.po')
                # write_po(open(translations + '\\' + locale + '\LC_MESSAGES\messages.po', 'wb'), new_catalog)
                write_po(open(translations + '/' + locale + '/LC_MESSAGES/messages.po', 'wb'), new_catalog)

    else:
        new_catalog = Catalog()
        for id in from_tron:
            if target in from_tron[id].keys():
                new_catalog.add(id, from_tron[id][target])
        new_catalog.update(template)
        # os.rename(translations + '\\' + target + '\LC_MESSAGES\messages.po', translations + '\\' + target + '\LC_MESSAGES\\bak\\' + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7] + '_messages.po')
        os.rename(translations + '/' + target + '/LC_MESSAGES/messages.po', translations + '/' + target + '/LC_MESSAGES/bak/' + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7] + '_messages.po')
        # write_po(open(translations + '\\' + target + '\LC_MESSAGES\messages.po', 'wb'), new_catalog)
        write_po(open(translations + '/' + target + '/LC_MESSAGES/messages.po', 'wb'), new_catalog)


# def parse_strings(source='en', target=None, format=None):
#     strings = json.loads(open(app_path + '/json_strings/strings.json', 'r', encoding='utf-8').read())
#
#     if not target:
#         for id in strings:


if __name__ == '__main__':
    # export_strings('en')
    import_strings(r'uk_strings.json', 'en', 'uk')
    # print(translations)

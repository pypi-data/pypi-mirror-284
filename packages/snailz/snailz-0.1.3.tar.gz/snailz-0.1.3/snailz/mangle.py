'''Mangle readings files.'''

import csv
from pathlib import Path
import random
import sqlite3


SELECT = '''
select
    plate.plate_id as plate_id,
    plate.filename as filename,
    plate.date as date,
    staff.staff_id as staff_id,
    staff.personal as personal,
    staff.family as family
from
    plate join performed join staff
on
    (plate.sample_id = performed.sample_id)
    and
    (performed.staff_id = staff.staff_id)
'''


def mangle(options):
    '''Main driver.'''
    con = sqlite3.connect(options.dbfile)
    con.row_factory = sqlite3.Row
    rows = list(dict(r) for r in con.execute(SELECT).fetchall())
    random.seed(len(rows))
    rows = consolidate(rows)
    for row in rows:
        mangle_file(options, row)


def consolidate(rows):
    '''Pick a single record at random for each physical plate.'''
    grouped = {}
    for r in rows:
        if r['plate_id'] not in grouped:
            grouped[r['plate_id']] = []
        grouped[r['plate_id']].append(r)

    result = []
    for group in grouped.values():
        result.append(random.choice(group))
    return result


def do_date(settings, sections):
    '''Mangle by adding date in header.'''
    row = [''] * len(sections['header'][0])
    row[0] = 'Date'
    row[1] = settings['date']
    sections['header'].append(row)
do_date.prob = 0.1


def do_footer(settings, sections):
    '''Mangle by adding a footer.'''
    blank = [''] * len(sections['header'][0])
    foot = [''] * len(sections['header'][0])
    foot[0] = settings['staff_id']
    sections['footer'] = [blank, foot]
do_footer.prob = 0.1


def do_indent(settings, sections):
    '''Mangle by indenting.'''
    for section in sections.values():
        for row in section:
            row.insert(0, '')
do_indent.prob = 0.1


def do_staff_name(settings, sections):
    '''Mangle by adding staff name.'''
    sections['header'][0][-2] = f'{settings["personal"]} {settings["family"]}'
do_staff_name.prob = 0.1


def mangle_file(options, settings):
    '''Mangle a single file.'''
    sections = read_sections(options, settings['filename'])
    for func in (do_staff_name, do_date, do_footer, do_indent,):
        if random.random() < func.prob:
            func(settings, sections)
    write_sections(options, settings['filename'], sections)


def read_sections(options, filename):
    '''Read tidy file and split into sections.'''
    with open(Path(options.tidy, filename), 'r') as raw:
        rows = [row for row in csv.reader(raw)]
    return {
        'header': rows[0:1],
        'headspace': rows[1:2],
        'body': rows[2:],
        'footer': []
    }


def write_sections(options, filename, sections):
    '''Write sections of mangled file.'''
    with open(Path(options.outdir, filename), 'w') as raw:
        writer = csv.writer(raw, lineterminator='\n')
        for section in sections.values():
            writer.writerows(section)

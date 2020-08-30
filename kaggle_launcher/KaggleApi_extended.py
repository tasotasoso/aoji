# -*- coding: utf-8 -*-
"""Descendant class from kaggle.api.kaggle_api_extended

This class is descendant from kaggle.api.kaggle_api_extended.
In order to use for this package, some functions aare overrided.
To refer orginal functions, please see folloing codes.
https://github.com/Kaggle/kaggle-api/blob/master/kaggle/api/kaggle_api_extended.py

For LICENSE, plesase read ./kaggle_api_LICENSE/LICENSE .
"""

from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleApi_extended(KaggleApi):

    def print_table(self, items, fields):
        """ print a table of items with ref number, for a set of fields defined

            Parameters
            ==========
            items: a list of items to print
            fields: a list of fields to select from items
        """

        formats = ["{:<8}"]
        borders = ["------  "]
        headers = ["number  "]
        for f in fields:
            length = max(len(f),
                         max([len(self.string(getattr(i, f))) for i in items]))
            justify = '>' if isinstance(getattr(
                items[0], f), int) or f == 'size' or f == 'reward' else '<'
            formats.append('{:' + justify + self.string(length + 2) + '}')
            borders.append('-' * length + '  ')
        row_format = u''.join(formats)
        headers += [f + '  ' for f in fields]
        print(row_format.format(*headers))
        print(row_format.format(*borders))
        for num, i in enumerate(items):
            i_fields = [num] + [self.string(getattr(i, f)) + '  ' for f in fields]
            try:
                print(row_format.format(*i_fields))
            except UnicodeEncodeError:
                print(row_format.format(*i_fields).encode('utf-8'))

    def competitions_list_cli(self,
                              group=None,
                              category=None,
                              sort_by=None,
                              page=1,
                              search=None,
                              csv_display=False):
        """ a wrapper for competitions_list for the client.
            Parameters
            ==========
            group: group to filter result to
            category: category to filter result to
            sort_by: how to sort the result, see valid_sort_by for options
            page: the page to return (default is 1)
            search: a search term to use (default is empty string)
            csv_display: if True, print comma separated values

            Returns
            ==========
            competitions: list of Competition instance.
        """
        competitions = self.competitions_list(group=group,
                                              category=category,
                                              sort_by=sort_by,
                                              page=page,
                                              search=search)
        fields = [
            'ref', 'deadline', 'category', 'reward', 'teamCount',
            'userHasEntered'
        ]
        if competitions:
            if csv_display:
                self.print_csv(competitions, fields)
            else:
                self.print_table(competitions, fields)
        else:
            print('No competitions found')

        return competitions
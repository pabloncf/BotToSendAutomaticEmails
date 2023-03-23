# Install:
# pip install pandas

import pandas as pd


class Table:
    tableWay = '../socios.xlsx'
    table = pd.read_excel(tableWay)

    def tableTests(self):

        self.table = Table.table

        # pulling the information from the table
        self.table.info()

    def colectingActivePartners(self):
        self.table = Table.table

        # separating active from non-active customers
        self.active_partners = self.table.loc[self.table['Status'] == 'Ativo']

        return self.active_partners
